def combo_string(a, b):
    short = a if len(a) < len(b) else b
    long = a if len(a) > len(b) else b
    return short + long + short