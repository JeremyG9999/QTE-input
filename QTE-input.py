import time
import random
def qte():
    # Generate a random number between 1 and 4
    target_number = random.randint(1, 4)
    print(f"Type the number: {target_number}")
    start_time = time.time()
    user_input = input("Your guess: ")
    elapsed_time = time.time() - start_time
    # Check if the input was within the time limit and matches the target number
    if elapsed_time <= 5:  # 5 seconds time limit
        if user_input.isdigit() and int(user_input) == target_number:
            print("Success! You typed the correct number in time.")
        else:
            print(f"Wrong number! The correct number was {target_number}.")
    else:
        print(f"Too late! You missed the timing. The correct number was {target_number}.")
qte()