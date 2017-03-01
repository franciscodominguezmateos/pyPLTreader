'''
Created on 20/11/2013

@author: Francisco
'''
def getCommands(content):
    rl=[]
    for line in content:
        l=line.split(";")
        for c in l:
            ts=c.strip()
            if ts!="":
                rl.append(c.strip())
    return rl
def isCommand(s,c):
    d=s[0:2]
    if d==c:
        return True
    return False
def isPU(s):
    return isCommand(s,"PU")
def isPD(s):
    return isCommand(s,"PD")
def isIN(s):
    return isCommand(s,"IN")
def splitCommand(s):
    c=s[0:2]
    r=s[2:]
    if r!="":
        r.replace(" ",",")
        l=r.split(",")
        if len(l)==1:
            pass
        return (c,l[0],l[1])
    return (c)
def getTriplas(cmd):
    l=[]
    for c in cmd:
        if isPU(c) or isPD(c):
            t=splitCommand(c)
            l.append(t)
    return l
def getPLT(fname):
    #fname="C:\Users\paco\Desktop\mini3DprinterCaseMotoresZdentro13102701.dxf"
    #fname="C:\\Users\\paco\\Desktop\\a4x2laser.dxf"
    #fname="/home/francisco/workspace/pyhotdrawtets/src/pyHotDraw/Core/Qt/a4x2laser.plt"
    with open(fname) as f:
        content = f.readlines()
    p=getCommands(content)
    return getTriplas(p)
 