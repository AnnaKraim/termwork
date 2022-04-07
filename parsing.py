from findmask import find_mask
def params(number):
    match number:
        case 1:
            def par1(bytes_data,data):
                print(number)
            return par1
        case 2:
            def par1(bytes_data, data):
                print(number)
            return par1
        case 3:
            def par1(bytes_data, data):
                print(number)
            return par1
        case 4:
            def par1(bytes_data, data):
                print(number)
            return par1
        case 5:
            def par1(bytes_data, data):
                print(number)
            return par1
        case 6:
            def par1(bytes_data, data):
                print(number)
            return par1
        case 9:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 11:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 12:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 14:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 16:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 17:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 22:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 23:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 24:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 26:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 28:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 29:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 31:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 32:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 33:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 37:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 38:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 41:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 42:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 43:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 49:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 50:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 51:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 55:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 63:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 71:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 72:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 90:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 93:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 94:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 100:
            def par1(bytes_data, data):
                print(number)

            return par1
        case 123:
            def par1(bytes_data, data):
                print(number)

            return par1
def bytes(data):
    s = ""
    for i in range(len(data)):
        string = str(bin(data[i]))[2:]
        s += "0" * (8 - len(string))
        s += string
    return s
def cut(mask,data):
    bytes_mask = bytes(mask)
    bytes_data = bytes(data)
    funcs_names = [i for i in range(1,129)]
    lst = [params(i) for i in funcs_names]
    for i,elem in enumerate(bytes_mask):
        print(i,elem)
        if int(elem)==1:
            lst[i](bytes_data,data)
def parser(file_name):
    f = open(file_name, 'rb')
    lines = f.readlines()
    i = 0
    n = len(lines)
    while i < n:
        a = lines[i]
        a = list(map(int,a))
        if a[0]==49 and a[1] == 50 and a[2] == 52 and a[3] == 48:
            mask = a[4:20]
            data = a[20:]
            cut(mask,data)
        i+=1
    f.close()
parser("/Users/annakraim/Downloads/TZ_Clearing/ic201121.001")