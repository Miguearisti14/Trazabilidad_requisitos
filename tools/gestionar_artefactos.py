#!/usr/bin/env python3
"""
Gestión automatizada de artefactos de ingeniería de requisitos.

Fuente única de verdad: artefactos.json (raíz del repositorio).

Uso:
    python tools/gestionar_artefactos.py validar    # IDs únicos, archivos existentes, relaciones válidas
    python tools/gestionar_artefactos.py generar    # regenera README.md raíz y de cada proyecto
    python tools/gestionar_artefactos.py verificar  # falla si los README no están actualizados (CI)
    python tools/gestionar_artefactos.py etiquetar  # crea tags git <ID>/v<version> que falten
    python tools/gestionar_artefactos.py listar     # tabla rápida por consola
"""
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CATALOGO = RAIZ / "artefactos.json"
PATRON_ID = re.compile(r"^[A-Z]{3}-[A-Z]{3}-\d{3}$")
MARCA = "<!-- Archivo generado automáticamente por tools/gestionar_artefactos.py. No editar a mano: edite artefactos.json y ejecute `generar`. -->"


def cargar():
    with open(CATALOGO, encoding="utf-8") as f:
        return json.load(f)


def fecha_dmy(iso):
    return date.fromisoformat(iso).strftime("%d/%m/%Y")


def validar(cat):
    errores = []
    ids = [a["id"] for a in cat["artefactos"]]
    vistos = set()
    for a in cat["artefactos"]:
        i = a["id"]
        if i in vistos:
            errores.append(f"ID duplicado: {i}")
        vistos.add(i)
        if not PATRON_ID.match(i):
            errores.append(f"{i}: no cumple la convención {cat['convencion_id']}")
        proy, tipo, _ = i.split("-")
        if proy not in cat["proyectos"]:
            errores.append(f"{i}: proyecto '{proy}' no registrado")
        elif not a["archivo"].startswith(cat["proyectos"][proy] + "/"):
            errores.append(f"{i}: el archivo no está en la carpeta del proyecto {cat['proyectos'][proy]}")
        if tipo not in cat["tipos"]:
            errores.append(f"{i}: tipo '{tipo}' no registrado")
        if not (RAIZ / a["archivo"]).is_file():
            errores.append(f"{i}: no existe el archivo {a['archivo']}")
        if not re.match(r"^\d+\.\d+$", a["version"]):
            errores.append(f"{i}: versión inválida '{a['version']}'")
        try:
            date.fromisoformat(a["fecha_cierre"])
        except ValueError:
            errores.append(f"{i}: fecha de cierre inválida '{a['fecha_cierre']}'")
        for r in a["relacionados"]:
            if r not in ids:
                errores.append(f"{i}: relación con ID inexistente {r}")
            elif r == i:
                errores.append(f"{i}: se relaciona consigo mismo")
    return errores


def enlace(a, desde_proyecto):
    ruta = a["archivo"].split("/", 1)[1] if desde_proyecto else a["archivo"]
    return f"[{Path(ruta).name}](<{ruta}>)"


def nombres_rel(a, por_id):
    if not a["relacionados"]:
        return "Sin artefactos relacionados"
    return ", ".join(f"`{r}` {por_id[r]['nombre']}" for r in a["relacionados"])


def ficha(a, cat, por_id):
    tipo = cat["tipos"][a["id"].split("-")[1]]
    filas = [
        ("ID único", f"`{a['id']}`"),
        ("Tipo", tipo),
        ("Archivo", enlace(a, True)),
        ("Versión", a["version"]),
        ("Estado final", a["estado_final"]),
        ("Autor o revisor", a["autor_revisor"]),
        ("Fecha de cierre", fecha_dmy(a["fecha_cierre"])),
        ("Artefactos relacionados", nombres_rel(a, por_id)),
    ]
    if a.get("notas") and a["relacionados"]:
        filas.append(("Notas", a["notas"]))
    elif a.get("notas") and not a["relacionados"] and a["notas"] != "Sin artefactos relacionados":
        filas[-1] = ("Artefactos relacionados", a["notas"])
    out = [f"### `{a['id']}` · {a['nombre']}", "", "| Campo | Valor |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in filas]
    return "\n".join(out)


def readme_proyecto(clave, carpeta, cat, por_id):
    arts = [a for a in cat["artefactos"] if a["id"].startswith(clave + "-")]
    out = [MARCA, "", f"# Proyecto {carpeta} (`{clave}`)", "",
           f"Artefactos: **{len(arts)}**", ""]
    for a in arts:
        out += [ficha(a, cat, por_id), ""]
    return "\n".join(out)


def readme_raiz(cat, por_id):
    arts = cat["artefactos"]
    out = [MARCA, "",
           "# Trazabilidad de requisitos — Gestión de artefactos", "",
           "Repositorio de artefactos de modelado de software (SRS, RFC, prototipos, modelos y código) "
           "versionados con Git. Cada artefacto tiene un **ID único** y sus metadatos se gestionan "
           "de forma automatizada desde [`artefactos.json`](artefactos.json).", "",
           "## Convención de identificadores", "",
           f"Formato: `{cat['convencion_id']}` — proyecto (3 letras) · tipo de artefacto (3 letras) · consecutivo por proyecto.", "",
           "| Proyecto | Carpeta |  | Tipo | Descripción |", "|---|---|---|---|---|"]
    ps, ts = list(cat["proyectos"].items()), list(cat["tipos"].items())
    for k in range(max(len(ps), len(ts))):
        p = ps[k] if k < len(ps) else ("", "")
        t = ts[k] if k < len(ts) else ("", "")
        out.append(f"| {('`'+p[0]+'`') if p[0] else ''} | {f'[{p[1]}]({p[1]}/)' if p[1] else ''} | | {('`'+t[0]+'`') if t[0] else ''} | {t[1]} |")
    out += ["", "## Inventario de artefactos", "",
            "| ID | Proyecto | Artefacto | Versión | Estado final | Autor/Revisor | Fecha de cierre | Relacionados |",
            "|---|---|---|---|---|---|---|---|"]
    for a in arts:
        proy = cat["proyectos"][a["id"].split("-")[0]]
        rel = ", ".join(f"`{r}`" for r in a["relacionados"]) or (a["notas"] or "—")
        out.append(f"| `{a['id']}` | {proy} | {enlace(a, False)} | {a['version']} | {a['estado_final']} | "
                   f"{a['autor_revisor']} | {fecha_dmy(a['fecha_cierre'])} | {rel} |")
    out.append("")
    out += ["## Control de versiones", "",
            "- Cada versión cerrada de un artefacto se marca con un tag Git `<ID>/v<versión>` "
            "(p. ej. `MUD-MOD-001/v2.0`). Ver la pestaña *Tags* del repositorio.",
            "- Para registrar una nueva versión: reemplace el archivo, actualice `version`, `estado_final` y "
            "`fecha_cierre` en `artefactos.json`, y ejecute:", "",
            "```bash", "python tools/gestionar_artefactos.py validar",
            "python tools/gestionar_artefactos.py generar",
            "git add -A && git commit -m \"<ID>: versión X.Y\"",
            "python tools/gestionar_artefactos.py etiquetar",
            "git push --follow-tags   # o: git push && git push --tags", "```", "",
            "- Un flujo de GitHub Actions (`.github/workflows/validar-artefactos.yml`) valida el catálogo "
            "y comprueba que los README estén al día en cada *push* o *pull request*.", ""]
    return "\n".join(out)


def generados(cat):
    por_id = {a["id"]: a for a in cat["artefactos"]}
    res = {RAIZ / "README.md": readme_raiz(cat, por_id)}
    for clave, carpeta in cat["proyectos"].items():
        res[RAIZ / carpeta / "README.md"] = readme_proyecto(clave, carpeta, cat, por_id)
    return res


def git(*args):
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validar"
    cat = cargar()
    errores = validar(cat)
    if errores:
        print("Catálogo inválido:")
        for e in errores:
            print("  -", e)
        sys.exit(1)
    if cmd == "validar":
        print(f"OK: {len(cat['artefactos'])} artefactos válidos.")
    elif cmd == "generar":
        for ruta, texto in generados(cat).items():
            ruta.write_text(texto, encoding="utf-8", newline="\n")
            print("escrito", ruta.relative_to(RAIZ))
    elif cmd == "verificar":
        desact = [r for r, t in generados(cat).items()
                  if not r.exists() or r.read_text(encoding="utf-8") != t]
        if desact:
            print("README desactualizados (ejecute `generar`):", *[r.relative_to(RAIZ) for r in desact])
            sys.exit(1)
        print("OK: README actualizados.")
    elif cmd == "etiquetar":
        existentes = set(git("tag").stdout.split())
        for a in cat["artefactos"]:
            tag = f"{a['id']}/v{a['version']}"
            if tag in existentes:
                continue
            msg = f"{a['id']} {a['nombre']} v{a['version']} - {a['estado_final']} - cierre {fecha_dmy(a['fecha_cierre'])} - {a['autor_revisor']}"
            r = git("tag", "-a", tag, "-m", msg)
            print(("creado " if r.returncode == 0 else "ERROR ") + tag, r.stderr.strip())
    elif cmd == "listar":
        for a in cat["artefactos"]:
            print(f"{a['id']:12} v{a['version']:4} {a['fecha_cierre']}  {a['archivo']}")
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
