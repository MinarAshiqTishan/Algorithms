# profiling algebra algorithms
import BinaryExponentiation as be
import cProfile as cpr
import pstats


def f8(x):
    """
    A simple monkeypath for the pstats module to be able to see sub-millisecond timings
    If display value is 0.000, display the time in microseconds
    """
    ret = "%8.3f" % x
    if ret != '   0.000':
        return ret
    return "%6dµs" % (x * 10000000)


pstats.f8 = f8


if __name__ == "__main__":
    # Normal Exponentiation
    num = 4
    expo = 13
    result = be.norm_exp(num, expo)
    print(result)
    cpr.run('be.norm_exp(num, expo)')

    # Binary Exponentiation
    num = 4
    expo = 13
    result = be.bin_exp(num, expo)
    print(result)
    cpr.run('be.bin_exp(num, expo)')

    # Binary Exponentiation
    num = 53
    expo = 13
    result = be.bin_exp(num, expo)
    print(result)
    cpr.run('be.bin_exp(num, expo)')

