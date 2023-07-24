import random

# returns a d6 dice roll. i.e. a random number between 1 and 6
def roll_d6(d=6):

    return random.randint(1, d)

# checks if the last two number of a list are the same
def check_win(input_list):

    # if it's a 1, it can't be a win
    if input_list[-1] == 1:
        return False
    
    # if it's a 6, return true
    if input_list[-1] == 6:
        return True
    
    # check if the length of list is two or greater
    if len(input_list) > 1:

        # if the last two numbers are equal, return true
        return input_list[-1] == input_list[-2]
    
    # if the list has a length of less than 2, return None

    return None

# roll dice sequentially until n_max dice have been rolled
def roll_sequential_dice(n_max=13):

    dice_rolls = [roll_d6()]

    for n in range (1, n_max):
        dice_rolls.append(roll_d6())

        if check_win(dice_rolls):
            return n

    return False

def repeat_experiments(number_of_repeats, sequential_dicerolls_max=13):


    results = [0 for _ in range(sequential_dicerolls_max)]

    # repeat experiment multiple times
    for _ in range(number_of_repeats):

        result = roll_sequential_dice(sequential_dicerolls_max)

        # if the sequential roll returns a win, add the result to the tally
        if result:
            results[result] += 1
        
        # the first element in the results list is the number of fails
        else:
            results[0] += 1


    return results


def summarise_results(results):

    print("\n ===== Summary of Results ===== \n")

    number_of_results = sum(results)
    number_of_wins = sum(results[1:])
    number_of_losses = results[0]

    wins_percentage = number_of_wins / number_of_results * 100
    loss_percentage = number_of_losses / number_of_results * 100

    print(f"After {number_of_results} repeats: \n")

    print(f"There were {number_of_wins} wins ({round(wins_percentage, 1)}%)")
    print(f"There were {number_of_losses} losses ({round(loss_percentage, 1)}%)")

    print("\n ---- \n")

    if len(results) > 3:

        for i in range(2, len(results)):

            number_of_dice_rolled = i + 1
            number_of_wins_dice = results[i]
            number_of_wins_sum = sum(results[1:i+1])
            percentage_wins_sum = round(number_of_wins_sum / number_of_results * 100)

            print(f"After {number_of_dice_rolled} dice have been rolled, the percentage of trials which were wins is {percentage_wins_sum}")
            




experiment_results = repeat_experiments(1000000)

summarise_results(experiment_results)