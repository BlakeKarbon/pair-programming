


def expirationStatus(expirationDate, today):
    if expirationDate == None:
        raise TypeError()

    days = expirationDate - today

    if days < 0:
        return "EXPIRED"
    elif days == 0:
        return "USE_TODAY"
    elif days >= 1 and days <= 3:
        return "USE_SOON"
    else:
        return "OK"


def testExpired():

    try: 
        expirationStatus(None, 10)
    except TypeError:
        print("Test is green")
    else:
        print("Test Failed")


#def testToday():


#def testSoon():


#def testOk():




testExpired()



