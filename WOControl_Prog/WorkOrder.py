from xml.sax.handler import DTDHandler
import mysql.connector

#Conección con la base de datos
mydb = mysql.connector.connect(user='root',
                               password='Slimypanda97!',
                               database='produccion')
mycursor = mydb.cursor()

class WorkOrder:
    def __init__(self, df):
        # Definiciones y cabeceras por cada elemento en DataMatrix
        # [)>@06
        # @0PN 12204716-00
        # @1MP FS32K146HFT0VLHR
        # @2DT 2420
        # @3WO 029663
        # @4CU KOS
        # @5MS 3
        # @6BP 12034852
        # @7BT Q25010
        # @8CS E653F36Ah
        # @9QT 500
        # @ALT QB32JG.000
        # @BPO NA
        # @CMK 12204716-00-ESW0067
        # @DCN Kostal
        # @EJN 12204716-00
        # @FEP EPS MEXICO@@
        self.df = df
        self.hd_header = '[)>@06'
        self.hd_PPN = '@0PN'
        self.hd_MPN = '@1MP'
        self.hd_DT = '@2DT'
        self.hd_WO = '@3WO'
        self.hd_CU = '@4CU'
        self.hd_MS = '@5MS'
        self.hd_BP = '@6BP'
        self.hd_BT = '@7BT'
        self.hd_CS = '@8CS'
        self.hd_QT = '@9QT'
        self.hd_LT = '@ALT'
        self.hd_PO = '@BPO'
        self.hd_MK = '@CMK'
        self.hd_CN = '@DCN'
        self.hd_JN = '@EJN'
        self.hd_EP = '@FEP'
        self.hd_end = '@@'
        self.Offset = 4

        #Orden de la trama en DataMatrix
        self.Stack = [self.hd_header, self.hd_PPN, self.hd_MPN, self.hd_DT, self.hd_WO, self.hd_CU, self.hd_MS,
                      self.hd_BP, self.hd_BT, self.hd_CS, self.hd_QT, self.hd_LT, self.hd_PO, self.hd_MK,
                      self.hd_CN, self.hd_JN, self.hd_EP, self.hd_end]

        for i in range(1,17):
            result = ''
            cursor_i = self.df.find(self.Stack[i]) + self.Offset
            cursor_f = self.df.find(self.Stack[i+1])
            for j in range(cursor_f - cursor_i):
                result = result + df[cursor_i + j]
            self.Stack[i] = result

        #Asignación de atributos
        self.PPN = self.Stack[1]
        self.MPN = self.Stack[2]
        self.DT = self.Stack[3]
        self.WO = self.Stack[4]
        self.CU = self.Stack[5]
        self.MS = self.Stack[6]
        self.BP = self.Stack[7]
        self.BT = self.Stack[8]
        self.CS = self.Stack[9]
        self.QT = self.Stack[10]
        self.LT = self.Stack[11]
        self.PO = self.Stack[12]
        self.MK = self.Stack[13]
        self.CN = self.Stack[14]
        self.JN = self.Stack[15]
        self.EP = self.Stack[16]
    def isValid(self):
        if self.df.find(self.hd_header) == 0:
            if self.df.find(self.hd_end) != -1:
                return True
            else:
                return False
        else:
            return False
    def Prod_Exists(self):
        sql = "SELECT * FROM produccion WHERE WO = %s"
        val = (self.WO,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result != []:
            return True
        else:
            return False
    def Prod_Add(self):
        sql = "INSERT INTO produccion(PPN,MPN,DT,WO,CU,MS,BP,BT,CS,QT,LT,PO,MK,CN,JN,EP) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.PPN, self.MPN, self.DT, self.WO, self.CU, self.MS, self.BP, self.BT, self.CS, self.QT, self.LT, self.PO,
               self.MK, self.CN, self.JN, self.EP)
        mycursor.execute(sql, val)
        mydb.commit()
    def Prod_Delete(self):
        sql = "DELETE from produccion WHERE WO = %s"
        val = (self.WO,)
        mycursor.execute(sql,val)
        mydb.commit()
    def PT_Exists(self):
        sql = "SELECT * FROM producto_terminado WHERE WO = %s"
        val = (self.WO,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result != []:
            return True
        else:
            return False
    def PT_Add(self):
        sql = "INSERT INTO producto_terminado(PPN,MPN,DT,WO,CU,MS,BP,BT,CS,QT,LT,PO,MK,CN,JN,EP) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.PPN, self.MPN, self.DT, self.WO, self.CU, self.MS, self.BP, self.BT, self.CS, self.QT, self.LT, self.PO, self.MK, self.CN, self.JN, self.EP)
        mycursor.execute(sql, val)
    def PT_Delete(self):
        sql = "DELETE from producto_terminado WHERE WO = %s"
        val = (self.WO,)
        mycursor.execute(sql, val)
        mydb.commit()


def Prod_Show():
    sql = "SELECT * FROM produccion"
    mycursor.execute(sql)
    number_rows = mycursor.rowcount
    result = mycursor.fetchall()
    print(result)
    print(number_rows)