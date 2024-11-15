# Proyecto de Visualización y Exportación de Datos

Este proyecto permite a los usuarios gestionar datos mediante una interfaz gráfica construida con `Tkinter`, realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y visualizar los datos en gráficos interactivos. También incluye la funcionalidad de exportar datos a un archivo Excel.

## **Requisitos del Sistema**

Antes de ejecutar el proyecto, asegúrate de que tu sistema cumple con los siguientes requisitos:

- **Python 3.7 o superior**
- **Bibliotecas necesarias**:
  - `Tkinter` (incluido con Python en la mayoría de distribuciones)
  - `mysql-connector-python`
  - `pandas`
  - `openpyxl`
  - `matplotlib`
  - `seaborn`
- **Servidor MySQL** instalado y configurado.

---

## **Instalación de Dependencias**

### 1. Instalar Python y pip
Si no tienes Python instalado, descárgalo desde [Python.org](https://www.python.org/downloads/). Asegúrate de agregar Python al PATH durante la instalación.

### 2. Instalar las bibliotecas necesarias
Ejecuta el siguiente comando en tu terminal o línea de comandos para instalar las bibliotecas requeridas:

```bash
pip install mysql-connector-python pandas openpyxl matplotlib seaborn
```

### 3. Verificar la instalación de Tkinter
`Tkinter` viene preinstalado con Python en la mayoría de los sistemas. Para verificar si está disponible, abre una terminal y ejecuta:

```bash
python -m tkinter
```

Si aparece una ventana de ejemplo, `Tkinter` está correctamente instalado. Si no, consulta la documentación de tu sistema operativo para instalarlo.

---

## **Configuración de MySQL**

### 1. Crear la base de datos
Asegúrate de tener acceso a un servidor MySQL en funcionamiento. Luego, crea la base de datos y la tabla necesarias:

```sql
CREATE DATABASE proyecto_datos;

USE proyecto_datos;

CREATE TABLE ENCUESTA (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Edad INT NOT NULL,
    Sexo VARCHAR(10) NOT NULL,
    BebidasSemana INT NOT NULL,
    CervezasSemana INT NOT NULL,
    BebidasFinSemana INT NOT NULL,
    BebidasDestiladasSemana INT NOT NULL,
    VinosSemana INT NOT NULL,
    PerdidasControl BOOLEAN,
    DiversionDependenciaAlcohol BOOLEAN,
    ProblemasDigestivos BOOLEAN,
    TensionAlta BOOLEAN,
    DolorCabeza BOOLEAN
);
```

### 2. Configurar la conexión a MySQL
Edita el archivo del proyecto donde se encuentra la función `conectar_db` para agregar tus credenciales de MySQL:

```python
def conectar_db():
    return mysql.connector.connect(
        host="localhost",        # Cambia esto si tu servidor no está en localhost
        user="tu_usuario",       # Reemplaza con tu usuario de MySQL
        password="tu_contraseña",# Reemplaza con tu contraseña de MySQL
        database="proyecto_datos" # Asegúrate de que sea el nombre correcto de tu base de datos
    )
```

---

## **Ejecución del Programa**

### 1. Clonar el repositorio
Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/proyecto_datos.git
cd proyecto_datos
```

### 2. Ejecutar el programa
Ejecuta el archivo principal del proyecto usando Python:

```bash
python main.py
```

---

## **Funciones Principales**

### Operaciones CRUD
1. **Crear (Agregar datos)**:
   - Llena los campos en la interfaz y haz clic en "Agregar".
2. **Leer (Consultar datos)**:
   - Los datos se muestran automáticamente en un `Treeview`.
3. **Actualizar**:
   - Selecciona una fila, edita los campos y haz clic en "Actualizar".
4. **Eliminar**:
   - Selecciona una fila y haz clic en "Eliminar".

### Exportar a Excel
1. Haz clic en el botón "Exportar a Excel".
2. Selecciona la ubicación para guardar el archivo y confirma.

### Visualizar Gráficos
1. **Gráfico de Barras**:
   - Haz clic en el botón "Gráfico de Barras" para mostrar un gráfico de distribución de consumo por grupo de edad.
2. **Gráfico Circular**:
   - Haz clic en el botón "Gráfico Circular" para mostrar un gráfico de proporciones de consumo por grupo de edad.

---

## **Notas Adicionales**
- Asegúrate de tener permisos de escritura en el directorio donde deseas exportar el archivo Excel.
- Si encuentras algún error relacionado con la conexión a la base de datos, verifica que el servidor MySQL esté en ejecución y que las credenciales sean correctas.

---

## **Contribuciones**

Si deseas contribuir a este proyecto, envía un **Pull Request** o crea un **Issue** en el repositorio.

---

## **Licencia**

Este proyecto está licenciado bajo la [MIT License](LICENSE).
```

Este archivo `README.md` proporciona instrucciones claras para la instalación, configuración y uso del proyecto. Puedes personalizarlo según los detalles específicos de tu aplicación.
