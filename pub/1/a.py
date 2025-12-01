zero = 0
dial = 50

for rotation in puz:
    direction, magnitude = rotation[0], int(rotation[1:])

    if direction == "L":
        dial -= magnitude
    else:
        dial += magnitude

    dial %= 100

    if dial == 0:
        zero += 1

zero