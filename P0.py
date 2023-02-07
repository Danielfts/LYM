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

def openCode(file):
    data = ''
    f = open(file,'r')
    for i in f:
        i = re.sub(',',' , ',i)
        i = re.sub('\n'," ",string=i) 
        i = i.lower()
        data += i
    data = data.split()
    print(tuple(data))
    f.close()
    return data

#Tokenizer

def tokenizer(data:list)->bool:
    result = False
    if data[0] == 'robot_r':

        pass
    else:
        result = False
    return result

#FUNCION LISTA VARIABLES

variables=[]


def addItem (var: str)->list:
    variables.append(var)

def searchItem(var:str)->bool:
    for i in variables:
        if (variables[i]=="var"):
            return True
    return False

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

def recognizeNot (cond: str, function:list, command,list)->bool:
    if cond=="not":
        return checkNot(function,command)
    else:
        return False

#Main

def main():
    loadLang('lang.txt')
    openCode('code.txt')

#TODO cambiar tipos de dato str -> int
#TODO identificar bloques de codigo con []

main()
