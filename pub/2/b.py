with open("input.txt", "r") as f:
    ranges = f.read().split(",")

r = [i.split("-") for i in ranges]

def check(num):
    valid = False
    c = int(len(num) / 2)
    for window_size in range(1, c + 1):
        if len(num) % window_size == 0:
            first = num[0:window_size]
            sub_valid = True
            for window_index in range(len(num) // window_size):
                if num[window_size * window_index:window_size * (window_index + 1)] != first:
                    sub_valid = False

            if sub_valid:
                valid = True

    return valid

count = 0

for low, high in r:
    for i in range(int(low), int(high) + 1):
        if check(str(i)):
            count += i
            
count