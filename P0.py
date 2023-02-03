""" 
Proyecto P0 de lenguajes y máquinas 
"""
import re

noTerminales = []
terminales = []
parseTree= {

}

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

def tokenizer(data:list)->bool:
    result = False
    if data[0] == 'robot_r':

        pass
    else:
        result = False
    return result

def main():
    loadLang('lang.txt')
    openCode('code.txt')

def checkAssignTo(function:list)-> bool:
    "Lista de tamaño 4"
    ": n, name"
    if len(function)!=4:
        return False
    else:
        if function[0]==":" and type(function[1]=="int") and type(function[2])=="str":
            return True
        else:
            return False

main()
