def Binary_Search(a, target_value):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == target_value:
            return mid
        
        if a[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1

    return -1

My_Array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
My_Target = 15

result = Binary_Search(My_Array, My_Target)

if result != -1:
    print("Value",My_Target,"found at index", result)
else:
    print("Target not found in array.")