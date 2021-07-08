"""
A word w is an anagram of a word v if a permutation of the letters transforming w into v exists.
"""
def anagram(statement: str):
    dic = {}  
    
    for word in statement.split(' '):
        sorted_word = ''.join(sorted(word))  # calculate the signature (unique term by sorting in lexicographical order)
        if sorted_word in dic:
            dic[sorted_word].append(word)  # append a word to an existing signature
        else:
            dic[sorted_word] = [word]  # add a new signature and its first word
    
    return [dic[s] for s in dic if len(dic[s]) > 1]

print(anagram("night thing"))