
def binaryToDecimal(num):
    bits = list(num)
    decimal_value = 0
    count = 0

    for i in reversed(bits):
        decimal_value += 2**count * int(i)
        count = count + 1
    return decimal_value


def decimalToBinary(num):
    list_binary = [0,0,0,0,0,0,0,0]
    length = len(list_binary)-1
    while int(num) > 0:
        r = int(num) % 2
        if r != 0:
            list_binary[length] = 1
        length = length-1
        num = int(num) // 2
    binary_value = ''.join(str(i) for i in list_binary)
    return binary_value


            


