# Trazabilidad de requisitos

Repositorio de artefactos de ingeniería de requisitos (SRS, RFC, prototipos, modelos y matrices de trazabilidad) de la asignatura Ingeniería de Requisitos, versionados con Git.

Cada proyecto está en su propia rama. Esta rama (`master`) solo presenta el repositorio.

## Proyectos

| Rama | Proyecto | Descripción |
|---|---|---|
| [`dietas`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/dietas) | Dietas al Día | Prototipo PWA para la asignación de tratamiento nutricional |
| [`mudanzas`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/mudanzas) | Portal Web de Transporte de Carga | Modelado UML (casos de uso, clases y entidad relación) |
| [`simulador`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/simulador) | Simulador de Transmisión Mecánica | SRS, diagramas de actividad e impacto y matriz de trazabilidad |
| [`tripulaciones`](https://github.com/Miguearisti14/Trazabilidad_requisitos/tree/tripulaciones) | Sistema Integral de Gestión de Tripulaciones | Vision Board, Product Backlog y solicitudes de cambio (RFC) |

El README de cada rama describe:

1. el contexto del proyecto;
2. las necesidades originales;
3. los requisitos priorizados;
4. la validación;
5. la cadena de trazabilidad;
6. la gestión de cambios.

También incluye las versiones actuales de sus artefactos.

## Identificadores de artefactos

Cada artefacto tiene un ID único con el formato `<PROYECTO>-<TIPO>-<NNN>`: clave del proyecto (`DIE`, `MUD`, `SIM`, `TRI`), tipo de artefacto y consecutivo dentro del proyecto. Por ejemplo, `SIM-SIS-003` es la Sistematización del Simulador.

## Aprendizaje

Oportunidades de mejora y conocimientos para futuros desarrollos, a partir de la construcción de este repositorio y de lo encontrado al trazar los artefactos de los cuatro proyectos.

### ¿Qué funcionó y debería repetirse?

- **ID único por artefacto.** La convención `<PROYECTO>-<TIPO>-<NNN>` permitió referenciar cualquier artefacto sin ambigüedad (por ejemplo, `SIM-SIS-003`), relacionar artefactos entre sí y registrar su versión, estado, autor y fecha de cierre.
- **Una rama por proyecto.** Cada proyecto tiene su propio historial y sus archivos no se mezclan con los de otros. `master` queda como punto de entrada al repositorio.
- **Un README con la misma estructura en cada rama.** Contexto, necesidades, requisitos priorizados, validación, cadena de trazabilidad y gestión de cambios. Esta estructura hace comparables los proyectos y deja a la vista qué información falta en cada uno.
- **Gestión de cambios formal en Tripulaciones.**
  - Cada escenario de cambio quedó trazado hasta su RFC, y cada RFC hasta los requisitos, casos de prueba, módulos de código y manuales que afecta.
  - Las decisiones del CCB quedaron justificadas: el rechazo de RFC-C1 por ser un modelo de "caja negra" y la priorización por votación.
  - La dependencia entre RFC-B1 y RFC-C2 quedó explícita.
- **Criterios de aceptación ligados a la implementación en Dietas.** Cada criterio (CA1–CA4) se relaciona con un elemento del prototipo y se valida con escenarios de demostración concretos.
- **Fichas de requisitos en el SRS del Simulador (IEEE 830).** Tipo, fuente y prioridad por requisito, que se pudieron llevar directamente a la matriz de trazabilidad.

### ¿Qué falló y cómo se detectó?

| Falla | Cómo se detectó |
|---|---|
| Se fusionaron las ramas de proyecto con `master` mediante pull requests (#2, #3, #4), y `master`, `dietas` y `tripulaciones` quedaron con archivos de otros proyectos | Aparecieron conflictos al subir cambios y, al revisar el contenido de cada rama en GitHub, había archivos que no correspondían |
| La automatización del versionamiento (script, validación en GitHub Actions y tags por versión) generó más fricción que beneficio: conflictos y reescrituras forzadas de tags | Los conflictos al hacer *push*. Se decidió simplificar y dejar solo las ramas y README descriptivos |
| El SRS del Simulador tiene inconsistencias:<br>• la sección del RF-05 está vacía;<br>• TC_FUNCT_02 y TC_FUNCT_03 referencian un requisito distinto del que prueban;<br>• los casos de prueba usan una 6.ª marcha, aunque el SRS define 5 | Al construir la matriz de trazabilidad y cruzar cada caso de prueba con su requisito |
| El diagrama de impacto guardado en Simulador describe la RFC-B1 del caso de Tripulaciones (asignación de pilotos, TC-107/108) | Al cruzar el diagrama con el documento de RFC de Tripulaciones |
| En los metadatos iniciales, la Sistematización aparecía relacionada consigo misma | Al asignar los IDs y validar las relaciones entre artefactos |
| Algunos artefactos no contienen información propia, solo enlaces externos:<br>• el Product Backlog enlaza a Zoho, y el backlog de Federico, que era un adjunto, no está;<br>• el prototipo de Dietas enlaza a otro repositorio | Al documentar las necesidades y requisitos de cada proyecto no había contenido que trazar |
| Mudanzas no tiene prioridades, criterios de aceptación ni casos de prueba, y el Simulador no tiene necesidades de negocio con ID | Al llenar las secciones "Requisitos priorizados" y "Validación", y la columna de necesidades de la matriz |

### ¿Qué haríamos diferente desde el inicio?

1. **Definir la estructura del repositorio antes de subir artefactos.** Una rama por proyecto, con la regla explícita de no fusionarlas con `master`, reforzada con protección de ramas en GitHub.
2. **Asignar el ID y el nombre definitivo al crear cada artefacto,** no al final. Así se evitan nombres generados por plataformas y relaciones mal registradas.
3. **Registrar las necesidades de negocio con ID desde la visión del producto,** para que cada requisito nazca trazado a una necesidad.
4. **Revisar la trazabilidad en ambos sentidos antes de cerrar cada SRS:**
   - cada requisito con su ficha completa y al menos un caso de prueba;
   - cada caso de prueba apuntando al requisito correcto y coherente con las restricciones.
5. **Guardar el contenido de los artefactos dentro del repositorio** (por ejemplo, exportar el backlog de Zoho) en lugar de solo enlaces, para que la trazabilidad no dependa de sistemas externos.
6. **Aplicar la misma plantilla mínima a todos los proyectos:** prioridad y criterios de aceptación por requisito, y registro de cambios, aunque el proyecto sea pequeño.
7. **Empezar el versionamiento de forma simple** (ramas, README y versiones documentadas) y automatizar solo cuando el proceso sea estable y todos lo entiendan.
8. **Ubicar cada artefacto en su proyecto desde que se produce,** verificando que su contenido corresponda al caso de estudio.

**Autor:** Miguel Aristizábal Pabón — Universidad Pontificia Bolivariana, 2026.
