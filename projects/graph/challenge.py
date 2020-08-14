
def challenge(arrays):
    result = 0

    for arr in arrays:
        result += min(arr) 

    return result

print(challenge([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]))

