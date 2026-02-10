import os
DATA_DIR = os.path.expanduser('~/.pgadmin4_data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')

