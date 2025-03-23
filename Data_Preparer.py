import pandas as pd


class dataChamge:
    def __init__(self):

        m1 = ["До 20 ", "До 50","До 100","Понад 100"]
        m2 = ["Повна", "Частково імпорт", "Більшість імпорт", "Готові комплекти"]
        m3 = ["Поліпшення", "Ще більше погіршення", "Збереження негативної тенденції",""]
        m4 = ["Так", "Ні","",""]
        m5 = ["Так", "Ні","",""]
        m6 = ["Дуже низька", "Нижче бажаного", "Достатня", "Висока"]
        d1={"Виготовлено машин на місяць": m1, "Локалізація": m2, "Фінансовий стан": m3, "Стабільна якість": m4, "Готовність йти назустріч": m5, "Надійність контрактів": m6}
        self.morph1 = pd.DataFrame(d1)
        d1 = ["Прямі інвестиції", "Оборонне замовлення", "Податкові пільги", "Націоналізація","Уникнення ведення справ"]
        self.decisions = pd.DataFrame(d1, columns=["Можливі рішення"])

    def makeMorpHtable(self,alternatives):
        for i in range(6):
            for j in range(4):
                self.morph1.iloc[j, i] = self.morph1.iloc[j, i] + " = " + str(alternatives.iloc[j, i])
            if i == 2:
                self.morph1.iloc[3, i] = " "
            elif (i==3) or (i==4):
                self.morph1.iloc[3, i] = " "
                self.morph1.iloc[2,i] = " "



    def makeDecisionTable(self, decisis):
        for j in range(5):
            self.decisions.iloc[j, 0] = self.decisions.iloc[j, 0] + " = " + str(decisis.iloc[j, 1])

    def recognise_config(self,config, decis):
        decidi = decis.iloc[:,1].idxmax()
        config = config.loc[:,"1":"6"]
        for k in range(6):
            i, j = config.iloc[0,k].split('.')
            config.iloc[0,k] = self.morph1.iloc[int(j)-1,int(i)-1]
        decname = self.decisions.iloc[decidi,0]
        config.insert(6, "Decision", [decname], True)
        return config
        


"""
morphTabled = pd.read_csv("baseAlternatives.csv").fillna(0)
data = dataChamge()
print(data.morph1)
data.makeMorpHtable(morphTabled)
print(data.morph1)
"""
"""data = dataChamge()
datas = {'1':'1.3', '2':'2.4', '3':'3.3', '4':'4.2', '5':'5.2', '6':'6.1'}
datas1 = pd.DataFrame(datas, index=[0])
print(data.recognise_config(datas1))"""