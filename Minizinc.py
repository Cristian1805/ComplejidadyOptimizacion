from tkinter import Tk,Label,Place,Button,Entry,CENTER,Scrollbar,END
from tkinter import ttk

raiz=Tk()
raiz.title("Implementacion")

Label(raiz,text="Ingrese Numero de Filas",font=('Arial',12),fg="blue").place(x=30,y=30)

entra_numeroFilas=Entry(raiz)
entra_numeroFilas.place(x=30,y=80)

Label(raiz,text="Ingrese Datos",font=("Arial",12),fg="blue").place(x=30,y=120)

Label(raiz,text="Region").place(x=40,y=190)
entra_region=Entry(raiz)
entra_region.focus()
entra_region.place(x=40,y=170)

Label(raiz,text="Poblacion").place(x=200,y=190)
entra_poblacion=Entry(raiz)
entra_poblacion.place(x=200,y=170)

Label(raiz,text="Congeladores Disponibles").place(x=360,y=190) 
entra_congeladora=Entry(raiz)
entra_congeladora.place(x=360,y=170)

Label(raiz,text="Unidades de Vacunas").place(x=40,y=250)
entra_vacunas=Entry(raiz)
entra_vacunas.place(x=40,y=230)

Label(raiz,text="Costo Adecuacion").place(x=200,y=250)
entra_costo=Entry(raiz)
entra_costo.place(x=200,y=230)

Label(raiz,text="Muertes").place(x=360,y=250)
entra_muertes=Entry(raiz)
entra_muertes.place(x=360,y=230)

####################BOTON AGREGAR#################

btn_agregar=Button(raiz,text="AGREGAR",width=17,command=lambda:agregar())
btn_agregar.place(x=40,y=300)

####################TABLA RESULTADOS ############

Label(raiz,text="RESULTADOS",font=("Arial",12)).place(x=40,y=350)

tabla_resultados=ttk.Treeview(raiz,columns=[f"#{n}" for n in range(0,2)])
tabla_resultados.place(x=40,y=380)

tabla_resultados.column("#0",width=0,minwidth=1)
tabla_resultados.column("#1",width=150,minwidth=100,anchor=CENTER)
tabla_resultados.column("#2",width=150,minwidth=100,anchor=CENTER)

tabla_resultados.heading("#0",text="")
tabla_resultados.heading("#1",text="REGION")
tabla_resultados.heading("#2",text="NUMEROS DE VACUNAS")

######################### TABLA MUESTRA DATOS INGRESADOS ####################

Label(raiz,text="DATOS INGRESADOS",font=("Arial",14),fg="blue").place(x=700,y=100)

tabla_datos=ttk.Treeview(raiz,columns=[f"#{n}" for n in range(0,6)])
tabla_datos.place(x=600,y=170)

tabla_datos.column("#0",width=0,minwidth=1)
tabla_datos.column("#1",width=70,minwidth=100,anchor=CENTER)
tabla_datos.column("#2",width=70,minwidth=100,anchor=CENTER)
tabla_datos.column("#3",width=70,minwidth=100,anchor=CENTER)
tabla_datos.column("#4",width=70,minwidth=100,anchor=CENTER)
tabla_datos.column("#5",width=100,minwidth=100,anchor=CENTER)
tabla_datos.column("#6",width=250,minwidth=140,anchor=CENTER)

tabla_datos.heading("#0", text="")
tabla_datos.heading("#1", text="Region")
tabla_datos.heading("#2", text="Poblacion")
tabla_datos.heading("#3", text="Congeladores")
tabla_datos.heading("#4", text="Unidad Vacunas")
tabla_datos.heading("#5", text="Costos")
tabla_datos.heading("#6", text="Muertes")

################SCROLLBAR###################
scroll_Tabladatos=ttk.Scrollbar(raiz,orient="vertical",command=tabla_datos.yview)
scroll_Tabladatos.place(x=1232,y=170,height=225)
tabla_datos.configure(yscrollcommand=scroll_Tabladatos.set)

#################BOTONES CALCULAR EDITAR ELIMINAR##############

btn_calcular=Button(raiz,text="CALCULAR",width=17)
btn_calcular.place(x=650,y=430)

btn_calcular=Button(raiz,text="EDITAR",width=17)
btn_calcular.place(x=800,y=430)

btn_calcular=Button(raiz,text="ELIMINAR",width=17)
btn_calcular.place(x=950,y=430)

###############BOTON AGREGAR ##############
def agregar():
    x=[(entra_region.get().upper()),(entra_poblacion.get()),(entra_congeladora.get()),(entra_vacunas.get()),(entra_costo.get()),(entra_muertes.get())]
    
    tabla_datos.insert("",0,values=x)
        
    entra_congeladora.delete(0,END)
    entra_costo.delete(0,END)
    entra_muertes.delete(0,END)
    entra_region.delete(0,END)
    entra_poblacion.delete(0,END)
    entra_vacunas.delete(0,END)
    

################BOTON SALIR####################

btn_calcular=Button(raiz,text="SALIR",width=17,command=lambda:salir())
btn_calcular.place(x=1100,y=430)

def salir():
    raiz.destroy()


raiz.state(newstate="zoomed")
raiz.mainloop()