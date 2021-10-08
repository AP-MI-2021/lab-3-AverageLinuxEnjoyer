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

            if 1 in properties:
                data = get_longest_all_perfect_squares(data)
            if 2 in properties:
                data = get_longest_all_primes(data)
            if 3 in properties:
                data = get_longest_alternating_signs(data)
            if 4 in properties:
                data = get_longest_sorted_asc(data)
            if 5 in properties:
                data = get_longest_all_palindromes(data)
            if 6 in properties:
                k = int(input("Pentru proprietatea 6 e necesara citirea lui k. Cat sa fie k?"))
                data = get_longest_div_k(data, k)
            if 7 in properties:
                data = get_longest_all_not_prime(data)
            if 8 in properties:
                data = get_longest_sum_is_prime(data)
            if 9 in properties:
                 data = get_longest_product_is_odd(data)
            if 10 in properties:
                 data = get_longest_all_even(data)
            if 11 in properties:
                 data = get_longest_same_bit_counts(data)
            if 12 in properties:
                 data = get_longest_same_div_count(data)
            if 13 in properties:
                data = get_longest_prime_digits(data)
            if 14 in properties:
                data = get_longest_equal_int_real(data)
            if 15 in properties:
                k = int(input("Pentru proprietatea 15 e necesara citirea lui k. Cat sa fie k?"))
                data = get_longest_powers_of_k(data, k)
            if 16 in properties:
                 data = get_longest_arithmetic_progression(data)
            if 17 in properties:
                 k = int(input("Pentru proprietatea 17 e necesara citirea unei valori. Cat sa fie valoarea?"))
                 data = get_longest_average_below(data, k)
            if 18 in properties:
                 data = get_longest_digit_count_desc(data)
            if 19 in properties:
                 data = get_longest_concat_digits_asc(data)
            if 20 in properties:
                data = get_longest_concat_is_prime(data)                
                
            print(f"Cea mai lunga subsecventa cu proprietatile {properties} e {data}")

        elif option == '3':
            break
        else:
            print("Nu exista o astfel de optiune, incearca din nou.")







if __name__ == "__main__":
    main()