
# retorna si es numero o digito True
def isLiteral(char):
    return char.isalpha() or char.isdigit() or char in ['ε']


def agregarKleenStar(expresion):
    parentesisContador = 0
    parentesisControl = False
    for index in range(len(expresion) - 1, -1, -1):
        if (expresion[index] == ")"):
            parentesisContador += 1
            parentesisControl = True

        if (expresion[index] == "("):
            parentesisContador -= 1
        
        if (parentesisContador == 0 and parentesisControl):
            return expresion[:index] + ["("] + expresion[index :] + ["*" , "ε" , ")"]


def createParentesis(operacion):
    lista = []
    concatControl = False
    kleenControl = False

    for index in range(len(operacion)):
        item = operacion[index]
        if (isLiteral(item) and concatControl):
            lista.append('.')
            concatControl = False
        
        if (isLiteral(item) and kleenControl):
            lista.append('.')
            kleenControl = False

        if (isLiteral(item) and not concatControl):
            concatControl = True
        else:
            concatControl = False
        
        if (item == '*'):
            lista = agregarKleenStar(lista)
            kleenControl = True
        else:
            lista.append(item)


    
    return ''.join(lista)





entradaOriginal = "((a|b)*b)" 
entradaFinal = "(((a|b)*ε).b)"

entradaPreprocesada = createParentesis(entradaOriginal)

print(entradaPreprocesada)
print(entradaPreprocesada == entradaFinal)