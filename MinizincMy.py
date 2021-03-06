import minizinc as mz
import DataLoad as ld


class MinizincMy:
    
    def __init__(self, listaDeRegiones, numUnidades, presupuesto, kits, listaNombreRegionCA,  listaCualificacionCA, valorDeCondiconesA):
        
        self.listaDeRegiones = listaDeRegiones
        self.stringFinal = ""
        self.stringResultado = "Resultados: \n"
        self.numUnidades =  int(numUnidades)
        self.presupuesto = int(presupuesto)
        self.kits =  int(kits)
        
        # para condiciones adicionales (CA)
        self.listaNombreRegionCA = listaNombreRegionCA
        self.listaCualificacionCA =  listaCualificacionCA
        
        if (valorDeCondiconesA  == ""):
            self.valorDeCondiconesA = ""
        else:
            self.valorDeCondiconesA = int(valorDeCondiconesA)
    

    def crearVarRegiones(self):
        stringX = "\nvar int: Beneficio;\n"
        base = "var int: "
        for regionX in self.listaDeRegiones:
            stringX = stringX + base + regionX.get_nombreCorto()+ ";\n"

        self.stringFinal = self.stringFinal + stringX + "\n"
        # print(stringX)

    def kitsPorUnidad(self):    

        stringX = "constraint "
        stringCola = "<= " + str(self.kits) + ";"
        for i in range(len(self.listaDeRegiones)):

            if (self.listaDeRegiones[i].get_nombreCorto() == "NE" or self.listaDeRegiones[i].get_nombreCorto() == "S"):
                stringX =  stringX + "2*"+ self.listaDeRegiones[i].get_nombreCorto() + " "
            else:
                stringX =  stringX + self.listaDeRegiones[i].get_nombreCorto() + " "

            if (i != (len(self.listaDeRegiones)-1)):
                stringX = stringX + "+ "

        stringX = stringX + stringCola

        self.stringFinal = self.stringFinal + stringX + "\n"
        # print(stringX)

    def Unidades(self):
        divisor= "10000"
        stringX = "constraint "
        stringCola = "<= " + str(self.numUnidades) + ";"
        
        for i in range(len(self.listaDeRegiones)):
            stringX =  stringX + str(self.listaDeRegiones[i].get_unidadesReque())+ "*" + self.listaDeRegiones[i].get_nombreCorto() + "/" + divisor + " "

            if (i != (len(self.listaDeRegiones)-1)):
                stringX = stringX + "+ "

        stringX = stringX + stringCola

        self.stringFinal = self.stringFinal + stringX + "\n"
        # print (stringX)

    def costosAdecuacion(self):
        divisor = 100000
        divisor2 = "50000"
        stringX = "constraint "
        stringCola = "<= " + str(self.presupuesto/divisor) + ";"
        
        for i in range(len(self.listaDeRegiones)):
            stringX =  stringX + str(self.listaDeRegiones[i].get_costos()/divisor)+ "*" + self.listaDeRegiones[i].get_nombreCorto() + "/" + divisor2 + " "

            if (i != (len(self.listaDeRegiones)-1)):
                stringX = stringX + "+ "

        stringX = stringX + stringCola

        self.stringFinal = self.stringFinal + stringX + "\n"
        # print (stringX)

    def condicionesAdicionales(self):
        stringX = "constraint "
        stringCola = ">= " + str(self.valorDeCondiconesA) + ";\n"
        
        for i in range(len(self.listaNombreRegionCA)):            
            stringX =  stringX + str(self.listaCualificacionCA[i]) + "*" + self.listaNombreRegionCA[i]  + " "
            
            if (i != (len(self.listaNombreRegionCA)-1)):
                stringX = stringX + "+ "
                
        stringX = stringX + stringCola
            
        self.stringFinal = self.stringFinal + stringX + "\n"
        # print(stringX)
        
    def poblacion(self):
        stringX = "constraint Beneficio >= 0;\n"
        base = "constraint "
        base2 = " <= "
        
        for i in range(len(self.listaDeRegiones)):
            stringX = stringX + base + str(self.listaDeRegiones[i].get_EscalaValoracion()) + "*" + self.listaDeRegiones[i].get_nombreCorto() + base2 + str(self.listaDeRegiones[i].get_poblacion()) + ";\n"
               

       
        self.stringFinal = self.stringFinal + stringX + "\n"
        
    def noNegatividad(self):
        stringX = "constraint Beneficio >= 0;\n"
        base = "constraint "
        base2 = " >= 0;\n"
        
        for regionX in self.listaDeRegiones:        
            stringX = stringX + base + regionX.get_nombreCorto() + base2
        
        self.stringFinal = self.stringFinal + stringX + "\n"
        # print(stringX)
        
    def funcionObjetivo(self):
        stringX = "constraint Beneficio = "
        stringCola = ";\nsolve maximize Beneficio;\n"
        
        for i in range(len(self.listaDeRegiones)):
            stringX = stringX + str(self.listaDeRegiones[i].get_EscalaValoracion()) + "*" + self.listaDeRegiones[i].get_nombreCorto()
            
            if (i != (len(self.listaDeRegiones)-1)):
                stringX = stringX + " + "
        
        stringX = stringX + stringCola
        
        self.stringFinal = self.stringFinal + stringX + "\n"
        print(self.stringFinal)

    def calcular(self, siCondicionesA):
        self.crearVarRegiones()
        self.kitsPorUnidad()
        self.Unidades()
        self.costosAdecuacion()
        
        if(siCondicionesA):
            self.condicionesAdicionales() 
        
        self.poblacion()
        self.noNegatividad()
        self.funcionObjetivo()
        
        # desde aca se resilve el codigo en minizinc, en alguna parte desde aca iria la funcion de parar en X minutos        
        
        # Create a MiniZinc model
        model = mz.Model()
        model.add_string(self.stringFinal)

        # Transform Model into a instance
        gecode = mz.Solver.lookup("gecode")
        inst = mz.Instance(gecode, model)

        # Solve the instance
        result = inst.solve()
        
        print("*************************   RESULTADOS MINIZINC   *************************")
        
        for regionX in self.listaDeRegiones:
            nombreRegionX = str(regionX.get_nombreCorto()) + " = "
            resultadoX = result[str(regionX.get_nombreCorto())]
            print(resultadoX)
            
            print(nombreRegionX, end = "")
            print(resultadoX)
            
            self.stringResultado = self.stringResultado + nombreRegionX + str(resultadoX) + "\n"

        self.stringResultado = self.stringResultado + "Beneficio = " + str(result["Beneficio"]) + "\n"
        
        print("Beneficio", end = " = ")
        print(result["Beneficio"])
        print("\n*************************   FIN DE PROGRAMA   *************************")

    def getResultado(self):
        return self.stringResultado
