
# retorna si es numero o digito True
def isLiteral(char):
    return char.isalpha() or char.isdigit() or char in ['ε','α']

def isOperador(char):
    return char in ['|','+','?','*']

def agregarKleenStar(expresion):
    if(isLiteral(expresion[-1])):
        return expresion[:-1] + ["("] + expresion[-1 :] + ["*" , "α" , ")"]

    parentesisContador = 0
    parentesisControl = False
    for index in range(len(expresion) - 1, -1, -1):
        if (expresion[index] == ")"):
            parentesisContador += 1
            parentesisControl = True

        if (expresion[index] == "("):
            parentesisContador -= 1
        
        if (parentesisContador == 0 and parentesisControl):
            return expresion[:index] + ["("] + expresion[index :] + ["*" , "α" , ")"]

def agregarAgrupacionConcat(expresion):
    parentesisContador = 0
    parentesisControl = False
    for index in range(len(expresion) - 1, -1, -1):
        if (expresion[index] == ")"):
            parentesisContador += 1
            parentesisControl = True

        if (expresion[index] == "("):
            parentesisContador -= 1
        
        if (parentesisContador == 0 and parentesisControl):
            return expresion[:index] + ['('] + expresion[index :] + [')']


def separarExpresiones(operacion):
    lista = []
    operacionTemp = ""

    parentesisAbierto = False
    parentesisContador = 0
    for i in range(len(operacion)):
        if (isLiteral(operacion[i]) == True and isLiteral(operacion[i +1]) == False and parentesisAbierto == False):
            lista.append(operacion[i])
        
        if (isLiteral(operacion[i]) and parentesisAbierto):
            operacionTemp += operacion[i]

        if (isOperador(operacion[i]) and parentesisAbierto):
            operacionTemp += operacion[i]
        
        if (isOperador(operacion[i]) and not parentesisAbierto):
            if (operacion[i] in ['+','*','?']):
                lista.append(lista.pop() + operacion[i])
            else:
                lista.append(operacion[i])

        if (operacion[i] == '('):
            operacionTemp += operacion[i]
            parentesisAbierto = True
            parentesisContador += 1
        
        if (operacion[i] == ')'):
            operacionTemp += operacion[i]
            parentesisContador -= 1

            if (parentesisContador == 0):
                lista.append(operacionTemp)
                operacionTemp = ""
                parentesisAbierto = False
                parentesisContador = 0
        
        
         
    return lista

def concatenar(operacion, inicio, fin):
    print(f"({operacion[:fin]}.{operacion[fin:]})")

def operacionToList(operacion):
    lista = []
    temp = ""
    parentesisAbierto = False
    contadorParentesis = 0 

    if(operacion[0] == "(" and (operacion[-1] == ")" or operacion[-1] in ['+','*','?'])):
        lista.append(operacion)
        return lista
        return 0

    for i in operacion:
        if (isLiteral(i) and not parentesisAbierto):
            lista.append(i)
        
        if (isLiteral(i) and parentesisAbierto):
            temp += i


        if (isOperador(i) and not parentesisAbierto):
            lista.append(i)
        
        if (isOperador(i) and parentesisAbierto and contadorParentesis == 0):
            temp += i
            lista.append(temp)
            temp = ""
            parentesisAbierto = False
        
        if (i == "(" and not parentesisAbierto):
            parentesisAbierto = True
            temp += i
            contadorParentesis += 1
        
        if (i == ")"):
            temp += i
            contadorParentesis -= 1
            

    
    return lista




def armarSubExpresion(operacion):
    if (len(operacion) == 1):
        return operacion
    
    if(operacion[0] == "(" and operacion[-1] == ")"):
        operacion = operacion[1:-1]
    

    return operacionToList(operacion)
    

    '''
    for i in range(len(operacion)):
        if (isLiteral(operacion[i]) and isLiteral(operacion[i+1])):
            print(f"CONCATENAR {operacion[i]} . {operacion[i+1]}")
            concatenar(operacion, i, i+1)
        
        if (isLiteral(operacion[i]) and operacion[i+1] == "("):
            print(f"CONCATENAR {operacion[i]} . {operacion[i+1]}")
            concatenar(operacion, i, i+1)
    '''


def preProcesarExpresion(operacion):
    lista = separarExpresiones(operacion)
    
    for i in lista:
        print(i)
        print(f"armarSubExpresion: {armarSubExpresion(i)}")
        print()

    return lista
    




if __name__ == '__main__':
    entradaOriginal = "a(ba)+|(a(b)*a)|(a|b)" 
    entradaFinal = '(((a.((b.a).((b.a)*α)))|((a.(b*α)).a))|(a|b))'

    entradaPreprocesada = preProcesarExpresion(entradaOriginal)
    print(entradaPreprocesada)




    #print(list(entradaFinal))
    print(entradaPreprocesada == entradaFinal)


