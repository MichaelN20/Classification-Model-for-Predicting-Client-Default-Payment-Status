# GRADED CHALLENGE 5
# Nama  : Michael Nathaniel
# Batch : HCK-009

import streamlit as st
import eda
import models

page = st.sidebar.selectbox(label='Menu:', options=['Beranda', 'Exploration Data Analysis', 'Model Inference'])

if page == 'Beranda':
    st.title('Graded Challenge 5')
    st.write('FTDS - Phase 1')
    st.header('')

    col1, col2 = st.columns(2)

    # ======================= Columns 1 =======================
    col1.write('**Nama             :**')
    col1.write('**Batch            :**')
    col1.write('**Tujuan Milestone :**')

    # ======================= Columns 2 =======================
    col2.write('Michael Nathaniel')
    col2.write('HCK-009')
    col2.write("Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Classification dengan Logistic Regression, SVM, dan KNN, persiapan data dengan memperoleh data menggunakan BigQuery, mempersiapkan data untuk digunakan dalam model Logistic Regression, SVM, dan KNN, dan mengimplementasikan Logistic Regression, SVM, dan KNN untuk membuat prediksi.")

    st.header('')
    st.write('**Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!**')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Kita diberikan data mengenai status default payment kline-klien suatu bank. Dataset yang diberikan berisi id, limit balance, gender, martial status, repayment status bulan tertentu, jumlah bill statement, jumlah pembayaran tagihan sebelumnya, dan status default payment bulan selanjutnya. Dari data yang dimiliki kita diminta untuk membuat prediksi default payment client yang meminjam.')

    with st.expander("Problem Statement"):
        st.caption('Buatlah model Classification untuk memprediksi `default_payment_next_month` menggunakan dataset yang sudah kalian simpan.')

    with st.expander("Outline"):
        st.caption("1. Memuat data dan memeriksa informasi mengenai kumpulan data.")
        st.caption("2. EDA pada kumpulan data yang melibatkan analisis data lebih lanjut untuk mendapatkan wawasan.")
        st.caption("3. Feature Engineering untuk mendapatkan fitur dan target pemodelan.")
        st.caption("4. Mendefinisikan Model menggunakan pipeline.")
        st.caption("5. Melatih model.")
        st.caption("6. Evaluasi model yang terdiri dari hypertuning untuk mendapatkan model terbaik dengan hasil terbaik.")
        st.caption("7. Menyimpan modelnya.")
        st.caption("8. Kesimpulan.")
        st.caption("9. Deployment.")

    with st.expander("Kesimpulan"):
        st.caption("Dataset yang kita miliki merupakan data yang bersih dimana tidak ditemukan adanya missing values. Kita temukan bahwa ada sebanyak `23 kolom` dengan `2,965 data entries`. Data-data yang dimiliki dataset ini mayoritas memiliki distribusi yang tidak normal.")
        st.caption("Mayoritas peminjam adalah mereka yang merupakan tamatan S1`, disusul dengan tamatan S2-S3, dan diikuti oleh tamatan SMA. Kita temukan bahwa `78.58% orang yang terdaftar pada dataset kita dikategorikan aman dari default payment/ TIDAK gagal bayar`.")
        st.caption("Dari hasil uji korelasi kita temukan bahwa data-data seperti `limit_balance, sex, education_level, martial_status, age, bill_amt, dan pay_amt memiliki korelasi yang sangat rendah. Namun kita tetap akan memasukan limit_balance, pay, bill_amt, dan pay_amt kedalam data untuk pemodelan kita berdasarkan domain knowldege karena kita menganggap hal-hal ini mempengaruhi.` Begitupun dengan Multicollinearity, kita temukan adanya korelasi tinggi antar variabel independen pada data-data bill_amt dan akan tetap digunakan karena alasan yang sama.")
        st.caption("Dari keseluruhan uji model kita memperoleh bahwa kita akan melakukan prediksi klasifikasi default payment menggunakan model `Logistic Regression yang di perbaiki dengan Hyperparameter Tuning`. Dibandingkan dengan metode SVM dan KNN, `model Logistic Regression memiliki hasil yang jauh lebih baik dalam hal prediksi, akurasi, dan fittingnya`. Logistic Regression mendapatkan hasil yang lebih tidak ekstrem fittingnya.")
        st.caption("Menurut hasil evaluasi model yang diujikan (Logistic regression), `kita memperoleh model yang fit antara uji train dengan tes`t meskipun precision untuk mendeteksi default paymentnya 0.50 dari 1.0. Intercept dari model ini adalah -0.08345099 yang menjadi nilai awal default payment jiak variabel lainnya 0. Melihat dari hasil coefficientnya, kita peroleh bahwa tidak semua variabel yang digunakan pada model ini memberikan dampak terhadap target (default_payment_next_month).')")

elif page == 'Exploration Data Analysis':
    eda.run()
else:
    models.run()