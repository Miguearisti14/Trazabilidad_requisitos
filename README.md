<!-- Archivo generado automáticamente por tools/gestionar_artefactos.py. No editar a mano: edite artefactos.json y ejecute `generar`. -->

# Trazabilidad de requisitos — Gestión de artefactos

Repositorio de artefactos de modelado de software (SRS, RFC, prototipos, modelos y código) versionados con Git. Cada artefacto tiene un **ID único** y sus metadatos se gestionan de forma automatizada desde [`artefactos.json`](artefactos.json).

## Convención de identificadores

Formato: `<PROYECTO>-<TIPO>-<NNN>` — proyecto (3 letras) · tipo de artefacto (3 letras) · consecutivo por proyecto.

| Proyecto | Carpeta |  | Tipo | Descripción |
|---|---|---|---|---|
| `DIE` | [Dietas](Dietas/) | | `PRO` | Prototipo |
| `MUD` | [Mudanzas](Mudanzas/) | | `MOD` | Modelo UML (Enterprise Architect) |
| `SIM` | [Simulador](Simulador/) | | `DAC` | Diagrama de actividad |
| `TRI` | [Tripulaciones](Tripulaciones/) | | `DIM` | Diagrama de impacto |
|  |  | | `SIS` | Sistematización de requisitos |
|  |  | | `RFC` | RFC (Request for Change) |
|  |  | | `PBL` | Product Backlog |
|  |  | | `VIS` | Vision Board |

## Inventario de artefactos

| ID | Proyecto | Artefacto | Versión | Estado final | Autor/Revisor | Fecha de cierre | Relacionados |
|---|---|---|---|---|---|---|---|
| `DIE-PRO-001` | Dietas | [Github_prototipo.html](<Dietas/Github_prototipo.html>) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 21/09/2026 | Sin artefactos relacionados |
| `MUD-MOD-001` | Mudanzas | [Modelado de SW.qea](<Mudanzas/Modelado de SW.qea>) | 2.0 | Se realizaron 2 iteraciones | Miguel Aristizabal | 10/08/2026 | Incluye diagrama de casos de uso, diagrama de clases y diagrama entidad relación |
| `SIM-DAC-001` | Simulador | [Diagrama de actividad.pdf](<Simulador/Diagrama de actividad.pdf>) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 | `SIM-DIM-002`, `SIM-SIS-003` |
| `SIM-DIM-002` | Simulador | [Diagrama de impacto.pdf](<Simulador/Diagrama de impacto.pdf>) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 | `SIM-DAC-001`, `SIM-SIS-003` |
| `SIM-SIS-003` | Simulador | [Sistematización.pdf](<Simulador/Sistematización.pdf>) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 31/08/2026 | `SIM-DAC-001`, `SIM-DIM-002` |
| `TRI-RFC-001` | Tripulaciones | [RFC_Actividades_Desarrolladas.pdf](<Tripulaciones/RFC_Actividades_Desarrolladas.pdf>) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 | `TRI-PBL-002`, `TRI-VIS-003` |
| `TRI-PBL-002` | Tripulaciones | [Product_backlog.html](<Tripulaciones/Product_backlog.html>) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 04/08/2026 | `TRI-RFC-001`, `TRI-VIS-003` |
| `TRI-VIS-003` | Tripulaciones | [Vision-Board.docx](<Tripulaciones/Vision-Board.docx>) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 26/07/2026 | `TRI-RFC-001`, `TRI-PBL-002` |

## Control de versiones

- Cada versión cerrada de un artefacto se marca con un tag Git `<ID>/v<versión>` (p. ej. `MUD-MOD-001/v2.0`). Ver la pestaña *Tags* del repositorio.
- Para registrar una nueva versión: reemplace el archivo, actualice `version`, `estado_final` y `fecha_cierre` en `artefactos.json`, y ejecute:

```bash
python tools/gestionar_artefactos.py validar
python tools/gestionar_artefactos.py generar
git add -A && git commit -m "<ID>: versión X.Y"
python tools/gestionar_artefactos.py etiquetar
git push --follow-tags   # o: git push && git push --tags
```

- Un flujo de GitHub Actions (`.github/workflows/validar-artefactos.yml`) valida el catálogo y comprueba que los README estén al día en cada *push* o *pull request*.
