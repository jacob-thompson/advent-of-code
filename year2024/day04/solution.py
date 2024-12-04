DESIRED = "MAS"
BYTES_TO_SEARCH = 3

def get_word_search():
    word_search = list()

    with open("input.txt", "r") as file:
        for line in file:
            word_search.append(line)

    return word_search

def check_nearby_chars(word_search, line_index, char_index):
    counter = 0
    if word_search[line_index][char_index] != "X":
        return counter

    #horizontals
    right = str()
    try:
        char = char_index

        for _ in range(BYTES_TO_SEARCH):
            char += 1
            right += word_search[line_index][char]
    except IndexError:
        pass
    if right == DESIRED:
        counter += 1

    left = str()
    try:
        if char_index < BYTES_TO_SEARCH:
            raise Exception("avoiding wrapping")

        char = char_index

        for _ in range(BYTES_TO_SEARCH):
            char -= 1
            left += word_search[line_index][char]
    except IndexError:
        pass
    except Exception:
        pass
    if left == DESIRED:
        counter += 1

    #verticals
    down = str()
    try:
        line = line_index

        for _ in range(BYTES_TO_SEARCH):
            line += 1
            down += word_search[line][char_index]
    except IndexError:
        pass
    if down == DESIRED:
        counter += 1

    up = str()
    try:
        if line_index < BYTES_TO_SEARCH:
            raise Exception("avoiding wrapping")

        line = line_index

        for _ in range(BYTES_TO_SEARCH):
            line -= 1
            up += word_search[line][char_index]
    except IndexError:
        pass
    except Exception:
        pass
    if up == DESIRED:
        counter += 1

    #diagonals
    downright = str()
    try:
        line = line_index
        char = char_index

        for _ in range(BYTES_TO_SEARCH):
            line += 1
            char += 1
            downright += word_search[line][char]
    except IndexError:
        pass
    except Exception:
        pass
    if downright == DESIRED:
        counter += 1

    downleft = str()
    try:
        if char_index < BYTES_TO_SEARCH:
            raise Exception("avoiding wrapping")

        line = line_index
        char = char_index

        for _ in range(BYTES_TO_SEARCH):
            line += 1
            char -= 1
            downleft += word_search[line][char]
    except IndexError:
        pass
    except Exception:
        pass
    if downleft == DESIRED:
        counter += 1

    upright = str()
    try:
        if line_index < BYTES_TO_SEARCH:
            raise Exception("avoiding wrapping")

        line = line_index
        char = char_index

        for _ in range(BYTES_TO_SEARCH):
            line -= 1
            char += 1
            upright += word_search[line][char]
    except IndexError:
        pass
    except Exception:
        pass
    if upright == DESIRED:
        counter += 1

    upleft = str()
    try:
        if line_index < BYTES_TO_SEARCH or char_index < BYTES_TO_SEARCH:
            raise Exception("avoiding wrapping")

        line = line_index
        char = char_index

        for _ in range(BYTES_TO_SEARCH):
            line -= 1
            char -= 1
            upleft += word_search[line][char]
    except IndexError:
        pass
    except Exception:
        pass
    if upleft == DESIRED:
        counter += 1

    return counter

def check_cross(word_search, line_index, char_index):
    is_cross = False
    if word_search[line_index][char_index] != "A":
        return is_cross

    try:
        if line_index == 0 or char_index == 0:
            raise Exception("avoiding wrapping")

        topleft = word_search[line_index - 1][char_index - 1]
        topright = word_search[line_index - 1][char_index + 1]
        botleft = word_search[line_index + 1][char_index - 1]
        botright = word_search[line_index + 1][char_index + 1]

        first_half = topleft == "S" and botright == "M" or topleft == "M" and botright == "S"
        second_half = topright == "S" and botleft == "M" or topright == "M" and botleft == "S"
        is_cross = first_half and second_half
    except IndexError:
        pass
    except Exception:
        pass

    return is_cross

def get_search_count(word_search):
    count = 0
    for line_index, line in enumerate(word_search):
        for char_index, _ in enumerate(line):
            count += check_nearby_chars(word_search, line_index, char_index)

    return count

def get_cross_count(word_search):
    count = 0
    for line_index, line in enumerate(word_search):
        for char_index, _ in enumerate(line):
            if check_cross(word_search, line_index, char_index):
                count += 1

    return count

def main():
    word_search = get_word_search()

    count = get_search_count(word_search)
    print(count)

    cross_count = get_cross_count(word_search)
    print(cross_count)

if __name__ == "__main__":
    main()
