import Region as rg
import openpyxl as op
from prettytable import PrettyTable


class DataLoad:
    
    def __init__(self, ruta):
        self.ruta = ruta
        self.hoja = ""
        self.listaRegiones = []
        self.titulos = []
        
        # datos para la cualificaion
        self.listaNombreRegiones = []
        self.listaCualificaiones = []
        
        self.load()
        
    def load(self):
        wb = op.load_workbook(self.ruta, data_only = True)
        self.hoja = wb.active 
         
        print("")
        titles  = []
        rowData = []
        cont = 1
        table = PrettyTable()
        for row in self.hoja.rows:
            for item in row:
                if (cont == 1):
                    titles.append(item.value.replace("\n", ""))
                else:
                    rowData.append(item.value)

            if (cont == 1):
                table.field_names = titles
                cont = 0
            else:
                table.add_row(rowData)
                rowData = []
            
        print(table)
    
    def getRegiones(self):
        titlesX = True
        valorunidad=self.congeladorestotal()
        print("Valor: %i " % valorunidad)

        for row in self.hoja.rows:
            if (titlesX):
                for item in row:
                    self.titulos.append(item.value.replace("(En cientos de miles)", "").replace("(En miles)", ""))
                titlesX = False
                # print(self.titulos)
            else:
                regionX = rg.Region(self.editarNombre(row[0].value), row[0].value,row[1].value ,row[2].value , self.congeladorestotal(), row[3].value, row[4].value, row[5].value)
                self.listaRegiones.append(regionX)
                print(self.listaRegiones )

        self.titulos.append("Proporcion\n(Congeladores/Total Congeladores)")
        self.titulos.append("Escala de valoración\ndel beneficio")
        
        self.calcularEscalaValoracion()
        
        return self.listaRegiones

        

    def congeladorestotal(self):         
        titlesX = True
        conteo = 0
        for row in self.hoja.rows: 
            if (titlesX):
                titlesX = False
                # print(self.titulos)
            else:
            #print ("unidad = %i" % unidad)
                valor=(row[2].value)
                print("CONGELADORES")
                
                print (type(int(row[2].value)))
                conteo=conteo + valor 
                print("Conteo: %i" % conteo)

        return conteo
    
    def editarNombre(self, nombreX):        
        textoAux = nombreX
        print("nombreOriginal: "+textoAux)

        while(textoAux[:1] == " "):
            textoAux = textoAux[1:]
            
        while(textoAux[-1:] == " "):
            textoAux = textoAux[:-1]

        textoAux = textoAux.replace("-", " ")
        textoAux = textoAux.replace("     ", " ")
        textoAux = textoAux.replace("    ", " ")
        textoAux = textoAux.replace("   ", " ")
        textoAux = textoAux.replace("  ", " ")

        # comentar desde aca si solo se dejara nombre con uppercase
        textoAux = textoAux.split(" ")
        textoFinal = ""
        for word in textoAux:
            textoFinal = textoFinal + word[0]
        textoFinal = textoFinal.upper()
        print("nombreModificado: "+ textoFinal)
        print("")
        

        return textoFinal
        
    
    def crearCondicionesA(self):
        titlesX = True
        for row in self.hoja.rows:
            if (titlesX): # es para ignorar la prmera fila de titulos que no nos importan
                titlesX = False
            else:
                self.listaNombreRegiones.append(self.editarNombre(row[0].value))
                self.listaCualificaiones.append(row[1].value)
            
        print(self.listaNombreRegiones)
        print(self.listaCualificaiones)
    
    def getNombreRegionesCA(self):
        return self.listaNombreRegiones
    
    def getCualificaionCA(self):
        return self.listaCualificaiones
    
    def getTitulos(self):
        return self.titulos
    
   
    
    def calcularEscalaValoracion(self):
        listaProporciones = []
        listaNombresCortos = []


        

        for regionX in self.listaRegiones:
            listaProporciones.append(regionX.get_proporcion())
        
        orden = []
        orden = sorted(listaProporciones)

        print(orden)  
        print("//////////////")
                
        listaEscalaValoracion = []
        contador=1
        for a in range(len(listaProporciones)):

            listaEscalaValoracion.append(contador)
            contador=contador+1

        # opcion 1 tiene en cuenta el valor maximo de escala
        #index = len(listaProporciones)
        #k = index
        #for i in range(len(listaProporciones)):
        #    if ( i<len(listaProporciones)-1 and listaProporciones[i] != listaProporciones[i+1]):
        #        index = k
        #        listaEscalaValoracion.append(index)
        #        index = index - 1 
        #        k =  k -1 
        #    else:
        #        listaEscalaValoracion.append(index)
        #        k = k - 1

        bandera2 = False
        for  i in range(len(listaProporciones)):
            bandera2 = False
            for s in range(len(self.listaRegiones)):
                numero1 = float(self.listaRegiones[i].get_proporcion())
                numero2 = float(orden[s])
                if (numero1 == numero2 and bandera2 != True): 
                    print("Proporciones ",self.listaRegiones[i].get_nombreCorto())
                    print("Cantidad Proporcion ",self.listaRegiones[i].get_proporcion())
                    print("Indice ", s)
                    nombre = self.listaRegiones[i].get_nombreCorto()
                    listaNombresCortos.insert(s,nombre)
                    bandera2 = True
                
                


        print("Nombre Cortos")
        print(listaNombresCortos)
        print("Proporciones")
        print(orden) 

        for i in range(len(listaNombresCortos)):
            for j in range(len(self.listaRegiones)):                
                if (listaNombresCortos[i] == self.listaRegiones[j].get_nombreCorto()):
                    print("iguales")
                    print(listaNombresCortos[i])
                    print(self.listaRegiones[j].get_proporcion())
                    print(listaEscalaValoracion[i])
                    
                    self.listaRegiones[j].set_EscalaValoracion(listaEscalaValoracion[i])
                    
                    # listaRegionesAux.append(regionX)
                    print("retornar ->", str(self.listaRegiones[j].get_EscalaValoracion()))