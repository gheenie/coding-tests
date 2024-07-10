# Get an input
print("Type a string to test if it is a twin string: ", end = "")
string = input()

# Odd length inputs will never be a twin string
if len(string) % 2 == 1:
    print('This string is not a twin string.')
    exit()

# Split the input into two halves
first_part = string[: len(string) // 2]
second_part = string[len(string) // 2:]

# Compare the two strings and display results
if first_part == second_part:
    print('This string is a twin string.')
else:
    print('This string is not a twin string.')
