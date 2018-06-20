a = float(input('Спожита вода в кубометрах: '))
if a >= 0 and a <= 30:
    b = a * 9.86
elif a > 30 and a <= 50:
    c = a - 30
    b = (c * 11.22) + (30 * 9.86)
elif a > 50:
    c = a - 30 - 50
    b = (c * 17.89) + (30 * 9.86) + (50 * 11.22)
else:
    print('Error')
b += 20
print('Рахунок: {0} грн.'.format(b))