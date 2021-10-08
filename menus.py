
def list_input() -> list[int]:
    print("Introdu elementele listei separate printr-o virgula")
    lst = input("lista: ")
    lst = [int(x) for x in lst.split(",")]
    
    return lst

def select_properties():
    print("""
Bazat pe ce proprietati sa fie gasita cea mai lunga subsecventa?

    1.  Toate numerele sunt pătrate perfecte.
    2.  Toate numerele sunt prime.
    3.  Numerele au semne alternante.
    4.  Numerele sunt ordonate crescător.
    5.  Toate numerele sunt palindroame.
    6.  Toate numerele sunt divizibile cu k (citit).
    7.  Toate numerele sunt neprime.
    8.  Suma numerelor este număr prim.
    9.  Produsul numerelor este impar.
    10. Toate numerele sunt pare.
    11. Toate numerele au același număr de biți de 1 în reprezentarea binară.
    12. Toate numerele același număr de divizori.
    13. Toate numerele sunt formate din cifre prime.
    14. Toate numerele au partea întreagă egală cu partea fracționară.
    15. Toate numerele se pot scrie ca x**k, k citit, x întreg pozitiv.
    16. Toate numerele sunt în progresie aritmetică.
    17. Media numerelor nu depășește o valoare k citită.
    18. Numărul de cifre este în ordine descrescătoare.
    19. Concatenarea numerelor din subsecvență are cifrele în ordine crescătoare.
    20. Concatenarea numerelor din subsecvență este număr prim.

Poate fi selectata o proprietate (ex: 5) sau mai multe, separate prin virgula (ex: 1,6,9,15)
    """)

    properties = input("Proprietati:")
    properties = [int(x) for x in properties.split(",")]
    return properties


