def get_digit(num, base, digit):
    # Get the digit at the specified position
    return (num // (base ** (digit - 1))) % base

def radix_pass(arr, base, digit):
    n = len(arr)

    counter = [0] * base
    # Count occurrences of each digit
    for i in range(n):
        counter[get_digit(arr[i], base, digit)] += 1

    position = [0] * base
    # Calculate positions of each digit in the sorted array
    for v in range(1, base):
        position[v] = position[v - 1] + counter[v - 1]

    temp = [0] * n
    # Place elements in temporary array according to their digit
    for i in range(n):
        d = get_digit(arr[i], base, digit)
        temp[position[d]] = arr[i]
        position[d] += 1

    # Copy elements back to original array
    for i in range(n): arr[i] = temp[i]


def radix_sort(arr, base, digits):
    for digit in range(1, digits + 1):
        radix_pass(arr, base, digit)


# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr, 10, 3)  # Sorting base 10 integers with maximum of 3 digits
print("Sorted array:", arr)




def get_char(string, position):
    # Get the character at the specified position (from the end)
    if position < len(string):
        return string[-position - 1]
    else:
        return '\0'  # Padding character (lexicographically precedes all other characters)

def radix_pass(strings, position):
    base = 256  # Assuming ASCII characters (extend for Unicode)
    n = len(strings)

    counter = [0] * base
    for i in range(n):
        char = get_char(strings[i], position)
        counter[ord(char)] += 1

    position_sum = [0] * base
    for v in range(1, base):
        position_sum[v] = position_sum[v - 1] + counter[v - 1]

    temp = [None] * n
    for i in range(n):
        char = get_char(strings[i], position)
        temp[position_sum[ord(char)]] = strings[i]
        position_sum[ord(char)] += 1

    for i in range(n):
        strings[i] = temp[i]

def radix_sort(strings):
    max_length = max(len(s) for s in strings)
    for position in range(max_length):
        radix_pass(strings, position)

# Example usage:
word_list = ["Monday", "Friday", "Sunday", "Apple", "Banana", "Cherry"]
radix_sort(word_list)
print("Sorted strings:", word_list)
