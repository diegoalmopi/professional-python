import os

def decorator(func):
    def wrapper():
        os.system('clear')
        print('❤❤❤                                                     ⭐⭐⭐')
        func()

    return wrapper    


@decorator
def gereetings():
    greeting = input('intruduce tu nombre: ')
    print('hola un gusto conocerte', greeting.capitalize(), 'nos alegra mucho conocerte')


def run():
    gereetings()


if __name__=='__main__':
    run()