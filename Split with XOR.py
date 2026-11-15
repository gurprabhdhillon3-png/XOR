numbers=[2,4,7,9,2,4]
xor_result=0
for num in numbers:
    xor_result=xor_result^num
    print("XOR of unique numbers: ", xor_result)
mask=1
while(xor_result & mask)==0:
    mask=mask<<1
print("Rightmost set bit: ", mask)
first=0
second=0
for num in numbers:
    if(num & mask)!=0:
        first=first^num
    else:
        second=second^num
        print("First unique number: ", first)
        print("Second unique number: ", second)
