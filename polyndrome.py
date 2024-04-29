n=int(input())
s=str(n)
r=s[::-1]
if s==r:
    print("palindrome")
else:
    print("not palindrome")