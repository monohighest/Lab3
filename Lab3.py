print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 1
SORT_DESCENDING = 2


def bubble_sort(arr, sorting_order):
    
    # REQ-05: If any of the values entered are not integers, return 2
    if not all(isinstance(item, int) for item in arr):
        return 2

    # REQ-04: If 0 numbers are entered, return 0
    if len(arr) == 0:
        return 0

    # REQ-03: If >= 10 numbers are entered, return 1
    if len(arr) >= 10:
        return 1

    # Copy input list to results list
    arr_result = arr.copy()
    n = len(arr_result)

    # Traverse through all array elements
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

            else:
                # Return an empty array for invalid sorting order
                return []

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

if __name__ == "__main__":
    main()