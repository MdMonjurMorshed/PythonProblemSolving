### LeetCode 75
### problem number 238

def product_of_arr_except_self(arr):
    ans = []
    mul = 1
    for i in range(len(arr)):
        if i == 0:
            ans.insert(i,1)
            continue
        ans.insert(i,ans[i-1]*arr[i-1])    
    for j in range(len(arr)-1,-1,-1):
        if j == len(arr)-1:
            ans[j] = ans[j] * mul
            continue
        mul = mul * arr[j+1]
        print('mul is',mul)
        ans[j] = ans[j]*mul   

    return ans

print(product_of_arr_except_self([-1,1,0,-3,3]))
          