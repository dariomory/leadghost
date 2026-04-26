"""Tests for the leadghost CLI."""

from typer.testing import CliRunner

from leadghost.cli import app

runner = CliRunner()


def test_main_exits_zero():
    """CLI main command exits with code 0."""
    result = runner.invoke(app, ["main"])
    assert result.exit_code == 0


def test_main_prints_banner():
    """CLI main command prints the LeadGhost banner."""
    result = runner.invoke(app, ["main"])
    assert "LeadGhost" in result.output
