def input_int(text):
    try:
        return int(input(text + ": "))
    except ValueError:
        print("Hattar var ikki eitt heiltal")
        return input_int(text)


def input_int_between(min, max):
    while True:
        result = input_int(f'Vel eitt tal millum {min} og {max}!')
        if min <= result <= max:
            return result
        print(f'Talið skal verða millum {min} og {max}!')


def input_float(text):
    try:
        return float(input(text + ": ").replace(',', '.'))
    except ValueError:
        print("Hattar var ikki eitt kommatal")
        return input_float(text)
