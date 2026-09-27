# Proyecto Tripulaciones — Sistema Integral de Gestión de Tripulaciones (`TRI`)

Rama `tripulaciones` del repositorio de trazabilidad de requisitos. El índice general de todos los proyectos está en la rama [`master`](https://github.com/Miguearisti14/Trazabilidad_requisitos).

## Versiones actuales

| ID | Artefacto | Tipo | Versión | Estado final | Autor o revisor | Fecha de cierre |
|---|---|---|---|---|---|---|
| `TRI-RFC-001` | [RFC_Actividades_Desarrolladas.pdf](<RFC_Actividades_Desarrolladas.pdf>) | RFC (Request for Change) | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 15/09/2026 |
| `TRI-PBL-002` | [Product_backlog.html](<Product_backlog.html>) | Product Backlog | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 04/08/2026 |
| `TRI-VIS-003` | [Vision-Board.docx](<Vision-Board.docx>) | Vision Board | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 26/07/2026 |

---

## 1. Contexto del proyecto

Una compañía aérea desea implantar un sistema informático para controlar la asignación de tripulaciones a los vuelos que opera. Cada tripulación está compuesta por un piloto y un copiloto. El criterio busca que la tripulación asignada a cada vuelo sea la más adecuada según las aptitudes profesionales del piloto y las características del vuelo.

**Consultas de la tripulación.** Los miembros de las tripulaciones pueden consultar:

- los vuelos que tienen asignados;
- las características de cualquier vuelo, esté asignado a ellos o no: fecha, origen, destino y condiciones meteorológicas y de visibilidad previstas.

**Datos que registra el personal administrativo:**

- tripulantes: nombre, número de empleado y fecha de nacimiento;
- tripulaciones: vuelos efectuados, horas de vuelo y observaciones;
- vuelos.

**Simulador de evaluación.** La compañía evalúa a los pilotos con un simulador externo al sistema:

- Las condiciones se recrean con parámetros de tres tipos: visibilidad, meteorología y relieve.
- Cada parámetro tiene un valor de dificultad y un factor de peso. Los de meteorología tienen además una frecuencia.
- Las combinaciones estandarizadas de parámetros se llaman escenarios.
- Cada piloto debe hacer al menos una simulación anual en cada escenario.
- El resultado es un valor numérico con fecha, único por piloto y escenario: al registrar uno nuevo se eliminan los anteriores. El personal administrativo lo actualiza periódicamente.
- Los pilotos pueden consultar los escenarios estándar y su evaluación en ellos.

**Asignación.** Los operadores de vuelos comparan las características de cada vuelo con los escenarios, eligen el más aproximado y asignan la tripulación. El piloto elegido debe ser el de mayor puntuación en ese escenario.

**Producto definido en el Vision Board (`TRI-VIS-003`):**

- **Nombre:** Sistema Integral de Gestión de Tripulaciones.
- **Frase representativa:** *"Proveer un sistema que permita administrar la información de vuelos, tripulaciones y simulaciones para asignar la tripulación más adecuada a cada vuelo."*

## 2. Necesidades originales

Grupos de usuarios del Vision Board:

| Grupo | Rol |
|---|---|
| Operadores de vuelos | Analizan las condiciones de los vuelos y asignan la tripulación más adecuada según sus resultados en las simulaciones |
| Pilotos y copilotos | Consultan sus vuelos asignados y los resultados de sus simulaciones |
| Personal administrativo | Registra y actualiza la información de tripulantes, tripulaciones, vuelos, escenarios y resultados de simulación |

Necesidades registradas en el Vision Board:

1. Los pilotos necesitan conocer sus resultados de simulación para hacer seguimiento a su desempeño.
2. El personal administrativo necesita registrar y actualizar información de forma sencilla y confiable.
3. La asignación de tripulaciones debe basarse en criterios objetivos y no en decisiones manuales.
4. La información de pilotos, tripulaciones, vuelos y simulaciones se debe centralizar.
5. Se necesita una integración con el simulador que sincronice los escenarios estándar y las evaluaciones de los pilotos de forma confiable y oportuna.

## 3. Requisitos priorizados

**Product Backlog.** El artefacto `TRI-PBL-002` enlaza al Product Backlog gestionado en Zoho Projects ([enlace](https://projects.zoho.com/portal/miguearisti8gmaildotcom#project/2702536000000101766)). También menciona un Product Backlog de Federico que estaba como archivo adjunto y no está en el repositorio. El detalle de sus ítems y prioridades no está en esta rama.

**Funcionalidades del Vision Board:**

- Acceso rápido de los pilotos a sus resultados de simulación por escenario.
- Módulo centralizado para administrar pilotos, copilotos, tripulaciones, vuelos, escenarios y resultados.
- Recomendación de la tripulación más adecuada para cada vuelo, con reglas de negocio basadas en las competencias en simulación y las características del vuelo.
- Plataforma única de consulta según el perfil de cada usuario.
- Sincronización de escenarios estándar y evaluaciones con el simulador.

**Requisitos afectados por cambios.** Los requisitos del SRS que se nombran en `TRI-RFC-001`, con la prioridad de la RFC que los modifica:

| Requisito | Redacción actual | RFC | Prioridad |
|---|---|---|---|
| Comparación vuelo–escenarios | "El sistema compara altitud y destino del vuelo con los escenarios disponibles" | RFC-A1 | Alta |
| REQ-ASIGNACIÓN | "El piloto con puntuación más alta en el escenario elegido" | RFC-B1 | Alta |
| REQ-RESULTADO-SIMULADOR | "El resultado es único para cada piloto en cada escenario, eliminándose los resultados anteriores" | RFC-B1 | Alta |
| Criterio de certificación | Basado en "Habilidades Máximas" | RFC-C2 | Crítica |

**Priorización del CCB (Actividad 3, nivel avanzado).** El CCB decidió por mayoría (4 votos contra 1) priorizar el incremento de la **frecuencia de simulaciones** sobre la **mejora de UI** del panel del operador. La mejora de UI quedó en el backlog.

## 4. Validación

**Criterios de aceptación de RFC-A1** (escenarios de tormenta):

1. Si un vuelo tiene registrada una alerta de tormenta eléctrica, al comparar con los escenarios estándar el sistema muestra solo los escenarios con el parámetro "Alerta Meteorológica Extrema" y una dificultad mayor a cero.
2. Si un escenario no tiene ese parámetro configurado, el sistema lo excluye automáticamente de las opciones que sugiere para un vuelo con alerta de tormenta.

**Pruebas previstas en las RFC:**

- **RFC-B1:** actualizar los casos de prueba de asignación de tripulación, para que verifiquen el promedio en lugar del máximo, y los de registro de resultados del simulador, para que cubran el histórico.
- **RFC-B2:** 2 días de QA para casos borde: piloto novel sin horas reales, veterano sin simulaciones recientes y empate entre pilotos.
- **RFC-C2:** actualizar los casos de prueba del proceso de certificación y ejecutar pruebas de regresión sobre el motor de asignación. La validación está a cargo del QA Lead.

## 5. Cadena de trazabilidad

Cada escenario de cambio del documento *Casos de Estudio: Escenarios de Cambio* (Academia de Operaciones Aéreas) está trazado hasta su RFC:

| Caso | Origen | RFC |
|---|---|---|
| A1 El Factor Meteorológico | Correo electrónico – Cap. Ricardo Méndez | RFC-A1 |
| A2 El Cuello de Botella Administrativo | Informe de Gestión | RFC-A2 |
| B1 La Trampa del "Golpe de Suerte" | Memorando de QA – Ing. Sofía Valdés | RFC-B1 |
| B2 Teoría vs. Práctica | Nota técnica – Dirección de Entrenamiento | RFC-B2 |
| C1 La Promesa de la IA | Propuesta de Transformación Digital | RFC-C1 |
| C2 El Choque Normativo | Circular de la Autoridad de Aviación Civil (AAC) | RFC-C2 |
| Caso adicional (Actividad 4, nivel inicial) | Dirección de Seguridad Operacional | RFC-A3 |
| Actividad 3, nivel intermedio | Dirección de Transformación Digital / Operaciones | RFC-B3 |

La RFC-B1 (sección 5.1) traza el cambio desde el requisito hasta el código y la documentación:

| Artefacto | Impacto |
|---|---|
| SRS / REQ-ASIGNACIÓN | Pasa a "el piloto con el mayor promedio de sus últimas 3 simulaciones en el escenario elegido" |
| SRS / REQ-RESULTADO-SIMULADOR | Debe conservar al menos los últimos 3 resultados por piloto y escenario |
| Casos de prueba | Asignación de tripulación y registro de resultados del simulador |
| Módulo de código | Servicio de cálculo de puntuación de pilotos, motor de comparación de escenarios y modelo de datos "Resultado de simulación por piloto y escenario" |
| Documentación de usuario | Manual del operador de vuelos y guía de interpretación de resultados del simulador |

**Dependencia entre RFC-C2 y RFC-B1.** La "Estabilidad de Competencias" que exige la norma NAC-2026 necesita el mismo histórico de simulaciones que propone RFC-B1. Por eso las dos RFC comparten un único cambio en el modelo de datos y deben aprobarse y ejecutarse en sincronía.

## 6. Gestión de cambios

Solicitudes de cambio registradas en `TRI-RFC-001`:

| RFC | Título | Solicitante | Tipo | Prioridad | Decisión / estado |
|---|---|---|---|---|---|
| RFC-A1 | Parámetro "Alerta Meteorológica Extrema" en la selección de escenarios | Cap. Ricardo Méndez | Mejora funcional | Alta | Sin decisión registrada |
| RFC-A2 | Notificación automática de la asignación vía Teams/Email | Área de Gestión Operativa | Mejora funcional | Media | Sin decisión registrada |
| RFC-A3 | Validación para impedir asignar pilotos no aptos | Dirección de Seguridad Operacional | Corrección de defecto | Crítica | Sin decisión registrada |
| RFC-B1 | Puntuación por promedio de las últimas 3 simulaciones | Ing. Sofía Valdés | Mejora funcional | Alta | Sin decisión registrada |
| RFC-B2 | Fórmula híbrida: 70 % simulación + 30 % horas de vuelo reales | Dirección de Entrenamiento | Mejora funcional | Media | Esfuerzo estimado ≈ 6 días |
| RFC-B3 | Eliminar la validación manual del operador de vuelos | Dirección de Transformación Digital / Operaciones | Cambio de arquitectura | Baja | Riesgos analizados si se aprueba y si se rechaza |
| RFC-C1 | Machine Learning para predecir el escenario | Propuesta de Transformación Digital | Cambio de arquitectura | No aplica | **Rechazada por el CCB**: modelo de "caja negra" no justificable ante auditorías |
| RFC-C2 | Alineación de la certificación con la norma NAC-2026 | Circular de la AAC | Cambio regulatorio | Crítica | Plan de implementación en 8 pasos para el sprint entrante; depende de RFC-B1 |
