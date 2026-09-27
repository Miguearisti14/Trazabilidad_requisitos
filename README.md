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

Oportunidades de mejora y conocimientos para futuros desarrollos, a partir del trabajo de requisitos en los cuatro proyectos.

### ¿Qué funcionó y debería repetirse?

- **Gestión de cambios formal en Tripulaciones.**
  - Cada escenario de cambio quedó trazado hasta su RFC, y cada RFC hasta los requisitos, casos de prueba, módulos de código y manuales que afecta.
  - Las decisiones del CCB quedaron justificadas: el rechazo de RFC-C1 por ser un modelo de "caja negra" no auditable y la priorización por votación.
  - La dependencia entre RFC-B1 y RFC-C2 quedó explícita, para ejecutarlas en sincronía.
- **Vision Board como punto de partida en Tripulaciones.** Definir grupos de usuarios, necesidades, funcionalidades y valor para el negocio antes de especificar dio una base clara para el backlog y para evaluar después el impacto de los cambios.
- **Criterios de aceptación ligados a la implementación en Dietas.**
  - Cada criterio (CA1–CA4) se relaciona con un elemento concreto del prototipo.
  - Los criterios se validan con escenarios de demostración que cubren casos normales, varios diagnósticos y estados vacíos.
  - El prototipo de alta fidelidad permitió validar la épica EPC 28 sin construir un backend.
- **Fichas de requisitos en el SRS del Simulador (IEEE 830).**
  - Cada requisito tiene tipo, fuente y prioridad.
  - Los requisitos no funcionales son medibles: ≤ 16 ms, < 1 fallo cada 10.000 cambios, cobertura ≥ 80 %.
  - El diagrama de actividad complementa el SRS mostrando el flujo completo del cambio de marcha.
- **Modelado del dominio en Mudanzas con tres vistas del mismo problema.** Casos de uso, clases y entidad relación, más una segunda iteración del modelo (v2.0), dejaron cada necesidad de la entrevista representada en el comportamiento y en los datos.

### ¿Qué falló y cómo se detectó?

| Falla | Cómo se detectó |
|---|---|
| El SRS del Simulador deja la sección del RF-05 (pedal de embrague) vacía, aunque el caso de uso y un caso de prueba sí lo contemplan | Al construir la matriz de trazabilidad: TC_FUNCT_04 apuntaba a un requisito sin ficha |
| En el SRS del Simulador, TC_FUNCT_02 y TC_FUNCT_03 referencian un requisito distinto del que prueban | Al cruzar cada caso de prueba con su requisito en la matriz |
| Los casos de prueba del Simulador usan una 6.ª marcha, pero las restricciones del SRS definen 5 marchas, neutra y reversa | Al comparar los pasos de las pruebas con las restricciones (§2.4) |
| Solo 6 de los 12 requisitos del Simulador tienen caso de prueba (RNF-02 a RNF-06 y RF-04 no tienen) | Al llenar la columna de casos de prueba de la matriz |
| El diagrama de impacto guardado en el Simulador describe la RFC-B1 del caso de Tripulaciones (asignación de pilotos, TC-107/108) | Al cruzar el diagrama con el documento de RFC de Tripulaciones |
| En Tripulaciones, el sistema original comparaba vuelos y escenarios solo por altitud y destino, y sobrescribía los resultados del simulador | Por incidentes y reportes externos: la tormenta del vuelo 402, el memorando de QA sobre inestabilidad y la circular NAC-2026. Estos originaron RFC-A1, RFC-B1 y RFC-C2 |
| Mudanzas no tiene prioridades, criterios de aceptación ni casos de prueba, y en el Simulador las necesidades de negocio no tienen ID | Al intentar documentar los requisitos priorizados y la validación de cada proyecto |
| Parte de la información solo está en enlaces externos:<br>• el Product Backlog enlaza a Zoho, y uno de los backlogs, que era un adjunto, no se conservó;<br>• el prototipo de Dietas enlaza a otro repositorio | Al revisar el contenido de los artefactos para trazar necesidades y requisitos |

### ¿Qué haríamos diferente desde el inicio?

1. **Identificar las necesidades de negocio con ID desde la visión del producto,** para que cada requisito nazca trazado a una necesidad, como se hizo con el Vision Board en Tripulaciones.
2. **Revisar la trazabilidad en ambos sentidos antes de cerrar cada SRS:**
   - cada requisito con su ficha completa y al menos un caso de prueba, incluidos los no funcionales;
   - cada caso de prueba apuntando al requisito correcto y coherente con las restricciones.
3. **Aplicar la misma plantilla mínima a todos los proyectos:** prioridad y criterios de aceptación por requisito, y casos de prueba, aunque el proyecto sea de modelado (Mudanzas).
4. **Especificar desde el inicio los criterios de negocio críticos con datos históricos.** En Tripulaciones, guardar varios resultados de simulación en lugar de uno solo habría evitado RFC-B1 y facilitado RFC-C2.
5. **Incluir las condiciones del entorno reales en los requisitos de comparación,** como las alertas meteorológicas, validándolos con usuarios expertos (pilotos, operadores) antes de construir.
6. **Conservar el contenido de cada artefacto,** no solo enlaces a herramientas externas, para que la trazabilidad no dependa de sistemas de terceros.
7. **Verificar que cada artefacto corresponda al caso de estudio de su proyecto** en el momento en que se produce.

**Autor:** Miguel Aristizábal Pabón — Universidad Pontificia Bolivariana, 2026.
