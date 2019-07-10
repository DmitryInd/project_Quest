"""For calculating(Polka)"""


def truth(expression):
    """Output correctness of expression"""
    expression = str(expression)
    i = 0
    while i < len(expression):
        if expression[i] == 'a':
            expression = expression[: i] + '*' + expression[i + 3:]
        elif expression[i] == 'o':
            expression = expression[: i] + '+' + expression[i + 2:]
        i += 1

    bin_answer = polka(expression)
    return False if bin_answer == 0 else True


def calculate(expression):
    """Return result of expression"""
    i = 0
    for i in range(len(expression)):
        if expression[i] == '<' or expression[i] == '>' or expression[i] == '=':
            break

    definition = polka(expression[: i])
    u = i
    while not expression[u].isdigit():
        u += 1
    b = polka(expression[u:])
    answer = False
    if expression[i] == "!":
        answer = (definition != b)
    else:
        while i < u and (expression[i] == '<' or
                         expression[i] == '>' or
                         expression[i] == '='):
            answer = answer or (expression[i] == '<' and definition < b)
            answer = answer or (expression[i] == '>' and definition > b)
            answer = answer or (expression[i] == '=' and definition == b)
            i += 1
    return "1" if answer else "0"


def polka(expression):
    """Calculator"""
    stack = []
    res = []
    num = ""
    prepare = 1
    i = ""
    for i in expression:  # Create reverse Polish notation
        if i.isdigit() or i == '.':
            num += i
            continue
        elif num != "":
            res.append((0 - float(num)) if prepare == 2 else float(num))
            prepare = 0
            num = ""
        if i == " ":
            continue
        if i == "*" or i == "/" or i == "(":
            stack.append(i)
            prepare = 1
            continue
        if i == ")":
            k = 0
            for k in range(len(stack) - 1, -1, -1):
                if stack[k] == "(":
                    break
                res.append(stack[k])
            stack = stack[: k]
            continue
        if i == "-" and prepare == 1:
            prepare = 2
            continue
        prepare = 1
        k = 0
        for k in range(len(stack) - 1, -1, -1):
            if stack[k] == "+" or stack[k] == "-" or stack[k] == "(":
                break
            res.append(stack[k])
        stack = stack[: k + 1] if k != 0 else []
        stack.append(i)
    if i.isdigit():
        res.append(float(num))
    for i in range(len(stack) - 1, -1, -1):
        res.append(stack[i])

    i = 2
    while len(res) > 1:  # Use it for calculating
        if (str(type(res[i])) != "<class 'float'>") and\
                (str(type(res[i])) != "<class 'int'>"):
            if res[i] == "+":
                res[i - 2] = res[i - 2] + res[i - 1]
                res.pop(i - 1)
                res.pop(i - 1)
                i -= 2
            elif res[i] == "-":
                res[i - 2] = res[i - 2] - res[i - 1]
                res.pop(i - 1)
                res.pop(i - 1)
                i -= 2
            elif res[i] == "*":
                res[i - 2] = res[i - 2] * res[i - 1]
                res.pop(i - 1)
                res.pop(i - 1)
                i -= 2
            elif res[i] == "/":
                if res[i - 1] != 0:
                    res[i - 2] = res[i - 2] / res[i - 1]
                else:
                    res[i - 2] = 0
                res.pop(i - 1)
                res.pop(i - 1)
                i -= 2
        i += 1
    return res[0]
