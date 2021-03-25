# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mateo\proyectoComplejidad\interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
import DataLoad as ld
import Region as rg
import MinizincMy as mz


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 570)
        MainWindow.setWindowIcon(QtGui.QIcon('ICOn.png'))
        MainWindow.setStyleSheet("color: green;"
                        "background-image: url(Plague-inc.jpg);"
                        "background-attachment: fixed;"
                        "selection-background-color: blue;"
                         "text-align: center;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)  
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet( "text-align: center;")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 101, 23))
        self.pushButton.setStyleSheet("color:white")

        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 520, 221, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("color:white")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 470, 131, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("color:white")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 60, 800, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("background:white;")


        self.QFileDialog = QtWidgets.QFileDialog()
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 400, 21, 21))
        self.label.setObjectName("label")        
        self.label.setStyleSheet("color:white")
       
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 400, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:white")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 400, 71, 21))
        self.label_3.setObjectName("label_3")       
        self.label_3.setStyleSheet("color:white")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 470, 71, 27))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color:white")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 510, 50, 31))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color:white")
                
        self.lineEditkits = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditkits.setGeometry(QtCore.QRect(90, 400, 113, 20))
        self.lineEditkits.setObjectName("lineEdit")
        self.lineEditkits.setEnabled(False)
        self.lineEditkits.setStyleSheet("color:white;")

        self.lineEditUnidades = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUnidades.setGeometry(QtCore.QRect(270, 400, 113, 20))
        self.lineEditUnidades.setObjectName("lineEdit_2")
        self.lineEditUnidades.setEnabled(False)
        self.lineEditUnidades.setStyleSheet("color:white;")


        self.lineEditPresupuesto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPresupuesto.setGeometry(QtCore.QRect(500, 400, 121, 21))
        self.lineEditPresupuesto.setObjectName("lineEdit_3")
        self.lineEditPresupuesto.setEnabled(False)
        self.lineEditPresupuesto.setStyleSheet("color:white;")


        self.lineEditCualificacion = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCualificacion.setGeometry(QtCore.QRect(290, 470, 121, 21))
        self.lineEditCualificacion.setObjectName("lineEdit_4")
        self.lineEditCualificacion.setEnabled(False)
        self.lineEditCualificacion.setStyleSheet("color:white;")


        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 440, 141, 17))
        self.radioButton.setObjectName("radioButton")
        
            
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.listaDeRegiones = []
        self.listaNombreRegionCA = [] 
        self.listaCualificacionCA = [] 
        self.siCondicionesA = False
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid APP"))
           
        self.pushButton.setText(_translate("MainWindow", "Cargar Archivo"))
        self.pushButton.clicked.connect(self.cargarArchivo)
        
        self.label.setText(_translate("MainWindow", "Kits"))
        self.label_2.setText(_translate("MainWindow", "Unidades"))
        self.label_3.setText(_translate("MainWindow", "Presupuesto"))        
        self.label_4.setText(_translate("MainWindow", "Cualificacion"))
        self.label_5.setText(_translate("MainWindow", "Solucion"))
        
        self.radioButton.setText(_translate("MainWindow", "Condiciones adicionales"))
        self.radioButton.clicked.connect(self.radioButtonAction)
        self.radioButton.setEnabled(False)
        
        self.pushButton_3.setText(_translate("MainWindow", "Cargar Archivo C.A"))        
        self.pushButton_3.clicked.connect(self.cargarCondicionesA)
        self.pushButton_3.setEnabled(False)
        
        self.pushButton_2.setText(_translate("MainWindow", "Calcular Distribucion de Vacunas"))        
        self.pushButton_2.clicked.connect(self.calcularDistribucionV)
        self.pushButton_2.setEnabled(False) 
       
    def verDialogo(self, resultadoFinal):
        dialogo = QMessageBox()
        dialogo.setStyleSheet("color: white;"
                        "background-image: url(Plague-inc.jpg);"
                        "background-attachment: fixed;" "text-align: center;")
        dialogo.setWindowTitle("Resultados del Analisis")
        dialogo.setText(resultadoFinal)
        x =  dialogo.exec_()
        
    
    def cargarArchivo(self):       
        
        fname = self.QFileDialog.getOpenFileName(None, 'Open file',  "*.xlsx" )
            
        if (fname[0]!=""):
            # self.pushButton.setText("Button is clicked")
            ruta = str(fname[0])
                
            load = ld.DataLoad(ruta)
            listaDeRegiones = load.getRegiones()
            listaDeTitulos = load.getTitulos()
            
            # poblacion de la tabla en interfaz
            self.tableWidget.setColumnCount(len(listaDeTitulos))
            self.tableWidget.setRowCount(len(listaDeRegiones))
            
            # cargando header en tabla
            self.tableWidget.setHorizontalHeaderLabels(listaDeTitulos)
            
            # cargando datos a tabla
            listaDeRegiones = sorted(listaDeRegiones, key = lambda region: region.get_EscalaValoracion(), reverse=True)

            row = 0
            for regionX in listaDeRegiones:
                item = QtWidgets.QTableWidgetItem(str(regionX.get_nombre()))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(row, 0,  item)
                
                item = QtWidgets.QTableWidgetItem(str(regionX.get_poblacion()))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(row, 1,  item)
                
                item = QtWidgets.QTableWidgetItem(str(regionX.get_congeladores()))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(row, 2,  item)
                
                item = QtWidgets.QTableWidgetItem(str(regionX.get_unidadesReque()))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(row, 3,  item)
                
                item =  QtWidgets.QTableWidgetItem(str(regionX.get_costos()))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(row, 4, item)
                
                item = QtWidgets.QTableWidgetItem(str(regionX.get_muertes()))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(row, 5,  item)
       
                row = row + 1               
            
            self.listaDeRegiones = listaDeRegiones
            self.pushButton_2.setEnabled(True)
            self.radioButton.setEnabled(True)
            self.lineEditkits.setEnabled(True)
            self.lineEditUnidades.setEnabled(True)
            self.lineEditPresupuesto.setEnabled(True)    
            
        else:
            print("no load file")

    def cargarCondicionesA(self):        
        fname = self.QFileDialog.getOpenFileName(None, 'Open file',  "*.xlsx" )
            
        if (fname[0]!=""):
            # self.pushButton.setText("Button is clicked")
            ruta = str(fname[0])
        
            load = ld.DataLoad(ruta)
            load.crearCondicionesA()
            self.listaNombreRegionCA = load.getNombreRegionesCA()
            self.listaCualificacionCA = load.getCualificaionCA()
            #  colocar el bolean de que si cargo C.A
            self.siCondicionesA = True
        else:
            self.siCondicionesA = False

    def calcularDistribucionV(self): 
        bandera = True
        if (self.lineEditkits.text() == ""):
            self.lineEditkits.setStyleSheet("border: 1px solid red;")
            bandera = False
 
        if (self.lineEditUnidades.text() == ""):
            self.lineEditUnidades.setStyleSheet("border: 1px solid red;")
            bandera = False
            
        if (self.lineEditPresupuesto.text() == ""):
            self.lineEditPresupuesto.setStyleSheet("border: 1px solid red;")
            bandera = False
        
        if (bandera):
            kitsX = self.lineEditkits.text()
            presupuestoX = self.lineEditPresupuesto.text()
            unidadesX = self.lineEditUnidades.text()
            cualificacionX = self.lineEditCualificacion.text()  
                      
            self.label_5.setText("Calculando...")
            minizinc = mz.MinizincMy(self.listaDeRegiones,unidadesX, presupuestoX,kitsX, self.listaNombreRegionCA, self.listaCualificacionCA, cualificacionX)
            minizinc.calcular(self.siCondicionesA)
            resultadoFinal = minizinc.getResultado()
            self.verDialogo(resultadoFinal)
            self.label_5.setText(resultadoFinal)
                        
            self.lineEditkits.setStyleSheet("border: 1px solid black;")
            self.lineEditUnidades.setStyleSheet("border: 1px solid black;")
            self.lineEditPresupuesto.setStyleSheet("border: 1px solid black;")
  
        else:
            self.label_5.setText("introduce valores de Kits, Personal, Presupuesto")
        
    def radioButtonAction(self):
        self.pushButton_3.setEnabled(self.radioButton.isChecked())
        self.lineEditCualificacion.setEnabled(self.radioButton.isChecked())
        self.siCondicionesA = self.radioButton.isChecked()
                    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

