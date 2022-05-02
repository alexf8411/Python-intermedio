def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return string  == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        print(palindrome(""))
    except TypeError:
        print("Solo se admiten cadenas de caracteres")


if __name__ == '__main__':
    run()
