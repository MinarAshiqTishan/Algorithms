# Binary Exponentiation Algorithm


def norm_exp(num, expo):
    result = 1
    for i in range (0, expo):
        result *= num
    return result


def bin_exp(num, expo):
    res_sq = 1
    result = 1
    while expo != 0:
        res_sq = res_sq * num
        num = res_sq
        if expo & 1:
            result *= num
        expo >>= 1
    return result
