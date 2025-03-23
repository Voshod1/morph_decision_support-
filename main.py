import pandas as pd
from PyQt5 import QtWidgets, uic
import sys
from file_loader import Data
from forMorphTable import UiTables
from MorphologicalAnalysis import MorphologicalMethod
from Data_Preparer import dataChamge
import numpy as np


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('MAinWindow.ui', self)
        #Input Data
        self.M1field = self.findChild(QtWidgets.QLineEdit, 'M1file')
        self.M2field = self.findChild(QtWidgets.QLineEdit, 'M2file')
        self.M3field = self.findChild(QtWidgets.QLineEdit, 'M3file')
        #Buttons
        self.Launch = self.findChild(QtWidgets.QPushButton, 'LaunchButton')
        self.MorphPossibleOpen = self.findChild(QtWidgets.QPushButton, 'CalForMorphPossibilities')
        self.ConfigurationsOpen = self.findChild(QtWidgets.QPushButton, 'CalForConfigurations')
        self.DecisionsOpen = self.findChild(QtWidgets.QPushButton, 'CalForDecisionsTable')
        self.helping = self.findChild(QtWidgets.QAction,"OpenHelp")
        #ButtonsBinding
        self.Launch.clicked.connect(self.open_launchProgram)
        self.MorphPossibleOpen.clicked.connect(self.open_CalMorphPossible)
        self.ConfigurationsOpen.clicked.connect(self.open_CalForConfigurations)
        self.DecisionsOpen.clicked.connect(self.open_CalForDecisionsTable)
        self.helping.triggered.connect(self.open_help)
        #OutputResults
        self.NumberOfPeoducedFinal = self.findChild(QtWidgets.QLabel, 'NumberOfPeoducedFinal')
        self.LocalisationFinal = self.findChild(QtWidgets.QLabel, 'LocalisationFinal')
        self.FinancialStatusFinal = self.findChild(QtWidgets.QLabel, 'FinancialStatusFinal')
        self.StableQualityFinal = self.findChild(QtWidgets.QLabel, 'StableQualityFinal')
        self.AnsweresFinal = self.findChild(QtWidgets.QLabel, 'AnsweresFinal')
        self.ReliabilityFinal = self.findChild(QtWidgets.QLabel, 'ReliabilityFinal')
        self.BestDecisionFinal = self.findChild(QtWidgets.QLabel, 'BestDecisionFinal')
        self.show()


    #For launch
    def open_launchProgram(self):
        self.data = Data(self.M1field.text(),self.M2field.text(),self.M3field.text())
        morphWork = MorphologicalMethod(self.data)
        morphWork.work()
        self.data = morphWork.data
        self.bestResult = dataChamge().recognise_config(morphWork.resultConfig,self.data.matrixOfUzgodzhiennia)
        print(self.bestResult)
        self.displayResults()
        return 0


    #ForOpening CalMorphPossibleOpen
    def open_CalMorphPossible(self):
        self.table1 = UiTables(self.data.morphTable, 'MorphTableShow1.ui')
        self.table1.show()
        return 0


    #ForOpening CalForConfigurations
    def open_CalForConfigurations(self):
        self.table2 = UiTables(self.data.connectionTable,'ConnectTableShow1.ui',u=2)
        self.table2.show()
        return 0


    #ForOpening CalForDecisionsTable
    def open_CalForDecisionsTable(self):
        self.table1 = UiTables(self.data.matrixOfUzgodzhiennia, 'MorphTableShow1.ui',u=1)
        self.table1.show()
        return 0


    def displayResults(self):
        self.NumberOfPeoducedFinal.setText(self.bestResult.iloc[0,0])
        self.LocalisationFinal.setText(self.bestResult.iloc[0,1])
        self.FinancialStatusFinal.setText(self.bestResult.iloc[0,2])
        self.StableQualityFinal.setText(self.bestResult.iloc[0,3])
        self.AnsweresFinal.setText(self.bestResult.iloc[0,4])
        self.ReliabilityFinal.setText(self.bestResult.iloc[0,5])
        self.BestDecisionFinal.setText(self.bestResult.iloc[0,6])


    def open_help(self):
        instructions = ["Введіть назви файлів з даними", "Натисніть ЗАПУСК РОБОТИ"]
        inst_outcomes = ["Для відкриття параметрів Натиснути кнопку","Таблиця ймовірностей для характеристик"]
        datas = {"Запуск":instructions, "Виведення таблиці станів:": inst_outcomes, "Виведення доступних конфігурацій":["Для відкриття конфігурацій Натиснути кнопку","Таблиця ймовірностей для конфігурацій",],
                 "Виведення всіх доступних рішень":["Натиснути кнопку","Таблиця ефективності ріщень"], "Особливості програми":["Всі таблиці зберігаються на ПК", "Для роботи з новими даними просто введдіть їх"]}
        helper = pd.DataFrame(datas)
        self.table1 = UiTables(helper, 'MorphTableShow1.ui', u=2)
        self.table1.show()
        return 0


app = QtWidgets.QApplication(sys.argv)
window = Ui()

app.exec_()



