def jackie_bananas(piles, h):
    k = 1
    new_h = h + 1

    for x in piles:
        if (x < 1):
            return -1

    if (len(piles) > h or len(piles) < 1):
        return -1

    while (new_h > h):
        new_h = 0
        for x in piles:
            if (k >= x):
                new_h += 1
            elif (k == 1 or x % k == 0):
                new_h += x // k
            else:
                new_h += 1 + x // k

        if (new_h > h):
            k += 1
    return k


if __name__ == "__main__":
    print(jackie_bananas([3, 6, 7, 11], 8))
    print(jackie_bananas([30, 11, 23, 4, 20], 5))
    print(jackie_bananas([30, 11, 23, 4, 20], 6))

