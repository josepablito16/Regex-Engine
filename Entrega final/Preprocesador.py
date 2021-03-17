
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

def revisarOperadoresLista(operacion):
    listaNueva = []

    print()
    #listaNueva += operacion[:operacion.index('+')]
    
    return listaNueva


        



def preProcesarExpresion(operacion):
    lista = separarExpresiones(operacion)
    print(lista)
    lista = revisarOperadoresLista(lista)
    print(lista)





if __name__ == '__main__':
    entradaOriginal = "a(ba)+|(a(b)*a)|(a|b)" 
    entradaFinal = '(((a.((b.a).((b.a)*α)))|((a.(b*α)).a))|(a|b))'

    entradaPreprocesada = preProcesarExpresion(entradaOriginal)

    print(entradaPreprocesada)
    #print(list(entradaFinal))
    print(entradaPreprocesada == entradaFinal)


