from typing import Callable

def get_longest_subsequence(lst: list[int], has_property: Callable) -> list[int]:
    """Returns the longest subsequence of a list, with a specified property

    Args:
        lst (list[int]): The main list
    
    Returns:
        list[int]: The longest subsequence with the specified property
    """
    returned_subsequence = []
    max_length = 0
    
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            current_subsequence = lst[i:j+1]
            if len(current_subsequence) > max_length and has_property(current_subsequence):
                max_length = len(current_subsequence)
                returned_subsequence = current_subsequence
    
    return returned_subsequence

def test_get_longest_subsequence():
    # inca trb gandit la asta
    pass