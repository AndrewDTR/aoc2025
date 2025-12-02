with open("input.txt", "r") as f:
    ranges = f.read().split(",")

r = [i.split("-") for i in ranges]

def check(num):
    if num[0] == "0": return False
    n = len(num)
    if n % 2 != 0:
        return False

    s = n // 2


    return num[0:s] == num[s:]

count = 0

for low, high in r:
    for i in range(int(low), int(high) + 1):
        if check(str(i)):
            count += i
            
count   