from get_longest_subsequence import get_longest_subsequence

def get_bytes1(n: int) -> int:
    """Returneaza numarul de biti cu valoare 1 al unui numar

    Args:
        n (str): Numarul verificat

    Returns:
        int: Numarul de biti cu valoarea 1
    """

    bytes1 = 0
    while n:
        if n % 2 == 1:
            bytes1+=1
        n //= 2

    return bytes1

def test_get_bytes1():
    assert get_bytes1(7) == 3
    assert get_bytes1(64) == 1
    assert get_bytes1(0) == 0
    assert get_bytes1(9) == 2

test_get_bytes1()

def same_bit_counts(lst: list[int]) -> bool:
    """Verifica daca toate numerele din lista au acelasi numar de biti de 1 in reprezentarea binara

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca toate numerele au acelasi numar de biti de 1, False in caz contrar
    """
    for i in range(1, len(lst)):
        if get_bytes1(lst[i]) != get_bytes1(lst[i-1]):
            return False
    
    return True
        
def test_same_bit_counts():
    assert same_bit_counts([7, 21, 76]) == True
    assert same_bit_counts([2,8,16]) == True
    assert same_bit_counts([]) == True
    assert same_bit_counts([0,1]) == False

test_same_bit_counts()

def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa cu elemente ce au acelasi numar de biti de 1 in reprezentarea lor binara

    Args:
        lst (list[int]): Lista principala

    Returns:
        list[int]: Subsecventa
    """
    return get_longest_subsequence(lst, same_bit_counts)

def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([5,9,2,1,7,21,76,48]) == [7,21,76]
    assert get_longest_same_bit_counts([12,4,16,91,5]) == [4,16]
    assert get_longest_same_bit_counts([]) == []
    assert get_longest_same_bit_counts([0]) == []

test_get_longest_same_bit_counts()