"""Tests for Bot scraper logic (no browser required)."""

from leadghost.bot import Bot


def test_average_company_size():
    """average_company_size parses employee range strings."""
    assert Bot.average_company_size("10-50") == 30.0
    assert Bot.average_company_size("1,000-5,000") == 3000.0


def test_highest_company_size():
    """highest_company_size returns the upper bound."""
    assert Bot.highest_company_size("10-50") == 50
    assert Bot.highest_company_size("1,000-5,000") == 5000


def test_highest_company_size_no_numbers():
    """highest_company_size returns 1 when no numbers are found."""
    assert Bot.highest_company_size("Unknown") == 1


def test_lowercase_set():
    """lowercase_set converts list to a lowercased set."""
    result = Bot.lowercase_set(["Hello", "WORLD", "Test"])
    assert result == {"hello", "world", "test"}


def test_get_after_list_found():
    """get_after_list returns the element after the matching term."""
    li = ["header", "Company Name", "Acme Corp", "other"]
    assert Bot.get_after_list(li, "Company Name") == "Acme Corp"


def test_get_after_list_not_found():
    """get_after_list returns None when term is missing."""
    assert Bot.get_after_list(["a", "b"], "missing") is None
