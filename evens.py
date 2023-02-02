evens = []
def highest_even(li):
    for value in li:
        if value % 2 == 0:
            evens.append(value)
    return max(evens)
print(highest_even([666,000,111,222,333,444,555,666]))
