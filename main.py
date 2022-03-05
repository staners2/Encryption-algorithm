alfavit = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
           13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
           25: 'Z', 26: 'А', 27: 'Б', 28: 'В', 29: 'Г', 30: 'Д', 31: 'Е', 32: 'Ё', 33: 'Ж', 34: 'З', 35: 'И', 36: 'Й',
           37: 'К', 38: 'Л', 39: 'М', 40: 'Н', 41: 'О', 42: 'П', 43: 'Р', 44: 'С', 45: 'Т', 46: 'У', 47: 'Ф', 48: 'Х',
           49: 'Ц', 50: 'Ч', 51: 'Ш', 52: 'Щ', 53: 'Ъ', 54: 'Ы', 55: 'Ь', 56: 'Э', 57: 'Ю', 58: 'Я', 59: 'А', 60: 'Б',
           61: 'В', 62: 'Г', 63: 'Д', 64: 'Е', 65: 'Ё', 66: 'Ж', 67: 'З', 68: 'И', 69: 'Й', 70: 'К', 71: 'Л', 72: 'М',
           73: 'Н', 74: 'О', 75: 'П', 76: 'Р', 77: 'С', 78: 'Т', 79: 'У', 80: 'Ф', 81: 'Х', 82: 'Ц', 83: 'Ч', 84: 'Ш',
           85: 'Щ', 86: 'Ъ', 87: 'Ы', 88: 'Ь', 89: 'Э', 90: 'Ю', 91: 'Я', 92: " "}


def get_key(dictionary: dict, s: str) -> int:
    for key, value in dictionary.items():
        if value == s:
            return key


def get_square_array() -> []:
    arr = []
    alf = list(alfavit.values())
    arr.append(alf)
    for i in range(1, len(alfavit)):
        alf = alf[1:] + alf[:1]
        arr.append(alf)

    return arr


def append_to_size(word: str, length: int):
    while len(word) <= length:
        word += word

    return word[0:length]


def сaesar(is_encode: bool) -> str:
    print("Введите слово")
    word = input()
    print("Введите ключ (цифру)")
    key = input()
    # кол-во сдвига
    n = int(key) if is_encode else -int(key)
    encode = ""
    for char in word:
        index = get_key(alfavit, char.upper())
        new_index = (index + n) % len(alfavit)
        print(f"{index} | {new_index}")

        encode += alfavit[new_index]

    return encode


def vigenere(is_encode: bool) -> str:
    # row - key[index] | column - value[index]
    word = input("Введите слово: ")
    key = append_to_size(input("Введите ключ шифра: "), len(word))
    arr = get_square_array()
    print(arr)
    new_word = ""
    if is_encode:
        for i in range(0, len(word)):
            row = get_key(alfavit, key[i].upper())
            column = get_key(alfavit, word[i].upper())
            new_word += arr[row][column]
            print(f"arr[{row}][{column}] = {arr[row][column]}")
    else:
        for i in range(0, len(word)):
            row = get_key(alfavit, key[i].upper())
            index = arr[row].index(word[i].upper())
            new_word += alfavit.get(index)

    return new_word


def wanderers(is_encode: bool) -> str:
    word = input("Введите слово: ")
    count_row = int(input("Введите кол-во строк: "))

    count_column = (len(word)) // count_row if (len(word)) % count_row == 0 else (len(word)) // count_row + 1

    while len(word) < count_column * count_row:
        print(f"{len(word)} < {count_column} * {count_row}")
        word += " "
    print(f"Word: |{word}|")

    print(f"count row = {count_row} | count column = {count_column}")
    arr = []
    if is_encode:
        index_char = 0
        for i in range(0, count_row):
            arr_column = []
            for j in range(0, count_column):
                arr_column.append(word[index_char])
                index_char += 1
            arr.append(arr_column)

        new_word = ""
        for i in range(0, count_column):
            for j in range(0, count_row):
                new_word += alfavit[get_key(alfavit, arr[j][i].upper())]

        return new_word
    else:
        out_text_char = [i for i in range(len(word))]
        print(out_text_char)
        index = 0
        for i in range(0, count_column):
            for j in range(0, count_row):
                out_text_char[i + count_column * j] = word[index]
                index += 1

        new_word = "".join(out_text_char)

        return new_word.rstrip()
        # index_char = len(word) - 1
        # for i in range(count_column, 0, -1):
        #     arr_row = []
        #     for j in range(count_row, 0, -1):
        #         arr_row.append(word[index_char])
        #         index_char -= 1
        #     arr.append(arr_row)
        #
        # print(f"{arr} => len {len(arr)}")
        # new_word = ""
        # for i in range(len(arr) - 1, 0, -1):
        #     for j in range(len(arr[i]) - 1, 0, -1):
        #         new_word += alfavit[get_key(alfavit, arr[i][j].upper())]

    #return new_word


if __name__ == '__main__':
    while True:
        print("=" * 16)
        print("Выберите шифр:\n1. Цезаря\n2. Виженера\n3. Скиталы\n4. Exit")
        while True:
            try:
                number = int(input("Номер: "))
                if number in range(1, 5):
                    break
                else:
                    print("Введите число от 1 до 4")
            except:
                print("Введите корректное число")

        if number == 1:
            question = input("1. Шифровать\n2. Расшифровать\n")
            is_encode = True if int(question) == 1 else False
            word = сaesar(is_encode)
        elif number == 2:
            question = input("1. Шифровать\n2. Расшифровать\n")
            is_encode = True if int(question) == 1 else False
            word = vigenere(is_encode)
        elif number == 3:
            question = input("1. Шифровать\n2. Расшифровать\n")
            is_encode = True if int(question) == 1 else False
            word = wanderers(is_encode)
        else:
            print("Bye bye")
            break

        print(f"Слово: |{word.lower()}|")
