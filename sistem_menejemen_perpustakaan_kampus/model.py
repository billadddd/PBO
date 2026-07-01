class Peminjaman:

    def __init__(
        self,
        nama_mahasiswa,
        judul_buku,
        kategori,
        tanggal_pinjam,
        tanggal_kembali,
        id_peminjaman=None
    ):

        self.id = id_peminjaman
        self.nama_mahasiswa = nama_mahasiswa
        self.judul_buku = judul_buku
        self.kategori = kategori
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali