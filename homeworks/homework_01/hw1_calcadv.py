#!/usr/bin/env python
# coding: utf-8


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''

    def calc(arr):
        sol = []
        operators = "*/+-"
        for var in arr:
            if var in operators:
                if len(sol) == 1:
                    sol[-1] = float(var + str(sol[-1]))
                    continue
                if var == "+":
                    res = sol[-2] + sol[-1]
                elif var == "-":
                    res = sol[-2] - sol[-1]
                elif var == "*":
                    res = sol[-2] * sol[-1]
                elif var == "/":
                    if sol[-1] != 0.0:
                        res = sol[-2] / sol[-1]
                    else:
                        return None
                sol.pop()
                sol[-1] = res
            elif is_number(var):
                sol.append(float(var))
        return sol[-1]

    def is_number(string):
        if "." in string:
            if string.replace(".", "1").isdigit():
                return True
            else:
                return False
        else:
            if string.isdigit():
                return True
            else:
                return False

    if input_string == "":
        return None
    nums = "1234567890"
    res = ""
    stek = []
    opers = "+-*/"
    operators = "*/+-()"
    op_dic = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1, ")": 1}
    symb = ""
    from_this = False
    for c in range(len(input_string)):
        if input_string[c] == " " or input_string[c] == "\t":
            if len(res) >= 1 and (symb in nums or symb == ")") and \
                    (c < len(input_string) - 2) and input_string[c+1] in nums:
                return None
            else:
                continue
        else:
            if not from_this:
                prev_symb = symb
            from_this = False
            symb = input_string[c]
            if c < len(input_string) - 2:
                if input_string[c + 1] != " ":
                    next_symb = input_string[c+1]
                else:
                    next_symb = input_string[c + 2]
        if symb in nums:
            res += symb
        elif symb == "." and is_number(res[-1]):
            res += symb
        elif symb == "." and not is_number(res[-1]):
            if is_number(input_string[c+1]):
                res += symb
        elif symb in operators:
            res += " "
            if stek != []:
                if prev_symb == "-" and symb == "-":
                    stek[-1] = "+"
                    prev_symb = "+"
                    from_this = True
                    continue
                elif prev_symb in opers and symb in opers:
                    if prev_symb == "+" and symb == "-":
                        stek[-1] = "-"
                        prev_symb = "-"
                        from_this = True
                        continue
                    elif prev_symb == "+" and symb == "+":
                        continue
                    elif (prev_symb == "/" or prev_symb == "*") and \
                            symb == "-" and next_symb in nums:
                        continue
                    else:
                        return None
            if stek == []:
                if symb != ")":
                    stek.append(symb)
                else:
                    return None
            else:
                if symb == "(":
                    stek.append(symb)
                elif symb == ")":
                    if "(" not in stek:
                        return None
                    elif stek[-1] == "(":
                        return None
                    else:
                        while stek[-1] != "(":
                            if res[-1] != " ":
                                res += " " + stek[-1] + " "
                            else:
                                res += stek[-1] + " "
                            stek.pop()
                        stek.pop()
                elif op_dic[stek[-1]] < op_dic[symb] and symb != ")":
                    stek.append(symb)
                elif op_dic[stek[-1]] >= op_dic[symb] and symb != ")":
                    while stek != [] and op_dic[stek[-1]] >= op_dic[symb] \
                            and stek[-1] != "(" and symb != ")":
                        if prev_symb in opers and symb in opers:
                            if prev_symb != "+" and symb != "-":
                                return None
                        if res[-1] != " ":
                            res += " " + stek.pop() + " "
                        else:
                            res += stek.pop() + " "
                    stek.append(symb)
        else:
            return None
    if stek != []:
        for var in stek[::-1]:
            if res[-1] != " ":
                res += " " + var
            else:
                res += var
    if stek.count("(") != stek.count(")"):
        return None
    eq = res.split()
    for var in eq:
        if var.count(".") > 1:
            return None
    count = 0
    for var in eq:
        if is_number(var):
            count += 1
    if len(eq) > 2:
        if count < 2:
            return None
        else:
            return calc(eq)
    else:
        if len(eq) == 2:
            if is_number(eq[0]) and (eq[1] in "+-"):
                return float(eq[1] + eq[0])
            elif (eq[0] in "+-") and is_number(eq[1]):
                return float(eq[0] + eq[1])
            else:
                return None
        elif len(eq) == 1:
            if is_number(eq[0]):
                return float(eq[0])
            else:
                return None
