#!/usr/bin/env python3
"""
Gestión automatizada de artefactos de ingeniería de requisitos.

Organización del repositorio: una rama por proyecto (dietas, mudanzas,
simulador, tripulaciones) con sus artefactos en la raíz, y la rama master
como índice general.

En una rama de proyecto, artefactos.json contiene "proyecto" y "artefactos".
En master, artefactos.json contiene "proyectos" (clave, nombre, rama) y el
índice se construye leyendo el artefactos.json de cada rama.

Uso:
    python tools/gestionar_artefactos.py validar    # IDs únicos, archivos existentes, relaciones válidas
    python tools/gestionar_artefactos.py generar    # regenera README.md
    python tools/gestionar_artefactos.py verificar  # falla si README.md no está actualizado (CI)
    python tools/gestionar_artefactos.py etiquetar  # crea tags git <ID>/v<version> que falten (ramas de proyecto)
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
MARCA = ("<!-- Archivo generado automáticamente por tools/gestionar_artefactos.py. "
         "No editar a mano: edite artefactos.json y ejecute `generar`. -->")


def git(*args):
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")


def cargar():
    with open(CATALOGO, encoding="utf-8") as f:
        return json.load(f)


def es_indice(cat):
    return "proyectos" in cat


def fecha_dmy(iso):
    return date.fromisoformat(iso).strftime("%d/%m/%Y")


def catalogo_de_rama(rama):
    """Lee artefactos.json de una rama (local u origin)."""
    for ref in (rama, f"origin/{rama}"):
        r = git("show", f"{ref}:artefactos.json")
        if r.returncode == 0:
            return json.loads(r.stdout)
    return None


def validar_artefactos(arts, clave, tipos, revisar_archivos):
    errores, ids = [], [a["id"] for a in arts]
    vistos = set()
    for a in arts:
        i = a["id"]
        if i in vistos:
            errores.append(f"ID duplicado: {i}")
        vistos.add(i)
        if not PATRON_ID.match(i):
            errores.append(f"{i}: no cumple la convención <PROYECTO>-<TIPO>-<NNN>")
            continue
        proy, tipo, _ = i.split("-")
        if proy != clave:
            errores.append(f"{i}: el prefijo no corresponde al proyecto {clave}")
        if tipo not in tipos:
            errores.append(f"{i}: tipo '{tipo}' no registrado")
        if revisar_archivos and not (RAIZ / a["archivo"]).is_file():
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


def validar(cat):
    if es_indice(cat):
        errores, todos = [], []
        for p in cat["proyectos"]:
            sub = catalogo_de_rama(p["rama"])
            if sub is None:
                errores.append(f"No se encontró artefactos.json en la rama {p['rama']}")
                continue
            if sub["proyecto"]["clave"] != p["clave"]:
                errores.append(f"La rama {p['rama']} no corresponde al proyecto {p['clave']}")
            todos += [a["id"] for a in sub["artefactos"]]
        dup = {i for i in todos if todos.count(i) > 1}
        errores += [f"ID duplicado entre ramas: {i}" for i in sorted(dup)]
        return errores
    return validar_artefactos(cat["artefactos"], cat["proyecto"]["clave"], cat["tipos"], True)


def relacionados_txt(a, por_id):
    if not a["relacionados"]:
        return a.get("notas") or "Sin artefactos relacionados"
    return ", ".join(f"`{r}` {por_id[r]['nombre']}" for r in a["relacionados"])


def readme_proyecto(cat):
    p, arts = cat["proyecto"], cat["artefactos"]
    por_id = {a["id"]: a for a in arts}
    out = [MARCA, "", f"# Proyecto {p['nombre']} (`{p['clave']}`)", "",
           f"Rama `{p['rama']}` del repositorio de trazabilidad de requisitos. "
           f"Artefactos: **{len(arts)}**. El índice general de todos los proyectos está en la rama `master`.", "",
           "## Inventario", "",
           "| ID | Artefacto | Tipo | Versión | Estado final | Autor/Revisor | Fecha de cierre |",
           "|---|---|---|---|---|---|---|"]
    for a in arts:
        out.append(f"| `{a['id']}` | [{a['archivo']}](<{a['archivo']}>) | {cat['tipos'][a['id'].split('-')[1]]} | "
                   f"{a['version']} | {a['estado_final']} | {a['autor_revisor']} | {fecha_dmy(a['fecha_cierre'])} |")
    out += ["", "## Fichas de artefactos", ""]
    for a in arts:
        filas = [("ID único", f"`{a['id']}`"),
                 ("Tipo", cat["tipos"][a["id"].split("-")[1]]),
                 ("Archivo", f"[{a['archivo']}](<{a['archivo']}>)"),
                 ("Versión", a["version"]),
                 ("Estado final", a["estado_final"]),
                 ("Autor o revisor", a["autor_revisor"]),
                 ("Fecha de cierre", fecha_dmy(a["fecha_cierre"])),
                 ("Artefactos relacionados", relacionados_txt(a, por_id))]
        if a.get("notas") and a["relacionados"]:
            filas.append(("Notas", a["notas"]))
        out += [f"### `{a['id']}` · {a['nombre']}", "", "| Campo | Valor |", "|---|---|"]
        out += [f"| {k} | {v} |" for k, v in filas]
        out.append("")
    out += ["## Control de versiones", "",
            "Cada versión cerrada se marca con un tag `<ID>/v<versión>`. Para registrar una nueva versión:", "",
            "```bash", f"git checkout {p['rama']}",
            "# reemplace el archivo y actualice version, estado_final y fecha_cierre en artefactos.json",
            "python tools/gestionar_artefactos.py validar",
            "python tools/gestionar_artefactos.py generar",
            "git add -A && git commit -m \"<ID>: versión X.Y\"",
            "python tools/gestionar_artefactos.py etiquetar",
            f"git push origin {p['rama']} --tags", "```", ""]
    return "\n".join(out)


def readme_indice(cat):
    url = cat.get("url_repositorio", "").rstrip("/")
    out = [MARCA, "", "# Trazabilidad de requisitos — Gestión de artefactos", "",
           "Repositorio de artefactos de modelado de software (SRS, RFC, prototipos, modelos y código) "
           "versionados con Git. **Cada proyecto vive en su propia rama**; esta rama (`master`) es el índice general.", "",
           "## Ramas por proyecto", "",
           "| Rama | Proyecto | Clave | Artefactos |", "|---|---|---|---|"]
    subs = {p["rama"]: catalogo_de_rama(p["rama"]) for p in cat["proyectos"]}
    for p in cat["proyectos"]:
        sub = subs[p["rama"]]
        n = len(sub["artefactos"]) if sub else 0
        enlace = f"[`{p['rama']}`]({url}/tree/{p['rama']})" if url else f"`{p['rama']}`"
        out.append(f"| {enlace} | {p['nombre']} | `{p['clave']}` | {n} |")
    out += ["", "## Convención de identificadores", "",
            "Formato `<PROYECTO>-<TIPO>-<NNN>`: clave del proyecto (3 letras), tipo de artefacto (3 letras) "
            "y consecutivo dentro del proyecto.", "", "| Tipo | Descripción |", "|---|---|"]
    tipos = {}
    for sub in subs.values():
        if sub:
            tipos.update(sub["tipos"])
    out += [f"| `{k}` | {v} |" for k, v in tipos.items()]
    out += ["", "## Inventario de artefactos", "",
            "| ID | Rama | Artefacto | Versión | Estado final | Autor/Revisor | Fecha de cierre | Relacionados |",
            "|---|---|---|---|---|---|---|---|"]
    for p in cat["proyectos"]:
        sub = subs[p["rama"]]
        if not sub:
            continue
        for a in sub["artefactos"]:
            rel = ", ".join(f"`{r}`" for r in a["relacionados"]) or (a.get("notas") or "—")
            out.append(f"| `{a['id']}` | `{p['rama']}` | {a['archivo']} | {a['version']} | {a['estado_final']} | "
                       f"{a['autor_revisor']} | {fecha_dmy(a['fecha_cierre'])} | {rel} |")
    out += ["", "## Cómo trabajar", "",
            "```bash", "git checkout simulador        # cambiar al proyecto", "git checkout master           # volver al índice",
            "python tools/gestionar_artefactos.py generar   # en master: reconstruye este índice desde las ramas", "```", "",
            "- Cada versión cerrada de un artefacto se marca con un tag `<ID>/v<versión>` (p. ej. `MUD-MOD-001/v2.0`).",
            "- GitHub Actions valida el catálogo y que el README esté al día en cada *push*.", ""]
    return "\n".join(out)


def generado(cat):
    return readme_indice(cat) if es_indice(cat) else readme_proyecto(cat)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validar"
    cat = cargar()
    errores = validar(cat)
    if errores:
        print("Catálogo inválido:")
        for e in errores:
            print("  -", e)
        sys.exit(1)
    destino = RAIZ / "README.md"
    if cmd == "validar":
        print("OK: catálogo válido.")
    elif cmd == "generar":
        destino.write_text(generado(cat), encoding="utf-8", newline="\n")
        print("escrito README.md")
    elif cmd == "verificar":
        if not destino.exists() or destino.read_text(encoding="utf-8") != generado(cat):
            print("README.md desactualizado: ejecute `generar`.")
            sys.exit(1)
        print("OK: README.md actualizado.")
    elif cmd == "etiquetar":
        if es_indice(cat):
            print("La rama master no tiene artefactos que etiquetar.")
            return
        existentes = set(git("tag").stdout.split())
        for a in cat["artefactos"]:
            tag = f"{a['id']}/v{a['version']}"
            if tag in existentes:
                continue
            msg = (f"{a['id']} {a['nombre']} v{a['version']} - {a['estado_final']} - "
                   f"cierre {fecha_dmy(a['fecha_cierre'])} - {a['autor_revisor']}")
            r = git("tag", "-a", tag, "-m", msg)
            print(("creado " if r.returncode == 0 else "ERROR ") + tag, r.stderr.strip())
    elif cmd == "listar":
        if es_indice(cat):
            for p in cat["proyectos"]:
                print(f"{p['rama']:14} {p['clave']}  {p['nombre']}")
        else:
            for a in cat["artefactos"]:
                print(f"{a['id']:12} v{a['version']:4} {a['fecha_cierre']}  {a['archivo']}")
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
