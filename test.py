"""Test by experient for solution
"""
import random
from datetime import datetime
import solution


random.seed(datetime.now())


def argmax(arr):
    """Get index of max
    :param: arr, list
    """
    imax, vmax = 0, 0
    for index, value in enumerate(arr):
        if vmax < value:
            vmax = value
            imax = index
    return imax


def gen_data(low=1, high=6, max_dices=8, n_set=5):
    """Generate data
    """
    set_dices = []
    for _ in range(n_set):
        n_dices = random.randint(2, max_dices)
        dices = [[random.randint(low, high) for j in range(6)] for i in range(n_dices)]
        set_dices.append(dices)

    return set_dices


def best_dice_with_experience(dices, n_throw=10000):
    """Test input with set of dices, return index of dice win
    :param: dices, 2d array of int
    :return: int
    """
    dice_wins = [0] * len(dices)
    for _ in range(n_throw):
        result = []
        for dice in dices:
            val = dice[random.randint(0, 5)]
            result.append(val)
        dice_wins[argmax(result)] += 1

    return argmax(dice_wins), max(dice_wins)


def test_case_best_dice(dices, i_best_dice, n_throw=10000):
    """Test case when best dice exist
    :param: dice, 2d array of int
    :param: i_best_dice, int
    :return: None
    """
    best_dice_exp, n_wins = best_dice_with_experience(dices, n_throw)
    if best_dice_exp != i_best_dice:
        print(f'No, best dice must be {best_dice_exp}(not {i_best_dice}) win {n_wins} rounds after {n_throw} throws')
    else:
        print(f'Good! Solution is best, dice {i_best_dice} win {n_wins} after 10000 throws')


def test_case_not_best_dice(dices, strategy, n_throw=10000):
    """Test case not best dice
    """
    n_dice = len(dices)
    for first_choice in range(n_dice):
        second_choice = strategy[first_choice]
        best_dice_exp, n_wins = best_dice_with_experience(
            [dices[first_choice], dices[second_choice]],
            n_throw
        )
        if best_dice_exp == second_choice:
            print(f'Good, if first person choice dice {first_choice}, second person choice dice {second_choice} win with number of win is {n_wins} after {n_throw} rounds')
        else:
            print(f'No, if first person choice dice {first_choice}, second person choice dice {second_choice} then first person win {n_wins} round after {n_throw} rounds')


if __name__ == '__main__':
    index = 0
    for dices in gen_data(n_set=10):
        print(f' Set {index} has {len(dices)} dices '.center(120, '-'))
        strategy = solution.compute_strategy(dices)
        if strategy['choose_first']:
            test_case_best_dice(dices, strategy['first_dice'])
        else:
            test_case_not_best_dice(dices, strategy, 100000)
        index += 1
