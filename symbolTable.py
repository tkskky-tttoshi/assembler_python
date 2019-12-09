#Don't Change default_symboltable
default_symboltable={"R0":0,"R1":1,"R2":2,"R3":3,"R4":4,"R5":5,"R6":6,"R7":7,"R8":8,"R9":9,"R10":10,"R11":11,"R12":12,"R13":13,"R14":14,"R15":15,
"SCREEN":16384,"KBD":24576,"SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4}
#Can Change symboltable
symboltable={"R0":0,"R1":1,"R2":2,"R3":3,"R4":4,"R5":5,"R6":6,"R7":7,"R8":8,"R9":9,"R10":10,"R11":11,"R12":12,"R13":13,"R14":14,"R15":15,
"SCREEN":16384,"KBD":24576,"SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4}

class symbolTable:
    def __init__(self):
        pass
    def addEntry(self,symbol, address):
        #Adds the (sym, add) to the Table
        new_tuple={symbol:address}
        if not self.contains(symbol):
            symboltable.update(new_tuple)

    def contains(self,symbol):
        #Check the existence of the symbol
        return symbol in default_symboltable

    def getAddress(self,symbol):
        #Returns the Address associated with the symbol
        return symboltable[symbol]