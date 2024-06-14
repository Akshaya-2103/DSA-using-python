#find a value in the list whithout using membership identities.(Linear search)

arr = input("Enter the list of numbers seperated by spaces:").split()
arr = [int(x) for x in arr]

target = int(input("Enter the target value to search:"))

found = False
for i in range(len(arr)):
    if arr[i]==target:
        print(f"Target {target} found at index {i}")
        found = True
        break

if not found:
    print(f"Target {target} not found in the array.")

#Enter the list of numbers seperated by spaces:1 4 8 6 9
#Enter the target value to search:6
#Target 6 found at index 3