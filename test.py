def array_manipulate(arr):
    new_arr = []
    i = 0
    while i <len(arr):
        num = arr[i]
        mul = 1
        while num >0:
            mul = mul*(num%10)
            num = num//10
        new_arr.append(mul)
        mul = 1
        i+=1
    return new_arr

print(array_manipulate([212,2135869,456,789,12345]))
