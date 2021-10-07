def input_int(text):
    try:
        return int(input(text + ": "))
    except ValueError:
        print("Hattar var ikki eitt tal")
        return input_int(text)
    
def input_int_between(min, max):
    while True:
        result = input_int(f'Vel eitt tal millum {min} og {max}!')
        if result >= min and result <= max:
            return result
        print(f'Talið skal verða millum {min} og {max}!')
