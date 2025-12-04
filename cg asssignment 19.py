def sort_list(numbers):
    """
    Sorts a list of numbers in ascending order.

    Parameters:
    numbers (list): A list of numbers

    Returns:
    list: A new list containing the same numbers sorted in ascending order
    """
    return sorted(numbers)

# Example usage:
my_list = [5, 2, 9, 1, 7]
sorted_list = sort_list(my_list)
print("Sorted list:", sorted_list)