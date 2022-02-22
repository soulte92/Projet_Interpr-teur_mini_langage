names = {}
functions_void = {}
functions_values = {}
# functions_return_values = {}

def eval_Expr(t):
    if type(t) is int :
        return t
    elif type(t) is str:
        if t in names:
            return names[t]
        return t
    elif type(t) is list:
        eval_Inst(t[1])

        return eval_Expr(t[2])

    if type(t) is tuple:
        if t[0] ==  "multiExpr":
            return eval_Expr(t[1]) 

        elif t[0] == 'callValue' :
            eval_Inst(functions_values[t[1]][1])
            return eval_Expr(functions_values[t[1]][2])

        elif t[0] == 'callValueParam':
            #Fonction content
            our_function = functions_values[t[1]][1]
            return_value = functions_values[t[1]][2]
            #Les paramètres de la function
            p = functions_values[t[1]][0]
            while len(t[2])!= 1 and len(p)!=1:
                if len(p) == 2 and len(t[2]) == 2:
                    names[p[1]] = eval_Expr(t[2][1])
                    #functions_values[new_t[1]] Return fonction dict tuple
                    eval_Inst(our_function)
                    return eval_Expr(return_value)
                elif len(p) == len(t[2]) and len(p)>=3:
                    names[p[1]] = eval_Expr(t[2][1])
                    t = t[2]
                    p = p[2]     
        elif t[0]== '+':
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
        elif t[0]== '==':
            return eval_Expr(t[1]) > eval_Expr(t[2])
        # elif t[0] == 'incPlus':
        #     names[t[1]] = names[t[1]] + 1
        #     return names[t[1]]
        # elif t[0] == 'incExpr':
        #     names[t[1]] = names[t[1]] + eval_Expr(t[2])
        #     return names[t[1]]
        # elif t[0] == 'decMinus':
        #     names[t[1]] = names[t[1]] - 1
        #     return names[t[1]]
        # elif t[0] == 'decExpr':
        #     names[t[1]] = names[t[1]] - eval_Expr(t[2])
        #     return names[t[1]]

def eval_Inst(t): 
    print("eval_Expr= ", t)       
    if t == 'Empty' or t is None:
        return
    elif t[0] == 'bloc':
        eval_Inst(t[1])
        eval_Inst(t[2])

    elif t[0] == 'print':
        if len(t[1]) == 2:
            print('print >', eval_Expr(t[1]))
        else:
            p = t[1]
            while 1:
                if len(p) == 2:
                    print('print >', eval_Expr(p[1]))
                    break
                else:
                    print('print >', eval_Expr(p[1]))
                    p = p[2]

    elif t[0] == 'affect':
        names[t[1]] = eval_Expr(t[2])

    elif t[0] == 'multiname':
        #on vient de functions_void
        if len(t) == 3:
            #multiple param
            eval_Inst(t[2])
            names[t[2]] = None
        else:
            #sans param
            names[t[1]] = None    

    elif t[0] == 'if':
        if len(t) == 3:
            if eval_Expr(t[1]):
                eval_Inst(t[2])
        else:
            if eval_Expr(t[1]):
                eval_Inst(t[2])
            else:
                eval_Inst(t[4])

    elif t[0] == 'while':
        while bool(eval_Expr(t[1])) == True :
            eval_Inst(t[2])     

    elif t[0] == 'for':
        eval_Inst(t[1])
        while bool(eval_Expr(t[2])) == True:
            eval_Inst(t[3])
            eval_Inst(t[4]) 

    elif t[0] == 'functionVoid':
        if len(t) == 3:
            #sans param
            functions_void[t[1]] = ('Empty',t[2]) 
        else:
            #avec param
            functions_void[t[1]] = (t[2],t[3]) 
            eval_Inst(t[2])  

    elif t[0] == 'functionValue':
        if len(t) == 4:
            #sans param
            functions_values[t[1]] = ('Empty',t[2], t[3]) 
        else:
            #avec param
            functions_values[t[1]] = (t[2],t[3], t[4]) 
            eval_Inst(t[2])

    elif t[0] == 'callVoid':
        if t[1] in functions_void:
            eval_Inst(functions_void[t[1]][1])
    elif t[0] == 'callVoidParam':
        #Les instructions de la function
        our_function = functions_void[t[1]][1]
        #Les paramètres de la function
        p = functions_void[t[1]][0]
        while len(t[2])!= 1 and len(p)!=1:
            if len(p) == 2 and len(t[2]) == 2:
                names[p[1]] = eval_Expr(t[2][1])
                eval_Inst(our_function)
                break
            elif len(p) == len(t[2]) and len(p)>=3:
                names[p[1]] = eval_Expr(t[2][1])
                t = t[2]
                p = p[2]
