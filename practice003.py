def longest_unique_substring(s):
    seen = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        # If the character is already seen, move the start pointer
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1
        
        seen[s[end]] = end  # Update last seen position
        max_length = max(max_length, end - start + 1)
    
    return max_length


# 🔹 Test cases
print("Input: 'abcabcbb' →", longest_unique_substring("abcabcbb"))
print("Input: 'bbbbb' →", longest_unique_substring("bbbbb"))
print("Input: 'pwwkew' →", longest_unique_substring("pwwkew"))
print("Input: 'abcdefg' →", longest_unique_substring("abcdefg"))
print("Input: 'aab' →", longest_unique_substring("aab"))
