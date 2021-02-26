# Verifica si el primer caracter concuerda
def does_unit_match(expr, string):
    return expr[0] == string[0]


# Verifica si una palabra concuerda con el
# lenguaje generado por una expresion regular
def match_expr(expr, string, match_length=0):
    if (len(expr) == 0):
        return [True, match_length]

    # Si el primer caracter concuerda, extraemos ese caracter
    # y volvemos a llamar a la funcion
    if (does_unit_match(expr, string)):
        return match_expr(expr[1:], string[1:], match_length + 1)
    else:
        return [False, None]

# Itera toda la palabra intentando hacer match
# con la expresion regular


def match(expr, string):
    match_pos = 0
    matched = False
    max_match_pos = len(string) - 1
    while not matched and match_pos < max_match_pos:
        [matched, match_length] = match_expr(expr, string[match_pos:])
        if matched:
            return [matched, match_pos, match_length]
        match_pos += 1

    return [False, None, None]


def main():

    # Expresion regular
    expr = 'abc'

    # Palabra que deseamos ver si concuerda
    string = 'Hello abc!'
    [matched, match_pos, match_length] = match(expr, string)

    if (matched):
        print(
            f'match_expr({expr}, {string}) = {string[match_pos: match_pos + match_length]}')
    else:
        print(f'match_expr({expr}, {string}) = False')


if __name__ == '__main__':
    main()
