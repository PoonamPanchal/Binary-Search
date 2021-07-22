def binary_search(arr, low, high, x):
    if high >= low:
        mid =(high + low)//2
        
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid + 1,high,x)
    else:
        return -1

n=int(input("Enter number of elements in array"))
arr=list(map(int,input("Enter array element: ").strip().split()))[:n]
arr.sort()
print("your array is: ",arr)

x=int(input("enter the element you want to search"))
result=binary_search(arr,0,len(arr)-1,x)
if result != -1:
    print("Element {} found at index [{}]".format(x,result))
else:
    print("sorry, Element not found")



