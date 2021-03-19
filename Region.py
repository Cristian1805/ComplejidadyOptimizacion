class Region:
    
    def __init__(self, nombreCorto, nombre, poblacion,congeladores, CongeladoresActuales, unidadesReque, costos, muertes):
        
        self.nombreCorto = nombreCorto
        self.nombre = nombre
        self.poblacion = (poblacion*10000)
        self.congeladores = congeladores
        self.CongeladoresActuales = CongeladoresActuales
        self.unidadesReque = unidadesReque
        self.costos = costos*100000
        self.muertes = muertes
        self.proporcion = "{:.6f}".format(self.congeladores / self.CongeladoresActuales)
        self.escalaValoracion = ""
        #self.muertePorMillon  =  self.poblacion/self.muertes
        
        # estas aun no estoy seguro de como incluirlas ademas creo que faltarian mas variables pero sno se como son los calculos al final
        self.vacunasPorEstacion = ""
        self.vacunasDisponibles = ""


    def get_nombre(self):
        return self.nombre
    
    def get_nombreCorto(self):
        return self.nombreCorto

    def get_poblacion(self):
        return self.poblacion
    
    def get_congeladores(self): 
        return self.congeladores
    
    def get_CongeladoresActuales(self):
        return self.CongeladoresActuales
    
    def get_unidadesReque(self):
        return self.unidadesReque
    
    def get_costos(self):
        return self.costos
    
    def get_muertes(self):
        return self.muertes
    
    def get_proporcion(self):
        return self.proporcion
    
    def get_EscalaValoracion(self):
        return self.escalaValoracion
    
    def get_vacunasPorEstacion(self):
        return self.vacunasPorEstacion
    
    def get_vacunasDisponibles(self):
        return self.vacunasDisponibles
    
    def set_EscalaValoracion(self, escalaValoracion):
        self.escalaValoracion = escalaValoracion


    def printRegion(self):
        print(self.nombre, end=" - ")
        print(self.nombreCorto, end=" - ")
        print(self.poblacion, end=" - ")
        print(self.congeladores, end=" - ")
        print(self.CongeladoresActuales, end=" - ")
        print(self.unidadesReque, end=" - ")
        print(self.costos, end=" - ")
        print(self.muertes, end=" - ")
        print(self.proporcion, end=" - ")
        print(self.escalaValoracion)