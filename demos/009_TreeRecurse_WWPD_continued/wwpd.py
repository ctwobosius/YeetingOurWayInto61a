def get(grip):
    get = lambda: grip - 10
    while grip - get() > -10:

        grip = get() - 10
        print(grip)
        if grip < -100:
            return grip
    return grip

def confuse(confuse):
    if print(confuse, confuse):
        print(confuse + 10)
    if confuse:
        confuse = confuse + confuse + confuse / 2
    if confuse > 0:
        return confuse
    print(confuse + 10)

# WWPD: Put these in your terminal to check the answer
# print(print)(2019)
# confuse(10)
# get(23)
