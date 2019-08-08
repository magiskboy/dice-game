We will implement together a program that will play optimally in a tricky dice game! You program will be given a list of dices and will decide who chooses the dice first (you or your opponent).

When the dices are chosen, we will simulate 10000 throws. Each time your number is greater, you get $1 from your opponent. Conversely, each time your number is smaller, you pay $1 to your opponent.
Implement a function that takes a list of dices (possibly more than three) and returns a strategy. The strategy is a dictionary:

If, after analyzing the given list of dices, you decide to choose a dice first, set strategy["choose_first"] to True and set strategy["first_dice"] to be the (0-based) index of the dice you would like to choose

If you would like to be the second one to choose a dice, set strategy["choose_first"] to False. Then, specify, for each dice that your opponent may take, the dice that you would take in return. Namely, for each i from 0 to len(dices)-1, set strategy[i] to an index j of the dice that you would take if the opponent takes the i-th dice first.

### For test

```bash
$ python test.py
```
