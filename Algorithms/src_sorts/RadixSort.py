import math


def digit_counter_str(val: int) -> int:
    val = abs(val)
    return len(str(val))


def digit_counter_log(val: int) -> int:
    # returns wrong value after 999999999999997
    val = abs(val)
    return int(math.log10(val)) + 1


def digit_counter(val: int) -> int:
    val = abs(val)

    if val == 0:
        return 1

    counter = 0
    while val:
        counter += 1
        val //= 10
    return counter


# u_list = [681, 723, 433, 12333, 462, 455, 163, 261, 905, 394]


def radix_sort(u_list: [int]) -> [int]:
    max_val = max(u_list)
    k = 9
    length = len(u_list)
    digits = digit_counter(max_val)

    for d in range(0, digits):
        d_list = []
        for el in u_list:
            el_digit = (el % (10 ** (d + 1))) // (10 ** d)
            d_list.append(el_digit)

        # bucket
        # initialize an array of 0,
        # size: k+1 of the unordered list
        b_list = [0] * (k + 1)

        # count occurrences
        for i in range(0, length):
            el = d_list[i]
            b_list[el] += 1
        # print(b_list)

        # running sum or prefix sum
        for i in range(1, k + 1):
            b_list[i] = b_list[i - 1] + b_list[i]

        o_list = [0] * length
        for i in range(length - 1, -1, -1):
            el = u_list[i]
            el_digit = (el % (10 ** (d + 1))) // (10 ** d)
            count = b_list[el_digit]
            o_list[count - 1] = el
            b_list[el_digit] -= 1

        for i in range(0, length):
            u_list[i] = o_list[i]

    return o_list


def radix_sort2(u_list: [(any, int)]) -> [(any, int)]:
    max_val = max(u_list, key=lambda elem: elem[1])[1]  # extract the max 2nd val of tuple
    k = 9
    length = len(u_list)
    digits = digit_counter(max_val)

    for d in range(0, digits):
        d_list = []
        for el in u_list:
            el_digit = (el[1] % (10 ** (d + 1))) // (10 ** d)  # digit of tuple 2nd val
            d_list.append(el_digit)

        # bucket
        # initialize an array of 0,
        # size: k+1 of the unordered list
        b_list = [0] * (k + 1)

        # count occurrences
        for i in range(0, length):
            el = d_list[i]
            b_list[el] += 1
        # print(b_list)

        # running sum or prefix sum
        for i in range(1, k + 1):
            b_list[i] = b_list[i - 1] + b_list[i]

        o_list = [0] * length
        for i in range(length - 1, -1, -1):
            el = u_list[i][1]  # tuple 2nd val
            el_digit = (el % (10 ** (d + 1))) // (10 ** d)
            count = b_list[el_digit]
            o_list[count - 1] = u_list[i]  # put tuple element
            b_list[el_digit] -= 1

        for i in range(0, length):
            u_list[i] = o_list[i]

    return o_list
