import math
print('Введите значения a, b, c')
a=float(input('Введите коэффициент а',))
b=float(input('Введите коэффициент b',))
c=float(input('Введите коэффициент c',))
d=(b**2)-(4*a*c)
if d<0:
    print('Корней уравнения нет')
elif d>0:
    n=(math.sqrt(d)-b)/(2*a)
    m=(-math.sqrt(d)-b)/(2*a)
    print('Первый корень равен ','%.4f'%n)
    print('Второй корень равен ','%.4f'%m)
elif d==0:
    n=(-b)/(2*a)
    print('Корень равен ','%.4f'%n)
input()