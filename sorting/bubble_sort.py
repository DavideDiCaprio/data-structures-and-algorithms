def bubble_sort(arr: list) -> None:
    """
    Bubble Sort.
    
    Args:
        arr: list
    """
    n: int = len(arr)
    
    for i in range(n - 1):
        swapped: bool = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break