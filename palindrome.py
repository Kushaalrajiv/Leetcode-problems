# def palindrome(num):  
#     x=str(num)
#     x2=x[::-1]
#     if x2==x:
#         return True
#     else:
#         return False
# num=int(input())
# palindrome(num)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num1=x
        rev=0
        while x>0:
            d=x%10
            rev=rev*10+d
            x=x//10
        if rev==num1:
            return True
        else:
            return False




