from decimal import Decimal
from pathlib import Path
from sqlalchemy import create_engine, text
from recovery import fetch_summary, format_nu
from seed_demo import create_demo_database


def test_demo_summary(tmp_path: Path):
    db = tmp_path / 'demo.db'
    create_demo_database(db)
    engine = create_engine(f'sqlite:///{db}')
    try:
        summary = fetch_summary(engine)
        assert summary.total == Decimal('80000')
        assert summary.payment_count == 3
        assert format_nu(summary.total) == 'Nu. 80,000.00'
    finally:
        engine.dispose()


def test_empty_posted(tmp_path: Path):
    db = tmp_path / 'demo.db'
    create_demo_database(db)
    engine = create_engine(f'sqlite:///{db}')
    try:
        with engine.begin() as conn:
            conn.execute(text("UPDATE recovery_payments SET status='VOID' WHERE status='POSTED'"))
        summary = fetch_summary(engine)
        assert summary.total == Decimal('0')
        assert summary.payment_count == 0
    finally:
        engine.dispose()


def test_partial_payments_are_summed(tmp_path: Path):
    db = tmp_path / 'demo.db'
    create_demo_database(db)
    engine = create_engine(f'sqlite:///{db}')
    try:
        with engine.begin() as conn:
            conn.execute(text("INSERT INTO recovery_payments (observation_id,amount_nu,status,payment_date) VALUES ('OBS-001',125.50,'POSTED','2026-05-02')"))
        assert fetch_summary(engine).total == Decimal('80125.5')
    finally:
        engine.dispose()
