# N ** 2
def cou(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter =+ 1

        print(sym, counter)

#cou('aaaabbbcccd')

# M * N
def cou_2(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter =+ 1

        print(sym, counter)

#cou_2('aaaabbbcccd')

# N
def cou_3(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0) + 1

    for sym, count in syms_counter.items():
        print(sym, count)


cou_3('aaaabbbccd')