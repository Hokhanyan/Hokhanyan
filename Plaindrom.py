
def isPalindrom(s):
    return s[::-1]

s = input()
ans = isPalindrom(s)

if ans == s:
    print("Yes")
else:
    print("No")


