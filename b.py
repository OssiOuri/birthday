import decimal

def p(n, p_sum):
    """Function p computes the number of people (by simulation) that must enter a room
    until two of them share a birthday. It is assumed birthdays are independent
    and uniform from 0 to 364. Number of people is written to standard output.

    n - is the number of persons in the room
    p_sum - means the probability that everybody in the room have different birthdays
    p_sum = p(1) AND p(2) AND p(3) AND... so p_sum = p(1)*p(2)*p(3) and so on on each recursio.

    p_new is the probability that a new person entering room has different birthday than those already in the room.
    on the first round, p_new = p_new(1), there is 1 person and probability for different birthday is 1 ((366-1)/365)
    on the second round, p_new = p_new(2), there are 2 persons and probability the newcomer has different birthday 
    than the one in the room is ((366-2)/365) and so on... so p is calculated on each round p_new(3), p_new(4), ...

    If p_sum is the probability that everybody in room have different birthday then p_same_birthday = (1 - p_sum)
    is the probability that at least some 2 persons have some same birthday.
    """
        
    # decimal class is needed for accurate decimal calculation
    p_new = decimal.Decimal((366-n) / 365.)
    p_sum = decimal.Decimal(p_sum * p_new)
    p_same_birthday = decimal.Decimal(1 - p_sum)

    if p_same_birthday == 1:
        # probability is 100%, so now there are at least 2 persons having the same birthday
        return n
    else:
        n = p(n+1, p_sum)
        return n

if __name__ == '__main__':
    myOtherContext = decimal.Context(prec=256)
    decimal.setcontext(myOtherContext)

    # initial values for counting n: n = 1, p_sum = 1 (everybody have different birthday)
    n = p(1, 1)
    print n

