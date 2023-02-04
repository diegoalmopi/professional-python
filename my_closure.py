# Hola 3 -> HolaHolaHola

def make_repeater_of(n):

    def repeater(string):
        assert type(string) == str, 'Solo cadenas'
        return string*n
    return repeater

#This closure returns a function that returns the division
#of an x number by n
def make_division_by(n):
    def dividendo(x):
        return x/n
    return dividendo

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))

    division_by_2 = make_division_by(2)
    print(division_by_2(20))
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

if __name__ == '__main__':
    run()