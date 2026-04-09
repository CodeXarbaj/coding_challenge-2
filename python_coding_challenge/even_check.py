# Take input from
n = int(input("enter number: "))

# Loop from 1 to n
for i in range(1, n+1):
    if i % 2 == 0:   # Check even or not using if 
        print(i, end=" ")