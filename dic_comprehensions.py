def run():
    my_dic = {}

    for i in range(1, 101):
        if i % 3 != 0:
            my_dic[i] = i**3

    print(my_dic)

    my_dic1 = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dic1)

if __name__ == '__main__':
    run()