import CountingSort as cs
import cProfile as cpr
import pstats
import RadixSort as rs
import demo_rad_sort as drs


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
    # Counting Sort
    u_list = [4, 3, 4, 2, 1, 0, 1, 2, 1, 2, 999]  # input list
    o_list = cs.counting_sort(u_list)
    print(o_list)
    cpr.run('cs.counting_sort(u_list)')    # call cProfiler on the function

    u_list = [681, 1, 0, 723, 433, 12333, 462, 455, 163, 261, 905, 394, 211]
    o_list = drs.radix_sort(u_list, 12333)
    print(o_list)
    cpr.run('drs.radix_sort(u_list,  12333)')

    u_list = [681, 1, 0,  723, 433, 12333, 462, 455, 163, 261, 905, 394, 211]
    o_list = rs.radix_sort(u_list)
    print(o_list)
    cpr.run('rs.radix_sort(u_list)')

    u_list = [('zxca', 681), ('xcvxv', 1), ('as',0), ('xcw',1), ('zxcw', 433), ('qtyu', 12333),
              ('aa',462), ('vv',455), ('gg',163), ('rr',261), ('rr',163), ('ww',394), ('tt',211)]
    o_list = rs.radix_sort2(u_list)
    print(o_list)
    cpr.run('rs.radix_sort2(u_list)')
