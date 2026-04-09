# Take character input
ch = input("Enter character: ")

# Convert to lowercase
ch = ch.lower()

# Check vowel 
if ch in ['a', 'e', 'i', 'o', 'u']:
    print(ch,"Vowel")
else:
    print(ch,"Not Vowel")