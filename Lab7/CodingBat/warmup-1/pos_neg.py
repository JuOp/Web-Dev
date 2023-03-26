def pos_neg(a, b, negative):
    case1 = a >= 0 and b < 0 and not negative
    case2 = a < 0 and  b >= 0 and not negative
    case3 = a < 0 and b < 0 and negative
    return True if case1 or case2 or case3 else False