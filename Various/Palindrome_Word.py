def isPalindrome(text):
    reverse_text = ''.join(reversed(text)) #Join each letter upside down
    
    if text == reverse_text:
        print("This word is palindrome")
    else:
        print("This word is not palindrome")
    
isPalindrome(input("Enter a word: "))