# given dictionary
d = {"a": 1, "b": 2}
# taking Key from user to check
key = input("Enter key = ")
# Check existence
if key in d:
    print(key, "Yes exist in dictionary")
else:
    print("Not available in dictionary")