import random

def player(prev_play, opponent_history=[], my_history=[], play_order={}):
    counters = {"R": "P", "P": "S", "S": "R"}

    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
        play_order.clear()

    opponent_history.append(prev_play)

    n = 5
    guess = random.choice(["R", "P", "S"])

    if len(my_history) >= n:
        last_n = "".join(my_history[-n:])
        if last_n in play_order:
            likely_next = max(play_order[last_n], key=play_order[last_n].get)
            guess = counters[likely_next]

    if len(my_history) >= n:
        key = "".join(my_history[-n:])
        play_order.setdefault(key, {"R": 0, "P": 0, "S": 0})
        # we'll update this key's stats *after* we know what we actually played next

    my_history.append(guess)

    # update play_order retroactively now that my_history has grown
    if len(my_history) > n:
        key = "".join(my_history[-(n+1):-1])
        play_order.setdefault(key, {"R": 0, "P": 0, "S": 0})
        play_order[key][my_history[-1]] += 1

    return guess
