from PyQt5 import uic,QtWidgets
import random

def jogarDado():
    dado = random.randint(1,6)
    TelaSimuladorDado.label_2.setText(str(dado))

app=QtWidgets.QApplication([])
TelaSimuladorDado=uic.loadUi("TelaSimuladorDado.ui")
TelaSimuladorDado.pushButton.clicked.connect(jogarDado)

TelaSimuladorDado.show()
app.exec()