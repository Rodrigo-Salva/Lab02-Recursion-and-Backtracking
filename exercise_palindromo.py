def is_palindrome(string):
    # Remove spaces and convert to lowercase
    string = "".join(string.split()).lower()
    
    # Base case: if the string has 0 or 1 characters, it's a palindrome
    if len(string) <= 1:
        return True
    
    # If the first and last characters are different, it's not a palindrome
    if string[0] != string[-1]:
        return False
    
    # Recursive call by removing the first and last characters
    return is_palindrome(string[1:-1])

# Example usage
text = "Anita lava la tina"
print(is_palindrome(text))  # Output: True
