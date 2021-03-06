from Add_Param import Add_P, Add_S
from check import check_num


def params(number):
    match number:
        case 1:
            def par1(data, position, name):
                Add_S(name, "string")
                # print("".join(list(map(chr, data[0:2]))))
                a = "".join(list(map(chr, data[position:position + 2])))
                if check_num(a) == -1:
                    return -1
                a = int(a)
                if a > 19 or a < 1:
                    return -1
                return a

            return par1
        case 2:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[2:2 + position])))
                if check_num(a) == -1:
                    return -1
                Add_P(name, "PAN", a)
                # print("".join(list(map(chr, data[2:2 + position]))))
                pos = position + 2
                return pos

            return par1
        case 3:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:6 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:6 + position]))))
                pos = position + 6
                return pos

            return par1
        case 4:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:12 + position])))
                if check_num(a) == -1:
                    return -1
                Add_P(name, "Amount_transaction", a)
                # print("".join(list(map(chr, data[position:12 + position]))))
                pos = position + 12
                return pos

            return par1
        case 5:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:12 + position])))
                if check_num(a) == -1:
                    return -1
                Add_P(name, "Amount_settlement", a)
                # print("".join(list(map(chr, data[position:12 + position]))))
                pos = position + 12
                return pos

            return par1
        case 6:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:12 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:12 + position]))))
                pos = position + 12
                return pos

            return par1
        case 9:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:8 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:8 + position]))))
                pos = position + 8
                return pos

            return par1
        case 11:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:6 + position])))
                if check_num(a) == -1:
                    return -1
                Add_P(name, "Systems_trace_audit_number", a)
                # print("".join(list(map(chr, data[position:6 + position]))))
                pos = position + 6
                return pos

            return par1
        case 12:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:12 + position])))
                if check_num(a) == -1:
                    return -1
                Add_P(name, "Time_Local_transaction", a)
                # print("".join(list(map(chr, data[position:12 + position]))))
                pos = position + 12
                return pos

            return par1
        case 14:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:4 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:4 + position]))))
                pos = position + 4
                return pos

            return par1
        case 16:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:4 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:4 + position]))))
                pos = position + 4
                return pos

            return par1
        case 17:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:4 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:4 + position]))))
                pos = position + 4
                return pos

            return par1
        case 22:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:12 + position]))))
                pos = position + 12
                return pos

            return par1
        case 23:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:3 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:3 + position]))))
                pos = position + 3
                return pos

            return par1
        case 24:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:3 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:3 + position]))))
                pos = position + 3
                return pos

            return par1
        case 26:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:4 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:4 + position]))))
                pos = position + 4
                return pos

            return par1
        case 28:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:6 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:6 + position]))))
                pos = position + 6
                return pos

            return par1
        case 29:
            def par1(data, position, name):
                a = "".join(list(map(chr, data[position:3 + position])))
                if check_num(a) == -1:
                    return -1
                # print("".join(list(map(chr, data[position:3 + position]))))
                pos = position + 3
                return pos

            return par1
        case 31:
            def par1(data, position, name):
                a = list(map(chr, data[position:2 + position]))
                if check_num(a) == -1:
                    return -1
                a = int(a[0] + a[1])
                if a>23 or a<0:
                    return -1
                b = "".join(list(map(chr, data[position + 2:a + position + 2])))
                if check_num(b) == -1:
                    return -1
                # print("??????????", a, end=" ")
                # print("".join(list(map(chr, data[position + 2:a + position + 2]))))
                pos = position + a + 2
                return pos

            return par1
        case 32:
            def par1(data, position, name):
                a = list(map(chr, data[position:2 + position]))
                if check_num(a) == -1:
                    return -1
                a = int(a[0] + a[1])
                if a>11 or a<0:
                    return -1
                b = "".join(list(map(chr, data[position + 2:a + position + 2])))
                if check_num(b) == -1:
                    return -1
                # print("??????????", a, end=" ")
                # print("".join(list(map(chr, data[position + 2:a + position + 2]))))
                pos = position + a + 2
                return pos

            return par1
        case 33:
            def par1(data, position, name):
                a = list(map(chr, data[position:2 + position]))
                if check_num(a) == -1:
                    return -1
                a = int(a[0] + a[1])
                if a > 11 or a < 6:
                    return -1
                b = "".join(list(map(chr, data[position + 2:a + position + 2])))
                if check_num(b) == -1:
                    return -1
                # print("??????????", a, end=" ")
                # print("".join(list(map(chr, data[position + 2:a + position + 2]))))
                pos = position + a + 2
                return pos

            return par1
        case 37:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:12 + position]))))
                pos = position + 12
                return pos

            return par1
        case 38:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:6 + position]))))
                pos = position + 6
                return pos

            return par1
        case 41:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:8 + position]))))
                pos = position + 8
                return pos

            return par1
        case 42:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:15 + position]))))
                pos = position + 15
                return pos

            return par1
        case 43:
            def par1(data, position, name):
                a = list(map(chr, data[position:2 + position]))
                if check_num(a) == -1:
                    return -1
                a = int(a[0] + a[1])
                if a<20:
                    return -1
                # print("??????????", a, end=" ")
                # print("".join(list(map(chr, data[position + 2:a + position + 2]))))
                Add_P(name, "Card_acceptor_name_location", "".join(list(map(chr, data[position + 2:a + position + 2]))))
                pos = position + a + 2
                return pos

            return par1
        case 49:
            def par1(data, position, name):
                Add_P(name, "Currency_code_transaction", "".join(list(map(chr, data[position:3 + position]))))
                # print("".join(list(map(chr, data[position:3 + position]))))
                pos = position + 3
                return pos

            return par1
        case 50:
            def par1(data, position, name):
                Add_P(name, "Currency_code_settlement", "".join(list(map(chr, data[position:3 + position]))))
                # print("".join(list(map(chr, data[position:3 + position]))))
                pos = position + 3
                return pos

            return par1
        case 51:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:3 + position]))))
                pos = position + 3
                return pos

            return par1
        case 55:
            def par1(data, position, name):
                a = list(map(chr, data[position:3 + position]))
                if check_num(a) == -1:
                    return -1
                a = int(a[0] + a[1] + a[2])
                # print("??????????", a, end=" ")
                # print("".join(list(map(chr, data[position + 3:a + position + 3]))))
                Add_P(name, "EMV_DATA", "".join(list(map(chr, data[position + 3:a + position + 3]))))
                pos = position + a + 3
                return pos

            return par1
        case 63:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:16 + position]))))
                pos = position + 16
                return pos

            return par1
        case 71:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:8 + position]))))
                pos = position + 8
                return pos

            return par1
        case 72:
            def par1(data, position, name):
                a = list(map(chr, data[position:3 + position]))
                if check_num(a) == -1:
                    return -1
                a = int(a[0] + a[1] + a[2])
                # print("??????????", a, end=" ")
                # print("".join(list(map(chr, data[position + 3:a + position + 3]))))
                pos = position + a + 3
                return pos

            return par1
        case 90:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:42 + position]))))
                pos = position + 42
                return pos

            return par1
        case 93:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:5 + position]))))
                pos = position + 5
                return pos

            return par1
        case 94:
            def par1(data, position, name):
                # print("".join(list(map(chr, data[position:7 + position]))))
                pos = position + 7
                return pos

            return par1
        case 100:
            def par1(data, position, name):
                a = list(map(chr, data[position:2 + position]))
                a = int(a[0] + a[1])
                # print("??????????", a, end=" ")
                # print("".join(list(map(chr, data[position + 2:a + position + 2]))))
                pos = position + a + 2
                return pos

            return par1
        case 123:
            def par1(data, position, name):
                a = list(map(chr, data[position:3 + position]))
                a = int(a[0] + a[1] + a[2])
                # print("??????????", a, end=" ")
                # print("".join(list(map(chr, data[position + 3:a + position + 3]))))
                pos = position + a + 3
                return pos

            return par1


def bytes_data(data):
    s = ""
    for i in range(len(data)):
        string = str(bin(data[i]))[2:]
        s += "0" * (8 - len(string))
        s += string
    return s


def cut(mask, data, name):
    pos = 0
    bytes_mask = bytes_data(mask)
    funcs_names = [i for i in range(1, 129)]
    lst = [params(i) for i in funcs_names]
    for i, elem in enumerate(bytes_mask):
        if int(elem) == 1 and i <= 55:
            pos = lst[i](data, pos, name)
            if pos == -1:
                return -1
    return 1


def parser(file_name, name):
    f = open(file_name, 'rb')
    lines = f.readlines()
    i = 0
    n = len(lines)
    while i < n:
        a = lines[i]
        a = list(map(int, a))
        if a[0] == 49 and a[1] == 50 and a[2] == 52 and a[3] == 48:
            mask = a[4:20]
            data = a[20:]
            c = cut(mask, data, name)
            if c == -1:
                f.close()
                return -1
        i += 1
    f.close()
