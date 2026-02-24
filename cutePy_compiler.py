#Andreas Voutsinas  3153 cse53153
#Dimitrios Stalikas 3079 cse53079
import sys

symbols = [' ', 'A', '0', '_', '"','+', '-', '*', '/', '<', '>', '!', '=', ';', ',', ':', '[', ']', '(', ')', '#', '{', '}', '$', '']

intermediateStates = [i for i in range(20)]
giveBackStates = ["idtk", "constanttk", "lttk", "gttk", "assignmenttk", "declaretk"]
cutePyWords = ["def", "int", "input", "print", "return", "if", "else", "while", "or", "and", "not"]
startSimpleStatements = ["idtk", "printtk", "returntk"]
startStructuredStatements = ["iftk", "whiletk"]
startFactor = ["constanttk", "lptk", "idtk"]
addOp = ["plustk", "minustk"]
mulOp = ["multiplytk", "dividetk"]
relOp = ["letk", "lttk", "getk", "gttk", "netk", "eqtk"]

Trans_Diag = [
    [0, 1, 2, 3, 6, 'plustk', 'minustk', 'multiplytk', 9, 10, 11, 12, 13, 'semicolontk', 'commatk', 'colontk', 'lsptk', 'rsptk', 'lptk', 'rptk', 14, 'error_unexpected_0tk', 'error_unexpected_0tk', 'error_unexpected_0tk', 'eoftk'],
    ['idtk', 1, 1, 1, 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk', 'idtk'],
    
    ['constanttk', 'constanttk', 2, 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk', 'constanttk'],
    
    ['error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 4, 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk'],
    
    ['error_expected_usnderscore_lettertk', 4, 'error_expected_usnderscore_lettertk', 5, 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk'],
    
    ['error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'nametk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk'],
    
    ['error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 18, 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk'],
    
    ['error_expected_usnderscore_lettertk', 7, 'error_expected_usnderscore_lettertk', 8, 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk', 'error_expected_usnderscore_lettertk'],
    
    ['error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 19, 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk'],
    
    ['error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk', 'error_expected_dividetk'],
    
    ['lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'letk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk', 'lttk'],
    
    ['gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'getk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk', 'gttk'],
    
    ['error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'netk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk', 'error_expected_eqtk'],
    
    ['assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'eqtk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk', 'assignmenttk'],
    
    ['error_unexpected_after_hashtagtk', 17, 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk','error_unexpected_after_hashtagtk', 'error_unexpected_after_hashtagtk',  'error_unexpected_after_hashtagtk', 'begintk', 'endtk', 15, 'error_unexpected_after_hashtagtk'],
    
    [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,15, 15,  16, 15, 15, 15, 'error_comments_tk'],
    
    [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,15, 15,  16, 15, 15, 0, 'error_comments_tk'],
    
    ['declaretk', 17, 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk','declaretk', 'declaretk',  'declaretk', 'declaretk', 'declaretk', 'declaretk', 'declaretk'],
    
    ['error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 7, 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk'],
    
    
        ['error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'maintk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk', 'error_expected_usnderscoretk']
    
    ]

intCode = []
temporaryVariables = []

symbolTable = [[0, "main", []]]
isParameter = False

hasReturn = False

if len(sys.argv) < 2:
    print("Infile name is needed")
    exit(0)

infile = open(sys.argv[1], "r")
name = sys.argv[1][:len(sys.argv[1]) - 3]
name = name + "int"
outfile = open(name, "w")
name = sys.argv[1][:len(sys.argv[1]) - 3]
name = name + "symb"
outfile2 = open(name, "w")

name = sys.argv[1][:len(sys.argv[1]) - 3]
name = name + "asm"
outfile3 = open(name, "w")

startFinal = 0

line = 1

state = ""
word = ""


def error(message):
    print("Line %d: %s"%(line, message))
    exit(0)
def lex():
    global line
    state = 0
    word = ""
    isCharLine = False
    while state in intermediateStates:
        ch = infile.read(1)
        
        word = word + ch
        isCharLine = False
        if ch == ' ' or ch == '\t' or ch == '\n':
            if ch == '\n':
                line = line + 1
                isCharLine = True
            ch = ' '
        elif ch >= 'a' and ch <= 'z':
            ch = 'A'
        elif ch >= 'A' and ch <= 'Z':
            ch = 'A'
        elif ch >= '0' and ch <= '9':
            ch = '0'
        
        if ch not in symbols:
            error("character " + ch + " is not in CutePy alphabet")
        col = symbols.index(ch)
        
        state = Trans_Diag[state][col]
        
        if state == 0:
            word = ""
        
    if state in giveBackStates:
        infile.seek(infile.tell() - 1, 0)
        word = word[:-1]
        if isCharLine == True:
            line = line - 1
    
    if state == "error_unexpected_0tk":
        error("character " + ch + " is expected after #")
    if state == "error_expected_usnderscoretk":
        error("character _ is expected")
    if state == "error_expected_usnderscore_lettertk":
        error("character _ is expected after letters")    
    if state == "error_expected_dividetk":
        error("character / is expected after character /")
    if state == "error_expected_eqtk":
        error("character = is expected after character !")    
    if state == "error_unexpected_after_hashtagtk":
        error("character " + ch + " is unexpected after #")  
    if state == "error_comments_tk":
        error("eof in not expected before closing comments")    
    
    if state == "idtk" and len(word) > 30:
        error("the length of word " + word + " is not supported")
    if state == "constanttk" and int(word) > 2**32 - 1:
        error("constant " + word + "is out of bounds")
        
    if state == "maintk" and word != "\"__main__\"":
        error("token " + word + " is not supported")
    if state == "nametk" and word != "__name__":
        error("token " + word + " is not supported")
    if state == "declaretk" and word != "#declare":
        error("token " + word + " is not supported")
    
    if state == "idtk":
        if word in cutePyWords:
            state = word + "tk"

    return state, word

def start_rule():
    global state, word
    
    state, word = lex()
    def_main_part()
    call_main_part()
    

def def_main_part():
    global state, word
    
    if state != "deftk":
        error("keyword def was expected")
    while state == "deftk":
        state, word = lex()
        def_main_function()
        
    return

def def_main_function():
    global state, word, hasReturn
    
    if state != "idtk":
        error("main function name was expected")
    
    name = word
    
    if name.startswith("main_") == False:
        error("main function name must start with 'main_'")
        
    insertEntityToTable(name, "main_function")
    insertScopeToTable(name)
    state, word = lex()
    if state != "lptk":
        error("( was expected")
    
    state, word = lex()
    if state != 'rptk':
        error(") was expected")
    
    state, word = lex()
    if state != "colontk":
        error(": was expected")
    
    state, word = lex()
    if state != "begintk":
        error("#{ was expected")
        
    state, word = lex()
    declarations()
    while state == "deftk":
        state, word = lex()
        def_function()
    
    hasReturn = False
    lastEntityPos = len(symbolTable[len(symbolTable)-2][2]) - 1
    symbolTable[len(symbolTable)-2][2][lastEntityPos][1] = nextquad()    
    genquad("begin block", name, "_", "_")
    statements()
    genquad("end block", name, "_", "_")   
    lastEntityPos = len(symbolTable[len(symbolTable)-2][2]) - 1
    symbolTable[len(symbolTable)-2][2][lastEntityPos][2] = symbolTable[len(symbolTable)-1][3]
    
    if hasReturn == True:
        error("main function can't have return")
    deleteScopeFromTable()
    
    if state != "endtk":
        error("#} was expected")
    
    state, word = lex()

def def_function():
    global state, word, isParameter, hasReturn
    
    if state != "idtk":
        error("main function name was expected")
    
    name = word
    insertEntityToTable(name, "function")
    insertScopeToTable(name)
    
    state, word = lex()
    if state != "lptk":
        error("( was expected")
    state, word = lex()
    isParameter = True
    id_list()
    if state != 'rptk':
        error(") was expected")
    
    state, word = lex()
    if state != "colontk":
        error(": was expected")
    
    state, word = lex()
    if state != "begintk":
        error("#{ was expected")
        
    state, word = lex()
    declarations()
    while state == "deftk":
        state, word = lex()
        def_function()

    hasReturn = False

    lastEntityPos = len(symbolTable[len(symbolTable)-2][2]) - 1
    symbolTable[len(symbolTable)-2][2][lastEntityPos][1] = nextquad()
    genquad("begin block", name, "_", "_")
    statements()
    genquad("end block", name, "_", "_")   
    lastEntityPos = len(symbolTable[len(symbolTable)-2][2]) - 1
    symbolTable[len(symbolTable)-2][2][lastEntityPos][2] = symbolTable[len(symbolTable)-1][3] 

    if hasReturn == False:
        error("local function must have return")
    deleteScopeFromTable()

    
    if state != "endtk":
        error("#} was expected")
    
    state, word = lex()

def declarations():
    global state, word
    
    while state == "declaretk":
        state, word = lex()
        declaration_line()

def declaration_line():
    global state, word, isParameter
    
    isParameter = False
    id_list()
    
def id_list():
    global state, word, isParameter
    
    if isParameter == True:
        type = "parameter"
    else:
        type = "variable"
    
    if state == "idtk":
        insertEntityToTable(word, type)
        state, word = lex()
        
        while state == "commatk":
            state, word = lex()
            if state != "idtk":
                error("declared variable or parameter name was expected")
            
            insertEntityToTable(word, type)
            state, word = lex()
    

def statements():
    global state, word
    
    if state not in startSimpleStatements and state not in startStructuredStatements:
        error("start of statement was expected")
    
    while state in startSimpleStatements or state in startStructuredStatements:
        statement()
        
def statement():
    global state, word
    
    if state in startSimpleStatements:
        simple_statement()
    else:
        structured_statement()
        
def simple_statement():
    global state, word
    
    if state == "idtk":
        w = word
        state, word = lex()
        assignment_stat(w)
    elif state == "printtk":
        state, word = lex()
        print_stat()
    else:
        state, word = lex()
        return_stat()
    
def structured_statement():
    global state, word
    
    if state == "iftk":
        state, word = lex()
        if_stat()
    else:
        state, word = lex()
        while_stat()    

def assignment_stat(variable):
    global state, word
    
    searchEntityInTable(variable, "variable_parameter")
    if state != "assignmenttk":
        error("= was expected")
        
    state, word = lex()
    if state not in startFactor and state != "inttk":
        error("int, integer, ( or name was expected")
    
    if state in startFactor:
        place = expression()
        genquad("=", place, "_", variable)
        if state != "semicolontk":
            error("; was expected")
        state, word = lex()
    else:
        
        state, word = lex()
        if state != "lptk":
            error("( was expected")
        state, word = lex()
        
        if state != "inputtk":
            error("keyword input was expected")
        state, word = lex()
        
        if state != "lptk":
            error("( was expected")
        state, word = lex()
        
        if state != "rptk":
            error(") was expected")
        state, word = lex()
        
        if state != "rptk":
            error(") was expected")
        state, word = lex()

        if state != "semicolontk":
            error("; was expected")
        genquad("inp", variable, "_", "_")
        state, word = lex()

def print_stat():
    global state, word
    
    if state != "lptk":
        error("( was expected")
        
    state, word = lex()
    place = expression()
    genquad("out", place, "_", "_")
    if state != "rptk":
        error(") was expected")
        
    state, word = lex()    
    if state != "semicolontk":
        error("; was expected")
    state, word = lex()



def return_stat():
    global state, word, hasReturn
    
    hasReturn = True
    if state != "lptk":
        error("( was expected")
        
    state, word = lex()
    place = expression()
    genquad("retv", place, "_", "_")
    if state != "rptk":
        error(") was expected")
        
    state, word = lex()    
    if state != "semicolontk":
        error("; was expected")
    state, word = lex()


def if_stat():
    global state, word
    
    if state != "lptk":
        error("( was expected")
        
    state, word = lex()
    true, false = condition()
    if state != "rptk":
        error(") was expected")
        
    state, word = lex()    
    if state != "colontk":
        error(": was expected")
    state, word = lex()
    
    if state not in startSimpleStatements and state not in startStructuredStatements and state != "begintk":
        error("statement or #{ was expected")
    
    backpatch(true, nextquad())
    if state in startSimpleStatements or state in startStructuredStatements:
        statement()
    else:
        state, word = lex()
        statements()
        
        if state != "endtk":
            error("#} was expected")
        state, word = lex() 

#else

    if state != "elsetk":
        return
    jump = makelist(nextquad())
    genquad("jump", "_", "_", "_")
    
    state, word = lex()
    
    if state != "colontk":
        error(": was expected")
    state, word = lex()
    
    if state not in startSimpleStatements and state not in startStructuredStatements and state != "begintk":
        error("statement or #{ was expected")
    
    backpatch(false, nextquad())
    if state in startSimpleStatements or state in startStructuredStatements:
        statement()
    else:
       state, word = lex()
       statements()
       
       if state != "endtk":
           error("#} was expected")
       state, word = lex() 
    backpatch(jump, nextquad())

def while_stat():
    global state, word
    
    label = nextquad()
    
    if state != "lptk":
        error("( was expected")
        
    state, word = lex()
    true, false = condition()
    if state != "rptk":
        error(") was expected")
        
    state, word = lex()    
    if state != "colontk":
        error(": was expected")
    state, word = lex()
    
    backpatch(true, nextquad())
    if state not in startSimpleStatements and state not in startStructuredStatements and state != "begintk":
        error("statement or #{ was expected")
    
    if state in startSimpleStatements or state in startStructuredStatements:
        statement()
    else:
       state, word = lex()
       statements()
       
       if state != "endtk":
           error("#} was expected")
       state, word = lex() 
    genquad("jump", "_", "_", label)
    backpatch(false, nextquad())
def expression():
    global state, word
    
    optional_sign()
    t1 = term()
    
    while state in addOp:
        s = state
        state, word = lex()
        t2 = term()

        w = newtemp()
        if s == "plustk":
            genquad("+", t1, t2, w)
        else:
            genquad("-", t1, t2, w)
        t1 = w
        
    return t1
def term():
    global state, word
    
    f1 = factor()
    
    while state in mulOp:
        s = state
        state, word = lex()
        f2 = factor()
        
        w = newtemp()
        if s == "multiplytk":
            genquad("*", f1, f2, w)
        else:
            genquad("/", f1, f2, w)
        f1 = w
        
    return f1

def factor():
    global state, word
    
    if state not in startFactor:
        error("integer, ( or name was expected")   
        
    if state == "constanttk":        
        place = word
        state, word = lex()
    elif state == "lptk":
        state, word = lex()
        place = expression()
        if state != "rptk":
            error(") was expected")
        state, word = lex()
    else:        
        place = word
        state, word = lex()
        res = idtail()
        if res == True:
            w = newtemp()
            genquad("par", w, "RET", "_")
            genquad("call", place, "_", "_")
            searchEntityInTable(place, "function")
            place = w
        else:
            searchEntityInTable(place, "variable_parameter")
    
    return place
        
def idtail():
    global state, word
    
    if state == "lptk":
        state, word = lex()
        actual_par_list()
        
        if state != "rptk":
            error(") was expected")
        state, word = lex() 
        return True
    return False

def actual_par_list():
    global state, word
    
    if state in startFactor:
        place = expression()
        genquad("par", place, "CV", "_")
        while state == "commatk":
            state, word = lex()    
            place = expression()
            genquad("par", place, "CV", "_")
    
    
def optional_sign():
    global state, word
    
    if state in addOp:
        state, word = lex()
    
def condition():
    global state, word
    
    t1, f1 = bool_term()
    
    while state == "ortk":
        state, word = lex()
        
        backpatch(f1, nextquad())
        
        t2, f2 = bool_term()
        
        t1 = merge(t1, t2)
        f1 = f2
        
    return t1, f1


def bool_term():
    global state, word
    
    t1, f1 = bool_factor()
    
    while state == "andtk":
        state, word = lex()
        
        backpatch(t1, nextquad())
        
        t2, f2 = bool_factor()
        t1 = t2
        f1 = merge(f1, f2)
        
    return t1, f1

def bool_factor():
    global state, word
        
    if state == "nottk":
        state, word = lex()
        if state != "lsptk":
            error("[ was expected")
        
        state, word = lex()
        true, false = condition()
        true, false = false, true
        if state != "rsptk":
            error("] was expected")
        state, word = lex()
    elif state == "lsptk":
        state, word = lex()
        true, false = condition()
        if state != "rsptk":
            error("] was expected")
        state, word = lex()
    else:
        e1 = expression()
        if state not in relOp:
            error("relational operator was expected")
        s = state
        state, word = lex()
        e2 = expression()
        
        true = makelist(nextquad())
        if s == 'gttk':
            genquad(">", e1, e2, "_")
        elif s == 'getk':
            genquad(">=", e1, e2, "_")
        elif s == 'lttk':
            genquad("<", e1, e2, "_")
        elif s == 'letk':
            genquad("<=", e1, e2, "_")
        elif s == 'eqtk':
            genquad("==", e1, e2, "_")
        elif s == 'netk':
            genquad("!=", e1, e2, "_")
            
        false = makelist(nextquad())
        genquad("jump", "_", "_", "_")
    
    return true, false
def call_main_part():
    global state, word
    
    if state != "iftk":
        error("keyword if was expected")
    state, word = lex()
    
    if state != "nametk":
        error("keyword __name__ was expected")
    state, word = lex()
    
    if state != "eqtk":
        error("== was expected")
    state, word = lex() 
    
    if state != "maintk":
        error("keyword __main__ was expected")
    state, word = lex()
    
    if state != "colontk":
        error(": was expected")
    state, word = lex()
    
    if state != "idtk":
        error("main function name was expected")
    
    genquad("begin block", "main", "_", "_")
     
    while state == "idtk":
        
        genquad("call", word, "_", "_")
        searchEntityInTable(word, "main_function")
        state, word = lex()
        main_function_call()
    genquad("halt", "_", "_", "_")
    genquad("end block", "main", "_", "_")
    return

def main_function_call():
    global state, word
    
    if state != "lptk":
        error("( was expected")
        
    state, word = lex()

    if state != "rptk":
        error(") was expected")
        
    state, word = lex()    
    if state != "semicolontk":
        error("; was expected")
    state, word = lex()


def nextquad():
    global intCode
    
    return len(intCode)

def newtemp():
    global temporaryVariables
    
    t = len(temporaryVariables) + 1
    temp = "%" + str(t)
    insertEntityToTable(temp, "variable")
    temporaryVariables.append(temp)
    return temp

def genquad(op, x, y, z):
    global intCode
    
    quad = [nextquad(), op, x, y, z]
    
    intCode.append(quad)
    
def emptylist():
    return []

def makelist(x):
    return [x]

def merge(l1, l2):
    l1.extend(l2)
    return l1

def backpatch(l, z):
    global intCode
    
    for i in range(len(l)):
        intCode[l[i]][4] = z
        

def writeIntCode():
    global intCode
    
    for i in range(len(intCode)):
        quad = str(intCode[i])
        outfile.write(quad[1:len(quad) - 1])
        outfile.write("\n")
        
        
def insertScopeToTable(scopeName):
    global symbolTable
    
    scope = [len(symbolTable), scopeName, [], 12]
    
    symbolTable.append(scope)
    
def deleteScopeFromTable():
    global symbolTable
    global outfile3
    global startFinal
    
    outfile2.write("--------------------------------\n")
    for i in range(len(symbolTable) - 1, -1, -1):
        outfile2.write(str(symbolTable[i]))
        outfile2.write("\n")
        
    if startFinal == 0:
        outfile3.write(".data\n")
        outfile3.write("str_nl: .asciz \"\\n\"\n")
        outfile3.write(".text\n")
        outfile3.write("j Lmain\n")
    par = 0
    isMain = False 
    for i in range(startFinal, len(intCode)):
        outfile3.write("L%d:\n"%(intCode[i][0]))
        if intCode[i][1] == "jump":
            outfile3.write("j L%d\n"%(intCode[i][4]))
        elif intCode[i][1] == ">":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("bgt t1, t2, L%d\n"%(intCode[i][4]))
        elif intCode[i][1] == ">=":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("bge t1, t2, L%d\n"%(intCode[i][4]))
        elif intCode[i][1] == "<":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("blt t1, t2, L%d\n"%(intCode[i][4]))
        elif intCode[i][1] == "<=":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("ble t1, t2, L%d\n"%(intCode[i][4]))
        elif intCode[i][1] == "==":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("beq t1, t2, L%d\n"%(intCode[i][4]))
        elif intCode[i][1] == "!=":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("bne t1, t2, L%d\n"%(intCode[i][4]))
        elif intCode[i][1] == "=":
            loadvr(intCode[i][2], 1)
            storerv(1, intCode[i][4])
        elif intCode[i][1] == "+":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("add t1, t1, t2\n")
            storerv(1, intCode[i][4])
        elif intCode[i][1] == "-":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("sub t1, t1, t2\n")
            storerv(1, intCode[i][4])
        elif intCode[i][1] == "*":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("mul t1, t1, t2\n")
            storerv(1, intCode[i][4])
        elif intCode[i][1] == "/":
            loadvr(intCode[i][2], 1)
            loadvr(intCode[i][3], 2)
            outfile3.write("div t1, t1, t2\n")
            storerv(1, intCode[i][4])
        elif intCode[i][1] == "retv":
            loadvr(intCode[i][2], 1)
            outfile3.write("lw t0, -8(sp)\n")
            outfile3.write("sw t1, (t0)\n")
        elif intCode[i][1] == "par":
            if par == 0:
                for j in range(i+1, len(intCode)):
                    if intCode[j][1] == "call":
                        entity, entityNestingLevel = searchEntityInTable(intCode[j][2], "function")
                        outfile3.write("addi fp, sp, %d\n"%(entity[2]))
            if intCode[i][3] == "CV":
                x = -(12+4*par)
                loadvr(intCode[i][2], 0)
                outfile3.write("sw t0, %d(fp)\n"%(x))
            else:
               entity, entityNestingLevel = searchEntityInTable(intCode[i][2], "variable_parameter")
               outfile3.write("addi t0, sp, -%d\n"%(entity[1]))
               outfile3.write("sw t0, -8(fp)\n")
            par = par + 1
        elif intCode[i][1] == "call":
            par = 0
            if isMain == True:
                entity, entityNestingLevel = searchEntityInTable(intCode[i][2], "main_function")
            else:
                entity, entityNestingLevel = searchEntityInTable(intCode[i][2], "function")
            if entityNestingLevel == len(symbolTable) - 1:
                outfile3.write("sw sp, -4(fp)\n")
            else:
                outfile3.write("lw t0, -4(sp)\n")
                outfile3.write("sw t0, -4(fp)\n")
            outfile3.write("addi sp, sp, %d\n"%(entity[2]))
            outfile3.write("jal L%d\n"%(entity[1]))
            outfile3.write("addi sp, sp, -%d\n"%(entity[2]))
        elif intCode[i][1] == "begin block":
            if intCode[i][2] == "main":
                outfile3.write("Lmain:\n")
                isMain = True
            else:
                outfile3.write("sw ra, (sp)\n")
        elif intCode[i][1] == "end block":
            if intCode[i][2] == "main":
                outfile3.write("li a0, 0\n")
                outfile3.write("li a7, 93\n")
                outfile3.write("ecall\n")
            else:
                outfile3.write("lw ra, (sp)\n")
                outfile3.write("jr ra\n")        
        elif intCode[i][1] == "inp":
            outfile3.write("li a7, 5\n")
            outfile3.write("ecall\n")
            outfile3.write("mv t1, a0\n")
            storerv(1, intCode[i][2])
        elif intCode[i][1] == "out":
            loadvr(intCode[i][2], 1)
            outfile3.write("mv a0, t1\n")
            outfile3.write("li a7, 1\n")
            outfile3.write("ecall\n")
            outfile3.write("la a0, str_nl\n")
            outfile3.write("li a7, 4\n")
            outfile3.write("ecall\n")
        
    
    startFinal = len(intCode)
    
    
    
    
    
    
    
    
    
    symbolTable = symbolTable[:-1]

def insertEntityToTable(entityName, entityType):
    global symbolTable
    
    entities = symbolTable[len(symbolTable)-1][2]
    scopeName = symbolTable[len(symbolTable)-1][1]

    if entityName == scopeName:
        error(entityName + " is already defined in this scope")
            
    for i in range(len(entities)):
        if entityName == entities[i][0]:
            error(entityName + " is already defined in this scope")
            
    if entityType == "variable" or entityType == "parameter":
        entity = [entityName, symbolTable[len(symbolTable)-1][3]]
        if entityType == "parameter":
            entity.append("CV")
            lastEntityPos = len(symbolTable[len(symbolTable)-2][2]) - 1
            symbolTable[len(symbolTable)-2][2][lastEntityPos][3].append("CV")
        symbolTable[len(symbolTable)-1][2].append(entity)
        symbolTable[len(symbolTable)-1][3] = symbolTable[len(symbolTable)-1][3] + 4
    else:
        entity = [entityName, '', '', []]
        symbolTable[len(symbolTable)-1][2].append(entity)
        
        
def searchEntityInTable(entityName, entityType):
    global symbolTable
    #function, main_function, variable_parameter
    
    for i in range(len(symbolTable) - 1, -1, -1):
        entities = symbolTable[i][2]
        for j in range(len(entities)):
            if entityName == entities[j][0]:
                if entityType == "function" and len(entities[j]) == 4:
                    if entityName.startswith("main_"):
                        error("A main function can not be called at this point")
                    else:
                        return entities[j], symbolTable[i][0]
                elif  entityType == "function" and len(entities[j]) != 4:
                    error(entityName + " can not be called as function")
                elif entityType == "main_function" and len(entities[j]) == 4:
                    return entities[j], symbolTable[i][0]
                elif entityType == "variable_parameter" and len(entities[j]) == 4:
                    error(entityName + " is a function or main_function")
                elif entityType == "variable_parameter" and len(entities[j]) != 4:
                    return entities[j], symbolTable[i][0]
                
                    
                    
    
    error(entityName + " is not declared")
        
    
def gnlvcode(offset, N):
    global outfile3
    global symbolTable
    
    outfile3.write("lw t0, -4(sp)\n")
    
    for i in range(N):
        outfile3.write("lw t0, -4(t0)\n")
        
    outfile3.write("addi t0, t0, -%d\n"%(offset))

def loadvr(v, r):
    global symbolTable
    
    ch = v[0]
    if ch >= '0' and ch <= '9':
        outfile3.write("li t%d, %s\n"%(r, v))
    else:
        entity, entityNestingLevel = searchEntityInTable(v, "variable_parameter")
        offset = entity[1]
        
        if entityNestingLevel == len(symbolTable) - 1:
            outfile3.write("lw t%d, -%d(sp)\n"%(r, offset))
        else:
            N = len(symbolTable) -1 - entityNestingLevel - 1
            gnlvcode(offset, N)
            outfile3.write("lw t%d, (t0)\n"%(r))


def storerv(r, v):
    global symbolTable
    
    entity, entityNestingLevel = searchEntityInTable(v, "variable_parameter")
    offset = entity[1]
    
    if entityNestingLevel == len(symbolTable) - 1:
        outfile3.write("sw t%d, -%d(sp)\n"%(r, offset))
    else:
        N = len(symbolTable) -1 - entityNestingLevel - 1
        gnlvcode(offset, N)
        outfile3.write("sw t%d, (t0)\n"%(r))
        
start_rule()

writeIntCode()
deleteScopeFromTable()
