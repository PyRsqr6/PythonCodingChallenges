def anagram_check(string1, string2):
    #get the length of the strings
    len_1 = len(string1)
    len_2 = len(string2)

    if len_1 != len_2:
        return False
    
    string1 = sorted(string1)
    string2 = sorted(string2)

    #Disney & Sidney
    #deinsy
    for i in range(0,len_1):
        if string1[i] != string2[i]:
            return False
    return True

print(anagram_check("silent", "listen"))
print(anagram_check("mobile", "mobil"))
print(anagram_check("disney", "sidney"))
print(anagram_check("Fired", "Fried"))