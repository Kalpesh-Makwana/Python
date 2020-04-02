from itertools import combinations_with_replacement
MAX = 20


def find_fewest_coins(coins, target):
    """
    return exact change with fewest coins
    """
    if target == 0:
        return []
    num = 1
    while num < MAX:
        echange = [
            change
            for change in combinations_with_replacement(coins, num)
            if sum(change) == target
        ]
        if len(echange):
            return list(echange[0])
        num += 1

    raise (ValueError("Exact change not possible"))