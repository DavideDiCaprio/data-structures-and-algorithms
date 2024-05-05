'''
I'm using two pointers tecnique to reverse a string

 O(n) time complexity 
 O(1) space complexity

'''


def reverse_string(s) -> None:
    l = 0
    r = len(s)-1
    while l<r:
        s[l], s[r] = s[r], s[l]
        l +=1
        r -=1