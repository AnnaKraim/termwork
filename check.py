def check_num(s):
    for i in s:
        if i < "0" or i > "9":
            if i != "X" and i != " ":
                return -1
    return 1
