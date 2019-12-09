
dest_dic={"":"000","M":"001","D":"010","MD":"011","A":"100","AM":"101","AD":"110","AMD":"111"}
jump_dic={"":"000","JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JME":"101","JLE":"110","JMP":"111"}
comp_dic0={"0":"101010","1":"111111","-1":"111010","D":"001100","A":"110000","!D":"001101","!A":"110001",
"D+1":"011111","A+1":"110111","D-1":"001110","A-1":"110010","D+A":"000010","D-A":"010011","A-D":"000111","D&A":"000000","Dk|A":"010101"}
comp_dic1={"M":"110000","!M":"110001","-M":"11001","M+1":"110111","M-1":"110010","D+M":"000010","D-M":"010011","M-D":"000111","D&M":"000000","D|M":"010101"}

class code:
    def __init__(self):
        pass

    def dest(self,mnemonic):
        print("mnemonic:"+mnemonic) 
        if mnemonic in dest_dic:
            print("The Key Already Exists")
            return dest_dic[mnemonic]
        else:
            print("dest Wrong Grammar")

    def comp(self,mnemonic):
        if mnemonic in comp_dic0:
            return "0"+comp_dic0[mnemonic]
        elif mnemonic in comp_dic1:
            return "1"+comp_dic1[mnemonic]
        else:
            print("comp Wrong Grammar")
            

    def jump(self,mnemonic):
        if mnemonic in jump_dic:
            return jump_dic[mnemonic]
        else:
            print("jump Wrong Grammar")








