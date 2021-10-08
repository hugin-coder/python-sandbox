def __input_between(nMin, nMax, int):
    numType = 'heiltal' if int else 'kommatal'
    text = f'Vel eitt {numType} millum {nMin} og {nMax}!'
    while True:
        result = input_int(text) if int else input_float(text)
        if nMin <= result <= nMax:
            return result
        print(f'Talið skal verða eitt {numType} millum {nMin} og {nMax}!')


def input_int(text):
    try:
        return int(input(text + ": "))
    except ValueError:
        print("Hattar var ikki eitt heiltal")
        return input_int(text)


def input_float(text):
    try:
        return float(input(text + ": ").replace(',', '.'))
    except ValueError:
        print("Hattar var ikki eitt kommatal")
        return input_float(text)


def input_int_between(nMin, nMax):
    return __input_between(nMin, nMax, True)


def input_float_between(nMin, nMax):
    return __input_between(nMin, nMax, False)
