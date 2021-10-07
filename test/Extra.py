util.io.number_input.input_int('')
number_input.input_float('')

for i in range(5):
    number = int(input('Enter a number: '))
    print(number)
    if number < 0:
        print('That is a negative number')
    elif number > 0 and number != 21: #Tal er størri enn 0 og er ikki 21
        print('That is a postitive number')
    if number == 21:
        print('You found the secret number!')
        break



