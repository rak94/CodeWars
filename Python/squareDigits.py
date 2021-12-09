def square(num):
    result = ""
    for i in str(num):
        result += str(int(i)**2)
    return int(result)

print(square(2912))