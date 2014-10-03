def fizzbuzz(n):
    s = ""
    if n % 3 == 0: s += "fizz"
    if n % 5 == 0: s += "buzz"
    if s == "": s += str(n)
    return s

for i in range(1, 101):
    print(fizzbuzz(i))