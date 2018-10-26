def a_scramble(str_1,str_2):
    s1 = set(str_1.lower())
    s2 = set(str_2.lower())
    return s2 == s2.intersection(s1)
