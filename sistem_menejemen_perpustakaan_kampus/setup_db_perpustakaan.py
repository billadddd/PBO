import sqlite3
from konfigurasi import DB_PATH

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS peminjaman (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_mahasiswa TEXT NOT NULL,
    judul_buku TEXT NOT NULL,
    kategori TEXT,
    tanggal_pinjam DATE NOT NULL,
    tanggal_kembali DATE NOT NULL
)
""")

conn.commit()

conn.close()