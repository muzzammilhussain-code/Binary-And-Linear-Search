def Search_Linear(array, value):
    for index in range(len(array)):
        if array[index] == value:
            return index
    return -1

My_Numbers = [3, 7, 2, 9, 5]
Search_Value = 9

Search_Result = Search_Linear(My_Numbers, Search_Value)

if Search_Result != -1:
    print(f"Value {Search_Value} is located at index {Search_Result}")
else:
    print(f"Value {Search_Value} is not present in the array")
