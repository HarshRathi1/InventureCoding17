'''This function helps in finding the maximum element in the array. Execute this function to print the maximum element in the array with its index.
Assumptions
The index in the array for all the elements starts at 0.
The maximum element is in a different line in the output.
There has to be only one maximum element.
The function prints only what is required.
Example
Input:
23 45 82 27 66 12 78 13 71 86
Output:
86
9'''
def MaxInArray(arr,length):
        m=arr[0]
        for i in arr:
            if i>m:
                m=i
        print(m)
        return arr.index(m)
arr=list(i for i in input().split())
length=len(arr)
print(MaxInArray(arr,length))