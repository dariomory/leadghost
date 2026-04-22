"""Email generation and validation utilities."""

from .EmailGenerator import EmailGenerator, get_first_and_last_name
from .generator import generate_emails
from .validator import check_email, get_records, check_catchall

__all__ = [
    "EmailGenerator",
    "get_first_and_last_name",
    "generate_emails",
    "check_email",
    "get_records",
    "check_catchall",
]
