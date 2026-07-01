import streamlit as st
import pandas as pd
import datetime

from model import Peminjaman
from manajer_perpustakaan import ManajerPerpustakaan
from konfigurasi import KATEGORI_BUKU

st.set_page_config(
    page_title="Sistem Manajemen Perpustakaan Kampus",
    layout="wide"
)

manajer = ManajerPerpustakaan()

st.title("📚 Sistem Manajemen Perpustakaan Kampus")

menu = st.sidebar.radio(
    "Menu",
    [
        "Tambah Peminjaman",
        "Riwayat",
        "Ringkasan"
    ]
)

# ===================================
# MENU TAMBAH PEMINJAMAN
# ===================================

if menu == "Tambah Peminjaman":

    st.header("Form Peminjaman Buku")

    with st.form("form_peminjaman"):

        nama = st.text_input(
            "Nama Mahasiswa"
        )

        buku = st.text_input(
            "Judul Buku"
        )

        kategori = st.selectbox(
            "Kategori Buku",
            KATEGORI_BUKU
        )

        tanggal_pinjam = st.date_input(
            "Tanggal Pinjam",
            datetime.date.today()
        )

        tanggal_kembali = st.date_input(
            "Tanggal Kembali",
            datetime.date.today()
        )

        simpan = st.form_submit_button(
            "Simpan Data"
        )

        if simpan:

            data = Peminjaman(
                nama,
                buku,
                kategori,
                tanggal_pinjam,
                tanggal_kembali
            )

            manajer.tambah_peminjaman(data)

            st.success(
                "Data peminjaman berhasil disimpan"
            )

# ===================================
# MENU RIWAYAT
# ===================================

elif menu == "Riwayat":

    st.header("Riwayat Peminjaman")

    df = manajer.get_dataframe_peminjaman()

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("Hapus Data")

    id_hapus = st.number_input(
        "Masukkan ID Peminjaman",
        min_value=1,
        step=1
    )

    if st.button("Hapus Data"):

        manajer.hapus_peminjaman(
            id_hapus
        )

        st.success(
            "Data berhasil dihapus"
        )

        st.rerun()

# ===================================
# MENU RINGKASAN
# ===================================

elif menu == "Ringkasan":

    st.header("Ringkasan Perpustakaan")

    total = manajer.hitung_total_peminjaman()

    st.metric(
        "Total Peminjaman Buku",
        total
    )

    kategori = manajer.get_per_kategori()

    if kategori:

        df_kategori = pd.DataFrame(
            list(kategori.items()),
            columns=[
                "Kategori",
                "Total"
            ]
        )

        st.subheader(
            "Jumlah Peminjaman per Kategori"
        )

        st.dataframe(
            df_kategori
        )

        st.bar_chart(
            df_kategori.set_index(
                "Kategori"
            )
        )