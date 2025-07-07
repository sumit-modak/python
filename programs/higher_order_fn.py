def divisor(x):
    def dividend(y):
        return y / x
    return dividend

print(divisor(2)(10))