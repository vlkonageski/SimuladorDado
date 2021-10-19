from PyQt6 import uic,QtWidgets
import random

def abrirD4():
    TelaSimuladorDado.show()
    TelaSimuladorDado.pushButton.clicked.connect(jogarD4)
    TelaSimuladorDado.pushButton_2.clicked.connect(fecharD4)

def fecharD4():
    TelaSimuladorDado.label_2.clear()
    TelaSimuladorDado.close()

def jogarD4():
    dado = random.randint(1,4)
    TelaSimuladorDado.label_2.setText(str(dado))

def abrirD6():
    TelaSimuladorDado.show()
    TelaSimuladorDado.pushButton.clicked.connect(jogarD6)
    TelaSimuladorDado.pushButton_2.clicked.connect(fecharD6)

def fecharD6():
    TelaSimuladorDado.label_2.clear()
    TelaSimuladorDado.close()

def jogarD6():
    dado = random.randint(1,6)
    TelaSimuladorDado.label_2.setText(str(dado))

def abrirD8():
    TelaSimuladorDado.show()
    TelaSimuladorDado.pushButton.clicked.connect(jogarD8)
    TelaSimuladorDado.pushButton_2.clicked.connect(fecharD8)

def fecharD8():
    TelaSimuladorDado.label_2.clear()
    TelaSimuladorDado.close()

def jogarD8():
    dado = random.randint(1,8)
    TelaSimuladorDado.label_2.setText(str(dado))

def abrirD10():
    TelaSimuladorDado.show()
    TelaSimuladorDado.pushButton.clicked.connect(jogarD10)
    TelaSimuladorDado.pushButton_2.clicked.connect(fecharD10)

def fecharD10():
    TelaSimuladorDado.label_2.clear()
    TelaSimuladorDado.close()

def jogarD10():
    dado = random.randint(1,10)
    TelaSimuladorDado.label_2.setText(str(dado))

def abrirD12():
    TelaSimuladorDado.show()
    TelaSimuladorDado.pushButton.clicked.connect(jogarD12)
    TelaSimuladorDado.pushButton_2.clicked.connect(fecharD12)

def fecharD12():
    TelaSimuladorDado.label_2.clear()
    TelaSimuladorDado.close()

def jogarD12():
    dado = random.randint(1,12)
    TelaSimuladorDado.label_2.setText(str(dado))

def abrirD20():
    TelaSimuladorDado.show()
    TelaSimuladorDado.pushButton.clicked.connect(jogarD20)
    TelaSimuladorDado.pushButton_2.clicked.connect(fecharD20)

def fecharD20():
    TelaSimuladorDado.label_2.clear()
    TelaSimuladorDado.close()

def jogarD20():
    dado = random.randint(1,20)
    TelaSimuladorDado.label_2.setText(str(dado))
    

app=QtWidgets.QApplication([])
MenuPrincipal=uic.loadUi("MenuPrincipal.ui")
TelaSimuladorDado=uic.loadUi("TelaSimuladorDado.ui")
MenuPrincipal.pushButton.clicked.connect(abrirD4)
MenuPrincipal.pushButton_7.clicked.connect(abrirD6)
MenuPrincipal.pushButton_2.clicked.connect(abrirD8)
MenuPrincipal.pushButton_3.clicked.connect(abrirD10)
MenuPrincipal.pushButton_4.clicked.connect(abrirD12)
MenuPrincipal.pushButton_5.clicked.connect(abrirD20)

MenuPrincipal.show()
app.exec()