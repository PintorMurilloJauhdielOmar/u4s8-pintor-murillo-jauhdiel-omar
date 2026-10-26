# U4S8 — Pintor Murillo Jauhdiel Omar

## Demo en vivo (producción)
https://u4s8-pintor-murillo-jauhdiel-omar.onrender.com/servicios/

## Qué hace este proyecto
Este proyecto es una plataforma web desarrollada en Django para la gestión eficiente y publicación de un catálogo de servicios tecnológicos. Cuenta con autenticación de usuarios donde cada cuenta registrada tiene acceso a un panel interactivo (CRUD) para crear, consultar, actualizar y eliminar exclusivamente sus propios registros, asegurando integridad en la base de datos MySQL en la nube (Aiven).

## Stack técnico
Django + MySQL (Aiven) + Tailwind CSS + Render

## Cómo se prueba el aislamiento por usuario
Cada servicio está vinculado con el usuario que lo registra (`request.user`). El sistema filtra las consultas (`queryset`) en las vistas para que un usuario únicamente pueda visualizar, editar o eliminar los datos creados bajo su propia cuenta activa.

## Historial de unidades
- **Unidad 1:** Portafolio estático con HTML5 semántico + Tailwind CSS desplegado en Render.
- **Unidad 2:** Modelo `Servicio` migrado a MySQL en la nube (Aiven) y despliegue dinámico en Render.
- **Unidad 3:** CRUD completo mediante `ModelForms`, autenticación de usuarios y manejo de sesiones.
- **Unidad 4:** Paginación, filtros de búsqueda, pulido de interfaz de usuario, deploy final y versión etiquetada `v1.0`.
