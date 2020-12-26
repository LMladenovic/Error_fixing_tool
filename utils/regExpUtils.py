# used to match begin of the block of code
def isBeginOfCodeBlock():
    return '([ \t]*)(([a-zA-Z_-]+))[ ]+.*{'

# used to match definition of simple pointer
def isSimplePointerDefinition():
    return '([ \t]*)([a-zA-Z_-]+)([ ]*[\*][ ]*)+([a-zA-Z_-]+)[^;]*;'

    ## 110. linija uninitialisedFix
     #      '([ \t]*)([a-zA-Z_-]+)[ ]*[\*]+[ ]*([a-zA-z_0-9]+)[ ]*;'

# used to match line containing definition of variable
def isVariableDefinitionLine():
    return '([ \t]*)([a-zA-Z_-]+)[ ]+([a-zA-Z_-]+)[^;]*;'

# used to match data from line containing definition of multidimensional variable
def getMultidimensionalVariableDefinitionData():
    return '([ \t]*)([a-zA-Z_-]+)[ ]+([a-zA-Z0-9_-]+)\[(.+)\][^;]*;'

# used to match data from line containing definition of one dimensional variable
def getOneDimensionalVariableDefinitionData():
    return '([ \t]*)([a-zA-Z_-]+)[ ]+(.+)[^;]*;'

# used to match line containing dinamic alocation function
def lineContainingDinamicAlocationFunction():
    return '.+(malloc|calloc|realloc)(.+)'

# used to match line containing definition of variable with dinamic alocation function used
def simpleLineWithDinamicMemoryAlocationDefinition():
    return '(malloc|calloc|realloc)(.+)[^;]*;'

# used to match argument sizeof(varType) in line
def sizeArgumentForDinamicMemoryAlocationFunctions():
    return 'sizeof[ ]*\([ ]*([a-zA-Z\* _-]+)[ ]*\)'
         
          # ranije fukncija
          # 'sizeof[ ]*\([ ]*([a-zA-Z_-]+)[ ]*\)'
        # invalidRead 47 linija
       #     'sizeof[ ]*\(([a-zA-z0-9\* ]*)\)'
          

# used to match line containing definition of variable with dinamic alocation function used, inside condition block
def complexLineWithDinamicMemoryAlocationDefinition():
    return '([ \t]*).*\([ ]*(.*)[ ]*=[ ]*(malloc|calloc|realloc)[ ]*\((.*)NULL'
    
# used to get information about needed memory expansion
def getInformationAboutExpansion():    
    return 'Address [0-9a-zA-Z]+ is \d+ bytes after a block of size \d+ alloc\'d'

# used to get information about allocated memory
def getDataFromLineAboutMemoryAlocation():
    return '\(([a-zA-z0-9]*[ ]*\*[ ]*)*[ ]*sizeof[ ]*\(([a-zA-z0-9\* ]*)\)[ ]*(\*[ ]*[a-zA-z0-9]*)*([ ]*[\)\+])'

# used to match data related to allocated memory which will be changed with correct one
def changeMemoryAlocationSizeRelatedData():
	return '\(([a-zA-z0-9]*[ ]*\*[ ]*)*[ ]*sizeof[ ]*\(([a-zA-z0-9\* ]*)\)[ ]*(\*[ ]*[a-zA-z0-9]*)*[ ]*[\)\+]'

# used to get information about what have caused sys call error
def getInformationAboutDataCausedSysCallError():
    return '[ \t]*([a-zA-z_*]+)[ \t]+([a-zA-z0-9_]+)[ \t]+=[ \t]+(malloc|realoc)(.+)'

# used to match data from user defined structure with predefined name
def getUserDefinedStructureWithPredefinedName(varType):
    return 'typedef struct [a-zA-z0-9_-\{]+[ ]*([a-zA-z0-9\*\t \n;,_-]+)[ ]*[\}]+[ ]*' + varType.strip() + '[ ]*;'

# used to match data from user defined structure
def getUserDefinedStructure(varType):
    return 'typedef struct [ \t]*' + varType.strip() + '[\t {]+[ ]*([a-zA-z0-9\*\t \n;,_-]+)[ ]*[\}]+[ ]*;' 
