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
    #Lista de tamaño 4
    #assignTo: n,name
    if len(function)!=4:
        return False
    else:
        if function[0]==":" and type(function[1])=="int" and type(function[3])=="str" and  function[2]==",":
            return True
        elif function[0]==":" and type(function[3])=="str" and searchItem(function[1]) and function[2]==",":
            return True
        else:
            return False

def checkGoto (function: list)->bool:
    #Lista de tamaño 4
    # goto: x,y
    if len(function)!=4:
        return False
    else:
        #revisar variables----
        if function[0]==":" and type(function[1])=="int" and type(function[3])=="int" and function[2]==",":
            return True
        elif function[0]==":" and searchItem(function[1]) and type(function[3])=="int" and function[2]==",":
            return True
        else:
            return False

def checkMove (function: list)-> bool:
    #Lista de tamaño 2
    # move :n
    if len(function)!=2:
        return False
    else:
        if function [0]==":" and type(function[1])=="int":
            return True
        elif function[0]==":" and searchItem(function[1]):
            return True
        else: 
            return False

def checkTurn (function:list)-> bool:
    #Lista de tamaño 2
    #turn: d
    if len(function)!=2:
        return False
    else:
        if function[0]==":" and (function[1]=="left" or function[1]=="right" or function[1]=="around"):
            return True
        else:
            return False

def checkFace (function: list)-> bool:
    #Lista de tamaño 2
    #face: o
    if len(function)!=2:
        return False
    else:
        if function[0]==":" and (function[1]=="south" or function[1]=="east" or function[1]=="west" or function[1]=="north"):
            return True
        else:
            return False

def checkPutOrPick (function: list)-> bool:
    #Lista de tamaño 4
    #put/pick: n,x
    if len(function)!=4:
        return False
    else:
        if function[0]==":" and type(function[1])=="int" and (function[3]=="balloons" or function[3]=="chips") and function[2]==",":
            return True
        elif function[0]==":" and searchItem(function[1]) and (function[3]=="balloons" or function[3]=="chips") and function[2]==",":
            return True
        else:
            return False

def checkMoveToOrJumpTo (function: list) -> bool:
    #Lista de tamaño 4
    #movetothe/jumptothe; n,d
    if len(function)!=4:
        return False
    else:
        if function[0]==":" and type(function[1])=="int" and ((function[3]=="front")
            or function[3]=="back" or function[3]=="right" or function[3]=="left") and function[2]==",":
            return True
        elif function[0]==":"  and searchItem(function[1]) and ((function[3]=="front")
            or function[3]=="back" or function[3]=="right" or function[3]=="left") and  function[2]==",":
            return True
        else:
            return False

def checkMoveOrjumpIndir (function: list)->bool:
    #Lista de tamaño 4
    #jumpIndir: n,D
    if len(function)!=4:
        return False
    else:
        if function[0]==":" and type(function[1])=="int" and (function[3]=="south" or function[3]=="north" or
            function[3]=="east" or function[3]=="west") and function[2]==",":
            return True
        elif function[0]==":" and searchItem(function[1]) and (function[2]=="south" or function[2]=="north" or
            function[2]=="east" or function[2]=="west") and function[2]==",":
            return True
        else:
            return False

def chechNop (function: list)-> bool:
    #Lista de tamaño 1
    #nop:
    if len(function)!=1:
        return False
    else:
        if function[0]==":":
            return True
        else:
            return False

#FUNCIONES PARA IDENTIFICAR USO DE COMANDO

def recognizeCommand (command: str, function:list)->bool:
    recognized=False
    if command=="asignto":
        recognized=checkAssignTo(function)
    elif command=="goto":
        recognized=checkGoto(function)
    elif command=="move":
        recognized=checkMove(function)
    elif command=="turn":
        recognized=checkTurn(function)
    elif command=="face":
        recognized=checkFace(function)
    elif command=="put" or command=="pick":
        recognized=checkPutOrPick(function)
    elif command=="movetothe" or command=="jumptothe":
        recognized=checkMoveToOrJumpTo(function)
    elif command=="moveindir" or command=="jumpindir":
        recognized=checkMoveOrjumpIndir
    elif command=="nop":
        recognized=chechNop
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
variables=[]

def addVar (var: str)->list:
    global variables
    variables.append(var)

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
            #valid = checkPROCS(d)
            if not valid: return result


                


    else:
        result = False

    return result

def checkVARS(d)->bool:
    print('Esperando: vars NAMES ;')
    reserved = terminales
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
    return valid

def checkPROCS(d)->bool:
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
        while continues:
            word = pop(d)
            validName = bool(re.match('^[a-z]\w*',word))
            if expects == 'name' and validName: 
                pass 
            pass
    else: 
        print(f'Esperaba PROCS, encontré: {procs}')
    return valid

#Main

def main():
    loadLang('alphabet.txt')
    data = openCode('code.txt')
    print(parser(data))

#TODO cambiar tipos de dato str -> int
#TODO identificar bloques de codigo con []
#TODO fix toeknizer, separate commas, colons and semicolons

main()
