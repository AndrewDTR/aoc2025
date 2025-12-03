with open("input.txt", "r") as f:
    nums = f.read().splitlines()

inner_nums = [[int(j) for j in i] for i in nums]
res = 0

for line in inner_nums:
    # yeah it's a brute force but i want my medals and it runs in < 1s

    max_num = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            max_num = max(max_num, int(str(line[i]) + str(line[j])))
    
    res += max_num
            
res