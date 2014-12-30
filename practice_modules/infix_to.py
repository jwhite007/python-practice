#! /usr/bin/env python

import operator
from Queue import Queue

def infix_to_postfix(infix_string):
    prec_dict = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    operator_stack = []
    post_fix_list = []
    token_list = infix_string.split()

    for token in token_list:
        try:
            token = int(token)
        except:
            pass
        finally:
            if isinstance(token, int):
                post_fix_list.append(str(token))
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                top_token = operator_stack.pop()
                while top_token != '(':
                    post_fix_list.append(top_token)
                    top_token = operator_stack.pop()
            else:
                los = len(operator_stack)
                while los > 0 and prec_dict[operator_stack[los - 1]] >= prec_dict[token]:
                    post_fix_list.append(operator_stack.pop())
                operator_stack.append(token)
    while len(operator_stack) > 0:
        post_fix_list.append(operator_stack.pop())
    return ' '.join(post_fix_list)


def infix_to_prefix(infix_string):
    prec_dict = {'*': 3, '/': 3, '+': 2, '-': 2, ')': 1}
    operand_queue = Queue()
    operator_stack = []
    prefix_list = []
    token_list = infix_string.split()

    for token in token_list:
        try:
            token = int(token)
        except:
            pass
        finally:
            if isinstance(token, int):
                operand_queue.put(str(token))
            elif token == '(':
                if len(operator_stack) == 0:
                    pass
                else:
                    prefix_list.append(operator_stack.pop())
                    prefix_list.append(operand_queue.get())
            elif len(operator_stack) > 0 and operator_stack[len(operator_stack) - 1] == ')':
                operator_stack.pop()
                prefix_list.append(token)
                while len(operator_stack) > 0:
                    prefix_list.append(operator_stack.pop())
                while not operand_queue.empty():
                    prefix_list.append(operand_queue.get())
            else:
                if len(operator_stack) > 0 and prec_dict[token] > prec_dict[operator_stack[len(operator_stack) - 1]]:
                    prefix_list.append(operator_stack.pop())
                    prefix_list.append(operand_queue.get())
                    operator_stack.append(token)
                else:
                    operator_stack.append(token)
    while len(operator_stack) > 0:
        token = operator_stack.pop()
        if token == ')':
            continue
        else:
            prefix_list.append(token)
    while not operand_queue.empty():
        prefix_list.append(operand_queue.get())

    return ' '.join(prefix_list)


def evaluate(string):
    operand_stack = []
    token_list = string.split()
    if token_list[0] in '*/+-':
        token_list = token_list[::-1]
    for token in token_list:
        try:
            token = int(token)
        except:
            pass
        finally:
            if isinstance(token, int):
                operand_stack.append(token)
            else:
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                operand_stack.append(do_math(token, op1, op2))
    return operand_stack.pop()

def do_math(token, op1, op2):
    if token == '*':
        return op1 * op2
    elif token == '/':
        return op1 / op2
    elif token == '+':
        return op1 + op2
    else:
        return op1 - op2

if __name__ == '__main__':
    # from timeit import timeit
    # print(postfix_eval('10 2 *'))
    # print(timeit(stmt = "do_math('-', 10, 5)", setup = 'from __main__ import do_math'))
    # print(timeit(stmt = "do_math2('-', 10, 5)", setup = 'from __main__ import do_math2'))
    # print(postfix_eval(infix_to_postfix('( 10 + 4 ) * ( 3 + 2 )')))
    # print infix_to_postfix('( 10 + 4 ) * 3')
    # print infix_to_postfix('10 + 4 * 3')
    # print evaluate('+ + + 4 2 10 3')
    print evaluate(infix_to_prefix('( 4 + 2 ) * ( 10 + 3 )'))
    print evaluate(infix_to_prefix('4 + 2 * 10 + 3'))
    print evaluate(infix_to_prefix('4 + 2 + 10 + 3'))
    print evaluate(infix_to_prefix('4 + 2 * ( 10 + 3 )'))