name = "the quick brown fox jumps over the lazy dog"
alph ="abcdefghijklmnopqrstuvwxyz"

def panagram(item,alph):
    for item in alph:
        if item not in name:
            return "Not in panagram"
    return "In a panagram"

b=panagram(name,alph)
print(b)
