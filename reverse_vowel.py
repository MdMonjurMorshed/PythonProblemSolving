## This solve represent the reverse vowel from word 
## like 'hello' will be 'holle'

def reverse_vowel(s):
    vowel = 'aeiouAEIOU'
    n = s
    list_s = list(n)
    
    for i in range(len(list_s)):
        for j in range(i+1,len(list_s)):
            if list_s[i] in vowel and list_s[j] in vowel:

                temp = list_s[i]
                list_s[i] = list_s[j]
                list_s[j] = temp
    return ''.join(list_s)

print(reverse_vowel("Haeiullo"))

