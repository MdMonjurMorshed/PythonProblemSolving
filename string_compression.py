def string_compression(chars):
    
        
    i,result_index,list_length = 0,0,len(chars)
    while i < list_length:
        j = i+1
        while j < list_length and chars[j]==chars[i]:
            j+=1
        chars[result_index]=chars[i]
        result_index+=1
        if j-i>1:
            count = str(j-i)
            for c in count:
                chars[result_index]=c
                result_index+=1    
        i=j   
    chars[:] = chars[:result_index] 
    print(chars)   
    return result_index 

akta_var = ["a","a","b","b","c","c","c"]

print(string_compression(akta_var))
print(akta_var)
            