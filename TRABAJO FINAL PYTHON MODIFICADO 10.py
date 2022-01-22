import pandas as pd
import matplotlib.pyplot as plt

dicc={"RUC":[],"Cliente":[],"Operador":[],"Descripción":[],"Monto":[],"Fecha":[]}
df=pd.DataFrame(dicc)
def usuario_decision():
    decision=input("Escriba S para añadir Clientes, C para añadir nuevas Columnas, F para filtrar datos,O para ordenar segun alguna columna, D para Datos estadisticos, H para gráficos y cualquier otra tecla para Salir y guardar el Excel: ")
    if decision=="S":
        estado=1
    elif decision=="C":
        estado=2
    elif decision=="F":
        estado=3
    elif decision=="O":
        estado=4
    elif decision=="D":
        estado=5
    elif decision=="H":
        estado=6
    else:
        estado=7
    return estado

def añadir_fila():
    global df
    dicc_fila={}
    columnas_df=df.columns 
    for columna in columnas_df:
      dicc_fila[columna]=input("Ingrese valor de la columna{}: ".format(columna))
    df=df.append(dicc_fila,ignore_index=True)
def añadir_columna():
    global df
    name=input("Ingrese el nombre de la columna nueva: ")
    a=[]
    for i in range (int(len(df.index))):
        s=input("Escriba el valor del cliente N°{}".format(i))
        a.append(s)
    df=df.assign(n=a)
    df.rename(columns = {"n":name},inplace=True)
def filtrar():
    global df
    print("Las columnas son: ", df.columns)
    filtro=input("Ingrese la columna que desee filtrar: ")
    caract=input("Ingrese el valor que desea hallar: ")
    f=df.loc[df[filtro]==caract]
    return f
def ordenar():
    global df
    print("Las columnas son: ", df.columns)
    col=input("Ingrese la columna que desee ordenar: ")
    decision=input("Ingrese A para ordenar de manera ascendente o D para descendente: ")
    if decision=="A":
        df=df.sort_values(col,ascending=True)
    elif decision=="D":
        df=df.sort_values(col,ascending=False)

def histograma():
    global df
    print("Las columnas son: ", df.columns)
    Variable_Hist = list(df[ input("¿Con qué variable quiere realizar el histograma?")])
    plt.hist(Variable_Hist , bins = 6, alpha = 0.5, histtype='bar', color='steelblue', edgecolor = 'none')
    plt.show()

def dispersion():
    global df
    print("Las columnas son: ", df.columns)
    Var_Disp = int(input("¿Cuántas variables desea para el gráfico de dispersión?"))
    if Var_Disp == 2:
        Variable_Disp1 = list(df[ input("Ingrese la variable numérica 1: ")])
        Variable_Disp2 = list(df[ input("Ingrese la variable numérica 2: ")])
        plt.scatter(Variable_Disp1 ,Variable_Disp2, alpha=0.5, cmap='viridis')
        plt.colorbar()
        plt.show()
    elif Var_Disp == 3:
        Variable_Disp1 = list(df[ input("Ingrese la variable numérica 1: ")])
        Variable_Disp2 = list(df[ input("Ingrese la variable numérica 2: ")])
        Variable_Disp3 = list(df[ input("Ingrese la variable categórica para ser puesta como color del grafico: ")])
        plt.scatter(Variable_Disp1 ,Variable_Disp2,c = Variable_Disp3, alpha=0.5, cmap='viridis')
        plt.colorbar()
        plt.show()
    elif Var_Disp == 4:
        Variable_Disp1 = list(df[ input("Ingrese la variable numérica 1: ")])
        Variable_Disp2 = list(df[ input("Ingrese la variable numérica 2: ")])
        Variable_Disp3 = list(df[ input("Ingrese la variable categórica para ser puesta como color del grafico: ")])
        Variable_Disp4 = list(df[ input("Ingrese la variable númerica para ser puesta como tamaño de los puntos: ")])
        plt.scatter(Variable_Disp1 ,Variable_Disp2,c  = Variable_Disp3,s = Variable_Disp4,alpha=0.5, cmap='viridis')
        plt.colorbar()
        plt.show()

   
    
state=usuario_decision()
while True:
    if state==1:
        añadir_fila()
        print("Cliente(s) añadidos con éxito")
        state=usuario_decision()
        
    if state==2:
        añadir_columna()
        print("Columna agregada con éxito")
        state=usuario_decision()
         
    if state==3:
        f=filtrar()
        print("Filtro Aplicado: ")
        print(f)
        state=usuario_decision()
        
    if state==4:
        ordenar()
        print("Orden Aplicado")
        print(df)
        state=usuario_decision()
    if state==5:
        print(df.describe())
        state=usuario_decision()
    if state==6:
        resp_graf="S"
        while resp_graf == "S":
            Tipo_Graf = str(input("¿Qué tipo de gráfico desea?,  escriba hist para histograma, o disp para dispersión: "))
            if Tipo_Graf == "hist":
                histograma()
                break
            elif Tipo_Graf == "disp":
                dispersion()
                break
            else:
                break
        state=usuario_decision()
    if state==7:
        break

        
    
excel=input("Ingrese Nombre del Archivo excel(Se guardará en el escritorio)")
df.to_excel(excel+'.xlsx')    
print(df)
