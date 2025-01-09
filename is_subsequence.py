## 392. Is Subsequence (leetcode)

def is_subsequsence(s,t):
    if s == "":
        return True
    if s == "" and t == "":
        return True
    
    main_list = list(t)
    sub_list = list(s)
    sub_str = ""
    sub_str_ind = 0

    for i in range(len(main_list)):
        if sub_list[sub_str_ind] == main_list[i]:
            sub_str += main_list[i]
            sub_str_ind += 1
        if sub_str == s:
            return True
    return False


print(is_subsequsence("abc","abbbdfc"))
        