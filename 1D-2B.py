a = float(input('Введіть магнітуду: '))
if a <= 2.0 and a >= 0:
	print('Мікро')
elif a >= 2.0 and a <= 3.0 :
	print('Дуже слабкий')
elif a >= 3.0 and a <= 4.0 :
	print('Слабкий')
elif a >= 4.0 and a <= 5.0 :
	print('Легкий')
elif a >= 5.0 and a <= 6.0 :
	print('Помірний')
elif a >= 6.0 and a <= 7.0 :
	print('Сильний')
elif a >= 7.0 and a <= 8.0 :
	print('Дуже сильний')
elif a >= 8.0 and a <= 10.0 :
	print('Великий')
elif a >= 10.0 :
	print('Рідкісно великий')
else:
    print("Введіть коректне число")

