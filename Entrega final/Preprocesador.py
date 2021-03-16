
# retorna si es numero o digito True
def isLiteral(char):
    return char.isalpha() or char.isdigit() or char in ['ε','α']


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


def preProcesarExpresion(operacion):
    lista = []
    concatControl = False
    kleenControl = False
    

    for index in range(len(operacion)):
        print(lista)
        item = operacion[index]
        if (isLiteral(item) and concatControl):
            lista.append('.')
            concatControl = False
        
        if (isLiteral(item) and kleenControl):
            print(lista)
            lista.append('.')
            kleenControl = False

        if (isLiteral(item) and not concatControl):
            concatControl = True
        else:
            concatControl = False
        
        
        if (item == '*'):
            print()
            print(f"ALERTA EN {lista}")
            lista = agregarKleenStar(lista)
            kleenControl = True
        else:
            lista.append(item)

        if(isLiteral(item) and lista[-2] == "."):
            #print()
            #print(f"ALERTA EN {lista}")
            lista = agregarAgrupacionConcat(lista)

    
    return ''.join(lista)




if __name__ == '__main__':
    entradaOriginal = "(ε|a*b)" 
    entradaFinal = '((((((a|b)*α).a).b).b))'

    entradaPreprocesada = preProcesarExpresion(entradaOriginal)

    print(entradaPreprocesada)
    #print(list(entradaFinal))
    print(entradaPreprocesada == entradaFinal)


