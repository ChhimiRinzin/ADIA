"""Creates fictional data in a local SQLite database ONLY; never production."""
from pathlib import Path
from sqlalchemy import create_engine, text
from config import BASE_DIR

DB = BASE_DIR / 'data' / 'demo.db'

def create_demo_database(path: Path = DB) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    engine = create_engine(f'sqlite:///{path}')
    with engine.begin() as conn:
        conn.execute(text('DROP TABLE IF EXISTS recovery_payments'))
        conn.execute(text('''CREATE TABLE recovery_payments (
            id INTEGER PRIMARY KEY, observation_id TEXT NOT NULL,
            amount_nu NUMERIC(15,2) NOT NULL CHECK(amount_nu >= 0),
            status TEXT NOT NULL CHECK(status IN ('POSTED','PENDING','VOID')),
            payment_date TEXT NOT NULL,
            receipt_ref TEXT
        )'''))
        conn.execute(text('''INSERT INTO recovery_payments
            (id, observation_id, amount_nu, status, payment_date, receipt_ref)
            VALUES (:id,:obs,:amount,:status,:date,:receipt)'''), [
            {'id': 1, 'obs':'OBS-001','amount':'25000.00','status':'POSTED','date':'2026-01-20','receipt':'receipts/sample-001.pdf'},
            {'id': 2, 'obs':'OBS-002','amount':'40000.00','status':'POSTED','date':'2026-02-12','receipt':'receipts/sample-002.jpg'},
            {'id': 3, 'obs':'OBS-001','amount':'15000.00','status':'POSTED','date':'2026-03-16','receipt':'receipts/sample-003.png'},
            {'id': 4, 'obs':'OBS-003','amount':'10000.00','status':'PENDING','date':'2026-04-01','receipt':None},
            {'id': 5, 'obs':'OBS-004','amount':'9000.00','status':'VOID','date':'2026-04-12','receipt':None},
        ])
    engine.dispose()

if __name__ == '__main__':
    create_demo_database()
    print(f'Created fictional demo database: {DB}')
