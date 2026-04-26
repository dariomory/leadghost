"""Tests for utility functions."""

from leadghost.utils import generate_md5


def test_generate_md5_returns_hex_string():
    """generate_md5 returns a 32-character hex digest."""
    result = generate_md5("hello")
    assert isinstance(result, str)
    assert len(result) == 32


def test_generate_md5_deterministic():
    """Same input always produces the same hash."""
    assert generate_md5("test") == generate_md5("test")


def test_generate_md5_different_inputs():
    """Different inputs produce different hashes."""
    assert generate_md5("a") != generate_md5("b")
