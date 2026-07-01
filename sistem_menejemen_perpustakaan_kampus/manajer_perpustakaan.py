from model import Peminjaman
import database


class ManajerPerpustakaan:

    def tambah_peminjaman(self, data: Peminjaman):

        sql = """
        INSERT INTO peminjaman
        (
            nama_mahasiswa,
            judul_buku,
            kategori,
            tanggal_pinjam,
            tanggal_kembali
        )
        VALUES (?, ?, ?, ?, ?)
        """

        params = (
            data.nama_mahasiswa,
            data.judul_buku,
            data.kategori,
            data.tanggal_pinjam,
            data.tanggal_kembali
        )

        return database.execute_query(sql, params)


    def get_dataframe_peminjaman(self):

        sql = """
        SELECT *
        FROM peminjaman
        ORDER BY id DESC
        """

        return database.get_dataframe(sql)


    def hitung_total_peminjaman(self):

        sql = """
        SELECT COUNT(*)
        FROM peminjaman
        """

        hasil = database.fetch_query(
            sql,
            fetch_all=False
        )

        if hasil:
            return hasil[0]

        return 0


    def get_per_kategori(self):

        sql = """
        SELECT kategori,
               COUNT(*) AS total
        FROM peminjaman
        GROUP BY kategori
        """

        rows = database.fetch_query(sql)

        data = {}

        if rows:

            for row in rows:

                data[row["kategori"]] = row["total"]

        return data


    def hapus_peminjaman(self, id_peminjaman):

        sql = """
        DELETE FROM peminjaman
        WHERE id = ?
        """

        return database.execute_query(
            sql,
            (id_peminjaman,)
        )