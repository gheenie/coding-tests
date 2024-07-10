# Variable to store length of previous input
previous_string_length = 0
# Program assumes the inputs are ascending by default
is_ascending_length = True

finished = False
while not finished:
    # Get an input
    print("Type a string (end with an empty line): ", end = "")
    string = input()

    # Empty string indicates user is done inputting
    if string == '':
        finished = True
        continue

    # First string is being inputted and comparison hasn't started
    if previous_string_length == 0:
        previous_string_length = len(string)
        continue

    # Once an input is shorter than the previous, the sequence is not
    # ascending anymore, and stays that way for the rest of the inputs
    if len(string) < previous_string_length:
        is_ascending_length = False

# Display results
if is_ascending_length:
    print('Yes')
else:
    print('No')
