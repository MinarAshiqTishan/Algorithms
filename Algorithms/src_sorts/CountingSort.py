# Counting Sort
def counting_sort(u_list: [int]) -> [int]:
    # max value & length
    k = max(u_list)  # k is maximum possible value in array,
    length = len(u_list)

    # bucket
    # initialize an array of 0,
    # size: k+1 of the unordered list
    b_list = [0] * (k+1)

    # count occurrences
    for i in range(0, length):
        el = u_list[i]
        b_list[el] += 1
    # print(b_list)

    # running sum or prefix sum
    for i in range(1, k+1):
        b_list[i] = b_list[i - 1] + b_list[i]

    # print(b_list)

    # placement
    o_list = [0] * length
    count = 0
    for i in range(length - 1, -1, -1):
        el = u_list[i]
        count = b_list[el]
        o_list[count - 1] = el
        b_list[el] -= 1

    # print(o_list)
    return o_list

