def run():
    #dar como resultado el cuadrado de los umeros que no son divisibles entre 3
    # squares = []
    # for i in range(1, 101): #el range tiene el parametro 101 de manera no inclusiva
    #     if  i%3 != 0: #divisibles entre 3
    #         squares.append(i**2) saca el cuadrado


#Es lo mismo de arriba [element for element in interable if condicition]

#para cada elemento en el iterable voy a guardar ese elemento solo se si se cumple la condicion  
    squares = [i**2 for i in range(1, 101) if i % 3 != 0] 
    print(squares)
# [element for element in iterable if condition] 
#Element cada uno de los elementos  a poner en la nueva lista -- voy a guardar esa i elevada al cuadrado 
#ciclo a partir  del cial se extraen los elementos de otra lista o cualquier iterable -- para cada i que va en el rango de 1 a 101
#Condicion opcional para los filtros del ciclo -- solo si la i mod 3 es distinto de 0

#lista de todos los mutiplos de 4 que a su vez tambien son multiplos de 6 y  de 9 hasta 100000

    challenge = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(challenge)




if __name__ == '__main__':
    run()