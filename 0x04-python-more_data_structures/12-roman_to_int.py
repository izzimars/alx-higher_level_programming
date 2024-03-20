#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != str:
        return 0
    roman_string = roman_string.lower()
    rom_dict = {'m':1000, 'd':500, 'c':100, 'l':50, 'x':10, 'v':5, 'i':1}
    prev = 'o'
    new_list = list(roman_string)
    sumz = 0
    for i in roman_string:
        if i not in new_list:
            return 0
        cur = i
        if prev != 'o':
            if (rom_dict[prev] < rom_dict[cur]):
                temp = (rom_dict[cur] - rom_dict[prev])
                sumz = sumz - rom_dict[prev] + temp
                continue
        sumz = sumz + rom_dict[cur]
        prev = i
    return (sumz)
