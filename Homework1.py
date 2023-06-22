
st = input('Введите строку: ')

def reverse(st): 
    return st[::-1] 
  
def is_palindrome(st): 
    revers = reverse(st) 
    return (st == revers)

i = is_palindrome(st)
print(i)