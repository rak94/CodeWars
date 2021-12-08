def square(num):
    num = str(num)
    result = ""
    for i in num:
        result += str(int(i)**2)
    return int(result)