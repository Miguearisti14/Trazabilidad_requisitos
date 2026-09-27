# Trazabilidad de requisitos — Gestión de artefactos

Repositorio de artefactos de modelado de software (SRS, RFC, prototipos y modelos) versionados con Git.
**Cada proyecto está en su propia rama**; esta rama (`master`) es solo el índice general.

## Ramas por proyecto

| Rama | Proyecto | Clave | Artefactos |
|---|---|---|---|
| [`dietas`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/dietas) | Dietas | `DIE` | 1 |
| [`mudanzas`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/mudanzas) | Mudanzas | `MUD` | 1 |
| [`simulador`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/simulador) | Simulador | `SIM` | 4 |
| [`tripulaciones`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/tripulaciones) | Tripulaciones | `TRI` | 3 |

## Convención de identificadores

Formato `<PROYECTO>-<TIPO>-<NNN>`: clave del proyecto (3 letras), tipo de artefacto (3 letras) y consecutivo dentro del proyecto.

## Inventario de versiones

| ID | Rama | Artefacto | Versión | Estado final | Autor o revisor | Fecha de cierre |
|---|---|---|---|---|---|---|
| `DIE-PRO-001` | `dietas` | Github_prototipo.html | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 21/09/2026 |
| `MUD-MOD-001` | `mudanzas` | Modelado de SW.qea | 2.0 | Se realizaron 2 iteraciones | Miguel Aristizabal | 10/08/2026 |
| `SIM-DAC-001` | `simulador` | Diagrama de actividad.pdf | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 |
| `SIM-DIM-002` | `simulador` | Diagrama de impacto.pdf | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 |
| `SIM-SIS-003` | `simulador` | Sistematización.pdf | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 31/08/2026 |
| `SIM-MTR-004` | `simulador` | Matriz de trazabilidad.xlsx | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 26/09/2026 |
| `TRI-RFC-001` | `tripulaciones` | RFC_Actividades_Desarrolladas.pdf | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 |
| `TRI-PBL-002` | `tripulaciones` | Product_backlog.html | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 04/08/2026 |
| `TRI-VIS-003` | `tripulaciones` | Vision-Board.docx | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 26/07/2026 |

> Las ramas de proyecto son independientes y **no se fusionan** con `master`.
