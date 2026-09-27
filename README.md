<!-- Archivo generado automáticamente por tools/gestionar_artefactos.py. No editar a mano: edite artefactos.json y ejecute `generar`. -->

# Proyecto Tripulaciones (`TRI`)

Rama `tripulaciones` del repositorio de trazabilidad de requisitos. Artefactos: **3**. El índice general de todos los proyectos está en la rama `master`.

## Inventario

| ID | Artefacto | Tipo | Versión | Estado final | Autor/Revisor | Fecha de cierre |
|---|---|---|---|---|---|---|
| `TRI-RFC-001` | [RFC_Actividades_Desarrolladas.pdf](<RFC_Actividades_Desarrolladas.pdf>) | RFC (Request for Change) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 |
| `TRI-PBL-002` | [Product_backlog.html](<Product_backlog.html>) | Product Backlog | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 04/08/2026 |
| `TRI-VIS-003` | [Vision-Board.docx](<Vision-Board.docx>) | Vision Board | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 26/07/2026 |

## Fichas de artefactos

### `TRI-RFC-001` · RFC_Actividades_Desarrolladas

| Campo | Valor |
|---|---|
| ID único | `TRI-RFC-001` |
| Tipo | RFC (Request for Change) |
| Archivo | [RFC_Actividades_Desarrolladas.pdf](<RFC_Actividades_Desarrolladas.pdf>) |
| Versión | 1.0 |
| Estado final | Se realizó solo 1 iteración |
| Autor o revisor | Miguel Aristizabal |
| Fecha de cierre | 15/09/2026 |
| Artefactos relacionados | `TRI-PBL-002` Product_backlog, `TRI-VIS-003` Vision-Board |

### `TRI-PBL-002` · Product_backlog

| Campo | Valor |
|---|---|
| ID único | `TRI-PBL-002` |
| Tipo | Product Backlog |
| Archivo | [Product_backlog.html](<Product_backlog.html>) |
| Versión | 1.0 |
| Estado final | Se realizó solo 1 iteración |
| Autor o revisor | Miguel Aristizabal |
| Fecha de cierre | 04/08/2026 |
| Artefactos relacionados | `TRI-RFC-001` RFC_Actividades_Desarrolladas, `TRI-VIS-003` Vision-Board |

### `TRI-VIS-003` · Vision-Board

| Campo | Valor |
|---|---|
| ID único | `TRI-VIS-003` |
| Tipo | Vision Board |
| Archivo | [Vision-Board.docx](<Vision-Board.docx>) |
| Versión | 1.0 |
| Estado final | Se realizó solo 1 iteración |
| Autor o revisor | Miguel Aristizabal |
| Fecha de cierre | 26/07/2026 |
| Artefactos relacionados | `TRI-RFC-001` RFC_Actividades_Desarrolladas, `TRI-PBL-002` Product_backlog |

## Control de versiones

Cada versión cerrada se marca con un tag `<ID>/v<versión>`. Para registrar una nueva versión:

```bash
git checkout tripulaciones
# reemplace el archivo y actualice version, estado_final y fecha_cierre en artefactos.json
python tools/gestionar_artefactos.py validar
python tools/gestionar_artefactos.py generar
git add -A && git commit -m "<ID>: versión X.Y"
python tools/gestionar_artefactos.py etiquetar
git push origin tripulaciones --tags
```
