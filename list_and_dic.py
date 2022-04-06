def run():
    my_list = [1, "Hola", True, 3.14]
    my_dic = {"firstname": "Alex", "lastname": "Fonseca"}

    super_list = [
        {"firstname": "Jose", "lastname": "Fonseca"},
        {"firstname": "Carmen", "lastname": "Rodriguez"},
        {"firstname": "Alex", "lastname": "Fonseca"},
        {"firstname": "Alejandra", "lastname": "Fonseca"},
        {"firstname": "Katherine", "lastname": "Fonseca"}
    ]

    supper_dic = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
         "floating_nums": [1.1, 1.2, 1.3, 1.4]
    }

    for key, value in supper_dic.items():
        print(key, ("-"), value)

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

if __name__=='__main__':
    run()