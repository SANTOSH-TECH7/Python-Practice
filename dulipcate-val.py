arr = [2, 3, 1, 2, 3]
arr.sort()
arr_new=[]
for i in range (len(arr)-1):
    if arr[i]==arr[i+1]:
        if arr[i] not in arr_new:
            arr_new.append((arr[i]))
print(", ".join (map(str,arr_new)))