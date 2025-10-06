print("")
print("")

balance = float(input("balance starting point: "))
a = int(input("how many trades do you want: "))
b = float(input("how many percent you want to risk on winning: "))

for i in range(0, a) :
    x = balance * b / 100
    balance += x


print(f"your profit will be ${balance:.2f} with 0 loses")