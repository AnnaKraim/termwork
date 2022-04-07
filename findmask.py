def find_mask():
    file_name = "/Users/annakraim/Downloads/TZ_Clearing/ic201121.001"
    f = open(file_name, 'rb')
    a = f.readline()
    a = list(map(int,a))
    while not(a[0]==49 and a[1] == 50 and a[2] == 52 and a[3] == 48):
        a = f.readline()
        a = list(map(int, a))
    a = a[4:20]
    s = ""
    for i in range(len(a)):
        string = str(bin(a[i]))[2:]
        s+="0"*(8-len(string))
        s+=string
    f.close()
    return s