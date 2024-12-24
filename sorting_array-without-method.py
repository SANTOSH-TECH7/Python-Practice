arr = [2, 3, 1, 2, 3]
arr_new=[]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
         if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            arr_new.append(arr[j])#saves swaped elements in it , whenever the swap accours then it saves
            
print(arr)
print(arr_new)#prints swapped elements        