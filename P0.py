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

#FUNCIONES PARA IDENTIFICAR COMANDOS

def checkAssignTo(function:list)-> bool:
    #Lista de tamaño 4
    #assignTo: n,name
    if len(function)!=4:
        return False
    else:
        if function[0]==":" and type(function[1])=="int" and type(function[2])=="str":
            return True
        elif function[0]==":" and type(function[2])=="str" and searchItem(function[1]):
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
        if function[0]==":" and type(function[1])=="int" and type(function[2])=="int":
            return True
        elif function[0]==":" and searchItem(function[1]) and type(function[2])=="int":
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
        if function[0]==":" and type(function[1])=="int" and (function[2]=="balloons" or function[2]=="chips"):
            return True
        elif function[0]==":" and searchItem(function[1]) and (function[2]=="balloons" or function[2]=="chips"):
            return True
        else:
            return False

def checkMoveToOrJumpTo (function: list) -> bool:
    #Lista de tamaño 4
    #movetothe/jumptothe; n,d
    if len(function)!=4:
        return False
    else:
        if function[0]==":" and type(function[1])=="int" and ((function[2]=="front")
            or function[2]=="back" or function[2]=="right" or function[2]=="left"):
            return True
        elif function[0]==":"  and searchItem(function[1]) and ((function[2]=="front")
            or function[2]=="back" or function[2]=="right" or function[2]=="left"):
            return True
        else:
            return False

def checkMoveOrjumpIndir (function: list)->bool:
    #Lista de tamaño 4
    #jumpIndir: n,D
    if len(function)!=4:
        return False
    else:
        if function[0]==":" and type(function[1])=="int" and (function[2]=="south" or function[2]=="north" or
            function[2]=="east" or function[2]=="west"):
            return True
        elif function[0]==":" and searchItem(function[1]) and (function[2]=="south" or function[2]=="north" or
            function[2]=="east" or function[2]=="west"):
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


#Main

def main():
    loadLang('lang.txt')
    openCode('code.txt')

main()
