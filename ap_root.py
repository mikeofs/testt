from functools import reduce

def stripp(scr_str, signs):
    return for wrd in scr_str.replace(signs[0] + " ", signs[0]).replace(signs[1] + " ", signs[1]).split()

print(stripp("apples, pears # and bananas\\ngrapes\\nbananas !apples", ["#", "!"]))

def second():
    pass

