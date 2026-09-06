a = [10,20,30,40,50,89,93,99]
key = 50
start = 0
end = len(a)-1
while start <= end:
    mid = (start+end)//2
    if a[mid] == key:
        print(f"your key:{key} is found at index {mid}")
        break
    elif key<a[mid]:
        end = mid-1
        
    else:
        start = mid+1
else:
    print("key is not present in list")
        