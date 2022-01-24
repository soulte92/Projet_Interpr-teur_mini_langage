names = {}

def eval_Expr(t):
    if type(t) is int :
        return t
    elif type(t) is str :
        return names[t]

    if type(t) is tuple:
        if t[0]== '+':
            return eval_Expr(t[1]) + eval_Expr(t[2])
        elif t[0]== '-':
            return eval_Expr(t[1]) - eval_Expr(t[2])
        elif t[0]== '/':
            return eval_Expr(t[1]) / eval_Expr(t[2])
        elif t[0]== '*':
            return eval_Expr(t[1]) * eval_Expr(t[2])
        elif t[0]== '&':
            return eval_Expr(t[1]) & eval_Expr(t[2])
        elif t[0]== '|':
            return eval_Expr(t[1]) | eval_Expr(t[2])
        elif t[0]== '<':
            return eval_Expr(t[1]) < eval_Expr(t[2])
        elif t[0]== '>':
            return eval_Expr(t[1]) > eval_Expr(t[2])

def eval_Inst(t): 
    print("eval_Expr= ", t)       
    if t == 'Empty':
        return
    elif t[0] == 'bloc':
        eval_Inst(t[1])
        eval_Inst(t[2])
    elif t[0] == 'print':
        # print(t[3])
        print('calc >',eval_Expr(t[1]))
    elif t[0] == 'affect':
        names[t[1]] = t[2]
    elif t[0] == 'if':
        if eval_Expr(t[1]):
            eval_Inst(t[2])
    # if t[0] == 'while':
    #     while eval_Expr(t[1]) is True:
    #         eval_Inst(t[2])
    #     else:
    #         print('calc> while condition False')
    elif t[0] == 'while':
        while bool(eval_Expr(t[1])) == True :
            eval_Inst(t[2])      

    elif t[0] == 'for':
        eval_Inst(t[1])
        while bool(eval_Expr(t[2])) == True:
            eval_Inst(t[3])
            eval_Inst(t[4]) 