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

Oportunidades de mejora y conocimientos para futuros desarrollos, a partir de las prácticas y técnicas de ingeniería de requisitos aplicadas en los cuatro proyectos.

### ¿Qué práctica funciona y por qué debería repetirse?

| Práctica | Dónde se aplicó | Por qué debería repetirse |
|---|---|---|
| **Gestión de cambios con RFC y Comité de Control de Cambios (CCB)** | Tripulaciones | Cada cambio queda documentado con solicitante, motivación, tipo y prioridad, y cada decisión queda justificada. Así, las decisiones se pueden auditar: la RFC-C1 se rechazó porque un modelo de "caja negra" no se podía justificar ante la Autoridad de Aviación Civil. |
| **Análisis de impacto antes de aprobar un cambio** | Tripulaciones (RFC-B1), diagrama de impacto | Muestra de antemano todo lo que un cambio arrastra: requisitos, casos de prueba, código, manuales y plan. También hace visibles las dependencias, como la de RFC-C2 con RFC-B1, para ejecutarlas juntas y evitar estados inconsistentes. |
| **Prototipo de alta fidelidad con criterios de aceptación** | Dietas | La épica EPC 28 se validó con usuarios sin construir un backend. Los criterios CA1–CA4 son verificables (por ejemplo, "dieta segura en < 90 s") y los escenarios de demostración cubren casos normales, varios diagnósticos y estados vacíos. |
| **Vision Board antes de especificar** | Tripulaciones | Alinea desde el inicio los grupos de usuarios, las necesidades, las funcionalidades y el valor para el negocio. Da una referencia estable para construir el backlog y para evaluar después si un cambio aporta valor. |
| **Criterios de aceptación en formato Dado / Cuando / Entonces** | Tripulaciones (RFC-A1) | Cada criterio se convierte directamente en un caso de prueba y elimina la ambigüedad sobre cuándo el cambio está bien implementado. |
| **SRS con plantilla IEEE 830 y requisitos no funcionales medibles** | Simulador | Las fichas con tipo, fuente y prioridad permiten priorizar y trazar. Además, los requisitos no funcionales con valores concretos (≤ 16 ms, < 1 fallo cada 10.000 cambios, cobertura ≥ 80 %) se pueden verificar objetivamente. |
| **Modelar el mismo problema en varias vistas** | Mudanzas (casos de uso, clases y entidad relación) y Simulador (casos de uso y actividad) | Cada vista revisa a las otras: cada necesidad de la entrevista quedó representada tanto en el comportamiento como en los datos. La segunda iteración del modelo de Mudanzas (v2.0) lo refinó. |
| **Matriz de trazabilidad** | Simulador | Al cruzar requisito, caso de prueba y componente sacó a la luz errores que la sola lectura del SRS no mostraba (ver la siguiente pregunta). |

### ¿Qué técnica falló y cómo se detectó?

| Técnica que falló | Qué pasó | Cómo se detectó |
|---|---|---|
| **Redacción del SRS sin revisión cruzada entre requisitos y pruebas** | En el Simulador:<br>• la ficha del RF-05 (pedal de embrague) quedó vacía;<br>• TC_FUNCT_02 y TC_FUNCT_03 referencian un requisito distinto del que prueban;<br>• las pruebas usan una 6.ª marcha, aunque las restricciones definen 5. | Al construir la matriz de trazabilidad y cruzar cada caso de prueba con su requisito y con las restricciones (§2.4) |
| **Diseño de pruebas solo para requisitos funcionales** | 6 de los 12 requisitos del Simulador no tienen caso de prueba: RF-04 y RNF-02 a RNF-06 | Al llenar la columna "ID Caso de prueba" de la matriz |
| **Elicitación limitada al enunciado inicial** | En Tripulaciones, el sistema:<br>• comparaba vuelos y escenarios solo por altitud y destino;<br>• asignaba por un único puntaje máximo;<br>• sobrescribía los resultados anteriores del simulador. | Ya en operación, por fuentes externas: la tormenta no prevista del vuelo 402, el memorando de QA sobre el 15 % de pilotos inestables y la circular NAC-2026. De ahí surgieron RFC-A1, RFC-B1 y RFC-C2. |
| **Automatización total con Machine Learning como solución** | La propuesta RFC-C1 no permitía explicar por qué se elegía un escenario | En la revisión del CCB, al evaluarla frente a los requisitos de auditoría y seguridad. Se rechazó. |
| **Modelado sin priorización ni validación** | Mudanzas tiene casos de uso, clases y entidades, pero ningún requisito priorizado, criterio de aceptación ni caso de prueba | Al documentar los requisitos priorizados y la validación del proyecto |
| **Backlog gestionado solo en una herramienta externa** | El Product Backlog de Tripulaciones solo existe como enlace a Zoho, y uno de los backlogs, que era un adjunto, no se conservó | Al intentar trazar las necesidades del Vision Board hasta los ítems del backlog |

### ¿Qué haríamos diferente desde el inicio?

1. **Asignar un ID a cada necesidad de negocio desde el Vision Board** y derivar de ella cada requisito, para que la trazabilidad necesidad → requisito exista desde el principio y no se reconstruya al final.
2. **Construir la matriz de trazabilidad durante la especificación, no después.** Así los requisitos sin ficha o sin prueba, y las pruebas mal referenciadas, se detectan antes de cerrar el SRS.
3. **Diseñar al menos un caso de prueba por requisito,** incluidos los no funcionales, usando criterios Dado / Cuando / Entonces como en RFC-A1.
4. **Ampliar la elicitación con usuarios expertos y con la normativa** (pilotos, operadores, QA, Autoridad de Aviación Civil) antes de fijar reglas de negocio críticas. En Tripulaciones, guardar un histórico de simulaciones y considerar las alertas meteorológicas desde el inicio habría evitado RFC-A1, RFC-B1 y buena parte de RFC-C2.
5. **Priorizar todos los requisitos con una técnica explícita (por ejemplo, MoSCoW) y validarlos con prototipos,** incluso en proyectos de modelado como Mudanzas.
6. **Hacer análisis de impacto y pasar por el CCB en cada cambio desde la primera iteración,** no solo cuando el cambio es grande.
7. **Mantener el backlog y los demás artefactos exportados junto al proyecto,** para no depender de herramientas externas ni perder información.

**Autor:** Miguel Aristizábal Pabón — Universidad Pontificia Bolivariana, 2026.
