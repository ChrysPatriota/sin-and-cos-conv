import math
import numpy as np


def o(p):
    return 4 * p


def q(r):
    return 4 * r + 1


def s(t):
    return 4 * t + 2


def u(v):
    return 4 * v + 3


def ll(n, m):
    return math.floor((math.fabs(n - math.fabs(m))) / 4)


def cos(pot):
    if pot == 0:
        return ""
    elif pot == 1:
        return "cos(x)"
    else:
        return "cos^" + str(pot) + "(x)"


def sin(pot):
    if pot == 0:
        return ""
    elif pot == 1:
        return "sen(x)"
    else:
        return "sen^" + str(pot) + "(x)"


def sinofnx(n):
    ans = 'sen(' + str(n) + 'x) = '

    a = int(math.fabs(n))

    if n == 0:
        return ans + '0'

    for i in range(a + 1):

        if ll(a, 1) >= i and np.heaviside(a - 1, 1) == 1:

            if n < 0:
                ans = ans + ' - '
            else:
                ans = ans + ' + '

            ans = ans + str(math.comb(a, q(i))) + cos(a - q(i)) + sin(q(i))

        if ll(a, 3) >= i and np.heaviside(a - 3, 1) == 1:

            if n < 0:
                ans = ans + ' + '
            else:
                ans = ans + ' - '

            ans = ans + str(math.comb(a, u(i))) + cos(a - u(i)) + sin(u(i))

    return ans


def cosofnx(n):
    ans = 'cos(' + str(n) + 'x) = '

    a = int(math.fabs(n))

    if n == 0:
        return ans + '1'

    for i in range(a + 1):

        if ll(a, 0) >= i:
            ans = ans + ' + '

            ans = ans + str(math.comb(a, o(i))) + cos(a - o(i)) + sin(o(i))

        if ll(a, 2) >= i and np.heaviside(a - 2, 1) == 1:
            ans = ans + ' - '

            ans = ans + str(math.comb(a, s(i))) + cos(a - s(i)) + sin(s(i))

    return ans


func = ''

while func != 'seno' and func != 'coseno':
    func = str(input("Bem vindo, escolha qual função trigonométrica deseja: seno ou coseno"))

num = ''

while not (isinstance(num, int)):
    num = input("Selecione o numero inteiro:")