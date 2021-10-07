import random
import const
import util

maxGuess = int(input("hvussu ofta vil tú gita: "))
counter = 0
secret = int(random.random() * (const.MAX_NUM + 1))
go = True
while go and counter < maxGuess:   
    number = util.input_int_between(const.MIN_NUM, const.MAX_NUM)
    if number < secret:
        print("Ov lágt!")
    elif number > secret:
        print("Ov høgt!")
    else:
        go = False
    counter = counter + 1
    if go:
        print(f'Tú hevur {maxGuess - counter} ferðir eftir at gita')
        
if go:
    if counter == maxGuess:
        print("Tú vann ikki ;(")
        print("Rætta talið var:", secret)
else:
    print("TÚ HEVUR VUNNI JA!")
    print("Tú gitti", counter, "ferðir")
