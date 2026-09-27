<!-- Archivo generado automáticamente por tools/gestionar_artefactos.py. No editar a mano: edite artefactos.json y ejecute `generar`. -->

# Proyecto Dietas (`DIE`)

Rama `dietas` del repositorio de trazabilidad de requisitos. Artefactos: **1**. El índice general de todos los proyectos está en la rama `master`.

## Inventario

| ID | Artefacto | Tipo | Versión | Estado final | Autor/Revisor | Fecha de cierre |
|---|---|---|---|---|---|---|
| `DIE-PRO-001` | [Github_prototipo.html](<Github_prototipo.html>) | Prototipo | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 21/09/2026 |

## Fichas de artefactos

### `DIE-PRO-001` · Github_prototipo

| Campo | Valor |
|---|---|
| ID único | `DIE-PRO-001` |
| Tipo | Prototipo |
| Archivo | [Github_prototipo.html](<Github_prototipo.html>) |
| Versión | 1.0 |
| Estado final | Se realizó solo 1 iteración |
| Autor o revisor | Miguel Aristizabal |
| Fecha de cierre | 21/09/2026 |
| Artefactos relacionados | Sin artefactos relacionados |

## Control de versiones

Cada versión cerrada se marca con un tag `<ID>/v<versión>`. Para registrar una nueva versión:

```bash
git checkout dietas
# reemplace el archivo y actualice version, estado_final y fecha_cierre en artefactos.json
python tools/gestionar_artefactos.py validar
python tools/gestionar_artefactos.py generar
git add -A && git commit -m "<ID>: versión X.Y"
python tools/gestionar_artefactos.py etiquetar
git push origin dietas --tags
```
