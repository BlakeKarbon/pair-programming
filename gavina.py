


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
    except TypeError:
        print("Test is green")
    else:
        print("Test Failed")



def testExpired():
    word = expirationStatus(1, 10)
    print(word)

def testToday():
    word = expirationStatus(1, 1)
    print(word)

#def testSoon():


#def testOk():


testToday()



