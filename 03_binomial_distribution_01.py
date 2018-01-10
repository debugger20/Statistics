

# Some definitions
# A Random Variable is a set of possible values from a random experiment.

# A binomial experiment is a statistical experiment that has the following properties:
# 1. The experiment consists of n repeated times.
# 2. The trials are independent.
# 3. The outcome of each trial is either success or failure.

# b(x; n, P): Binomial probability - the probability that an n-trial binomial experiment results in exactly x successes, when the probability of success on an individual trial is P.

# b(x; n, P) = nCx * P^x * (1 - P)^n - x

# b(x; n, P) = { n! / x! * (n-x)! } * P^x * (1 - P)^n - x

# Example:
# Suppose a die is tossed 5 times. What is the probability of getting exactly 2 fours?

# b(2; 5, 1/6)
# = { 5! / 2! * 3! } * (0.167)^2 * (0.833)^3
# = 0.161

# A cumulative binomial probability refers to the probability that the binomial random variable falls within a specified range.
# b(x<=3; n, p) = b(x=0; n, p) + b(x=1; n, p) + b(x=2; n, p) + b(x=3; n, p)


# TASK
# The ratio of boys to girls for babies born in Russia is 1.09:1
# If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

pBoy  = 1.09 / 2.09
pGirl = 1 - pBoy

# b(X>=3; 6, pBoy)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binom(x, n, p):
	return ( factorial(n) / factorial(x) * factorial(n - x) ) * ( p**x ) * ( (1-p)**(n-x) )


total = 0
for x in range(3,7):
	total += binom(x, 6, pBoy)

print("{0:.3f}".format(total))