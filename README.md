# Binary-and-Linear-Search

## Overview
This project showcases the implementation of two fundamental searching algorithms in computer science: **Binary Search** and **Linear Search**. These algorithms are designed to efficiently locate a target value within an array or list, with each method demonstrating different approaches and time complexities.

---

## Purpose of the Code
The aim of this code is to deliver straightforward and effective implementations of search algorithms tailored for a DSA lab project. 

---

## How to Run the Program
1. Copy the code into your preferred IDE or text editor (e.g., VS Code, PyCharm, etc.).
2. Save the file with a `.py` extension (e.g., `search_algorithms.py`).
3. Run the script using Python:
   ```bash
   python search_algorithms.py
   ```

---

## Features

### Binary Search
- **Description**: Efficient searching algorithm that divides a sorted array into halves to locate the target value.
- **Requirements**: The input array must be sorted.
- **Steps**:
  1. Compare the target value to the middle element of the array.
  2. Narrow the search range to the left or right half based on the comparison.
  3. Repeat until the value is found or the range is empty.

### Linear Search
- **Description**: A straightforward algorithm that iterates through each element of the array to find the target value.
- **Requirements**: Works with both sorted and unsorted arrays.
- **Steps**:
  1. Traverse the array from the beginning.
  2. Check each element against the target value.
  3. Stop when the value is found or the end of the array is reached.

---

## Time Complexity

### Linear Search
- **Best Case**: \( O(1) \) - If the target is the first element.
- **Worst Case**: \( O(n) \) - If the target is the last element or not present in the array.

### Binary Search
- **Best Case**: \( O(1) \) - If the middle element matches the target.
- **Worst Case**: \( O(\log n) \) - For sorted arrays, the search range is halved on each iteration.

---

## Example Scenarios

### Binary Search
#### Input:
```python
My_Array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
My_Target = 15
```
#### Output:
```
Value 15 found at index 7
```

### Linear Search
#### Input:
```python
My_Numbers = [3, 7, 2, 9, 5]
Search_Value = 9
```
#### Output:
```
Value 9 is located at index 3
```

---

## LinkedIn Post
Read more about my coding journey and these algorithms on my LinkedIn post(https://www.linkedin.com/posts/muzzammil-hussain-13595a347_binarysearch-linearsearch-codingjourney-activity-7286651687996375040-NMho?utm_source=share&utm_medium=member_android).

