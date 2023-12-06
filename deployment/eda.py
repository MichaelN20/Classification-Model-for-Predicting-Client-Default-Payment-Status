# GRADED CHALLENGE 5
# Nama  : Michael Nathaniel
# Batch : HCK-009

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from phik.report import plot_correlation_matrix
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Explaration Data Analysis (EDA)')
    st.write('Analisis data lebih lanjut untuk mendapatkan wawasan')
    st.header('')

    # Memanggil data csv 
    data = pd.read_csv(r'Classification-Model-for-Predicting-Client-Default-Payment-Status.csv')

    # menampilakn 10 data teratas
    st.header('Menampilkan 10 data teratas')
    st.table(data.head(10))

    # menampilakn 10 data terbawah
    st.header('Menampilkan 10 data terbawah')
    st.table(data.tail(10))

    # Melihat distribusi data
    st.header('Melihat distribusi data')
    st.table(data.select_dtypes(include='number').agg(['count', 'skew', 'kurt', 'std', 'mean', 'median', 'min', 'max']))
    with st.expander("Penjalasan"):
        st.write(
            '''
            - Ada `beberapa data yang memiliki distribusi data yang tidak normal` dengan variasi tinggi seperti data limit_balance, bill_amt_(1-6), pay_amt_(1-6)
            - Namun, `ada juga data-data yang relatif normal distribusinya` seperti martial_status, pay_(0-6)
            ''')

    # Melihat distribusi data berdasarkan status default payment
    st.header('Melihat distribusi data berdasarkan status default payment')
    image = Image.open('Melihat distribusi data berdasarkan status default payment.png')
    st.image(image, caption='Figure 1: Melihat distribusi data berdasarkan status default payment')
    with st.expander("Penjalasan"):
        st.write(
            '''
            - Dari keterangan yang diperoleh dari sumber dataset, kita mendapati bahwa `0 mewakili mereka yang tidak mengalami default payment (gagal bayar) dan 1 mewakili mereka yang berstatus default payment`.
            - Dari visualisasi diatas, kita ketahui bahwa `jumlah orang yang tidak mengalami default payment (tunggakan/ gagal bayar) lebih banyak` daripada mereka yang default yaitu `dengan perbandingannya adalah 78.58% : 21.42%`
            ''')

    # Melihat distribusi data status default payment berdasarkan gender
    st.header('Melihat distribusi data status default payment berdasarkan gender')
    image = Image.open('Banyak Data Status Default Berdasarkan Gender.png')
    st.image(image, caption='Figure 2: Melihat distribusi data status default payment berdasarkan gender')
    with st.expander("Penjalasan"):
        st.write(
            '''
            - Dari keterangan yang diperoleh dari sumber dataset, kita mendapati bahwa `1 mewakili pria dan 2 mewakili wanita`.
            - Dari visualisasi diatas, kita ketahui bahwa `yang lebih banyak mengalami default payment adalah gender wanita dibandingkan pria` yaitu dengan `perbandingan yaitu 60.78% : 39.22%`
            ''')

    # Melihat distribusi data Jumlah Default dan Non-Default Payment Berdasarkan Education Level
    st.header('Melihat distribusi data Jumlah Default dan Non-Default Payment Berdasarkan Education Level')
    image = Image.open('Melihat distribusi data Jumlah Default dan Non-Default Payment Berdasarkan Education Level.png')
    st.image(image, caption='Figure 3: Melihat distribusi data Jumlah Default dan Non-Default Payment Berdasarkan Education Level')
    with st.expander("Penjalasan"):
        st.write(
            '''
            - Dari keterangan yang diperoleh dari sumber dataset, kita mendapati bahwa `1 mewakili graduate school (Tamatan S2 dan S3), 2 mewakili tamatan S1, 3 mewakili tamatan SMA, 4 mewakili others, 5 mewakili unknown`.
            - Dari visualisasi diatas, kita ketahui bahwa `anak kuliahan (S1) menjadi peminjam terbanyak disusul oleh Tamatan S2 dan S3 dan diurutan ketiga adalah tamatan SMA`.
            ''')

    # Melihat distribusi data limit_balance
    st.header('Melihat distribusi data limit_balance')
    image = Image.open('Melihat distribusi data limit_balance.png')
    st.image(image, caption='Figure 4: Melihat distribusi data limit_balance')

    # Melihat distribusi data pay (1-6)
    st.header('Melihat distribusi data pay (1-6)')
    image = Image.open('Melihat distribusi data pay (1-6).png')
    st.image(image, caption='Figure 5: Melihat distribusi data pay (1-6)')

    # Melihat distribusi data bill_amt (1-6)
    st.header('Melihat distribusi data bill_amt (1-6)')
    image = Image.open('Melihat distribusi data bill_amt (1-6).png')
    st.image(image, caption='Figure 6: Melihat distribusi data bill_amt (1-6)')

    # Melihat distribusi data pay_amt (1-6)
    st.header('Melihat distribusi data pay_amt (1-6)')
    image = Image.open('Melihat distribusi data pay_amt (1-6).png')
    st.image(image, caption='Figure 7: Melihat distribusi data pay_amt (1-6)')
    st.write('Dari visualisasi figur 4-7, kita bisa lihat bahwa ada banyak outliers pada data-data yang berupa nominal.')

    # Melihat korelasi data-data waktu terhadap harga
    st.header('Melihat korelasi data-data waktu terhadap harga')
    st.write(
        '''
        Untuk melakukan uji korelasi data dalam dataset terhadap `default_payment_next_mont`, kita bisa menggunakan metode uji korelasi seperti `metode kendall`.
        Metode kendall digunakan karena ada data kita yang bersifat kategorial seperti sex, education_level, martial_status.
        Berikut pengujiannya:
        '''
        )
    image = Image.open('Melihat korelasi data-data waktu terhadap harga.png')
    st.image(image, caption='Figure 8: Melihat korelasi data-data waktu terhadap harga')
    with st.expander("Penjalasan"):
        st.write(
            '''
            - Dari hasil uji korelasi, kita bisa melakukan `pemilihan kolom tertentu yang akan kita gunakan untuk pembuatan model`.
            - Mesikpun data limit_balance, bill_amt, dan pay_amt memilki korelasi yang sangat rendah terhadap default_payment_next_month, kita akan `tetap memasukkannya karena berdasarkan domain knowldege, data-data tersebut berisikan data history terdahulu yang dapat mempengaruhi keputusan default tidaknya seseorang`.
            ''')