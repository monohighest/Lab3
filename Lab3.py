
"""
EXERCISE 2 REQUIREMENTS (Table 3):

REQ-01: If < 10 numbers are entered and "SORT_ASCENDING" is passed to the
        function "bubble_sort()", then the function returns the list of numbers
        sorted in ascending order.

REQ-02: If < 10 numbers are entered and "SORT_DESCENDING" is passed to the
        function "bubble_sort()", then the function returns the list of numbers
        sorted in descending order.

REQ-03: If >= 10 numbers are entered, the function "bubble_sort()" shall
        return the integer value 1

REQ-04: If 0 numbers are entered, the function "bubble_sort()" shall
        return the integer value 0

REQ-05: If any of the values entered on the command line console are not
        integers, the function "bubble_sort()" shall return the integer value 2

TASKS:
(a) Update Table 3 column "PyTest Function/s" for existing test cases
(b) Implement missing Unit Test Cases in Test_Lab3.py for requirements without tests
(c) Update Python code if requirements are not implemented or implemented differently
(d) Execute all PyTest cases and verify all requirements pass
"""
SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    for item in arr_result:
        if type(item) != int:
            return 2


    # Get number of elements in the list
    n = len(arr_result)

    if n == 0: 
        return 0

  
    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array
                    arr_result = []
    else:
        arr_result = 1


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