with open("input.txt", "r") as f:
    nums = f.read().splitlines()

inner_nums = [[int(j) for j in i] for i in nums]
total_sum = 0

for case in inner_nums:
    case_idx_enum = enumerate(case)
    case_idx = [(j, i) for i, j in case_idx_enum]
    case_idx.sort(key=lambda x: (x[0], -x[1]))
    real = [i for i in reversed(case_idx)]
    
    res = []
    main_idx = 0
        
    while len(res) < 12:
        curr_val = case[main_idx]
        for idx, (listVal, listIdx) in enumerate(real):
            if listVal > curr_val and main_idx < listIdx <= (len(case) - (12 - len(res))):
                main_idx = listIdx
                real.pop(idx)
                break
                
        res.append(case[main_idx])
        main_idx += 1
        
    total_sum += int("".join([str(i) for i in res]))

total_sum