

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
# A manufacturer of metal pistons finds that, on average, %12 of the pistons they manufacture are rejected because they are incorrectly sized.
# What is the probability that a batch of 10 pistons will contain:
# 1. No more than 2 rejects
# 2. At least 2 rejects

pReject = 0.12

# b(X>=2; 10, pReject)
# b(X<=2; 10, pReject)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binom(x, n, p):
	return ( factorial(n) / (factorial(x) * factorial(n - x)) ) * ( p**x ) * ( (1-p)**(n-x) )

total = 0
for x in range(0,3):
	total += binom(x, 10, pReject)

print("{0:.3f}".format(total))


total = 0
for x in range(2,11):
	total += binom(x, 10, pReject)

print("{0:.3f}".format(total))