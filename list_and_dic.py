def run(): # definir una funcion principal
    #listas y diccionarios son mutables
    my_list = [1, "Hola", True, 3.14] # se crea la lista
    my_dic = {"firstname": "Samy", "lastname": "Fonseca"} # se crea diccionario

#una lista que contiene diccionarios
    super_list = [
        {"firstname": "Jose", "lastname": "Fonseca"},
        {"firstname": "Carmen", "lastname": "Rodriguez"},
        {"firstname": "Alex", "lastname": "Fonseca"},
        {"firstname": "Alejandra", "lastname": "Fonseca"},
        {"firstname": "Katherine", "lastname": "Fonseca"}
    ]

#un diccionario que contiene varias listas cada uno con una llave y un valor
    super_dic = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 1.2, 1.3, 1.4]
    }

    for key, value in super_dic.items(): #Se recorre las llaves y valores de un diccionario por medio del metodo items
        print(key, ("-"), value)

# recorrer la lista con la variable values
    for values in super_list:
        for key, value in values.items(): #recorre el diccionario presente en cada item de la lista 
            print(f'{key} - {value}')

if __name__=='__main__': #entry point punto de entrada que incia la fucnion cuando se ejecuta el archivo de python 
    run()