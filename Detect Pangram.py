# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/solutions/python

def is_pangram(s):
    list_of = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in list(s.lower()):
        if i in list_of:
            list_of.remove(i)
    return len(list_of) == 0
print(is_pangram('The quick, brown fox jumps over the lazy dog!'))

