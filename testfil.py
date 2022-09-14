while True:
    num_1 = input("Skriv inn et tall:")
    symbol = input("Skriv in ett symbol")
    num_2 = input("Skriv inn et tall:")

    print(f"{num_1} {symbol} {num_2} = {eval(num_1 + symbol + num_2)}")