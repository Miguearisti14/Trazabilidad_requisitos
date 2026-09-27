<!-- Archivo generado automáticamente por tools/gestionar_artefactos.py. No editar a mano: edite artefactos.json y ejecute `generar`. -->

# Proyecto Mudanzas (`MUD`)

Rama `mudanzas` del repositorio de trazabilidad de requisitos. Artefactos: **1**. El índice general de todos los proyectos está en la rama `master`.

## Inventario

| ID | Artefacto | Tipo | Versión | Estado final | Autor/Revisor | Fecha de cierre |
|---|---|---|---|---|---|---|
| `MUD-MOD-001` | [Modelado de SW.qea](<Modelado de SW.qea>) | Modelo UML (Enterprise Architect) | 2.0 | Se realizaron 2 iteraciones | Miguel Aristizabal | 10/08/2026 |

## Fichas de artefactos

### `MUD-MOD-001` · Modelado de SW

| Campo | Valor |
|---|---|
| ID único | `MUD-MOD-001` |
| Tipo | Modelo UML (Enterprise Architect) |
| Archivo | [Modelado de SW.qea](<Modelado de SW.qea>) |
| Versión | 2.0 |
| Estado final | Se realizaron 2 iteraciones |
| Autor o revisor | Miguel Aristizabal |
| Fecha de cierre | 10/08/2026 |
| Artefactos relacionados | Incluye diagrama de casos de uso, diagrama de clases y diagrama entidad relación |

## Control de versiones

Cada versión cerrada se marca con un tag `<ID>/v<versión>`. Para registrar una nueva versión:

```bash
git checkout mudanzas
# reemplace el archivo y actualice version, estado_final y fecha_cierre en artefactos.json
python tools/gestionar_artefactos.py validar
python tools/gestionar_artefactos.py generar
git add -A && git commit -m "<ID>: versión X.Y"
python tools/gestionar_artefactos.py etiquetar
git push origin mudanzas --tags
```
