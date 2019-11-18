def priority(z):
    if z in ['*', '/']:
        return 2
    elif z in ['+', '-']:
        return 1
    else:
        return 3


def judge_bracket(op1, op2):
    if op1 == '(' or op2 == '(':
        return False
    else:
        return True


def cal_postfix_expression(postfix_expression):
    num_stack = list()

    for z in postfix_expression:
        if z not in ['*', '/', '+', '-', "^"]:
            num_stack.append(z)
        else:
            a = num_stack.pop()
            b = num_stack.pop()
            if z == "^":
                z = "**"
            c = str(b) + z + str(a)
            c = eval(c.strip())
            num_stack.append(c)

    return num_stack[0]


def is_operation(z):
    if z in ['*', '/', '+', '-', '(', ')', "^"]:
        return True
    else:
        return False


def parse_input(input: str):
    if input[0] == "-":
        input = "0" + input

    index_list = list()
    for index, ele in enumerate(input):
        if is_operation(ele):
            index_list.append(index)

    for cnt, ind in enumerate(index_list):
        input = input[:(ind + 2 * cnt)] + \
            " " + input[(ind + 2 * cnt):(ind + 2 * cnt + 1)] + \
            " " + input[(ind + 2 * cnt + 1):]

    return input.split()


def parse_input_for_prefix(input: str):
    return input.split()


def write_exp(inexp):
    out_str = ""
    for ele in inexp:
        out_str += ele

    if out_str[0] == "(" and out_str[len(out_str) - 1] == ")":
        out_str = out_str[1:len(out_str) - 1]

    return out_str


def assign(var, val, inexp):
    outexp = inexp.copy()
    for ind, ele in enumerate(outexp):
        if ele == var:
            outexp[ind] = str(val)

    return outexp


def compound_inexp(ine1, ine2):
    if ine2[0] == "-":
        return ine1 + ine2
    else:
        return ine1 + ["+"] + ine2


def print_expression(exp):
    out_str = ""
    for ele in exp:
        out_str += (ele+" ")

    return out_str
