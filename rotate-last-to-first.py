arr = [1,2,3,4,5]
last_ele=arr[-1]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=last_ele
print(arr)