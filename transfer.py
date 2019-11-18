from module import priority, judge_bracket
from module import cal_postfix_expression, is_operation


def in2pre(inexpression):
    preexpression = list()
    assist_stack = list()
    expression_tmp = list()
    inexpression = inexpression[::-1]

    for z in inexpression:
        if z == '(':
            expression_tmp += [')']
        elif z == ')':
            expression_tmp += ['(']
        else:
            expression_tmp += [z]

    for z in expression_tmp:
        if not is_operation(z):
            preexpression = [z] + preexpression
        else:
            while len(assist_stack):
                if z == "(" or z == ")" or assist_stack[-1] == "(" or assist_stack[-1] == ")":
                    if judge_bracket(assist_stack[-1], z):
                        op = assist_stack.pop()
                        preexpression = [op] + preexpression
                    else:
                        break
                else:
                    if priority(assist_stack[-1]) > priority(z):
                        op = assist_stack.pop()
                        preexpression = [op] + preexpression
                    else:
                        break
            if len(assist_stack) == 0 or z != ')':
                assist_stack.append(z)
            else:
                assist_stack.pop()
    if len(assist_stack):
        preexpression = assist_stack + preexpression
    return preexpression


def in2post(inexpression):
    postfix_expression = list()
    operation_stack = list()

    for z in inexpression:
        if not is_operation(z):
            postfix_expression.append(z)
        else:
            if z != ')' and (not operation_stack
                             or z == '('
                             or operation_stack[-1] == '('
                             or priority(z) > priority(operation_stack[-1])):
                operation_stack.append(z)
            elif z == ')':
                while True:
                    x = operation_stack.pop()
                    if x != '(':
                        postfix_expression.append(x)
                    else:
                        break
            else:
                while True:
                    if operation_stack \
                            and operation_stack[-1] != '('\
                            and priority(z) <= priority(operation_stack[-1]):
                        postfix_expression.append(operation_stack.pop())
                    else:
                        operation_stack.append(z)
                        break
    while operation_stack:
        postfix_expression.append(operation_stack.pop())

    return postfix_expression


def pre2in(preexpression):
    assist_stack = list()

    len_pe = len(preexpression)
    for index in range(len_pe):
        if not is_operation(preexpression[len_pe - index - 1]):
            assist_stack.append([preexpression[len_pe - index - 1]])
        else:
            op1 = assist_stack.pop()
            op2 = assist_stack.pop()

            temp_list = ["("] + op1 + \
                [preexpression[len_pe - index - 1]] + \
                op2 + [")"]
            assist_stack.append(temp_list)

    return assist_stack[len(assist_stack) - 1]
