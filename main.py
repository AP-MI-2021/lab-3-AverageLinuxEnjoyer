from get_longest_all_perfect_squares import get_longest_all_perfect_squares         # 1
from get_longest_all_primes import get_longest_all_primes                           # 2
from get_longest_alternating_signs import get_longest_alternating_signs             # 3
from get_longest_sorted_asc import get_longest_sorted_asc                           # 4
from get_longest_all_palindromes import get_longest_all_palindromes                 # 5
from get_longest_div_k import get_longest_div_k                                     # 6
from get_longest_all_not_prime import get_longest_all_not_prime                     # 7
from get_longest_sum_is_prime import get_longest_sum_is_prime                       # 8
from get_longest_product_is_odd import get_longest_product_is_odd                   # 9
from get_longest_all_even import get_longest_all_even                               # 10
from get_longest_same_bit_counts import get_longest_same_bit_counts                 # 11
from get_longest_same_div_count import get_longest_same_div_count                   # 12
from get_longest_prime_digits import get_longest_prime_digits                       # 13
from get_longest_equal_int_real import get_longest_equal_int_real                   # 14
from get_longest_powers_of_k import get_longest_powers_of_k                         # 15
from get_longest_arithmetic_progression import get_longest_arithmetic_progression   # 16
from get_longest_average_below import get_longest_average_below                     # 17
from get_longest_digit_count_desc import get_longest_digit_count_desc               # 18
from get_longest_concat_digits_asc import get_longest_concat_digits_asc             # 19
from get_longest_concat_is_prime import get_longest_concat_is_prime                 # 20
import menus


def main():
    option = ''
    properties = []
    data = []

    functions = [get_longest_all_perfect_squares, get_longest_all_primes, get_longest_alternating_signs, get_longest_sorted_asc,
             get_longest_all_palindromes, get_longest_div_k, get_longest_all_not_prime, get_longest_sum_is_prime, get_longest_product_is_odd,
             get_longest_all_even, get_longest_same_bit_counts, get_longest_same_div_count, get_longest_prime_digits, get_longest_equal_int_real,
             get_longest_powers_of_k, get_longest_arithmetic_progression, get_longest_average_below, get_longest_digit_count_desc,
             get_longest_concat_digits_asc, get_longest_concat_is_prime]

    while True:
        print(
            """     Ce doresti sa faci? 
        1. Citire date
        2. Determinare cea mai lunga subsecventa pe baza uneia sau a mai multor proprietati
        3. Iesire
        """)
        option = input("Optiune meniu:")

        if option == '1':
            data = menus.list_input()
        elif option == '2':
            properties = menus.select_properties()

            for properti in properties:
                if properti in (6,15,17):
                    k = int(input(f"Pentru proprietatea {properti} e necesara citirea unui k aditional. Cat sa fie k?"))
                    data = functions[properti-1](data, k)
                else:
                    data = functions[properti-1](data)

            print(f"Cea mai lunga subsecventa cu proprietatile {properties} e {data}")

        elif option == '3':
            break
        else:
            print("Nu exista o astfel de optiune, incearca din nou.")


if __name__ == "__main__":
    main()
