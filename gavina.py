


def expirationStatus(expirationDate, today):
    if expiraationDate == None:
        raise Exception()

    days = expirationDate - today

    if days < 0:
        return "EXPIRED"
    elif days == 0:
        return "USE_TODAY"
    elif days >= 1 and days <= 3:
        return "USE_SOON"
    else:
        return "OK"









