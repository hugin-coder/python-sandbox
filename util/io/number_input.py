def __input_between(n_min, n_max, is_int: bool):
    num_type = 'heiltal' if is_int else 'kommatal'
    text = f'Vel eitt {num_type} millum {n_min} og {n_max}!'
    while True:
        result = input_int(text) if is_int else input_float(text)
        if n_min <= result <= n_max:
            return result
        print(f'Talið skal verða eitt {num_type} millum {n_min} og {n_max}!')


def input_int(text: str):
    try:
        return int(input(text + ": "))
    except ValueError:
        print("Hattar var ikki eitt heiltal")
        return input_int(text)


def input_float(text: str):
    try:
        return float(input(text + ": ").replace(',', '.'))
    except ValueError:
        print("Hattar var ikki eitt kommatal")
        return input_float(text)


def input_int_between(n_min: int, n_max: int):
    return __input_between(n_min, n_max, True)


def input_float_between(n_min: float, n_max: float):
    return __input_between(n_min, n_max, False)
