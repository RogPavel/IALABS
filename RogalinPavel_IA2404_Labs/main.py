def finite_automaton(word):
    # Пустое слово не подходит,
    # так как n >= 1 и m >= 1
    if not word:
        return False

    # Проверяем, что слово состоит только из a, b, c
    if any(ch not in "abc" for ch in word):
        return False

    i = 0
    n = 0
    m = 0

    # Сначала обязательно должен идти хотя бы один блок abc
    while i + 2 < len(word) and word[i:i + 3] == "abc":
        n += 1
        i += 3

    # n должно быть не меньше 1
    if n == 0:
        return False

    # Затем обязательно должен идти хотя бы один блок ab
    while i + 1 < len(word) and word[i:i + 2] == "ab":
        m += 1
        i += 2

    # m должно быть не меньше 1
    if m == 0:
        return False

    # Если дошли до конца — слово принято
    return i == len(word)


def main():
    print("=== Конечный автомат ===")
    print("Язык: (abc)^n(ab)^m")
    print("Условия: n >= 1, m >= 1")
    print("Введите 'exit' для завершения.\n")

    while True:
        word = input("Введите слово: ")

        if word == "exit":
            break

        if finite_automaton(word):
            print("✓ Слово принадлежит языку")
        else:
            print("✗ Слово не принадлежит языку")


if __name__ == "__main__":
    main()