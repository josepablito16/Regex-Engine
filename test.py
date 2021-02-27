
def is_star(char):
    return char == '*'


def is_plus(char):
    return char == '+'


def is_question(char):
    return char == '?'


def is_operator(char):
    return is_star(char) or is_plus(char) or is_question(char)


def is_dot(char):
    return char == '.'


def is_open_set(char):
    return char == '['


def is_close_set(char):
    return char == ']'


# retorna si es numero o digito True
def is_literal(char):
    return char.isalpha() or char.isdigit()


def is_set(term):
    return is_open_set(term[0]) and is_close_set(term[-1])


def is_unit(term):
    return is_literal(term[0]) or is_dot(term[0]) or is_set(term)


def split_set(set_head):
    set_inside = set_head[1: -1]
    set_terms = list(set_inside)
    return set_terms


def split_expr(expr):
    head = None
    operator = None
    rest = None
    last_expr_pos = 0

    '''
	[abc] * xyz
	hhhhh o rrr
	'''
    if is_open_set(expr[0]):
        last_expr_pos = expr.find(']') + 1
        head = expr[0: last_expr_pos]
    else:
        last_expr_pos = 1
        head = expr[0]

    if last_expr_pos < len(expr) and is_operator(expr[last_expr_pos]):
        operator = expr[last_expr_pos]
        last_expr_pos += 1

    rest = expr[last_expr_pos:]

    return head, operator, rest


def does_unit_match(expr, string):
    # verifica si el primer caracter concuerda
    head, operator, rest = split_expr(expr)

    if is_literal(head):
        return expr[0] == string[0]
    elif is_dot(head):
        return True
    elif is_set(head):
        set_terms = split_set(head)
        return string[0] in set_terms

    return False


def match_multiple(expr, string, match_length, min_match_length=None, max_match_length=None):
    head, operator, rest = split_expr(expr)

    if not min_match_length:
        min_match_length = 0

    submatch_length = -1

    # Encuentra la longitud de la  cadena maxima
    while not max_match_length or (submatch_length < max_match_length):
        # head * n es una expansion
        [subexpr_matched, subexpr_length] = match_expr(
            (head * (submatch_length + 1)), string, match_length
        )

        if subexpr_matched:
            submatch_length += 1
        else:
            break

    # si submatch_length es -1 no entra
    # Se retorna a la funcion match_expr sabiendo
    # submatch_length para expandir head y concatenar
    # rest
    while submatch_length >= min_match_length:
        [matched, new_match_length] = match_expr(
            (head * submatch_length) + rest, string, match_length
        )

        if matched:
            return [matched, new_match_length]
        submatch_length -= 1

    return [False, None]


def match_star(expr, string, match_length):
    return match_multiple(expr, string, match_length, None, None)


def match_plus(expr, string, match_length):
    return match_multiple(expr, string, match_length, 1, None)


def match_question(expr, string, match_length):
    return match_multiple(expr, string, match_length, 0, 1)

    # Verifica si una palabra concuerda con el
    # lenguaje generado por una expresion regular


def match_expr(expr, string, match_length=0):
    if (len(expr) == 0):
        return [True, match_length]

    head, operator, rest = split_expr(expr)

    if is_star(operator):
        return match_star(expr, string, match_length)
    elif is_plus(operator):
        return match_plus(expr, string, match_length)
    elif is_question(operator):
        return match_question(expr, string, match_length)
    elif is_unit(head):
        # Si el primer caracter concuerda, extraemos ese caracter
        # y volvemos a llamar a la funcion
        if (does_unit_match(expr, string)):
            return match_expr(rest, string[1:], match_length + 1)
    else:
        print(f'Unknown token in expr {expr}')

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
    '''
    print(split_expr('abc'))
    print(split_expr('[123]bc'))
    print(split_expr('a*bc'))
    print(split_expr('[123]*bc'))
    print(split_expr('[123]+bc'))
    print(split_expr('[123]+'))
    return
    '''
    # Expresion regular
    expr = 'a[123]*c'

    # Palabra que deseamos ver si concuerda
    string = 'a12321321321321321321321321321c'
    [matched, match_pos, match_length] = match(expr, string)

    if (matched):
        print(
            f'match_expr({expr}, {string}) = {string[match_pos: match_pos + match_length]}')
    else:
        print(f'match_expr({expr}, {string}) = False')


if __name__ == '__main__':
    main()
