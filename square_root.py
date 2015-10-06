running = True
epsilon = .01
guess = 1
counter = 0

while running:
    try:
        user_number = int(input("Please enter a Number: "))
        if user_number < 0:
            user_number = user_number * -1
        running = False

    except ValueError:
        print("Enter a valid Number!!")
        continue

thinking = True

while thinking:
    best_guess = abs(user_number - guess**2)
    if best_guess <= epsilon:
        thinking = False
        print("The Square Root of {} is {}". format(user_number,
                                                    round(guess, 2)))
    else:
        guess = (guess + user_number/guess) / 2
        counter += 1
        print("Guess number {} is {}". format(counter, round(guess, 2)))
