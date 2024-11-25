# Proyecto de Inventario de Objetos
## CREADO POR JOSE DIEGO JUNQUERA LOBÓN -> JJUNLOB074

Este repositorio contiene el proyecto final de **gestión de inventario de objetos** desarrollado como parte del curso de Python de IBM. El proyecto incluye diferentes implementaciones que muestran cómo gestionar un inventario a través de varias interfaces:

- **Consola**: Una versión interactiva para gestionar el inventario desde la terminal.
- **Automática**: Un script que gestiona el inventario de forma automatizada.
- **Tkinter**: Una interfaz gráfica de usuario simple basada en Python.
- **Flask Web**: Una aplicación web ligera para gestionar el inventario.

## Características

### Consola
- Gestión interactiva del inventario (añadir, eliminar, buscar y listar objetos).
- Interfaz sencilla para trabajar directamente desde la terminal.

### Automática
- Ejecución en consola automática del programa en python

### Tkinter / NECESITA TKINTER
- Interfaz gráfica intuitiva para usuarios no técnicos.
- Soporte para acciones comunes del inventario: añadir, buscar, editar y eliminar.

### Flask Web / NECESITA FLASK
- Aplicación web ligera y rápida para acceder al inventario desde un navegador.
- Endpoints RESTful para integrar con otras aplicaciones.
- Página de inicio para visualizar y gestionar los objetos.

## Instalación

**Clonar el repositorio**:
   Abre una terminal y ejecuta el siguiente comando para clonar este repositorio:
   ```bash
   git clone https://github.com/jjunlob074/pythonfinalIBM.git
   cd proyecto-inventario
   ```

## Cómo Crear un Entorno Virtual en Python

Un entorno virtual es una forma de aislar proyectos de Python para garantizar que las dependencias de un proyecto no interfieran con las de otro. A continuación, se explica cómo crear y usar un entorno virtual en Python.

---

### 1. Verificar la instalación de Python

Asegúrate de tener Python instalado en tu sistema. Abre una terminal y ejecuta:

```bash
python --version
```

o, en algunos sistemas:

```bash
python3 --version
```

Esto debería mostrar la versión instalada de Python. Si no está instalado, descárgalo desde [python.org](https://www.python.org/).

---

### 2. Crear el entorno virtual

Para crear un entorno virtual, usa el siguiente comando:

```bash
python -m venv nombre_del_entorno
```

o:

```bash
python3 -m venv nombre_del_entorno
```

Reemplaza `nombre_del_entorno` con el nombre que quieras para tu entorno virtual.

---

### 3. Activar el entorno virtual

#### En Windows:
```bash
nombre_del_entorno\Scripts\activate
```

#### En Linux/Mac:
```bash
source nombre_del_entorno/bin/activate
```

Cuando el entorno está activado, deberías ver su nombre al inicio de la línea de comandos, algo como esto:

```bash
(nombre_del_entorno) $
```

---

### 4. Instalar paquetes dentro del entorno virtual

Con el entorno activado, puedes instalar paquetes con `pip` sin afectar el sistema global:

```bash
pip install nombre_paquete
```

Por ejemplo:

```bash
pip install requests
```

---

### 5. Desactivar el entorno virtual

Cuando termines de trabajar, desactiva el entorno virtual con:

```bash
deactivate
```

---

### 6. Eliminar el entorno virtual

Si ya no necesitas el entorno virtual, simplemente elimina la carpeta `nombre_del_entorno`:

```bash
rm -rf nombre_del_entorno
```

En Windows, puedes eliminar la carpeta desde el Explorador de Archivos.

---

¡Eso es todo! Ahora sabes cómo crear y manejar un entorno virtual en Python.
