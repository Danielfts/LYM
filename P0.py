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

def checkAssignTo(function:list)-> bool:
    #assignTo: n,name
    
    if function[0]==":" and function[1].isdigit() and function[2]=="," and function[3] in variables:
        print(f'Assigned {function[1]} -> {function[3]}')
        del function[0:4]
        return True
    else:
        return False

def checkGoto (function: list)->bool:
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
    
    if function[0]==":" and (function[1].isdigit() or function[1] in variables or function[1] in parameters) and function[2]=="," and (function[3]=="balloons" or function[3]=="chips") :
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
    var=function[1].isdigit()
    if function[0]==":" and (function[1].isdigit() or function[1] in variables) and function[2]=="," and (function[3]=="south" or function[3]=="north" or function[3]=="east" or function[3]=="west") :
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

def recognizeCommand (function:list, command: str)->bool:
    print('Buscando COMMAND')
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
        recognized=checkMoveOrjumpIndir(function)
    elif command=="nop":
        print('Recognized command: nop')
        recognized=checkNop()
    return recognized

#FUNCIONES PARA VERIFICAR CONDICIONALES

def checkFacing(function: list)->bool:
    #Lista de tamaño 2
    #facing: O
    if function[0]==":" and (function[1]=="north" or function[1]=="south" or function[1]=="west" or function[1]=="east"):
        del function[0:2]
        return True
    else:
        return False

def checkCanPutPick(function:list)->bool:
    #Lista de tamaño 4
    #canput/pick: n,x
    if function[0]==":" and (function[1].isdigit() or function[1] in variables or function[1] in parameters) and function[2]=="," and (function[3]=="balloons" or function[3]=="chips"):
        del function[0:4]
        return True
    else:
        return False

def checkCanMoveJumpInDir (function:list)->bool:
    #Lista de tamaño 4
    #canmove/jumpindir: n,D
    if function[0]==":" and (function[1].isdigit() or function[1] in variables or function[1] in parameters) and function[2]=="," and  (function[3]=="north" or function[3]=="south" or function[3]=="west" or function[3]=="east"):
        del function[0:4]
        return True
    else:
        return False

def checkCanMoveJumpTo (function:list)->bool:
    #Lista de tamaño 4
    #canMove/jumptothe: n,o
    if function[0]==":" and (function[1].isdigit() or function[1] in variables or function[1] in parameters) and function[2]=="," and (function[3]=="front" or function[3]=="right" or
        function[3]=="back" or function[3]=="left"):
        del function[0:4]
        return True
    else:
        return False

def checkNot(function: list, command:list)->bool:
    #Lista de tamaño 2
    #not: cond
    if function[0]==":" and recognizeCommand(function[1], command):
        del function[0:2]
        return True
    else:
        return False

#IDENTIFICAR USO DE CONDICIONALES

def recognizeConditional (word:str, function: list)->bool:
    recognized=False
    if word=="facing":
        print('Recognized conditional: facing')
        recognized=checkFacing(function)
    elif word=="canput" or word=="canpick":
        print('Recognized conditional: canput | canpick')
        recognized=checkCanPutPick(function)
    elif word=="canmoveindir" or word=="canjumpindir":
        print('Recognized conditional: canmoveindir | canjumpindir')
        recognized=checkCanMoveJumpInDir(function)
    elif word=="canmovetothe" or word=="canjumptothe":
        print('Recognized conditional: canmovetothe | canjumptothe')
        recognized=checkCanMoveJumpTo(function)
    return recognized

def recognizeNot (cond: str, function:list, command:list)->bool:
    if cond=="not":
        print('Recognized conditional: not')
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
    valid = True
    print('Esperando: procs DEFINITIONS')
    procs = pop(d)
    if procs == 'procs': 
        print("Token PROCS encontrado")
    # DEFINITIONS -> DEF DEFINITIONS
    # DEFINITIONS -> DEF
    # DEF -> NAME [ PARAMS INSTRUCTIONS ]
        valid = recognizeDefinitions(d, reserved)
    else: 
        print(f'Esperaba PROCS, encontré: {procs}')
    return valid

def recognizeDefinitions(d, reserved):
    continues = True
    expects = 'name'
    openBlock = False
    while continues:
        word = pop(d) #Ojo con este pop(d)
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
            #INSTRUCTION -> COMMAND | control | call
        elif expects == 'instructions':
            valid = True
            print('Esperando INSTRUCTIONS')
            
            if word == ']':
                print('INSTRUCTIONS : λ')
            continues = recognizeBlock(d, word)

            if continues: 
                expects = 'name'


        else:
            continues = False
            break
    return valid

def recognizeBlock(d, word):
    print('Buscando BLOCK')
    expectsSemiColon = False
    expectsInstruction = False
    valid = True
    while word != ']':
        if not expectsSemiColon:
            if recognizeCommand(d, word) or recognizeLoop(d,word) or recognizeIf(d,word):
                expectsSemiColon = True
                expectsInstruction = False
            elif word == ';':
                print('Esperaba nombre, recibí ";"')
                valid = False
                break
            else: 
                valid = False
                break
        elif expectsSemiColon:
            if word == ';':
                expectsSemiColon = False
                expectsInstruction = True
                    
        word = pop(d)
        if expectsInstruction and word == ';':
            print(f'Esperaba instrucción, recibí ";"')
            valid = False
            break
    return valid

def recognizeLoop(d: list, word: str)->bool:
    print('Buscando LOOP')
    valid = True
    if word == 'while':
        word = pop(d)
        if word == ':':
            word = pop(d)
            if recognizeConditional(word,d):
                if d[0]=='do' and d[1] ==':':
                    word = pop(d)
                    word = pop(d)
                    word = pop(d)
                    if word == '[':
                        word=pop(d)
                        valid = recognizeBlock(d,word)
                
            else: 
                valid = False
        else:
            valid = False
    else: 
        valid = False
    return valid

def recognizeIf(d:list,word:str)->bool:
    print("Buscando IF")
    valid=True
    if word == 'if':
        word=pop(d)
        if word==":":
            word=pop(d)
            if recognizeConditional(word,d):
                valid= True
            else:
                valid=False
        else:
            valid=False
    else: 
        valid = False
    return valid


#Main

def main():
    loadLang('alphabet.txt')
    data = openCode('code.txt')
    print(parser(data))

#TODO cambiar tipos de dato str -> int

main()
