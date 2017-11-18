def get_summ(one, two, delimeter=' '):
	sum_str = str(one) + str(delimeter) + str(two)
    return (sum_str.upper())
my_one = input('Введите первое число:')
my_two = input('Введите второе число:')
print (get_sum(my_one, my_two))