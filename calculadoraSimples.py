def calculate():
    operation = input('''
    Por favor, digite um operador:
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
    -> digite aqui: 
    ''')

    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('Operador inválido, por favor digite um operador válido')
    again()

def again():
    calc_again = input('''
Você gostaria de calcular novamente?
Por favor digite S para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até mais!')
    else:
        again()
calculate()

