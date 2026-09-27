# Proyecto Simulador de Transmisión Mecánica (`SIM`)

Rama `simulador` del repositorio de trazabilidad de requisitos. El índice general de todos los proyectos está en la rama [`master`](https://github.com/Miguearisti14/Trazabilidad_requisitos).

## Versiones actuales

| ID | Artefacto | Tipo | Versión | Estado final | Autor o revisor | Fecha de cierre |
|---|---|---|---|---|---|---|
| `SIM-DAC-001` | [Diagrama de actividad.pdf](<Diagrama de actividad.pdf>) | Diagrama de actividad | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 |
| `SIM-DIM-002` | [Diagrama de impacto.pdf](<Diagrama de impacto.pdf>) | Diagrama de impacto | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 |
| `SIM-SIS-003` | [Sistematización.pdf](<Sistematización.pdf>) | Sistematización de requisitos (SRS) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 31/08/2026 |
| `SIM-MTR-004` | [Matriz de trazabilidad.xlsx](<Matriz de trazabilidad.xlsx>) | Matriz de trazabilidad de requisitos | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 26/09/2026 |

---

## 1. Contexto del proyecto

Una empresa de videojuegos pretende desarrollar un simulador de un vehículo de competición. El diagrama de clases del caso muestra la estructura de la parte de la aplicación que representa la transmisión mecánica del vehículo.

La transmisión tiene por objeto que el movimiento generado por el motor, a un determinado número de revoluciones, se transmita a las ruedas con diferentes velocidades de giro en función de las condiciones de marcha deseadas. El sistema permite al conductor cambiar de marcha para obtener un mayor rendimiento del movimiento generado por el motor en función de diferentes circunstancias.

Según el SRS (`SIM-SIS-003`, IEEE 830):

- **Alcance:** el software simula la transmisión mecánica completa, con cambio de marchas por palanca o selectores digitales, y gestiona palanca, selectores, unidad de control, embrague, pedal, caja de cambios y engranajes.
- **Perspectiva:** es un producto semi-independiente integrado en un videojuego de conducción. Recibe las señales del conductor (palanca, selectores, pedal de embrague) y envía el estado de la transmisión (marcha activa, relación de transmisión, estado del embrague) al subsistema de motor y ruedas.
- **Usuario:** conductor virtual, que maneja teclado, gamepad o volante con palanca y pedales.
- **Restricciones:**
  - Desarrollo en C# bajo el paradigma de POO, respetando el diagrama de clases.
  - Máximo 16 ms por cambio de marcha.
  - Plataforma mínima Windows 10/11.
  - 5 marchas hacia adelante, neutra y reversa.
  - La simulación del motor queda fuera del alcance: las RPM llegan como dato externo.

## 2. Necesidades originales

Tomadas del enunciado del caso:

- Transmitir el movimiento del motor a las ruedas con diferentes velocidades de giro según las condiciones de marcha deseadas.
- Permitir al conductor cambiar de marcha para obtener un mayor rendimiento del motor según las circunstancias.

El diagrama de casos de uso del SRS (§2.2) identifica estas funcionalidades del conductor:

- cambiar marcha con palanca;
- subir marcha "+";
- bajar marcha "−";
- cambiar modo de funcionamiento;
- pisar / soltar el pedal de embrague.

En la matriz de trazabilidad (`SIM-MTR-004`), los requisitos se agrupan en las necesidades de negocio NEG-01 a NEG-05. Cada celda tiene un comentario que explica su origen.

## 3. Requisitos priorizados

Prioridades tal como están marcadas en el SRS:

| ID | Requisito | Tipo en SRS | Prioridad | Fuente |
|---|---|---|---|---|
| RF-01 | Cambio de marcha mediante palanca | Requisito | Alta / Esencial | Clase Palanca (`cambiar(marcha)`) |
| RF-02 | Subir marcha con selector "+" | Requisito | Alta / Esencial | Clase Selector de marcha (pulsar "+") |
| RF-03 | Bajar marcha con selector "−" | Requisito | Alta / Esencial | Clase Selector de marcha (pulsar "−") |
| RF-04 | Cambio de modo de funcionamiento | Requisito | Media / Deseado | Clase Selector de modo (`cambiar()`) |
| RF-05 | *(sección 3.2.5 vacía en el SRS)* | — | — | Aparece en el caso de uso "Pisar / soltar pedal de embrague" |
| RF-06 | Consulta del estado de la transmisión | Requisito | Media / Deseado | Unidad de control (modo y marcha actual) |
| RNF-01 | Tiempo de respuesta del cambio de marcha (≤ 16 ms, 60 FPS) | Restricción | Alta / Esencial | Expectativa de experiencia de juego |
| RNF-02 | Integridad del estado interno del simulador | Restricción | Alta / Esencial | Calidad del software de simulación |
| RNF-03 | Fiabilidad (< 1 fallo cada 10.000 cambios) | Restricción | Alta / Esencial | Calidad del software de simulación |
| RNF-04 | Disponibilidad durante la sesión de juego (100 %) | Restricción | Alta / Esencial | Expectativa de experiencia de juego |
| RNF-05 | Mantenibilidad (SOLID, cobertura de pruebas ≥ 80 %) | Restricción | Media / Deseado | Estándares de desarrollo de la empresa |
| RNF-06 | Portabilidad (≥ 90 % del código independiente de plataforma) | Restricción | Media / Deseado | Estrategia de distribución del videojuego |

El SRS también incluye un requisito de localización (§3.4): los identificadores de marcha que se muestran en el HUD deben ser configurables.

## 4. Validación

- **Estado del SRS:** su ficha indica que la verificación del departamento de calidad está *pendiente* y que la aprobación está *pendiente de revisión por el docente*.
- **Casos de prueba:** están en el apéndice 4.1 del SRS. Ninguno tiene resultado Pass/Fail registrado.

| Caso de prueba | Qué verifica | Requisitos que indica el SRS |
|---|---|---|
| TC_FUNCT_01 | Cambio de marcha con la palanca en modo Manual | RF-01, RF-02 |
| TC_FUNCT_02 | El selector "+" sube una marcha y respeta el límite superior | RF-03 |
| TC_FUNCT_03 | El selector "−" baja una marcha y respeta el límite inferior | RF-04 |
| TC_FUNCT_04 | Embrague al pisar/soltar; se bloquea el cambio con el embrague engranado | RF-05 |
| TC_FUNCT_06 | El HUD expone marcha, RPM y modo con latencia ≤ 16 ms | RF-06 |
| TC_NFUNC_01 | Ciclo de actualización ≤ 16 ms (≥ 60 fps) en carga normal y máxima | RNF-01 |

Observaciones que ya están registradas en la matriz:

- TC_FUNCT_02 y TC_FUNCT_03 indican un requisito distinto del que prueban (el selector "+" es RF-02 y el "−" es RF-03).
- TC_FUNCT_01 y TC_FUNCT_02 usan una 6.ª marcha, aunque el SRS define 5.
- RNF-02 a RNF-06 no tienen caso de prueba.

## 5. Cadena de trazabilidad

Necesidad → requisito (SRS) → clase del diagrama → paso del diagrama de actividad (`SIM-DAC-001`) → caso de prueba.

| Requisito | Clase / componente | Paso en el diagrama de actividad | Caso de prueba |
|---|---|---|---|
| RF-01 | Palanca, Unidad de Control, Embrague, Caja de cambios | Accionar palanca o selector → ¿Cambio de marcha válido? → Aplicar cambio de marcha | TC_FUNCT_01 |
| RF-02 | Selector de marcha, Unidad de Control | Accionar palanca o selector (+ / −) → Aplicar cambio de marcha | TC_FUNCT_02 |
| RF-03 | Selector de marcha, Unidad de Control | Accionar palanca o selector (+ / −) → Aplicar cambio de marcha | TC_FUNCT_03 |
| RF-04 | Selector de modo, Unidad de Control | ¿Modo de funcionamiento? → (Automático) Monitorear RPM → ¿RPM fuera de umbral? → Determinar marcha objetivo | — |
| RF-05 | Pedal, Embrague | (Manual) Pisar / soltar pedal de embrague | TC_FUNCT_04 |
| RF-06 | Unidad de Control | Calcular relación de transmisión, velocidad y RPM → Actualizar indicadores | TC_FUNCT_06 |
| RNF-01 | Todo el ciclo de cambio de marcha | — | TC_NFUNC_01 |

El detalle completo por requisito (stakeholder, criterios de aceptación, módulo, responsable, estado y notas) está en la hoja **Matriz principal** de [`Matriz de trazabilidad.xlsx`](<Matriz de trazabilidad.xlsx>).

## 6. Gestión de cambios

- **Iteraciones:** todos los artefactos de esta rama están en la versión 1.0, con una sola iteración.
- **Diagrama de impacto (`SIM-DIM-002`):** registra el análisis de impacto de la **RFC-B1 "nodo de cambio": promedio de las últimas 3 simulaciones**.

| Elemento | Contenido del diagrama |
|---|---|
| Necesidad de negocio | NEG-01: fiabilidad de asignación |
| Requisitos afectados | REQ-ASIGNACION (criterio de asignación), REQ-SIMULADOR (guarda los últimos 3 valores) |
| Código | Motor de asignación |
| Documentación | Manual del operador |
| Plan | Sprint actual |
| Pruebas | TC-107, TC-108 |

- **Evolución prevista:** el SRS (§2.6) lista la evolución previsible del sistema, pero no son solicitudes de cambio registradas:
  - cajas de 6, 7 u 8 marchas;
  - cambio automático basado en curvas de par y potencia;
  - simulación de desgaste y fallos;
  - transmisiones de doble embrague (DCT) y secuenciales;
  - integración con realidad virtual.
