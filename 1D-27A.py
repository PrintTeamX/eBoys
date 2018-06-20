i1 = float(input("Яка зараз година?(1-24) \n"))
i2 = float(input("Чи говорить попугай?(1 - Tak, 2 - Hi) \n"))
if  i2 == 1 and (i1 <= 8 or i1 == 22 or i1 == 23 or i1 == 24):
	print ("Накрити ковдрою")
else:
	print("Не накривати ковдрою")