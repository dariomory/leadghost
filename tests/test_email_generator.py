"""Tests for the email generator module."""

from leadghost.email_generator.generator import generate_emails


def test_generate_emails_returns_non_empty():
    """generate_emails produces a non-empty list."""
    result = generate_emails("John", "Doe", "example.com")
    assert len(result) > 0


def test_generate_emails_all_have_domain():
    """Every generated email ends with the given domain."""
    domain = "acme.com"
    result = generate_emails("Jane", "Smith", domain)
    for email in result:
        assert email.endswith(f"@{domain}")


def test_generate_emails_contains_first_name_variant():
    """At least one email uses the first name alone."""
    result = generate_emails("Alice", "Jones", "test.org")
    assert "alice@test.org" in result


def test_generate_emails_contains_full_name_variant():
    """At least one email uses firstname.lastname."""
    result = generate_emails("Bob", "Lee", "corp.io")
    assert "bob.lee@corp.io" in result
