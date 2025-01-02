## This solve represent the reverse vowel from word 
## like 'hello' will be 'holle'

### leetcode75 , problem number 345

def reverse_vowel(s):
    vowel = 'aeiouAEIOU'
    # n = s
    list_s = list(s)
    
    # for i in range(len(list_s)):
    #     for j in range(i+1,len(list_s)):
    #         if list_s[i] in vowel and list_s[j] in vowel:

    #             temp = list_s[i]
    #             list_s[i] = list_s[j]
    #             list_s[j] = temp
    # return ''.join(list_s)
    left = 0
    right = len(list_s)-1
    for i in range(0,len(list_s)):
        if left < right:
            if list_s[left] not in vowel:
                left=left+1
            if list_s[right] not in vowel:
                right = right - 1
            if  list_s[left] in vowel and list_s[right] in vowel:  
                list_s[left],list_s[right] = list_s[right],list_s[left]  
                left+=1
                right-=1
                

    return ''.join(list_s)

print(reverse_vowel("IceCreAm"))

