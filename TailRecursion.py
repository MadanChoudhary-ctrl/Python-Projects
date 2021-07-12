def recursive(num):
    if num <= 0:
        return 0
    else:
        return num + recursive(num-1)


def non_recursive(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum

for i in range(3):
    num = int(input("num: "))
    print(f"recursive: {recursive(num)}")
    print(f"non-recursive: {non_recursive(num)}")
    print()
