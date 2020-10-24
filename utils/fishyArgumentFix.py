import re

def fishyArgumentFix(err, files, history):
    numOfLineToChange = err.getProblemLines()[0][1]
    fileToChange = err.getProblemLines()[0][0]
    addition=''
    print(numOfLineToChange)
    print(fileToChange)

    f = open(fileToChange, "r")
    data = f.readlines()
    f.close()

    lineToChange = data[numOfLineToChange-1]
    err.setChangedLine(numOfLineToChange)
    err.setChangedFile(fileToChange)

    if err.getErrorType().find('malloc')>=0:
        addition = lineToChange[0:lineToChange.find('(')+1]
        addition += 'abs('
        addition += lineToChange[lineToChange.find('(')+1:lineToChange.rfind(')')]
        addition += ')'
        addition += lineToChange[lineToChange.rfind(')'):]
    elif err.getErrorType().find('realloc')>=0:
        addition = lineToChange[0:lineToChange.find(',')+1]
        addition += 'abs('
        addition += lineToChange[lineToChange.find(',')+1:lineToChange.rfind(')')]
        addition += ')'
        addition += lineToChange[lineToChange.rfind(')'):]

    if addition and (addition, err.getChangedLine(), err.getChangedFile()) not in history:
        history.append((addition, err.getChangedLine(), err.getChangedFile()))		
        # set what should be changed
        err.setBug(lineToChange)
        err.setBugFix(addition)