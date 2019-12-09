import re
class parser:

    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3

    def __init__(self,assem):
        self.assem=assem
        

    def hasMoreCommands(self):
        return bool(self.assem[:] )

    def advance(self):
        if self.hasMoreCommands():
            self.line = self.assem.pop(0)
            print(self.line)
        #remove whitespace
        self.line=self.line.strip()
    
    def commandType(self):
        init_char=self.line[0]
        #print("init_char:"+init_char)
        if init_char=="@":
            return self.A_COMMAND
        elif init_char == "(":
            return self.L_COMMAND
        else:
            return self.C_COMMAND

    #cut out comment-out
    def cutout_comment(self,str):
        return re.split("[ /]",str)[0]

    def symbol(self):
        if self.commandType()==self.L_COMMAND:
            return self.line[1:-2]
        elif self.commandType()==self.A_COMMAND:
            return self.line[1:]
        return None

    def dest(self):
        if self.commandType()==self.C_COMMAND:
            #Cut Out the Comment-out
            dest=self.cutout_comment(self.line)
            #Split it by "=""
            if "=" in dest:
                dest=dest.split("=")
                print("Splited Dest:"+str(dest))
                return dest[0]
        return ""

    def comp(self):
        if self.commandType()==self.C_COMMAND:
            comp=self.cutout_comment(self.line)
            #In Comp Parts, There are Three Kinds of Parts
            #1. A=D, 2.D;JEQ, 3.M=D;JEQ

            if "=" in comp and ";" in comp:
                comp=re.split("[;=]",comp)
                return comp[1]
            elif "=" in comp and (";" not in comp):
                comp=comp.split("=")
                return comp[1]
                
            print("comp:"+str( comp ))
            return comp[0]
        return ""

    def jump(self):
        if self.commandType()==self.C_COMMAND:
            jump=self.cutout_comment(self.line)
            jump=re.split("[;]",jump)
            if len(jump)>=2:
                return jump[-1]
            else:
                return ""
            print("jump:"+str( jump ))
        return ""

        






    



