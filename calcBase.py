# -----------------------------------------------------------------------------
# calc.py
#
# Expressions arithmétiques sans variables
# -----------------------------------------------------------------------------
from genereTreeGraphviz2 import printTreeGraph
import ply.yacc as yacc

reserved = {
    'print' : 'PRINT',
    'if' : 'IF',
    'while' : 'WHILE',
    'for' : 'FOR',
}

tokens = ['NUMBER','MINUS',
    'PLUS','TIMES','DIVIDE',
    'LPAREN','RPAREN', 'AND', 'OR',
    'TRUE','FALSE', 'SEMICOLON', 'NAME',
    'AFFECT', 'INF', 'SUP', 'LACCOLADE', 'RACCOLADE']

tokens = tokens + list(reserved.values())

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE')
    )       


#Variables
names = {}

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
t_INF       = r'<'
t_SUP       = r'>'

import util_fonctions as uf

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


#Début d'exécution des règles
def p_start(p):
    'start : bloc'
    p[0] = ('START',p[1])
    print('Arbre de dérivation = ',p[1])
    printTreeGraph(p[1])
    print('CALC> ',uf.eval_Inst(p[1]))

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
    'statement : PRINT LPAREN expression RPAREN'
    # print(p[3])
    p[0] = ('print', p[3])

#Fait un une affection d'une expression dans une variable
def p_affect(p):
    'statement : NAME AFFECT expression'
    names[p[1]] = p[3]
    p[0] = ('affect',p[1], p[3])
 

def p_condition_if(p):
    '''statement : IF LPAREN expression RPAREN LACCOLADE bloc RACCOLADE'''
    p[0] = ('if', p[3], p[6])   
     
def p_boucle_while(p):
    'statement : WHILE LPAREN expression RPAREN LACCOLADE bloc RACCOLADE'
    p[0] = ('while', p[3], p[6])    

def p_boucle_for(p):
    '''statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LACCOLADE bloc RACCOLADE'''
    p[0] = ('for', p[3], p[5], p[7], p[10])       

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
    
#Element terminaux    
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : NAME'
    # p[0] = names[p[1]]
    # p[0] = (p[1], names[p[1]])
    p[0] = names[p[1]]
    #p[0] = p[1]
    
def p_expression_true(p):
    'expression : TRUE'
    p[0] = True

def p_expression_false(p):
    'expression : FALSE'
    p[0] = False

def p_error(p):
    print("Syntax error at '%s'" % p.value)

yacc.yacc()


# s = input('calc > ')
# s = 'a = (1+1)+1;'
# s = 'print(1+2);a=2;print(a);'
# s='print(1+2);x=4;x=x+1;print(x);'
#s = 'if(2<4){print(2*3);print(3);};'
#s = 'x=1;x=x+1;print(x);'
s = 'x=2;while(x<5){print(x);x=x+1;};'
#s = 'while(5){print(1);};'
# s = 'x=5;while(x<8){print(2+9);};'
#s = 'x=1+2;print(x);'
yacc.parse(s)

