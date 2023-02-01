""" 
Proyecto P0 de lenguajes y máquinas 
"""
import re

noTerminales = ["vars", "procs"]
terminales = [",", ";", "|", "[","]", ":",
    "robot_r"
]

def openCode(file):
    data = ''
    f = open(file,'r')
    for i in f:
        #i = re.sub(' ',"",string=i) 
        i = i.lower()
        data += i
    print(data)

    return data

openCode('code.txt')
