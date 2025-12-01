zero = 0
dial = 50

for rotation in puz:
    direction, magnitude = rotation[0], int(rotation[1:])
    step = -1 if direction == "L" else 1

    for i in range(magnitude):
        dial = (dial + step) % 100
        if dial == 0:
            zero += 1

zero