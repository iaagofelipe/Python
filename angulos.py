import math
angulo = float(input("digite um ângulo qualquer: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O Ângulo {} possui:\nseno {}\ncosseno {}\ntangente {}'.format(angulo, sen, cos, tan))
