def is_palindrome(s):
    """
    Checks if a given string is a palindrome.
    """
    s = s.lower().replace(" ", "")  # Normalize string
    return s == s[::-1]
