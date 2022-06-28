# testes praticos Turing

def calpoints(ops) -> int:

    lista = []
    for op in ops:
        if op == '+':
            lista.append(lista[-1]+lista[-2])
        elif op == 'D':
            lista.append(2 * lista[-1])
        elif op == 'C':
            lista.pop()
        else:
            lista.append(int(op))
    result = sum(lista)
    return result


if __name__ == '__main__':

    print(calpoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))