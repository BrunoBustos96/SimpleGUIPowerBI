"""
Réplica de las funciones de Power BI Master Team

Alejandro Thompson
Bruno Bustos
Juan Cruz
Camila Cruz
Juan Álvarez

"""
import tkinter as tk
import pandas as pd
import numpy as np
import datetime
from tkinter import filedialog
from tkinter import messagebox as msg
from tkinter import Toplevel
from pandastable import Table

from PIL import Image, ImageTk

todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date-datetime.timedelta(10), periods=10, freq='D')

"""
columns = ['A', 'B', 'C']
df_ = pd.DataFrame(index=index, columns=columns)
df_ = df_.fillna(0)
"""

root = tk.Tk()

root.title("Team Master - Menus de PowerBI")
canvas1 = tk.Canvas(root, width=600, height=350, scrollregion=(0, 0, 500, 500))

myImage = ImageTk.PhotoImage(Image.open("uto.jfif"),master = canvas1)
#my_label = Label(image=myImage)
my_label = tk.Label(root,image=myImage)
my_label.pack()
#canvas1.create_image(0, 0, anchor = NW, image = MyImage)

canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(250, 50, window=entry1)
entry2 = tk.Entry(root)
canvas1.create_window(250, 100, window=entry2)
def cargar_df():
    try:
        file_name = filedialog.askopenfilename(initialdir='/Desktop',
                                               title='Select a excel file',
                                               filetypes=(('excel file', '*.xls'),
                                                          ('excel file', '*.xlsx')))
        global df_
        df_ = pd.read_excel(file_name)
        df_.columns= [x.replace(".","_") for x in df_.columns]
        # leer pandas
        if(len(df_) == 0):
            msg.showinfo('el archivo parece vacio', 'no se tienen filas')
        else:
            print('se tienen ', len(df_), ' filas')
            msg.showinfo('archivo cargado',
                         'Se ha cargado el archivo exitosamente')
            frame = tk.Frame(root)
            frame.pack(fill='both', expand=True)
            pt = Table(frame, dataframe=df_)
            pt.show()
            canvas1.create_window(200, 230, window=pt)
    except FileNotFoundError as e:
        msg.showerror('Error al tratar de abrir el archivo', e)


def quitar():
    x1 = entry1.get()
    df2 = df_.copy()
    cadena = x1.split(",")
    print("--------",cadena)
    for columna in cadena:
        df2=df2.drop(columna, axis=1)
    new = Toplevel(root)
    new.geometry("750x250")
    new.title("Quitar columnas")
    frame = tk.Frame(new)
    frame.pack(fill='both', expand=True)
    global pt
    pt = Table(frame, dataframe=df2)
    pt.show()
    new.pack_slaves()


def seleccionar():
    x1 = entry1.get()
    df2 = df_.copy()
    cadena = x1.split(",")
    print("--------",cadena)
    sub_df=df2.loc[:,cadena]
    new = Toplevel(root)
    new.geometry("750x250")
    new.title("Seleccionar columnas")
    frame = tk.Frame(new)
    frame.pack(fill='both', expand=True)
    global pt
    pt = Table(frame, dataframe=sub_df)
    pt.show()
    new.pack_slaves()


def conservar_n():
    x1 = entry1.get()
    df2 = df_.copy()
    h=int(x1)
    sub_df=df2.head(h)
    new = Toplevel(root)
    new.geometry("750x250")
    new.title("Tomar primeras n filas")
    frame = tk.Frame(new)
    frame.pack(fill='both', expand=True)
    global pt
    pt = Table(frame, dataframe=sub_df)
    pt.show()
    new.pack_slaves()


def conservar_n_fin():
    x1 = entry1.get()
    df2 = df_.copy()
    h=int(x1)
    sub_df=df2.tail(h)
    new = Toplevel(root)
    new.geometry("750x250")
    new.title("Tomar n finales filas")
    frame = tk.Frame(new)
    frame.pack(fill='both', expand=True)
    global pt
    pt = Table(frame, dataframe=sub_df)
    pt.show()
    new.pack_slaves()

def conservar_n_filas():
    x1 = entry1.get()
    x2 = entry2.get()
    df2 = df_.copy()
    m=int(x1)
    n=int(x2)
    sub_df=df2.loc[m-1:n-1,:]
    new = Toplevel(root)
    new.geometry("750x250")
    new.title("Conservar filas")
    frame = tk.Frame(new)
    frame.pack(fill='both', expand=True)
    global pt
    pt = Table(frame, dataframe=sub_df)
    pt.show()
    new.pack_slaves()

def quitar_n_primeras():
    x1 = entry1.get()
    df2 = df_.copy()
    m=int(x1)
    sub_df=df2.tail(-m)
    new = Toplevel(root)
    new.geometry("750x250")
    new.title("Quitar N primeras filas")
    frame = tk.Frame(new)
    frame.pack(fill='both', expand=True)
    global pt
    pt = Table(frame, dataframe=sub_df)
    pt.show()
    new.pack_slaves()

def quitar_n_ultimas():
    x1 = entry1.get()
    df2 = df_.copy()
    m=int(x1)
    sub_df=df2.head(-m)
    new = Toplevel(root)
    new.geometry("750x250")
    new.title("Quitar N ultimas filas")
    frame = tk.Frame(new)
    frame.pack(fill='both', expand=True)
    global pt
    pt = Table(frame, dataframe=sub_df)
    pt.show()
    new.pack_slaves()
    
def eliminar_duplicados():
    df2 = df_.copy()
    sub_df = df2.drop_duplicates()
    new = Toplevel(root)
    new.geometry("750x250")
    new.title("Quitar duplicados")
    frame = tk.Frame(new)
    frame.pack(fill='both', expand=True)
    global pt
    pt = Table(frame, dataframe=sub_df)
    pt.show()
    new.pack_slaves()
    
def describir_cuantitativos():
    df2 = df_.copy()
    sub_df = df2.describe()
    new = Toplevel(root)
    new.geometry("750x250")
    new.title("Describir cuantitativos")
    frame = tk.Frame(new)
    frame.pack(fill='both', expand=True)
    global pt
    pt = Table(frame, dataframe=sub_df)
    pt.show()
    new.pack_slaves()
    
    
    
button1 = tk.Button(root,text='Cargar Excel', command=cargar_df)
button2 = tk.Button(root,text='Quitar c', command=quitar)
button3 = tk.Button(root,text='Seleccionar c', command=seleccionar)
button4 = tk.Button(root,text='N primeras filas', command=conservar_n)
button5 = tk.Button(root,text='N ultimas filas', command=conservar_n_fin)
button6 = tk.Button(root,text='Conservar n filas', command=conservar_n_filas)
button7 = tk.Button(root,text='Quitar N primeras', command=quitar_n_primeras)
button8 = tk.Button(root,text='Quitar N ultimas',command = quitar_n_ultimas)
button9 = tk.Button(root,text='Quitar duplicados',command = eliminar_duplicados)
button10 = tk.Button(root,text='Describir cuantitativos',command = describir_cuantitativos)

canvas1.create_window(50, 180, window=button1)
canvas1.create_window(150, 180, window=button2)
canvas1.create_window(270, 180, window=button3)
canvas1.create_window(380, 180, window=button4)
canvas1.create_window(500, 180, window=button5)
canvas1.create_window(60, 240, window=button6)
canvas1.create_window(190, 240, window=button7)
canvas1.create_window(320, 240, window=button8)
canvas1.create_window(450, 240, window=button9)
canvas1.create_window(75, 300, window=button10)

root.mainloop()
