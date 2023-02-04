# DESC: Zadanie 2
# DESC: Dla zadanej tablicy liczb całkowitych należy znaleźć dwa elementy znajdujące się obok siebie,
# DESC: których iloczyn będzie największy.

# DESC: Na przykład input_list = [3, 6, -2, -5, 7, 3], rozwiązanie(input_list) = 21.


def neighbour_multiplier(input_list):
    """
    Dla zadanej tablicy liczb całkowitych należy znaleźć dwa elementy znajdujące się obok siebie,
    których iloczyn będzie największy.
    """
    return max(
        [(input_list[i] * input_list[i + 1]) for i in range(len(input_list) - 1)]
    )


print(neighbour_multiplier([3, 6, -2, -5, 7, 3]))
