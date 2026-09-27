# Proyecto Mudanzas — Portal Web de Transporte de Carga (`MUD`)

Rama `mudanzas` del repositorio de trazabilidad de requisitos. El índice general de todos los proyectos está en la rama [`master`](https://github.com/Miguearisti14/Trazabilidad_requisitos).

## Versiones actuales

| ID | Artefacto | Tipo | Versión | Estado final | Autor o revisor | Fecha de cierre |
|---|---|---|---|---|---|---|
| `MUD-MOD-001` | [Modelado de SW.qea](<Modelado de SW.qea>) | Modelo UML (Enterprise Architect) | 2.0 | Se realizaron 2 iteraciones | Miguel Aristizabal | 10/08/2026 |

El modelo (paquete *Empresa de Mudanzas*) incluye tres diagramas:

- **Diagrama de casos de uso:** *Basic Use Case Model*.
- **Diagrama de clases:** *Domain Model*.
- **Diagrama entidad relación:** *Contiene*.

---

## 1. Contexto del proyecto

Una empresa de administración de hosting recibe el requerimiento de asesorar el rediseño de un portal web en el que se publicitan empresas de transporte de carga que ofrecen sus servicios y productos en Colombia.

En el portal los clientes pueden rellenar solicitudes de servicio a las distintas empresas. Después, tanto el cliente como la empresa de mudanzas pueden aceptar o rechazar esas solicitudes. La información se obtuvo en entrevistas con los gerentes de las empresas.

## 2. Necesidades originales

Obtenidas de las entrevistas con los gerentes:

1. **Empresas:** guardar el nombre (único), la dirección completa, los teléfonos y las poblaciones (nombre y provincia) donde ofrece servicios.
2. **Servicios:** cada empresa oferta distintos servicios (transporte, embalaje, desmontar/montar muebles, grúas, etc.), no necesariamente los mismos ni en las mismas poblaciones.
3. **Precios:** los servicios se identifican con un nombre común al sector. Se guarda el precio/hora de cada servicio por empresa y población.
4. **Transporte regulado:** los servicios de transporte están regulados por ley según intervalos estándar de peso (kg).
5. **Recargo por peso:** en transporte hay un plus de precio si la carga supera una cantidad de kg que fija cada empresa, sin importar la población (por ejemplo, 10 % sobre 500 kg o 15 % sobre 750 kg).
6. **Vehículos:** tamaño de carga, placa, conductor y otros datos generales.
7. **Solicitudes:**
   - Tienen un código único y registran la empresa, los servicios pedidos y las direcciones de inicio y de destino. Las direcciones deben estar dentro de las poblaciones que atiende la empresa.
   - Registran la fecha de solicitud y la de resolución, si fue aceptada o no, el precio total y el precio de cada servicio.
8. **Clientes:** código único, CC, dirección, nombre completo y teléfonos.
9. **Ejecución:** tras la aceptación se registran la fecha real, el tiempo de cada servicio y los empleados que trabajaron.
10. **Empleados:** CC, dirección, nombre, teléfono de contacto y de empresa, tipo y sueldo. Cualquier empleado puede hacer cualquier trabajo, y un empleado puede trabajar para varias empresas en distintos momentos.
11. **Pagos:** todos los pagos de los clientes se hacen por adelantado.

## 3. Requisitos priorizados

El modelo no asigna prioridades a los requisitos. Los requisitos funcionales están expresados como casos de uso del diagrama *Basic Use Case Model* (sistema *Portal Web de Transporte de Carga*):

| Actor | Casos de uso |
|---|---|
| Cliente | Crear solicitud de servicio · Consultar historial de solicitudes · Buscar empresas y servicios por población · Consultar precios de servicios · Aceptar / rechazar resolución de solicitud |
| Empresa de transporte | Gestionar datos de la empresa · Ofertar servicios · Gestionar vehículos · Gestionar empleados · Gestionar servicios y precios por población · Aceptar / rechazar solicitudes del cliente · Gestionar recargo por peso · Registrar ejecución del servicio |
| Administrador | Gestionar tipos de transporte · Gestionar catálogo de servicios |

Relaciones `include` del modelo:

- *Crear solicitud de servicio* incluye *Registrarse / Autenticarse* y *Buscar empresas y servicios por población*.
- *Consultar historial de solicitudes* incluye *Registrarse / Autenticarse*.

## 4. Validación

Los artefactos de este proyecto no incluyen casos de prueba, criterios de aceptación ni registros de validación.

## 5. Cadena de trazabilidad

Necesidad → caso de uso → clase (*Domain Model*) → entidad (diagrama ER):

| Necesidad | Caso(s) de uso | Clase | Entidad ER |
|---|---|---|---|
| 1. Empresas | Gestionar datos de la empresa | EmpresaTransporte, Población | EMPRESA TRANSPORTE, POBLACIÓN |
| 2–3. Servicios y precios | Ofertar servicios · Gestionar servicios y precios por población · Gestionar catálogo de servicios | Servicio, Oferta (empresa + servicio + población → precio/hora), Servicio Montaje, Servicio Grua | SERVICIO, SERVICIO_MONTAJE, SERVICIO_GRUA (relación *Oferta*) |
| 4. Transporte regulado | Gestionar tipos de transporte | ServicioTransporte, IntervaloKg | SERVICIO_TRANSPORTE, INTERVALO_KG (*Tiene Intervalo*) |
| 5. Recargo por peso | Gestionar recargo por peso | PlusKg (umbral kg, % recargo) | PLUS_KG (*Define*) |
| 6. Vehículos | Gestionar vehículos | Vehiculo | VEHICULO (*Posee*) |
| 7. Solicitudes | Crear solicitud de servicio · Aceptar / rechazar solicitudes · Aceptar / rechazar resolución · Consultar historial | Solicitud, Detalle Solicitud | SOLICITUD, DETALLE_SOLICITUD (*Realiza*, *Para*, *Contiene*) |
| 8. Clientes | Registrarse / Autenticarse | Cliente | CLIENTE |
| 9. Ejecución | Registrar ejecución del servicio | Detalle Solicitud (fecha real, tiempo empleado), asociación Empleado–Solicitud | DETALLE_SOLICITUD |
| 10. Empleados | Gestionar empleados | Empleado (asociación 1..* con EmpresaTransporte) | EMPLEADO (*Trabaja En*) |

## 6. Gestión de cambios

- **Versión:** el modelo está en la versión **2.0**, tras **2 iteraciones**. Fecha de cierre: 10/08/2026.
- **Fechas registradas en el modelo:** el diagrama de casos de uso se creó y modificó el 10/08/2026. El diagrama de clases y el diagrama ER se crearon el 10/08/2026 y su última modificación es del 16/08/2026.
- **Solicitudes de cambio:** no hay RFC ni solicitudes de cambio registradas para este proyecto.
