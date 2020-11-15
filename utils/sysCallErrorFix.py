import re

def sysCallWriteFix(err,files,history):
    fileToChange = err.getProblemLines()[0][0]
    numOfLineToChange = err.getProblemLines()[0][1]
    err.setChangedFile(fileToChange)
    err.setChangedLine(numOfLineToChange)

    addition = ''
    f = open(fileToChange, "r")
    data = f.readlines()
    f.close()

    lineToChange = data[numOfLineToChange-1]
    addition = lineToChange[0:lineToChange.find('=')+1]

    m = re.search('[ \t]*([a-zA-z_*]+)[ \t]+([a-zA-z0-9_]+)[ \t]+=[ \t]+(malloc)(.+)', lineToChange)
    if m:
        varType = m.group(1)[0:m.group(1).find('*')]
        allocatedSize = m.group(4)[m.group(4).find('(')+1:m.group(4).rfind(')')]
        addition += ' calloc( sizeof(' + varType + '), ' + allocatedSize + ')' +  lineToChange[lineToChange.find(';'):]

    if addition and (addition, err.getChangedLine(), err.getChangedFile()) not in history:
        history.append((addition, err.getChangedLine(), err.getChangedFile()))		
        # set what should be changed
        err.setBug(lineToChange)
        err.setBugFix(addition)

def sysCallExitFix(err,files,history):
    fileToChange = err.getProblemLines()[-1][0]
    numOfLineToChange = err.getProblemLines()[-1][1]
    err.setChangedFile(fileToChange)
    err.setChangedLine(numOfLineToChange)

    addition = ''
    f = open(fileToChange, "r")
    data = f.readlines()
    f.close()

    lineToChange = data[numOfLineToChange-1]
    var = lineToChange[lineToChange.find('(')+1:lineToChange.rfind(')')]

    addition = lineToChange.replace(var, '0') 

    if addition and (addition, err.getChangedLine(), err.getChangedFile()) not in history:
        history.append((addition, err.getChangedLine(), err.getChangedFile()))		
        # set what should be changed
        err.setBug(lineToChange)
        err.setBugFix(addition)
