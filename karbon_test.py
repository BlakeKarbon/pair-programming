#Partner: Blake Karbon | Branch: solo/blake | Start: 10:08 | Stop: 10:28 | Finished: Yes | Tests: 8.

from datetime import date
import pytest

from karbon_main import expirationStatus


@pytest.mark.parametrize(
    ("expiration_date", "today", "expected"),
    [
        (date(2025, 1, 9), date(2025, 1, 10), "EXPIRED"),
        (date(2025, 1, 10), date(2025, 1, 10), "USE_TODAY"),
        (date(2025, 1, 11), date(2025, 1, 10), "USE_SOON"),
        (date(2025, 1, 13), date(2025, 1, 10), "USE_SOON"),
        (date(2025, 1, 14), date(2025, 1, 10), "OK"),
    ],
)
def test_expiration_status(expiration_date, today, expected):
    assert expirationStatus(expiration_date, today) == expected


@pytest.mark.parametrize(
    ("expiration_date", "today"),
    [
        (None, date(2025, 1, 10)),
        (date(2025, 1, 10), None),
    ],
)
def test_missing_date_raises_error(expiration_date, today):
    with pytest.raises(ValueError):
        expirationStatus(expiration_date, today)


def test_wrong_type_raises_error():
    with pytest.raises(TypeError):
        expirationStatus("2025-01-10", date(2025, 1, 10))
