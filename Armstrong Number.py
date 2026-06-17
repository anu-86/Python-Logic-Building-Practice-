# Armstrong Number

n = int(input())
original = n
total = 0
while n > 0:
    digit = n % 10
    total = total + digit ** 3
    n = n // 10
if original == total:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
