your_pin = int(input("Please choose your secret 4 digit pin: "))
pin = 0000
while your_pin != pin:
    s = f'{pin:04}'
    print(s)
    pin += 1

else:
    #formating int into string so leading zeros can print
    secret_pin = f'{your_pin:04}'
    print("YOur secret pin is {}".format(secret_pin))
