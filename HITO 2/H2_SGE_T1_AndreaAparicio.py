import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import pandas as pd
from tkinter import filedialog
import seaborn as sns
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Conexión a la base de datos
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="campusfp",
            database="ENCUESTAS"
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se puede conectar a la base de datos: {err}")
        return None
    
#FUNCIONES
#Ingresar persona
def ingresar_persona():
    conexion = conectar_db()
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    bebidasSemana = entry_bebidasSemana.get()
    cervezasSemana = entry_cervezasSemana.get()
    bebidasFinSemana = entry_bebidasFinSemana.get()
    bebidasDestiladasSemana = entry_bebidasDestiladasSemana.get()
    vinosSemana = entry_vinosSemana.get()
    perdidasControl = entry_perdidasControl.get()
    diversionDependenciaAlcohol = entry_diversionDependenciaAlcohol.get()
    problemasDigestivos = entry_problemasDigestivos.get()
    tensionAlta = entry_tensionAlta.get()
    dolorCabeza = entry_dolorCabeza.get()
    
    if not edad or not sexo or not bebidasSemana or not cervezasSemana or not bebidasFinSemana or not bebidasDestiladasSemana or not vinosSemana or not perdidasControl or not diversionDependenciaAlcohol or not problemasDigestivos or not tensionAlta or not dolorCabeza:
        messagebox.showwarning("Campos incompletos", "Asegúrese de rellenar todos los campos por favor")
        return

    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(edad, sexo, bebidasSemana, cervezasSemana, bebidasFinSemana, bebidasDestiladasSemana, vinosSemana, perdidasControl, diversionDependenciaAlcohol, problemasDigestivos, tensionAlta, dolorCabeza))
            conexion.commit()
            messagebox.showinfo("Correcto", "Respuestas guardadas correctamente")
        except mysql.connector.Error as err:
            messagebox.showwarning("Error", f"No se han podido guardar los datos: {err}")
        finally:
            cursor.close()
            conexion.close()
            mostrar_persona()

#Mostrar
def mostrar_persona():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            for item in treeview.get_children():
                treeview.delete(item)
            cursor.execute("SELECT * FROM ENCUESTA")
            for cliente in cursor.fetchall():
                treeview.insert("", tk.END, values=cliente)
        except mysql.connector.Error as err:
            messagebox.showwarning("Error", f"No se han podido cargar los datos: {err}")
        finally:
            cursor.close()
            conexion.close()

#Seleccionar
def seleccionar_persona(event):
    try:
        item = treeview.selection()[0]
        cliente = treeview.item(item, "values")

        entry_id.config(state=tk.NORMAL)
        entry_id.delete(0, tk.END)
        entry_id.insert(tk.END, cliente[0])
        entry_id.config(state=tk.DISABLED)

        entry_edad.delete(0, tk.END)
        entry_edad.insert(tk.END, cliente[1])

        entry_sexo.set(cliente[2])

        entry_bebidasSemana.delete(0, tk.END)
        entry_bebidasSemana.insert(tk.END, cliente[3])

        entry_cervezasSemana.delete(0, tk.END)
        entry_cervezasSemana.insert(tk.END, cliente[4])


        entry_bebidasFinSemana.delete(0, tk.END)
        entry_bebidasFinSemana.insert(tk.END, cliente[5])

        entry_bebidasDestiladasSemana.delete(0, tk.END)
        entry_bebidasDestiladasSemana.insert(tk.END, cliente[6])

        entry_vinosSemana.delete(0, tk.END)
        entry_vinosSemana.insert(tk.END, cliente[7])

        entry_perdidasControl.delete(0, tk.END)
        entry_perdidasControl.insert(tk.END, cliente[8])

        entry_diversionDependenciaAlcohol.set(cliente[9])

        entry_problemasDigestivos.set(cliente[10])

        entry_tensionAlta.set(cliente[11])

        entry_dolorCabeza.set(cliente[12])
    except IndexError:
        pass

#Actualizar
# Función para actualizar una persona
def actualizar_persona():
    conexion = conectar_db()
    cursor = conexion.cursor()
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    bebidasSemana = entry_bebidasSemana.get()
    cervezasSemana = entry_cervezasSemana.get()
    bebidasFinSemana = entry_bebidasFinSemana.get()
    bebidasDestiladasSemana = entry_bebidasDestiladasSemana.get()
    vinosSemana = entry_vinosSemana.get()
    perdidasControl = entry_perdidasControl.get()
    diversionDependenciaAlcohol = entry_diversionDependenciaAlcohol.get()
    problemasDigestivos = entry_problemasDigestivos.get()
    tensionAlta = entry_tensionAlta.get()
    dolorCabeza = entry_dolorCabeza.get()
    id = entry_id.get()  # Agregar esta línea al inicio de actualizar_persona()


    try:
        cursor.execute("UPDATE ENCUESTA SET edad=%s, Sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s, ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s WHERE idEncuesta=%s",(edad, sexo, bebidasSemana, cervezasSemana, bebidasFinSemana, bebidasDestiladasSemana, vinosSemana, perdidasControl, diversionDependenciaAlcohol, problemasDigestivos, tensionAlta, dolorCabeza, id))
        conexion.commit()
        messagebox.showinfo("Correcto","Tabla actualizada correctamente")
        mostrar_persona()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se ha podido actualizar la tabla: {err}")
    finally:
        cursor.close()
        conexion.close()


#Eliminar
def eliminar_persona():
    conexion = conectar_db()
    id = entry_id.get()

    if conexion:
        cursor = conexion.cursor()
        confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Seguro que desea eliminar esta encuesta? Esta acción es irreversible.")
        if confirmacion:
            try:
                cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta=%s", (id,))
                conexion.commit()
                messagebox.showinfo("Eliminado", "Encuesta elminada correctamente")
                mostrar_persona()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo eliminar la encuesta: {err}")
            finally:
                cursor.close()
                conexion.close()
        else:
            messagebox.showinfo("Cancelado", "La eliminación ha sido cancelada.")    


#Limpiar campos
def limpiar_campos():
    entry_id.config(state=tk.NORMAL)
    entry_id.delete(0, tk.END)
    entry_id.config(state=tk.DISABLED)
    entry_edad.delete(0,tk.END)
    entry_sexo.set("")
    entry_bebidasSemana.delete(0,tk.END)
    entry_cervezasSemana.delete(0,tk.END)
    entry_bebidasFinSemana.delete(0,tk.END)
    entry_bebidasDestiladasSemana.delete(0,tk.END)
    entry_vinosSemana.delete(0,tk.END)
    entry_perdidasControl.delete(0,tk.END)
    entry_diversionDependenciaAlcohol.set("")
    entry_problemasDigestivos.set("")
    entry_tensionAlta.set("")
    entry_dolorCabeza.set("")

#Filtrar datos
def filtrar_datos():
    conexion = conectar_db()
    id = entry_id.get()
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    bebidasSemana = entry_bebidasSemana.get()
    cervezasSemana = entry_cervezasSemana.get()
    bebidasFinSemana = entry_bebidasFinSemana.get()
    bebidasDestiladasSemana = entry_bebidasDestiladasSemana.get()
    vinosSemana = entry_vinosSemana.get()
    perdidasControl = entry_perdidasControl.get()
    diversionDependenciaAlcohol = entry_diversionDependenciaAlcohol.get()
    problemasDigestivos = entry_problemasDigestivos.get()
    tensionAlta = entry_tensionAlta.get()
    dolorCabeza = entry_dolorCabeza.get()

    if conexion:
        cursor = conexion.cursor()
        parametros = []
        consulta = "SELECT idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza FROM ENCUESTA WHERE 1=1"
        if id:
            consulta += " AND idEncuesta = %s"
            parametros.append(id)   
        if edad:
            consulta += " AND edad = %s"
            parametros.append(edad)
        if sexo:
            consulta += " AND Sexo = %s"
            parametros.append(sexo)
        if bebidasSemana:
            consulta += " AND BebidasSemana = %s"
            parametros.append(bebidasSemana)
        if cervezasSemana:
            consulta += " AND CervezasSemana = %s"
            parametros.append(cervezasSemana)
        if bebidasFinSemana:
            consulta += " AND BebidasFinSemana = %s"
            parametros.append(bebidasFinSemana)
        if bebidasDestiladasSemana:
            consulta += " AND BebidasDestiladasSemana = %s"
            parametros.append(bebidasDestiladasSemana)
        if vinosSemana:
            consulta += " AND VinosSemana = %s"
            parametros.append(vinosSemana)
        if perdidasControl:
            consulta += " AND PerdidasControl = %s"
            parametros.append(perdidasControl)
        if diversionDependenciaAlcohol:
            consulta += " AND DiversionDependenciaAlcohol = %s"
            parametros.append(diversionDependenciaAlcohol)
        if problemasDigestivos:
            consulta += " AND ProblemasDigestivos = %s"
            parametros.append(problemasDigestivos)
        if tensionAlta:
            consulta += " AND TensionAlta = %s"
            parametros.append(tensionAlta)
        if dolorCabeza:
            consulta += " AND DolorCabeza = %s"
            parametros.append(dolorCabeza)

        try:
            # Ejecuta la consulta con los parámetros
            cursor.execute(consulta, parametros)
            resultados = cursor.fetchall()
            # Limpia el treeview
            for row in treeview.get_children():
                treeview.delete(row)
            # Inserta los datos en el treeview
            for row in resultados:
                treeview.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se han podido filtrar los datos: {err}")
        finally:
            cursor.close()
            conexion.close()

#Exportar a EXCEL
def exportar_excel():
    rows = []
    for row in treeview.get_children():
        rows.append(treeview.item(row, 'values'))
    
    if not rows:
        messagebox.showwarning("Sin Datos", "No hay datos para exportar")
        return

    # Crear un DataFrame de pandas
    columnas = ["ID", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"]
    df = pd.DataFrame(rows, columns=columnas)

    # Abrir un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo
    archivo_guardar = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])

    if archivo_guardar:
        try:
            # Guardar el DataFrame en un archivo Excel
            df.to_excel(archivo_guardar, index=False, engine='openpyxl')
            messagebox.showinfo("Éxitoso", f"Datos exportados correctamente a {archivo_guardar}")
        except Exception as err:
            messagebox.showerror("Error", f"Error al exportar el exportar el archivo: {err}")

#Generar Gráfico Barras
def graficoBarras():
    try:
        # Conectar a la base de datos
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT Edad, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana FROM ENCUESTA")
        rows = cursor.fetchall()

        if not rows:
            messagebox.showwarning("Advertencia", "No hay datos para graficar.")
            return
        
        # Convertir los datos en un DataFrame
        df = pd.DataFrame(rows, columns=["Edad", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana"])

        # Filtrar los datos para eliminar filas con valores nulos o cero
        df = df[(df[['BebidasSemana', 'CervezasSemana', 'BebidasFinSemana', 'BebidasDestiladasSemana', 'VinosSemana']].gt(0).any(axis=1))]

        if df.empty:
            messagebox.showwarning("Advertencia", "No hay datos relevantes para graficar.")
            return

        # Crear grupos de edades
        bins = [18, 25, 35, 45, 55, 65, 100]  # Definir los grupos de edad
        labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
        df['GrupoEdad'] = pd.cut(df['Edad'], bins=bins, labels=labels, right=False)

        # Agrupar por grupo de edad y sumar el consumo de bebidas
        grouped = df.groupby('GrupoEdad').agg({
            'BebidasSemana': 'sum',
            'CervezasSemana': 'sum',
            'BebidasFinSemana': 'sum',
            'BebidasDestiladasSemana': 'sum',
            'VinosSemana': 'sum'
        }).sum(axis=1)  # Sumar todos los consumos de bebidas por grupo de edad

        # Crear un gráfico de barras con la distribución por grupos de edad
        fig, ax = plt.subplots(figsize=(10, 6))
        grouped.plot(kind='bar', ax=ax, color=sns.color_palette("Set2", len(grouped)))
        ax.set_title('Distribución de Consumo de Bebidas por Grupo de Edad', fontsize=16, weight='bold')
        ax.set_xlabel('Grupo de Edad', fontsize=12)
        ax.set_ylabel('Consumo Total de Bebidas', fontsize=12)
        plt.xticks(rotation=45)

        # Mostrar el gráfico
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Error al generar el gráfico: {e}")
    finally:
        conn.close()

#Generar Gráfico Circular
def graficoCircular():
    try:
        # Conectar a la base de datos
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT Edad, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana FROM ENCUESTA")
        rows = cursor.fetchall()

        if not rows:
            messagebox.showwarning("Advertencia", "No hay datos para graficar.")
            return
        
        # Convertir los datos en un DataFrame
        df = pd.DataFrame(rows, columns=["Edad", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana"])

        # Filtrar los datos para eliminar filas con valores nulos o cero
        df = df[(df[['BebidasSemana', 'CervezasSemana', 'BebidasFinSemana', 'BebidasDestiladasSemana', 'VinosSemana']].gt(0).any(axis=1))]

        if df.empty:
            messagebox.showwarning("Advertencia", "No hay datos relevantes para graficar.")
            return

        # Crear grupos de edades
        bins = [18, 25, 35, 45, 55, 65, 100]  # Definir los grupos de edad
        labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
        df['GrupoEdad'] = pd.cut(df['Edad'], bins=bins, labels=labels, right=False)

        # Agrupar por grupo de edad y sumar el consumo de bebidas
        grouped = df.groupby('GrupoEdad').agg({
            'BebidasSemana': 'sum',
            'CervezasSemana': 'sum',
            'BebidasFinSemana': 'sum',
            'BebidasDestiladasSemana': 'sum',
            'VinosSemana': 'sum'
        }).sum(axis=1)  # Sumar todos los consumos de bebidas por grupo de edad

        # Crear un gráfico circular (Pie Chart) con la distribución por grupos de edad
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(grouped, labels=grouped.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2", len(grouped)))
        ax.set_title('Distribución de Consumo de Bebidas por Grupo de Edad', fontsize=16, weight='bold')

        # Mostrar el gráfico
        plt.axis('equal')  # Para que el gráfico sea un círculo perfecto
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Error al generar el gráfico: {e}")
    finally:
        conn.close()


#FUNCIONES DE LOS COMBOBOX
#Sexo
def combo_sexo():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DISTINCT Sexo FROM ENCUESTA")
            sexo_mostrar = [str(row[0]) for row in cursor.fetchall()]
            entry_sexo['values'] = sexo_mostrar
        except mysql.connector.Error as err:
            messagebox.showerror("ERROR", f"No se pueden cargar los valores de Sexo: {err}")
        finally:
            cursor.close()
            conexion.close()

#Diversion dependencia alcohol
def combo_dependencia():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DISTINCT DiversionDependenciaAlcohol FROM ENCUESTA")
            dependencia_mostrar = [str(row[0]) for row in cursor.fetchall()]
            entry_diversionDependenciaAlcohol['values'] = dependencia_mostrar
        except mysql.connector.Error as err:
            messagebox.showerror("ERROR", f"No se pueden cargar los valores de DiversionDependenciaAlcohol: {err}")
        finally:
            cursor.close()
            conexion.close()

#Problemas digestivos
def combo_digestivo():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DISTINCT ProblemasDigestivos FROM ENCUESTA")
            digestivo_mostrar = [str(row[0]) for row in cursor.fetchall()]
            entry_problemasDigestivos['values'] = digestivo_mostrar
        except mysql.connector.Error as err:
            messagebox.showerror("ERROR", f"No se pueden cargar los valores de ProblemasDigestivos: {err}")
        finally:
            cursor.close()
            conexion.close()

#Tension alta
def combo_tension():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DISTINCT TensionAlta FROM ENCUESTA")
            tension_mostrar = [str(row[0]) for row in cursor.fetchall()]
            entry_tensionAlta['values'] = tension_mostrar
        except mysql.connector.Error as err:
            messagebox.showerror("ERROR", f"No se pueden cargar los valores de TensionAlta: {err}")
        finally:
            cursor.close()
            conexion.close()

#Dolor de cabeza
def combo_cabeza():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DISTINCT DolorCabeza FROM ENCUESTA")
            cabeza_mostrar = [str(row[0]) for row in cursor.fetchall()]
            entry_dolorCabeza['values'] = cabeza_mostrar
        except mysql.connector.Error as err:
            messagebox.showerror("ERROR", f"No se pueden cargar los valores de DolorCabeza: {err}")
        finally:
            cursor.close()
            conexion.close()

#DISEÑO INTERFAZ
ventana = tk.Tk()
ventana.title("Hito 2 Andrea")

#Etiquetas y Entradas
tk.Label(ventana, text="ID:",font=("Arial",12,"bold"), fg="#260B01" ).grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(ventana, state=tk.DISABLED, width=55)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Edad:", font=("Arial",12,"bold"), fg="#260B01").grid(row=1, column=0, padx=5, pady=3)
entry_edad = tk.Entry(ventana, width=55)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Sexo:", font=("Arial",12,"bold"), fg="#260B01").grid(row=2, column=0, padx=5, pady=3)
entry_sexo = ttk.Combobox(ventana, state="readonly", width=52)
entry_sexo.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ventana, text="Número de bebidas a la semana:", font=("Arial",12,"bold"), fg="#260B01").grid(row=3, column=0, padx=5, pady=3)
entry_bebidasSemana = tk.Entry(ventana, width=55)
entry_bebidasSemana.grid(row=3, column=1, padx=5, pady=5)

tk.Label(ventana, text="Número de cervezas a la semana:", font=("Arial",12,"bold"), fg="#260B01").grid(row=4, column=0, padx=5, pady=3)
entry_cervezasSemana = tk.Entry(ventana, width=55)
entry_cervezasSemana.grid(row=4, column=1, padx=5, pady=3)

tk.Label(ventana, text="Número de bebidas el fin de semana:",font=("Arial",12,"bold"), fg="#260B01").grid(row=5, column=0, padx=5, pady=3)
entry_bebidasFinSemana = tk.Entry(ventana, width=55)
entry_bebidasFinSemana.grid(row=5, column=1, padx=5, pady=3)

tk.Label(ventana, text="Número de bebidas destiladas a la semana:", font=("Arial",12,"bold"), fg="#260B01").grid(row=6, column=0, padx=5, pady=3)
entry_bebidasDestiladasSemana = tk.Entry(ventana, width=55)
entry_bebidasDestiladasSemana.grid(row=6, column=1, padx=5, pady=3)

tk.Label(ventana, text="Número de vinos a la semana:", font=("Arial",12,"bold"), fg="#260B01").grid(row=7, column=0, padx=5, pady=3)
entry_vinosSemana = tk.Entry(ventana, width=55)
entry_vinosSemana.grid(row=7, column=1, padx=5, pady=3)

tk.Label(ventana, text="Número de pérdidas de control:", font=("Arial",12,"bold"), fg="#260B01").grid(row=8, column=0, padx=5, pady=3)
entry_perdidasControl = tk.Entry(ventana, width=55)
entry_perdidasControl.grid(row=8, column=1, padx=5, pady=3)

tk.Label(ventana, text="¿Dependes del alcohol para divertirte?", font=("Arial",12,"bold"), fg="#260B01").grid(row=9, column=0, padx=5, pady=3)
entry_diversionDependenciaAlcohol = ttk.Combobox(ventana, state="readonly", width=52)
entry_diversionDependenciaAlcohol.grid(row=9, column=1, padx=5, pady=3)

tk.Label(ventana, text="¿Tienes problemas digestivos?", font=("Arial",12,"bold"), fg="#260B01").grid(row=10, column=0, padx=5, pady=3)
entry_problemasDigestivos = ttk.Combobox(ventana, state="readonly", width=52)
entry_problemasDigestivos.grid(row=10, column=1, padx=5, pady=3)

tk.Label(ventana, text="¿Tienes la tensión alta?", font=("Arial",12,"bold"), fg="#260B01").grid(row=11, column=0, padx=5, pady=3)
entry_tensionAlta = ttk.Combobox(ventana, state="readonly", width=52)
entry_tensionAlta.grid(row=11, column=1, padx=5, pady=3)

tk.Label(ventana, text="¿Cada cuanto tienes dolores de cabeza?", font=("Arial",12,"bold"), fg="#260B01").grid(row=12, column=0, padx=5, pady=3)
entry_dolorCabeza = ttk.Combobox(ventana, state="readonly", width=52)
entry_dolorCabeza.grid(row=12, column=1, padx=5, pady=3)


#BOTONES
tk.Button(ventana, text="Ingresar",command=ingresar_persona, bg="#260B01", fg="#FFFFFF",width=15).grid(row=13, column=0, padx=5, pady=3)
tk.Button(ventana, text="Actualizar tabla",command=actualizar_persona, bg="#260B01", fg="#FFFFFF",width=15).grid(row=13, column=1, padx=5, pady=3)
tk.Button(ventana, text="Eliminar",command=eliminar_persona,bg="#260B01", fg="#FFFFFF",width=15).grid(row=14, column=0, padx=5, pady=3)
tk.Button(ventana, text="Limpiar",command=limpiar_campos, bg="#260B01", fg="#FFFFFF",width=15).grid(row=14, column=1, padx=5, pady=3)
tk.Button(ventana, text="Filtrar",command=filtrar_datos, bg="#260B01", fg="#FFFFFF",width=15).grid(row=15, column=0, padx=5, pady=3)
tk.Button(ventana, text="Exportar a Excel",command=exportar_excel, bg="#260B01", fg="#FFFFFF",width=15).grid(row=15, column=1, padx=5, pady=3)
tk.Button(ventana, text="Gráfico circular",command=graficoCircular, bg="#260B01", fg="#FFFFFF",width=15).grid(row=16, column=0, padx=5, pady=3)
tk.Button(ventana, text="Gráfico barras",command=graficoBarras, bg="#260B01", fg="#FFFFFF",width=15).grid(row=16, column=1, padx=5, pady=3)

#TREEVIEW para mostrar la lista de clientes
treeview = ttk.Treeview(ventana, columns=("ID", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"), show="headings")
treeview.bind("<ButtonRelease-1>", seleccionar_persona)

#Configura los encabezados de las columnas
treeview.heading("ID", text="Id")
treeview.heading("Edad", text="Edad")
treeview.heading("Sexo", text="Sexo")
treeview.heading("BebidasSemana", text="Nº bebidas semana")
treeview.heading("CervezasSemana", text="Nºcervezas semana")
treeview.heading("BebidasFinSemana", text="Nº bebidas finde")
treeview.heading("BebidasDestiladasSemana", text="Nº bebidas destiladas semana")
treeview.heading("VinosSemana", text="Nº vinos semana")
treeview.heading("PerdidasControl", text="Nº pérdidas control")
treeview.heading("DiversionDependenciaAlcohol", text="dependencia del alcohol para divertirse")
treeview.heading("ProblemasDigestivos", text="Problemas digestivos")
treeview.heading("TensionAlta", text="Tensión alta")
treeview.heading("DolorCabeza", text="Dolor de cabeza")

# Ajustar el ancho de las columnas (se puede ajustar según lo necesario)
for col in treeview["columns"]:
    treeview.column(col, width=100, anchor="center")

# Hacer que el Treeview se ajuste al ancho de la ventana
treeview.grid(row=17, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Configurar que el Treeview se expanda cuando la ventana cambie de tamaño
ventana.grid_rowconfigure(17, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

mostrar_persona()
combo_sexo()
combo_dependencia()
combo_digestivo()
combo_tension()
combo_cabeza()
ventana.mainloop()