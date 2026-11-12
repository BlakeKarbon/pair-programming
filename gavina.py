"""Partner: Michael Gavina | Branch: solo/mikey | Start: 10:08 | Stop: 10:28 | Finished: Yes | Tests: 5 """


def expirationStatus(expirationDate, today):
    if expirationDate == None:
        raise TypeError("Expiration Date has no date")

    days = expirationDate - today

    if days < 0:
        return "EXPIRED"
    elif days == 0:
        return "USE_TODAY"
    elif days >= 1 and days <= 3:
        return "USE_SOON"
    else:
        return "OK"


def testError():
    try: 
        expirationStatus(None, 10)
    except TypeError as e:
        if e == TypeError("Expiration Date has no date"):
            print("Pass")
    else:
        print("Fail")




def testExpired():
    word = expirationStatus(1, 10)
    if word == "EXPIRED":
        print("Pass")
    else:
        print("Fail")


def testToday():
    word = expirationStatus(1, 1)
    if word == "USE_TODAY":
        print("Pass")
    else:
        print("Fail")


def testSoon():
    word = expirationStatus(2, 1) 
    if word == "USE_SOON":
        print("Pass")
    else:
        print("Fail")


def testOk():
    word = expirationStatus(10, 1)
    if word == "OK":
        print("Pass")
    else:
        print("Fail")




testError()
testExpired()
testToday()
testSoon()
testOk()

