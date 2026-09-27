<!-- Archivo generado automáticamente por tools/gestionar_artefactos.py. No editar a mano: edite artefactos.json y ejecute `generar`. -->

# Trazabilidad de requisitos — Gestión de artefactos

Repositorio de artefactos de modelado de software (SRS, RFC, prototipos, modelos y código) versionados con Git. **Cada proyecto vive en su propia rama**; esta rama (`master`) es el índice general.

## Ramas por proyecto

| Rama | Proyecto | Clave | Artefactos |
|---|---|---|---|
| [`dietas`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/dietas) | Dietas | `DIE` | 1 |
| [`mudanzas`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/mudanzas) | Mudanzas | `MUD` | 1 |
| [`simulador`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/simulador) | Simulador | `SIM` | 4 |
| [`tripulaciones`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/tripulaciones) | Tripulaciones | `TRI` | 3 |

## Convención de identificadores

Formato `<PROYECTO>-<TIPO>-<NNN>`: clave del proyecto (3 letras), tipo de artefacto (3 letras) y consecutivo dentro del proyecto.

| Tipo | Descripción |
|---|---|
| `PRO` | Prototipo |
| `MOD` | Modelo UML (Enterprise Architect) |
| `DAC` | Diagrama de actividad |
| `DIM` | Diagrama de impacto |
| `SIS` | Sistematización de requisitos |
| `MTR` | Matriz de trazabilidad de requisitos |
| `RFC` | RFC (Request for Change) |
| `PBL` | Product Backlog |
| `VIS` | Vision Board |

## Inventario de artefactos

| ID | Rama | Artefacto | Versión | Estado final | Autor/Revisor | Fecha de cierre | Relacionados |
|---|---|---|---|---|---|---|---|
| `DIE-PRO-001` | `dietas` | Github_prototipo.html | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 21/09/2026 | Sin artefactos relacionados |
| `MUD-MOD-001` | `mudanzas` | Modelado de SW.qea | 2.0 | Se realizaron 2 iteraciones | Miguel Aristizabal | 10/08/2026 | Incluye diagrama de casos de uso, diagrama de clases y diagrama entidad relación |
| `SIM-DAC-001` | `simulador` | Diagrama de actividad.pdf | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 | `SIM-DIM-002`, `SIM-SIS-003`, `SIM-MTR-004` |
| `SIM-DIM-002` | `simulador` | Diagrama de impacto.pdf | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 | `SIM-DAC-001`, `SIM-SIS-003`, `SIM-MTR-004` |
| `SIM-SIS-003` | `simulador` | Sistematización.pdf | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 31/08/2026 | `SIM-DAC-001`, `SIM-DIM-002`, `SIM-MTR-004` |
| `SIM-MTR-004` | `simulador` | Matriz de trazabilidad.xlsx | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 26/09/2026 | `SIM-SIS-003`, `SIM-DAC-001`, `SIM-DIM-002` |
| `TRI-RFC-001` | `tripulaciones` | RFC_Actividades_Desarrolladas.pdf | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 | `TRI-PBL-002`, `TRI-VIS-003` |
| `TRI-PBL-002` | `tripulaciones` | Product_backlog.html | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 04/08/2026 | `TRI-RFC-001`, `TRI-VIS-003` |
| `TRI-VIS-003` | `tripulaciones` | Vision-Board.docx | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 26/07/2026 | `TRI-RFC-001`, `TRI-PBL-002` |

## Cómo trabajar

```bash
git checkout simulador        # cambiar al proyecto
git checkout master           # volver al índice
python tools/gestionar_artefactos.py generar   # en master: reconstruye este índice desde las ramas
```

- Cada versión cerrada de un artefacto se marca con un tag `<ID>/v<versión>` (p. ej. `MUD-MOD-001/v2.0`).
- GitHub Actions valida el catálogo y que el README esté al día en cada *push*.
