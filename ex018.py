from math import sin, cos, tan, radians

num = float(input('Digite um ângulo: '))

print('O seno deste ângulo é: {:.2f}'.format(sin(radians(num))))
print('O cosseno deste ângulo é: {:.2f}'.format(cos(radians(num))))
print('A tangente deste ângulo é: {:.2f}'.format(tan(radians(num))))

