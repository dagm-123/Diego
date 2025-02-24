print('Impresión de la suma de los números actuales y anteriores en un rango (10)')
num0 = 0
for num1 in range(10):
    print('Número actual',num1, 'Número anterior', num0,  'suma' ,'=', num1 + num0)
    num0 = num1