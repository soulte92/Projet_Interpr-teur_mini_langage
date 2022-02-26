# -----------------------------------------------------------------------------
# calc.py
#
# Expressions arithmétiques sans variables
# -----------------------------------------------------------------------------
from genereTreeGraphviz2 import printTreeGraph
import ply.yacc as yacc
import util_fonctions as uf

reserved = {
    'print' : 'PRINT',
    'if' : 'IF',
    'else': 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'functionVoid' : 'FUNCTIONVOID',
    'functionValue' : 'FUNCTIONVALUE',
    'functionValueImp':'FUNCTIONVALUEIMP',
    'return' : 'RETURN'
}
 
tokens = ['NUMBER','MINUS',
    'PLUS','TIMES','DIVIDE',
    'LPAREN','RPAREN', 'AND', 'OR',
    'TRUE','FALSE', 'SEMICOLON', 'NAME',
    'AFFECT', 'INF', 'SUP', 'EQUALS' , 'LACCOLADE', 'RACCOLADE',
    'VIRG', 'GUILLEMET']#, 'PLUSPLUS', 'MINUSMINUS', 'PLUSAFFECT', 'MINUSAFFECT' ]

tokens = tokens + list(reserved.values())

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE')
    )       


# Tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LACCOLADE   = r'\{'
t_RACCOLADE    = r'\}'
t_AND       = r'&'
t_OR        = r'\|'
t_FALSE     = r'F'
t_TRUE      = r'T'
t_SEMICOLON = r';'
t_AFFECT    = r'='
t_EQUALS    = r'=='
t_INF       = r'<'
t_SUP       = r'>'
t_VIRG       = r','
t_GUILLEMET = r'"'
# t_PLUSPLUS = r'\++'
# t_MINUSMINUS = r'--'
# t_PLUSAFFECT = r'\+='
# t_MINUSAFFECT = r'-='

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

names = {}
scope_func = {}

#Début d'exécution des règles
def p_start(p):
    'start : bloc'
    p[0] = ('START',p[1])
    print('Arbre de dérivation = ',p[1])
    # printTreeGraph(p[1])                                                                                                                                                                                                                                                                                               
    uf.eval_Inst(p[1], names, scope_func)

#Excution des bloc ( soit print, soit affect pour le moment)
def p_bloc(p):
    '''bloc : bloc statement SEMICOLON 
    | statement SEMICOLON'''
    if len(p) == 4:
        p[0] = ('bloc', p[1], p[2])
    else:
        p[0] = ('bloc', p[1], 'Empty')

#Affiche la valeur d'une expression
def p_print(p):
    '''statement : PRINT LPAREN multiExpr RPAREN'''
    p[0] = ('print', p[3])

#Fait un une affection d'une expression dans une variable
def p_affect(p):
    '''statement : NAME AFFECT expression'''
    p[0] = ('affect',p[1], p[3])

def p_condition_if(p):
    '''statement : IF LPAREN expression RPAREN LACCOLADE bloc RACCOLADE
    | IF LPAREN expression RPAREN LACCOLADE bloc RACCOLADE ELSE LACCOLADE bloc RACCOLADE'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if', p[3], p[6], 'else', p[10])   
     
def p_boucle_while(p):
    'statement : WHILE LPAREN expression RPAREN LACCOLADE bloc RACCOLADE'
    p[0] = ('while', p[3], p[6])    

def p_boucle_for(p):
    '''statement : FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LACCOLADE bloc RACCOLADE'''
    p[0] = ('for', p[3], p[5], p[7], p[10]) 

def p_mutiple_names(p):
    '''multiname : NAME VIRG multiname
    | NAME'''
    if len(p) == 4:
        p[0] = ('multiname', p[1], p[3])
    else:
        p[0] = ('multiname', p[1])

def p_multiExpr_names(p):
    '''multiExpr : expression VIRG multiExpr
    | expression'''
    if len(p) == 4:
        p[0] = ('multiExpr', p[1], p[3])
    else:
        p[0] = ('multiExpr', p[1])

def p_function_void(p):
    '''statement : FUNCTIONVOID NAME LPAREN RPAREN LACCOLADE bloc RACCOLADE
    | FUNCTIONVOID NAME LPAREN RPAREN LACCOLADE bloc RETURN SEMICOLON RACCOLADE
    | FUNCTIONVOID NAME LPAREN multiname RPAREN LACCOLADE bloc RACCOLADE
    | FUNCTIONVOID NAME LPAREN multiname RPAREN LACCOLADE bloc RETURN SEMICOLON RACCOLADE'''

    if len(p) == 10 or len(p) == 8 :
        p[0] = ('functionVoid', p[2], p[6])
    else:
        p[0] = ('functionVoid', p[2], p[4], p[7])

def p_function_value(p):
    '''statement : FUNCTIONVALUE NAME LPAREN RPAREN LACCOLADE func_instrs RACCOLADE
    | FUNCTIONVALUE NAME LPAREN multiname RPAREN LACCOLADE func_instrs RACCOLADE'''
     # Tuple format: ('functionValue', funcname, params, bloc, return)     
    #function value sans param
    if len(p) == 8 and p[1] == 'functionValue' :
        p[0] = ('functionValue', p[2], p[6][0], p[6][1])
            #function value avec param 
    elif len(p) == 9 and p[1] == 'functionValue':
        p[0] = ('functionValue', p[2], p[4], p[7][0], p[7][1]) 
            

def p_function_value_instruction(p):
    '''func_instrs : RETURN expression SEMICOLON
    | bloc RETURN expression SEMICOLON
    | RETURN expression SEMICOLON bloc
    | bloc RETURN expression SEMICOLON bloc'''

    # Tuple format: (bloc, return) 
    # return empty
    if len(p) == 4:
        p[0] = ('Empty',p[2])
    # bloc return empty
    elif len(p) == 5 and p[2] == 'return':
        p[0] = (p[1], p[3])  
    # empty return bloc     
    elif len(p) == 5 and p[1] == 'return':
        p[0] = ('Empty',p[2])
    # bloc return bloc 
    elif len(p) == 6 and p[2] == 'return':
        p[0] = (p[1], p[3])


# Return with implicit
def p_function_value_return_implicite(p):
    '''statement : FUNCTIONVALUEIMP NAME LPAREN multiname RPAREN LACCOLADE bloc NAME AFFECT expression SEMICOLON RACCOLADE
    | FUNCTIONVALUEIMP NAME LPAREN multiname RPAREN LACCOLADE bloc NAME AFFECT expression SEMICOLON bloc RACCOLADE
    | FUNCTIONVALUEIMP NAME LPAREN multiname RPAREN LACCOLADE NAME AFFECT expression SEMICOLON RACCOLADE
    | FUNCTIONVALUEIMP NAME LPAREN multiname RPAREN LACCOLADE NAME AFFECT expression SEMICOLON bloc RACCOLADE'''
    if len(p) == 13 and p[9] ==  '=' and p[8] == p[2]:
        p[0] = ('functionValueImp', p[2], p[4], p[7], p[10] )

    elif len(p) == 14 and p[9] ==  '=' and p[8] == p[2]:
        p[0] = ('functionValueImp', p[2], p[4], p[7], p[10] )

    elif len(p) == 12 and p[8] ==  '=' and p[7] == p[2]:
        p[0] = ('functionValueImp', p[2], p[4],'Empty', p[9] )

    elif len(p) == 13 and p[8] ==  '=' and p[7] == p[2]:
        p[0] = ('functionValueImp', p[2], p[4],'Empty', p[9] )


def p_call_Void_func(p):
    '''statement : NAME LPAREN RPAREN''' 
    p[0] = ('callVoid', p[1], 'Empty')

def p_call_Void_param_func(p):
    '''statement : NAME LPAREN multiExpr RPAREN''' 
    if len(p) == 5:
        p[0] = ('callVoidParam', p[1], p[3])    


def p_call_Value_func(p):
    '''callValue : NAME LPAREN RPAREN
    | NAME LPAREN multiExpr RPAREN''' 
    if len(p) == 5:
        p[0] = ('callValueParam', p[1], p[3]) 
    else:
        p[0] = ('callValue', p[1], 'Empty')
   

#Opération
def p_expression_binop_plus(p):
    'expression : expression PLUS expression'
    p[0] = ('+', p[1] , p[3])

def p_expression_binop_times(p):
    'expression : expression TIMES expression'
    p[0] = ('*', p[1] , p[3])

def p_expression_binop_divide_and_minus(p):
    '''expression : expression MINUS expression
				| expression DIVIDE expression'''
    if p[2] == '-': 
        p[0] = ('-', p[1] , p[3])
    else : 	
        p[0] = ('/', p[1] , p[3])

def p_expression_binop_bool(p):
    ''' expression : expression AND expression  
    | expression OR expression '''
    if p[2] == '&':
        p[0] = ('&', p[1] , p[3])
    else :
        p[0] = ('|', p[1] , p[3])

def p_expression_binop_comparison(p):
    '''expression : expression INF expression
				| expression SUP expression'''
    if p[2] == '<': 
        p[0] = ('<', p[1] , p[3])
    else : 	
        p[0] = ('>', p[1] , p[3])

def p_expression_binop_equals(p):
    '''expression : expression EQUALS expression'''
    p[0] = ('==', p[1] , p[3])

#Element terminaux    
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_callValue(p):
    'expression : callValue'
    p[0] = p[1]    

def p_expression_name(p):
    '''expression : NAME
    | GUILLEMET NAME GUILLEMET'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]
    
def p_expression_true(p):
    'expression : TRUE'
    p[0] = True

def p_expression_false(p):
    'expression : FALSE'
    p[0] = False

def p_error(p):
    print("Syntax error at '%s'" % p.value)

yacc.yacc()






