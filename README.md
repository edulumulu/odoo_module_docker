# Proyecto: Administración de Formación de Empleados con Odoo y Docker

Este proyecto tiene como objetivo administrar la formación de los empleados de la empresa utilizando **Odoo**, **Docker**, **PostgreSQL** y **pgAdmin**. Se ha desarrollado un módulo personalizado para gestionar cursos, sesiones y formadores dentro de la plataforma.

## Descripción

He creado un módulo para Odoo que permite gestionar la formación de los empleados, llamado **work_training**. El módulo incluye:

- **Creación de nuevas tablas**:
  - `course`: Información sobre los cursos ofrecidos.
  - `session`: Detalles de cada sesión de formación.
  - `trainer`: Información sobre los formadores.

- **Modificación de tablas existentes mediante herencia**:
  - `partner`: Para gestionar los contactos relacionados con los empleados y formadores.
  - `employee`: Para agregar campos específicos relacionados con la formación de los empleados.

- **Vistas personalizadas**:
  - Se han creado vistas para gestionar cada módulo (curso, sesión, formador) y para las tablas modificadas (`partner`, `employee`).

- **Generación de reportes**:
  - El sistema permite generar un reporte con las sesiones de formación realizadas por cada trabajador.

## Tecnologías Utilizadas

- **Odoo**: Plataforma ERP utilizada para la gestión empresarial.
- **Docker**: Se ha utilizado Docker para contenerizar la aplicación, facilitando su despliegue y configuración en cualquier entorno.
- **PostgreSQL**: Base de datos para almacenar los datos del módulo.
- **pgAdmin**: Herramienta para la administración y gestión de la base de datos PostgreSQL.

## Estructura del Proyecto

- **Módulo `work_training`**: Contiene la lógica y las vistas para gestionar la formación de los empleados.
- **Docker Compose**: Configuración para desplegar Odoo, PostgreSQL y pgAdmin de manera rápida y eficiente.


📌 **Autor:** *edulumulu* 
