import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = os.environ.get('ADIA_DATABASE_URL', f'sqlite:///{BASE_DIR / "data" / "demo.db"}')
CURRENCY = 'Nu.'
