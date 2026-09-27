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

Reflexión sobre los modelos y técnicas de requisitos elegidos en cada proyecto: si fueron adecuados para el problema y qué otro modelo habría convenido.

### ¿Qué práctica funciona y por qué debería repetirse?

| Proyecto | Modelo o técnica | Por qué fue adecuado |
|---|---|---|
| Simulador | SRS IEEE 830 con fichas por requisito y diagrama de actividad | Es un sistema en tiempo real integrado en un videojuego, con restricciones duras. El SRS permitió expresar requisitos no funcionales medibles (≤ 16 ms por cambio, < 1 fallo cada 10.000 cambios, cobertura ≥ 80 %). El diagrama de actividad representa bien el flujo del cambio de marcha, con sus decisiones: modo, validez del cambio y RPM fuera de umbral. |
| Tripulaciones | Vision Board, Product Backlog y gestión de cambios con RFC, análisis de impacto y CCB | El problema tiene reglas de negocio que cambian, varios interesados (operadores, pilotos, administrativos, QA) y una autoridad regulatoria. El Vision Board alineó necesidades y valor. Las RFC con CCB permitieron analizar, justificar y decidir cada cambio: por ejemplo, rechazar el modelo de "caja negra" de RFC-C1. |
| Mudanzas | Casos de uso, diagrama de clases y diagrama entidad relación | El problema está centrado en datos: las entrevistas describen qué guardar y cómo se relaciona (empresa–servicio–población, intervalos de peso, recargos, solicitudes). Los modelos de clases y ER eran el modelo natural, y los casos de uso ordenaron qué hace cada actor en el portal. |
| Dietas | Historia de usuario (EPC 28), criterios de aceptación y prototipo de alta fidelidad | Es un flujo interactivo con riesgo clínico. El prototipo validó con el usuario lo que un documento no puede validar: que la alerta de alergia sea inequívoca y que el médico asigne una dieta segura en menos de 90 s. |

**Práctica general:** elegir el modelo según la naturaleza del problema.

- Restricciones técnicas → SRS con requisitos no funcionales medibles.
- Reglas cambiantes → gestión de cambios.
- Datos → clases y ER.
- Interacción → prototipo.

### ¿Qué técnica falló y cómo se detectó?

| Proyecto | Qué falló del modelo elegido | Cómo se detectó |
|---|---|---|
| Simulador | El comportamiento depende del **estado**: marcha activa, embrague y modo; "cambio no válido en el estado actual"; "estado seguro en neutra". Sin embargo, solo se modeló con un diagrama de actividad. Así quedaron huecos: el RF-05 (embrague) sin ficha y casos de prueba con una 6.ª marcha que no existe entre las 7 posiciones definidas. | Al construir la matriz de trazabilidad y cruzar requisitos, pruebas y restricciones |
| Simulador | Se elaboró un diagrama de impacto, pero el proyecto no tenía ninguna solicitud de cambio propia. Esa técnica no aplicaba al proyecto. | Al compararlo con las RFC de Tripulaciones: su contenido era la RFC-B1 de ese caso |
| Tripulaciones | El Vision Board y el backlog no se acompañaron de un modelo de datos ni de una especificación de la regla de asignación. Las reglas "resultado único por piloto y escenario" y "piloto con puntuación más alta" venían del enunciado y nunca se analizaron ni se validaron. | Ya en operación, por reportes externos: el memorando de QA y la circular NAC-2026. Llegaron como RFC-B1 y RFC-C2, que en el fondo eran cambios del modelo de datos. |
| Tripulaciones | La comparación vuelo–escenario solo consideraba altitud y destino, sin las condiciones meteorológicas | Por el incidente del vuelo 402 (RFC-A1) |
| Mudanzas | Los casos de uso no tienen prioridad ni criterios de aceptación. Reglas de negocio como el recargo por peso o que las direcciones deban estar en las poblaciones de la empresa quedaron solo como notas del modelo, no como requisitos verificables. | Al trazar cada necesidad de la entrevista: había clase y entidad, pero no un requisito que se pudiera probar |
| Dietas | El prototipo se construyó sin un modelo del dominio (alimentos, nutrientes, dietas, enfermedades, alergias), aunque todo el flujo depende de cruzar esas relaciones. Además, RF1–RF6 no tienen prioridad. | Al documentar los requisitos: la lógica de compatibilidad solo existe en el código del prototipo |

### ¿Qué haríamos diferente desde el inicio?

| Proyecto | Qué haríamos diferente |
|---|---|
| Simulador | Complementar el diagrama de actividad con un **diagrama de máquina de estados**: las 7 posiciones de marcha, el embrague y el modo Manual/Automático, con sus transiciones válidas y el estado seguro. Agregar un **diagrama de secuencia** para la coordinación de la Unidad de Control con el embrague y la caja de cambios. Así los cambios inválidos y los límites de marcha se habrían especificado sin ambigüedad. |
| Tripulaciones | Además del Vision Board, especificar la regla de asignación con una **tabla de decisión** (escenario, puntuación, horas de vuelo, clima) y construir desde el inicio un **modelo de dominio** con histórico de resultados de simulación. Validar ambos con QA, los operadores y la normativa aeronáutica antes de construir. |
| Mudanzas | Al ser el rediseño de un portal web, agregar **wireframes o un prototipo** para validar con los gerentes, y **historias de usuario priorizadas** (por ejemplo, con MoSCoW) con criterios de aceptación. Expresar las reglas de negocio como requisitos verificables y derivar el ER del modelo de clases, en lugar de mantener dos modelos en paralelo. |
| Dietas | Hacer un **modelo de dominio** de los catálogos y sus relaciones antes del prototipo, y **priorizar RF1–RF6**, para que el prototipo se apoye en requisitos trazables y no al revés. |

**Regla general para futuros desarrollos:**

- Datos → entidad relación y clases.
- Comportamiento por estados → máquina de estados.
- Interacción con el usuario → prototipo con criterios de aceptación.
- Reglas de negocio cambiantes → tablas de decisión y gestión de cambios.

**Autor:** Miguel Aristizábal Pabón — Universidad Pontificia Bolivariana, 2026.
