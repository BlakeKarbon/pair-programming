from datetime import date, datetime

def expirationStatus(expirationDate, today):

    days = (expirationDate - today).days

    if days < 0:
        return "EXPIRED"
    if days == 0:
        return "USE_TODAY"
    if days <= 3:
        return "USE_SOON"
    return "OK"


print(expirationStatus(date(2025,1,9),date(2025, 1, 10)))
