import pandas as pd


class Data:
    def __init__(self,filename1,filename2, filename3):
        self.morphTable = pd.read_csv(filename1).fillna(0)
        self.connectionTable = pd.read_csv(filename2,index_col="index").fillna(0)
        self.matrixOfUzgodzhiennia = pd.read_csv(filename3,index_col="index").fillna(0)



    def return_morphTable(self):
        return self.morphTable


    def return_connectionTable(self):
        return self.connectionTable


    def return_connectionTable(self):
        return self.connectionTable