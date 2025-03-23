import pandas as pd
from PyQt5 import QtWidgets, uic, QtCore
from Data_Preparer import dataChamge


class DataFrameModel(QtCore.QAbstractTableModel):
    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame(), parent=None):
        super(DataFrameModel, self).__init__(parent)
        self._dataframe = df

    def setDataFrame(self, dataframe):
        self.beginResetModel()
        self._dataframe = dataframe.copy()
        self.endResetModel()

    def dataFrame(self):
        return self._dataframe

    dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=dataFrame, fset=setDataFrame)

    @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._dataframe.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self._dataframe.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount() \
            and 0 <= index.column() < self.columnCount()):
            return QtCore.QVariant()
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype

        val = self._dataframe.iloc[row][col]
        if role == QtCore.Qt.DisplayRole:
            return str(val)
        elif role == DataFrameModel.ValueRole:
            return val
        if role == DataFrameModel.DtypeRole:
            return dt
        return QtCore.QVariant()

    def roleNames(self):
        roles = {
            QtCore.Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value'
        }
        return roles


class UiTables(QtWidgets.QMainWindow):
    def __init__(self, table, uiname, u=0):
        super(UiTables, self).__init__()
        uic.loadUi(uiname, self)
        self.MorphTableShowerFinal = self.findChild(QtWidgets.QTableView, 'MorphTableShowerFinal')
        changer = dataChamge()
        if u==0:
            changer.makeMorpHtable(table)
            self.df = changer.morph1
        elif u==1:
            changer.makeDecisionTable(table)
            self.df = changer.decisions
        else:
            self.df=table
        print(self.df)
        model = DataFrameModel(self.df)
        self.MorphTableShowerFinal.model = model
        self.MorphTableShowerFinal.setModel(model)

    def launch(self):
        self.show()


"""app = QtWidgets.QApplication(sys.argv)
window = UiTables("baseAlternatives.csv",'MorphTableShow1.ui')
window1 = UiTables("endindVariants.csv",'ConnectTableShow1.ui')
app.exec_()"""



