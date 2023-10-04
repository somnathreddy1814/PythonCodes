def isPalindrome(s,l,r):

    if l>=r:
        return
    if s[l]==s[r]:
        isPalindrome(s,l+1,r-1)
        return True
    return False
    
if __name__=="__main__":
    s="s"
    print(isPalindrome(s,0,len(s)-1))