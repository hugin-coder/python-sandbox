def say1(name, msg1="Hello there", msg2="How are you"):
    print(f'{msg1} {name}! {msg2}?')


def say2(*args):
    print(args[0], args)


say1("Olaf")
say1("Olaf", "Shalom")
say1("Olaf", "Shalom", "my friend")
say1("Olaf", msg2="do you play minecraft")
say1(msg2="do you play minecraft", name="Olaf")
say1("Wally")
say1("Wally", msg2="do you play minecraft", msg1="Guddæ")
h = "800kr"
say2(h, 45, 50, 55, 60, 65, 70, 75, 80, 85)