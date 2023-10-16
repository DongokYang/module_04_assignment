while  True:
    num_1, num_2 = input().split()
    total = 0
    for char in num_1:
        for char_2 in num_2:
            total += int(char)*int(char_2)
    print(total)