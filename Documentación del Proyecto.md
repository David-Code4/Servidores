# 

## 1. Problema

La iglesia “SOS Para tu vida” enfrenta dificultades para organizar y agendar a las personas que sirven semanalmente en distintas áreas del ministerio: seguridad, comunicaciones, consolidación, ujieres, alabanza, kids e intercesión.  
Actualmente, el proceso se realiza de forma manual (por chats o hojas de cálculo), lo que genera confusión, duplicaciones y olvidos sobre quién sirve y en qué fecha.

Esto ocasiona que:

- Algunas áreas queden sin personal asignado.  
- Las personas no sepan cuándo les corresponde servir.  
- No exista un control centralizado del equipo de servidores.

---

## 2. Objetivo general

Desarrollar un programa en Python nativo que permita registrar, organizar y asignar personas a las diferentes áreas de servicio de la iglesia, de manera fácil y ordenada.

---

## 3. Objetivos específicos

- Permitir registrar servidores (nombre, edad, área, disponibilidad, etc.).  
- Mostrar una lista de todas las personas registradas por área.  
- Permitir seleccionar quiénes servirán en una fecha o evento determinado.  
- Guardar y consultar las asignaciones de cada semana.  
- Ofrecer una interfaz de consola clara y fácil de usar.

---

## 4. Historias de usuario

### Criterios de Aceptación

**HU01:** Como coordinador, quiero registrar a los servidores con sus datos personales para tener un control organizado.  
- El sistema debe permitir ingresar nombre, edad, y área de servicio.  
- Debe confirmar el registro exitoso.

**HU02:** Como coordinador, quiero ver la lista completa de servidores por área para poder planificar quiénes servirán.  
- El sistema debe permitir filtrar por área (seguridad, kids, etc.).  
- Debe mostrar nombre y disponibilidad.

**HU03:** Como coordinador, quiero asignar servidores a una fecha específica para definir el equipo de cada servicio.  
- El sistema debe permitir seleccionar un área y asignar servidores.  
- Debe guardar la fecha y los nombres asignados.

**HU04:** Como coordinador, quiero consultar quién sirvió en una fecha pasada para llevar un registro histórico.  
- El sistema debe listar las asignaciones previas.

**HU05:** Como administrador, quiero poder eliminar o actualizar la información de un servidor.  
- El sistema debe permitir buscar por nombre y modificar o eliminar su registro.

---

## 5. Requerimientos del sistema

### Requerimientos funcionales

- **RF01:** Registrar nuevos servidores con nombre, área y disponibilidad.  
- **RF02:** Mostrar la lista de servidores registrados.  
- **RF03:** Filtrar servidores por área.  
- **RF04:** Asignar servidores a fechas específicas.  
- **RF05:** Consultar historial de asignaciones.  
- **RF06:** Modificar o eliminar servidores.

### Requerimientos no funcionales

- **RNF01:** La interfaz debe ser de línea de comandos, clara y simple.  
- **RNF02:** El programa debe guardar los datos en un archivo local (servidores.json o .txt).  
- **RNF03:** El código debe ser modular, utilizando funciones y estructuras como listas y diccionarios.  
- **RNF04:** El sistema debe ser escalable a una versión web o interfaz gráfica.
