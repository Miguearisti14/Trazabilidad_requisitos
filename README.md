<!-- Archivo generado automáticamente por tools/gestionar_artefactos.py. No editar a mano: edite artefactos.json y ejecute `generar`. -->

# Proyecto Simulador (`SIM`)

Rama `simulador` del repositorio de trazabilidad de requisitos. Artefactos: **4**. El índice general de todos los proyectos está en la rama `master`.

## Inventario

| ID | Artefacto | Tipo | Versión | Estado final | Autor/Revisor | Fecha de cierre |
|---|---|---|---|---|---|---|
| `SIM-DAC-001` | [Diagrama de actividad.pdf](<Diagrama de actividad.pdf>) | Diagrama de actividad | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 |
| `SIM-DIM-002` | [Diagrama de impacto.pdf](<Diagrama de impacto.pdf>) | Diagrama de impacto | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 |
| `SIM-SIS-003` | [Sistematización.pdf](<Sistematización.pdf>) | Sistematización de requisitos | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 31/08/2026 |
| `SIM-MTR-004` | [Matriz de trazabilidad.xlsx](<Matriz de trazabilidad.xlsx>) | Matriz de trazabilidad de requisitos | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 26/09/2026 |

## Fichas de artefactos

### `SIM-DAC-001` · Diagrama de actividad

| Campo | Valor |
|---|---|
| ID único | `SIM-DAC-001` |
| Tipo | Diagrama de actividad |
| Archivo | [Diagrama de actividad.pdf](<Diagrama de actividad.pdf>) |
| Versión | 1.0 |
| Estado final | Se realizó solo 1 iteración |
| Autor o revisor | Miguel Aristizabal |
| Fecha de cierre | 15/09/2026 |
| Artefactos relacionados | `SIM-DIM-002` Diagrama de impacto, `SIM-SIS-003` Sistematización, `SIM-MTR-004` Matriz de trazabilidad |

### `SIM-DIM-002` · Diagrama de impacto

| Campo | Valor |
|---|---|
| ID único | `SIM-DIM-002` |
| Tipo | Diagrama de impacto |
| Archivo | [Diagrama de impacto.pdf](<Diagrama de impacto.pdf>) |
| Versión | 1.0 |
| Estado final | Se realizó solo 1 iteración |
| Autor o revisor | Miguel Aristizabal |
| Fecha de cierre | 15/09/2026 |
| Artefactos relacionados | `SIM-DAC-001` Diagrama de actividad, `SIM-SIS-003` Sistematización, `SIM-MTR-004` Matriz de trazabilidad |

### `SIM-SIS-003` · Sistematización

| Campo | Valor |
|---|---|
| ID único | `SIM-SIS-003` |
| Tipo | Sistematización de requisitos |
| Archivo | [Sistematización.pdf](<Sistematización.pdf>) |
| Versión | 1.0 |
| Estado final | Se realizó solo 1 iteración |
| Autor o revisor | Miguel Aristizabal |
| Fecha de cierre | 31/08/2026 |
| Artefactos relacionados | `SIM-DAC-001` Diagrama de actividad, `SIM-DIM-002` Diagrama de impacto, `SIM-MTR-004` Matriz de trazabilidad |

### `SIM-MTR-004` · Matriz de trazabilidad

| Campo | Valor |
|---|---|
| ID único | `SIM-MTR-004` |
| Tipo | Matriz de trazabilidad de requisitos |
| Archivo | [Matriz de trazabilidad.xlsx](<Matriz de trazabilidad.xlsx>) |
| Versión | 1.0 |
| Estado final | Se realizó solo 1 iteración |
| Autor o revisor | Miguel Aristizabal |
| Fecha de cierre | 26/09/2026 |
| Artefactos relacionados | `SIM-SIS-003` Sistematización, `SIM-DAC-001` Diagrama de actividad, `SIM-DIM-002` Diagrama de impacto |

## Control de versiones

Cada versión cerrada se marca con un tag `<ID>/v<versión>`. Para registrar una nueva versión:

```bash
git checkout simulador
# reemplace el archivo y actualice version, estado_final y fecha_cierre en artefactos.json
python tools/gestionar_artefactos.py validar
python tools/gestionar_artefactos.py generar
git add -A && git commit -m "<ID>: versión X.Y"
python tools/gestionar_artefactos.py etiquetar
git push origin simulador --tags
```
