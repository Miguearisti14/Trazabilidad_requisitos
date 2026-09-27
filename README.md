# Proyecto Dietas — Dietas al Día (`DIE`)

Rama `dietas` del repositorio de trazabilidad de requisitos. El índice general de todos los proyectos está en la rama [`master`](https://github.com/Miguearisti14/Trazabilidad_requisitos).

## Versiones actuales

| ID | Artefacto | Tipo | Versión | Estado final | Autor o revisor | Fecha de cierre |
|---|---|---|---|---|---|---|
| `DIE-PRO-001` | [Github_prototipo.html](<Github_prototipo.html>) | Prototipo | 1.0 | Se realizó solo 1 iteración | Miguel Aristizabal | 21/09/2026 |

El artefacto es un enlace al repositorio del prototipo: <https://github.com/Miguearisti14/Prototipado>. La información de esta página proviene del README de ese repositorio.

---

## 1. Contexto del proyecto

*Dietas al Día* es un prototipo MVP de alta fidelidad, construido como aplicación web progresiva (PWA), para el Departamento de Nutrición. Los datos son simulados y no tiene backend ni autenticación real.

- **Tecnología:** React 18 + Vite, styled-components, react-router-dom y lucide-react.
- **Persistencia:** los cambios se guardan en `localStorage`.

## 2. Necesidades originales

El prototipo valida la épica **EPC 28 – Asignación de tratamiento nutricional**:

> Como médico del Departamento de Nutrición quiero consultar las dietas compatibles con el diagnóstico de un paciente, señalando explícitamente si alguna dieta contiene alimentos incompatibles con sus alergias registradas, para elegir con seguridad un tratamiento sin cruzar manualmente la historia clínica con el catálogo de dietas.

## 3. Requisitos priorizados

El artefacto no registra prioridades. Los requisitos que cubre el prototipo son:

| ID | Requisito |
|---|---|
| EPC 28 | Asignación de tratamiento nutricional (flujo principal que valida el prototipo) |
| RF1 | Catálogo de alimentos (alta, edición y búsqueda) |
| RF2 | Catálogo de nutrientes |
| RF3 | Catálogo de vitaminas y minerales |
| RF4 | Dietas prediseñadas con sus alimentos |
| RF5 | Enfermedades con sus dietas asociadas |
| RF6 | Historia clínica del paciente (desde la ficha del paciente) |

## 4. Validación

Criterios de aceptación de la EPC 28 y cómo los cumple el prototipo:

| Criterio | Implementación |
|---|---|
| **CA1** Dietas del diagnóstico en un paso | Al abrir un paciente se muestran, agrupadas por enfermedad, todas las dietas asociadas ya cruzadas con sus alergias |
| **CA2** Alerta inequívoca | Las dietas con alimentos alérgenos o incompatibles llevan borde y banda roja con el alimento y el motivo. El rojo se usa solo para esto |
| **CA3** Ficha técnica sin perder contexto | La ficha se abre en un panel lateral (hoja completa en móvil) con el nombre y las alergias del paciente fijos en la cabecera |
| **CA4** Dieta segura en < 90 s | Flujo de 3 clics: paciente → *Asignar* → *Confirmar*. Si se elige una dieta con alerta, se exige marcar una casilla de revisión y se ofrece la alternativa segura |

Escenarios de demostración usados para validar:

| Paciente | Escenario |
|---|---|
| María López García | Diabetes tipo 2 con alergia a lácteos: la dieta hipocalórica contiene yogur (alerta) y la mediterránea es segura |
| Carlos Ruiz Mendoza | Anemia ferropénica con alergia a moluscos: la dieta rica en hierro hemo contiene mejillones |
| Ana Torres Vidal | Dos diagnósticos, alergia a frutos secos e incompatibilidad con pomelo (fármaco) |
| Jorge Pérez Sanz | Fenilcetonuria sin dietas prediseñadas (estado vacío) y peso sin registrar |
| Lucía Fernández Gil | Sin diagnóstico registrado (estado vacío) |

## 5. Cadena de trazabilidad

Necesidad (EPC 28) → criterio de aceptación → implementación en el prototipo:

| Requisito | Elemento del prototipo |
|---|---|
| EPC 28 / CA1–CA2 | `logic/compatibilidad.js`: cruza las alergias e incompatibilidades del paciente con los componentes de las dietas |
| EPC 28 / CA2–CA4 | `components/`: tarjeta de dieta, ficha técnica y confirmación |
| EPC 28 / CA1, CA4 | `pages/`: Pacientes y Paciente (tratamiento) |
| RF1–RF5 | `pages/` Catálogos y `data/catalogos.js` (configuración de campos de cada catálogo) |
| RF6 | Ficha del paciente (historia clínica) |
| Todos | `data/mockData.js`: datos simulados coherentes entre catálogos |

Los catálogos (RF1–RF6) alimentan el flujo principal. Por ejemplo, añadir un alérgeno a un alimento o una alergia a un paciente actualiza al instante las alertas de sus dietas.

## 6. Gestión de cambios

- **Versión:** el prototipo está en la versión **1.0**, con una sola iteración. Fecha de cierre: 21/09/2026.
- **Solicitudes de cambio:** no hay RFC ni solicitudes de cambio registradas para este proyecto.
