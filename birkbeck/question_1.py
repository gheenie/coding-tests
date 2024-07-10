'''
Possibly add input validation.
'''

# Variables to increment test results
fails = 0
passes = 0
distinctions = 0

finished = False
while not finished:
    # Get inputs for two tests
    print('Next student (first test): ', end = '')
    first_test = int(input())
    print('Next student (second test): ', end = '')
    second_test = int(input())

    # Sum test scores
    total_score = first_test + second_test
    
    # 51 for each test signals to end the program
    if total_score == 102:
        finished = True
        continue

    # Increment results variables according to summed score.
    if total_score >= 0 and total_score <= 49:
        fails += 1
    elif total_score >= 50 and total_score <= 69:
        passes += 1
    elif total_score >= 70 and total_score <= 100:
        distinctions += 1

# Display test results
print(f'Fails: {fails}, Passes: {passes}, Distinctions: {distinctions}')
