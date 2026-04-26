"""Tests for package imports and public API."""

import leadghost


def test_package_imports():
    """Verify the package can be imported."""
    assert leadghost


def test_version_defined():
    """Package exposes a version string."""
    assert isinstance(leadghost.__version__, str)
    assert len(leadghost.__version__) > 0


def test_bot_exported():
    """Bot class is accessible from the top-level package."""
    assert leadghost.Bot is not None


def test_selenium_bot_exported():
    """SeleniumBot class is accessible from the top-level package."""
    assert leadghost.SeleniumBot is not None


def test_generate_md5_exported():
    """generate_md5 utility is accessible from the top-level package."""
    assert callable(leadghost.generate_md5)
