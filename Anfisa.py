def get_longest_word(line: str) -> str:
    arr = line.split()
    max_lenght = len(arr)
    if max_lenght == 1:
        return ''.join(arr)
    current_word = arr[0]
    for i in range(1, max_lenght):
        if len(arr[i]) > len(current_word):
            current_word = arr[i]
    return current_word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
