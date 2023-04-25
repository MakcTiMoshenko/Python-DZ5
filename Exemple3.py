
"""Дано слово, состоящее только из строчных латинских букв. 
Проверьте, является ли это слово палиндромом. Выведите YES или NO.
При решении этой задачи нельзя пользоваться циклами, 
в решениях на питоне нельзя использовать срезы с шагом, отличным от 1."""

# slovo = str(input("Введите слово: "))
# a = slovo[::-1]
# if slovo == a:
#   print("YES")
# else:
#   print("NO")

def IsPalindrome(S):
    if len(S) <= 1:
        return True
    else:
        return S[0] == S[-1] and IsPalindrome(S[1:-1])
print(IsPalindrome(str(input("Введите слово: "))))