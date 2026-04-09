# Function to check prime 
def prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2, n):
        if n % i == 0:
            return (n,"is Not Prime")
    
    return "Prime"

# Take input
num = int(input("Enter number = "))

# Call function
print(prime(num))