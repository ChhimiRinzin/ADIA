"""Read-only recovery calculations. Replace approved SQL views only after schema mapping."""
from dataclasses import dataclass
from decimal import Decimal
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

QUERY = text("""
SELECT COALESCE(SUM(amount_nu), 0) AS total
FROM recovery_payments
WHERE status = :status
""")

@dataclass(frozen=True)
class RecoverySummary:
    total: Decimal
    payment_count: int


def make_engine(url: str) -> Engine:
    return create_engine(url, future=True)


def fetch_summary(engine: Engine) -> RecoverySummary:
    """Count posted payments, not amounts marked due or pending.

    The demo uses one row per payment. Real definitions must be confirmed with RAA.
    """
    with engine.connect() as conn:
        total = conn.execute(QUERY, {'status': 'POSTED'}).scalar_one()
        count = conn.execute(text('SELECT COUNT(*) FROM recovery_payments WHERE status=:status'), {'status': 'POSTED'}).scalar_one()
    return RecoverySummary(total=Decimal(str(total)), payment_count=int(count))


def format_nu(amount: Decimal) -> str:
    return f'Nu. {amount:,.2f}'
