
def adder(num1,num2):
    a = []
    b = []

    for i in range(0, len(list(num1))):
        a.append(int(num1[i]))
    for i in range(0, len(list(num2))):
        b.append(int(num2[i]))
  
    while(len(a) != 8):
        a.insert(0,0)

    while(len(b) != 8):
        b.insert(0,0)
        

    carry_in = 0
    carry = []
    sum_bin = []

    for i in range(len(a)-1,-1,-1):
        sum = carry_in ^ (a[i] ^ b[i])
        sum_bin.insert(0,sum)
        
        carry_out = (a[i]&b[i])| (b[i]&carry_in) | (a[i]&carry_in)
        carry.insert(0,carry_out)
        carry_in = carry_out

    return ''.join(str(i) for i in sum_bin)




