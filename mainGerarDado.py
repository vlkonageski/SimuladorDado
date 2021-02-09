from PyQt5 import uic,QtWidgets
import random

def girarDado():
    dado = random.randint(1,6)
    TelaSimuladorDado.label_2.setText(str(dado))

app=QtWidgets.QApplication([])
TelaSimuladorDado=uic.loadUi("TelaSimuladorDado.ui")
TelaSimuladorDado.pushButton.clicked.connect(girarDado)

TelaSimuladorDado.show()
app.exec()