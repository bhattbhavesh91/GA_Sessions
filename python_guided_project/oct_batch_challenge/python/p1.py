#Function to check for palindrome
def palindrome_check(num):
    num=str(num)
    return (num[::-1]==num)

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num
