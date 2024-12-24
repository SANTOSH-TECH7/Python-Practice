s="Santosh Ravi is a good man"
mid=len(s)//2
first=s[:mid]
second=s[mid:]
print(f"{first.upper()}{second.lower()}")

#Another method

s = "Santosh Ravi is a good man"

# Find the middle index
mid = len(s) // 2

# Directly concatenate the transformed halves
result = s[:mid].upper() + s[mid:].lower()

# Print the result
print(result)
