class Region:
    
    def __init__(self, nombreCorto, nombre, congeladores, congeladoresActuales, personalReque, costos, muertes):
        
        self.nombreCorto = nombreCorto
        self.nombre = nombre
        ##self.poblacion = (poblacion*100000)
        self.congeladoresActuales = congeladoresActuales
        self.personalReque = personalReque
        self.costos = costos*1000000
        self.muertes = muertes
        self.proporcion = "{:.6f}".format(self.CongeladoresActuales / self.congeladores)
        self.escalaValoracion = ""
        #self.muertePorMillon  =  self.poblacion/self.muertes
        
        # estas aun no estoy seguro de como incluirlas ademas creo que faltarian mas variables pero sno se como son los calculos al final
        self.ventiladoresPorEstacion = ""
        self.ventiladoresDisponibles = ""
        
    def get_nombre(self):
        return self.nombre
    
    def get_nombreCorto(self):
        return self.nombreCorto
    
    #def get_poblacion(self):
     #   return self.poblacion
    
    def get_congeladoresActuales(self):
        return self.congeladoresActuales
    
    def get_unidadesReque(self):
        return self.personalReque
    
    def get_costos(self):
        return self.costos
    
    def get_muertes(self):
        return self.muertes
    
    def get_proporcion(self):
        return self.proporcion
    
    def get_EscalaValoracion(self):
        return self.escalaValoracion
    
    def get_ventiladoresPorEstacion(self):
        return self.ventiladoresPorEstacion
    
    def get_ventiladoresDisponibles(self):
        return self.ventiladoresDisponibles
    
    def set_EscalaValoracion(self, escalaValoracion):
        self.escalaValoracion = escalaValoracion

    def get_MuertePorMillon(self):
        return self.muertePorMillon

    def printRegion(self):
        print(self.nombre, end=" - ")
        print(self.nombreCorto, end=" - ")
        print(self.poblacion, end=" - ")
        print(self.congeladoresActuales, end=" - ")
        print(self.personalReque, end=" - ")
        print(self.costos, end=" - ")
        print(self.muertes, end=" - ")
        print(self.proporcion, end=" - ")
        print(self.muertePorMillon, end=" - ")
        print(self.escalaValoracion)