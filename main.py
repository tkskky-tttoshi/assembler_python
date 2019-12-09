import parser as pa
import symbolTable as st
import code as co


def make_c_binary(dest_binary,comp_binary,jump_binary):
    #Make C Binary Code
    return "111"+comp_binary+dest_binary+jump_binary

def make_al_binary(this_address):
    #Make A or L Binary Code
    binary=bin(this_address).lstrip("0b")

    return binary.zfill(16)

file_name="MaxL"
file_data=open("HW-05/"+file_name+".asm","r")
line=file_data.readline()
lines=""
#read document and blank line, and put them onto list
lines=file_data.read().strip().split("\n")
file_data.close

parser=pa.parser(lines)
code=co.code()
symboltable=st.symbolTable()

#Address
n=16
#Number of Sentense
sen=1

#New Binary Hack File
new_file=open(file_name+".hack","wt")
this_binary="0000000000000000"
#Routine Until the Last Sentense
while parser.hasMoreCommands():
    parser.advance()
    this_command=parser.commandType()
    if this_command == parser.C_COMMAND:
        print("Now C Command")
        dest_binary=code.dest(parser.dest())
        comp_binary=code.comp(parser.comp())
        jump_binary=code.jump(parser.jump())
        #Make C Binary Code
        this_binary=make_c_binary(dest_binary,comp_binary,jump_binary)
        

    elif this_command == (parser.A_COMMAND or parser.L_COMMAND):
        print("Now A or L Command")
        #Current Symbol
        this_symbol=parser.symbol()
        this_address=0
        #Current Address
        if this_command==parser.A_COMMAND:
            #Distinguish the char from int 
            #if char: send it to symboltable, elif int: use the original digit
            if this_symbol.isdecimal():
                this_address=int(this_symbol)
            else:
                this_address = n
        elif this_command==parser.L_COMMAND:
            this_address = sen
        else:
            print("in-this Error")
        #Set the Current Symbol and Address
        symboltable.addEntry(this_symbol,this_address)
        print("This Symbol:"+str( this_symbol )+" This Address:"+str(this_address))
        #Get the Address of the Symbol
        this_address=symboltable.getAddress(this_symbol)
        #Make A or L Binary Code
        this_binary=make_al_binary(this_address)

        n=n+1
        sen=sen+1
    else:
        print("Understanding Error")

    print("----"+this_binary+"----")
    print("")
    new_file.write(this_binary+"\n")
    new_file.close


print(lines)
