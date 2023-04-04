import math

def run():


    my_dic = {}
#guardar en la llaves del diccionario solamenete los numeros que no sean divisibles en 3 hsdts el 100
#    for i in range(1, 101):
#        if i % 3 != 0:
#            my_dic[i] = i**3

    print(my_dic)
# pone como valor del diccionario en corchetes i como llave los dos puntos : i**3 como valor , el rango y las condiciones
#    my_dic1 = {i: i**3 for i in range(1, 101) if i % 3 != 0}
#    print(my_dic1)    
    
#{key:value for value in iterable if condition}

#Dictionary comprehension con un diccionario cuyas llaves sean los 1000 primeros numeros naturales con sus 
#raices cuadradas como valores    

my_dic2 = {i:round((math.sqrt (i)), 2) for i in range(1, 1001)}
print(my_dic2)

if __name__ == '__main__':
    run()
    
