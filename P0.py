""" 
Proyecto P0 de lenguajes y máquinas 
"""
import re

#Definición del lenguaje

noTerminales = []
terminales = []
parseTree= {

}

#Carga de datos

def loadLang(file):
    global terminales
    f = open(file, 'r')
    for i in f:
        terminales.append(i.strip())
    #print(terminales)     
    f.close()

def printWords(data):
    for i in data: print(i)
    pass

def openCode(file):
    data = ''
    f = open(file,'r')
    for i in f:
        i = re.sub(',',' , ',i)
        i = re.sub(';',' ; ',i)
        i = re.sub('\|',' | ',i)
        i = re.sub('\[',' [ ',i)
        i = re.sub('\]',' ] ',i)
        i = re.sub(':',' : ',i)
        i = re.sub('\n'," ",string=i) 
        i = i.lower()
        data += i
    data = data.split()
    printWords(data)
    f.close()
    return data





#FUNCIONES PARA VERIFICAR COMANDOS

def checkAssignTo(function:list[str])-> bool:
    #assignTo: n,name
    
    if function[0]==":" and function[1].isdigit() and function[2]=="," and function[3] in variables:
        print(f'Assigned {function[1]} -> {function[3]}')
        del function[0:4]
        return True
    else:
        return False

def checkGoto (function: list[str])->bool:
    #Lista de tamaño 4
    # goto: x,y
    #revisar variables----
    if function[0]==":" and (function[1].isdigit() or function[1] in variables )and function[2] == ',' and (function[4].isdigit() or function[4] in variables ) :
        del function[0:4]
        return True
    
    else:
        return False

def checkMove (function: list)-> bool:
    #Lista de tamaño 2
    # move :n

    if function [0]==":" and  (function[1].isdigit() or function[1] in variables):
        del function[0:2]
        return True
    else: 
        return False

def checkTurn (function:list)-> bool:
    #Lista de tamaño 2
    #turn: d
    if function[0]==":" and (function[1]=="left" or function[1]=="right" or function[1]=="around"):
        del function[0:2]
        return True
    else:
        return False

def checkFace (function: list)-> bool:
    #Lista de tamaño 2
    #face: o
   
    if function[0]==":" and (function[1]=="south" or function[1]=="east" or function[1]=="west" or function[1]=="north"):
        del function[0:2]
        return True
    else:
        return False

def checkPutOrPick (function: list)-> bool:
    #Lista de tamaño 4
    #put/pick: n,x
    
    if function[0]==":" and (function[1].isdigit() or function[1] in variables) and function[2]=="," and (function[3]=="balloons" or function[3]=="chips") :
        del function[0:4]
        return True
    else:
        return False

def checkMoveToOrJumpTo (function: list) -> bool:
    #Lista de tamaño 4
    #movetothe/jumptothe; n,d
    if function[0]==":" and (function[1].isdigit() or function[1] in variables) and function[2]=="," and function[3]== ('back' or 'right' or 'left' or 'front') :
        del function[0:4]
        return True
    
    else:
        return False

def checkMoveOrjumpIndir (function: list)->bool:
    #Lista de tamaño 4
    #jumpIndir: n,D
   
    if function[0]==":" and (function[1].isdigit() or function[1] in variables) and function[2]=="," and (function[3]==("south" or "north" or
        "east" or "west")) :
        del function[0:4]
        return True

    else:
        return False

def checkNop (function: list)-> bool:
    #Lista de tamaño 1
    #nop:
    if function[0]==":":
        del function[0:2]
        return True
    else:
        return False

#FUNCIONES PARA IDENTIFICAR USO DE COMANDO

def recognizeCommand (command: str, function:list[str])->bool:
    recognized=False
    if command=="assignto":
        print('Recognized command: assignto')
        recognized=checkAssignTo(function)
    elif command=="goto":
        print('Recognized command: goto')
        recognized=checkGoto(function)
    elif command=="move":
        print('Recognized command: move')
        recognized=checkMove(function)
    elif command=="turn":
        print('Recognized command: turn')
        recognized=checkTurn(function)
    elif command=="face":
        print('Recognized command: face')
        recognized=checkFace(function)
    elif command=="put" or command=="pick":
        print('Recognized command: put | pick')
        recognized=checkPutOrPick(function)
    elif command=="movetothe" or command=="jumptothe":
        print('Recognized command: movetothe | jumptothe')
        recognized=checkMoveToOrJumpTo(function)
    elif command=="moveindir" or command=="jumpindir":
        print('Recognized command: moveindir | jumpindir')
        recognized=checkMoveOrjumpIndir()
    elif command=="nop":
        print('Recognized command: nop')
        recognized=checkNop()
    return recognized

#FUNCIONES PARA VERIFICAR CONDICIONALES

def checkFacing(function: list)->bool:
    #Lista de tamaño 2
    #facing: O
    if len(function)!=2:
        return False
    elif function[0]==":" and (function[1]=="north" or function[1]=="south" or function[1]=="west" or function[1]=="east"):
        return True
    else:
        return False

def checkCanPutPick(function:list)->bool:
    #Lista de tamaño 4
    #canput/pick: n,x
    if len(function)!=4:
        return False
    elif function[0]==":" and (type(function[1]))=="int" and function[2]=="," and (function[3]=="balloons" or function[3]=="chips"):
        return True
    else:
        return False

def checkCanMoveJumpInDir (function:list)->bool:
    #Lista de tamaño 4
    #canmove/jumpindir: n,D
    if len(function)!=4:
        return False
    elif function[0]==":" and (type(function[1]))=="int" and function[2]=="," and  (function[3]=="north" and function[3]=="south"
        and function[3]=="west" and function[3]=="east"):
        return True
    else:
        return False

def checkCanMoveJumpTo (function:list)->bool:
    #Lista de tamaño 4
    #canMove/jumptothe: n,o
    if len(function)!=4:
        return False
    elif function[0]==":" and (type(function[1]))=="int" and function[2]=="," and (function[3]=="front" and function[3]=="right" and
        function[3]=="back" and function[3]=="left"):
        return True
    else:
        return False

def checkNot(function: list, command:list)->bool:
    #Lista de tamaño 2
    #not: cond
    if len(function):
        return False
    elif function[0]==":" and recognizeCommand(function[1], command):
        return True
    else:
        return False

#IDENTIFICAR USO DE CONDICIONALES

def recognizeConditional (cond:str, function: list)->bool:
    recognized=False
    if cond=="facing":
        recognized=checkFacing(function)
    elif cond=="canput" or cond=="canpick":
        recognized=checkCanPutPick(function)
    elif cond=="canmoveindir" or cond=="canjumpindir":
        recognized=checkCanMoveJumpInDir(function)
    elif cond=="canmovetothe" or cond=="canjumptothe":
        recognized=checkCanMoveJumpTo(function)
    return recognized

def recognizeNot (cond: str, function:list, command:list)->bool:
    if cond=="not":
        return checkNot(function,command)
    else:
        return False
#FUNCION LISTA VARIABLES
variables = []
procedures = []
parameters = []
def addVar (var: str)->list:
    global variables
    variables.append(var)

def addProc (var: str)->list:
    global procedures
    procedures.append(var)

def addParams (var: str)->list:
    global parameters
    parameters.append(var)

def searchItem(var:str)->bool:
    global variables
    for i in variables:
        if (variables[i]==var):
            return True
    return False

#parser

def pop(l:list):
    return(l.pop(0))

def parser(data:list)->bool:
    global variables

    result = False
    d = data
    # S0
    if pop(d) == 'robot_r': 
        print('Found robot_r')
    # BODY -> lambda
        if len(data) == 0: 
            result = True
            print('Cuerpo vacío: Fin')
    # BODY -> VARIABLES PROCEDURES BLOCK
        else: 
            print('Esperando: VARIABLES PROCEDURES BLOCK')
    # VARIABLES -> vars NAMES ;
            valid = checkVARS(d)
            if not valid: return result

    # PROCEDURES -> procs DEFINITIONS
            valid = checkPROCS(d)
            if not valid: return result


                


    else:
        result = False

    return result

def checkVARS(d)->bool:
    print('Esperando: vars NAMES ;')
    reserved = terminales.copy()
    reserved.remove(';')
    reserved.remove(',')
    valid = True
    if pop(d) == 'vars':
        print('Token VARS encontrado')
    # NAMES -> NAME
    # NAMES -> NAME , NAMES
        expectsComma = False
        expectsWord = False
        word = pop(d)
        while word != ';':
    # NAME -> [a-z]\w*   
            validName = bool(re.match('(^[a-z])\w*',word))
            if not expectsComma:
                if  validName and not (word in reserved):
                    print(f'Found word: {word}')
                    addVar(word)
                    expectsComma = True
                    expectsWord = False
                elif word in reserved :
                    print(f'{word} es una palabra reservada')
                    valid = False
                    break
                elif word == ',':
                    print('Esperaba nombre, recibí ","')
                    valid = False
                    break
                elif not validName:
                    print('Nombre inválido')
                    valid = False
                    break

            elif expectsComma:
                if word == ',':
                    expectsComma = False
                    expectsWord = True
                else: 
                    print(f'Esperaba coma, recibí {word}')
                    valid = False
                    break
            word = pop(d)
            if expectsWord and word == ';':
                print(f'Esperaba nombre, recibí ";"')
                valid = False
                break
    return valid

def checkPROCS(d)->bool:
    reserved = terminales.copy()
    reserved.remove('|')
    reserved.remove(',')
    valid = False
    print('Esperando: procs DEFINITIONS')
    procs = pop(d)
    if procs == 'procs': 
        print("Token PROCS encontrado")
    # DEFINITIONS -> DEF DEFINITIONS
    # DEFINITIONS -> DEF
    # DEF -> NAME [ PARAMS INSTRUCTIONS ]
        continues = True
        expects = 'name'
        openBlock = False
        while continues:
            word = pop(d)
            validName = bool(re.match('^[a-z]\w*',word))
            if expects == 'name' and validName: 
                print(f'Nombre de procedimiento: {word}')
                addProc(word)
                expects = 'open'
            elif expects == 'open' and word == '[':
                openBlock == True
                expects = 'parameters'
    # PARAMS -> |NAMES|
            elif expects == 'parameters' and word == '|':
            # NAMES -> NAME
            # NAMES -> NAME , NAMES
                expectsComma = False
                expectsWord = False
                word = pop(d)
            # NAME -> [a-z]\w*   
                if word == '|':
                    print('Parameters: |λ|')
                while word != '|':
                    validName = bool(re.match('(^[a-z])\w*',word))
                    if not expectsComma:
                        if  validName and not (word in reserved):
                            print(f'Found parameter: {word}')
                            addParams(word)
                            expectsComma = True
                            expectsWord = False
                        elif word in reserved :
                            print(f'{word} es una palabra reservada')
                            continues = False
                            valid = False
                            break
                        elif word == ',':
                            print('Esperaba nombre, recibí ","')
                            continues = False
                            valid = False
                            break
                        elif not validName:
                            print('Nombre inválido')
                            valid = False
                            continues = False
                            break

                    elif expectsComma:
                        if word == ',':
                            expectsComma = False
                            expectsWord = True
                        else: 
                            print(f'Esperaba coma, recibí {word}')
                            valid = False
                            continues = False
                            break
                    word = pop(d)
                    if expectsWord and word == '|':
                        print(f'Esperaba nombre, recibí "|"')
                        valid = False
                        continues = False
                        break
                
                if continues:
                    expects = 'instructions'
            #INSTRUCTIONS -> INSTRUCTION ; INSTRUCTIONS
            #INSTRUCTIONS -> INSTRUCTION
            #INSTRUCTION -> COMMAND
            #INSTRUCTION -> CONTROL
            #INSTRUCTION -> CALL
            elif expects == 'instructions':
                print(word)
                print('Esperando INSTRUCTIONS')
                expectsSemiColon = False
                expectsInstruction = False
                while word != ']':
                    if not expectsSemiColon:
                        if recognizeCommand(word, d): 
                            expectsSemiColon = True
                            expectsInstruction = False
                        elif word == ';':
                            print('Esperaba nombre, recibí ";"')
                            valid = False
                            break
                        else: 
                            valid = False
                            continues = False
                            break
                    elif expectsSemiColon:
                        if word == ';':
                            expectsSemiColon = False
                            expectsInstruction = True
                        pass
                    word = pop(d)
                    if expectsInstruction and word == ';':
                        print(f'Esperaba instrucción, recibí ";"')
                        valid = False
                        break
                if word == ']':
                    print('INSTRUCTIONS : λ')

            else:
                continues = False
                break
    else: 
        print(f'Esperaba PROCS, encontré: {procs}')
    return valid

#Main

def main():
    loadLang('alphabet.txt')
    data = openCode('code.txt')
    print(parser(data))

#TODO cambiar tipos de dato str -> int

main()
