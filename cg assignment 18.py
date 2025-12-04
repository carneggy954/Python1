def concat_tuples(tuple1, tuple2):
    """
    Concatenates two tuples and returns a new tuple.

    Parameters:
    tuple1 (tuple): The first tuple
    tuple2 (tuple): The second tuple

    Returns:
    tuple: A new tuple containing elements from both input tuples
    """
    return tuple1 + tuple2

# Example usage:
t1 = (1, 2, 3)
t2 = (4, 5, 6)

result = concat_tuples(t1, t2)
print("Concatenated tuple:", result)