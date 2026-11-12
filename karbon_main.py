#Partner: Blake Karbon | Branch: solo/blake | Start: 10:08 | Stop: 10:28 | Finished: Yes | Tests: 8.
# * 94663b6 (HEAD -> solo/blake) Wrong value checks
# * 63de610 None checks
# * 777b1da pytest testing
# * d7c5233 bounds and outputs
# * acbe452 base day calculation
# * a05d237 (tag: keep-base, origin/main, origin/HEAD, main) Base

from datetime import date, datetime

def expirationStatus(expirationDate, today):
    if expirationDate is None or today is None:
        raise ValueError("expirationDate and today are required")

    if (not isinstance(expirationDate, date) or isinstance(expirationDate, datetime) or not isinstance(today, date) or isinstance(today, datetime)):
        raise TypeError("expirationDate and today must be date objects")

    days = (expirationDate - today).days

    if days < 0:
        return "EXPIRED"
    if days == 0:
        return "USE_TODAY"
    if days <= 3:
        return "USE_SOON"
    return "OK"
