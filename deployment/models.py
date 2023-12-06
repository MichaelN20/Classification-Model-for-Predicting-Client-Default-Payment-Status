# GRADED CHALLENGE 5
# Nama  : Michael Nathaniel
# Batch : HCK-009

import streamlit as st
import pandas as pd
import pickle
from PIL import Image

def run():
# Load All Files

    st.title('Model Inference')
    st.write('Silahkan berikan imputasi data untuk dilakukan prediksi')
    st.header('')

    with open('model_logistic_regression.pkl', 'rb') as file:
        full_process = pickle.load(file)

    limit_balance = st.number_input(label='Masukkan limit balance',min_value=0.0)
    
    sex = st.selectbox(label='Pilih gender (1= Pria, 2= Wanita)',options=[1, 2])

    education_level = st.selectbox(label='Pilih education level (1=Graduate School, 2=University, 3=High School, 4=Others, 5=Unknown)',options=[1, 2, 3, 4, 5])

    marital_status = st.selectbox(label='Pilih martial status (1=Married, 2=Single, 3=Others)',options=[1, 2, 3])

    age = st.number_input(label='Masukkan umur',min_value=0.0)

    pay_1 = st.selectbox(label='Masukkan Status pelunasan pada bulan September 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_2 = st.selectbox(label='Masukkan Status pelunasan pada bulan Agustus 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_3 = st.selectbox(label='Masukkan Status pelunasan pada bulan Juli 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_4 = st.selectbox(label='Masukkan Status pelunasan pada bulan Juni 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_5 = st.selectbox(label='Masukkan Status pelunasan pada bulan Mei 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    pay_6 = st.selectbox(label='Masukkan Status pelunasan pada bulan April 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)',options=[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    bill_amt_1 = st.number_input(label='Masukkan Jumlah tagihan bulan September 2005 (dolar NT)',min_value=0.0)
    bill_amt_2 = st.number_input(label='Masukkan Jumlah tagihan bulan Agustus 2005 (dolar NT)',min_value=0.0)
    bill_amt_3 = st.number_input(label='Masukkan Jumlah tagihan bulan Juli 2005 (dolar NT)',min_value=0.0)
    bill_amt_4 = st.number_input(label='Masukkan Jumlah tagihan bulan Juni 2005 (dolar NT)',min_value=0.0)
    bill_amt_5 = st.number_input(label='Masukkan Jumlah tagihan bulan Mei 2005 (dolar NT)',min_value=0.0)
    bill_amt_6 = st.number_input(label='Masukkan Jumlah tagihan bulan April 2005 (dolar NT)',min_value=0.0)
    
    pay_amt_1 = st.number_input(label='Masukkan Jumlah pembayaran sebelumnya pada bulan September 2005 (dolar NT)',min_value=0.0)
    pay_amt_2 = st.number_input(label='Masukkan Jumlah pembayaran sebelumnya pada bulan Agustus 2005 (dolar NT)',min_value=0.0)
    pay_amt_3 = st.number_input(label='Masukkan Jumlah pembayaran sebelumnya pada bulan Juli 2005 (dolar NT)',min_value=0.0)
    pay_amt_4 = st.number_input(label='Masukkan Jumlah pembayaran sebelumnya pada bulan Juni 2005 (dolar NT)',min_value=0.0)
    pay_amt_5 = st.number_input(label='Masukkan Jumlah pembayaran sebelumnya pada bulan Mei 2005 (dolar NT)',min_value=0.0)
    pay_amt_6 = st.number_input(label='Masukkan Jumlah pembayaran sebelumnya pada bulan April 2005 (dolar NT)',min_value=0.0)
    
    st.write('Berikut hasil data yang anda input :')
    
    data_inf = pd.DataFrame({
        "limit_balance": limit_balance,
        "sex": sex,
        "education_level": education_level,
        "marital_status": marital_status,
        "age": age,
        "pay_1": pay_1,
        "pay_2": pay_2,
        "pay_3": pay_3,
        "pay_4": pay_4,
        "pay_5": pay_5,
        "pay_6": pay_6,
        "bill_amt_1": bill_amt_1,
        "bill_amt_2": bill_amt_2,
        "bill_amt_3": bill_amt_3,
        "bill_amt_4": bill_amt_4,
        "bill_amt_5": bill_amt_5,
        "bill_amt_6": bill_amt_6,
        "pay_amt_1": pay_amt_1,
        "pay_amt_2": pay_amt_2,
        "pay_amt_3": pay_amt_3,
        "pay_amt_4": pay_amt_4,
        "pay_amt_5": pay_amt_5,
        "pay_amt_6": pay_amt_6
        }, index=[0])

    st.table(data_inf)


    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = full_process.predict(data_inf)

        if y_pred_inf[0] == 1:
            st.write('Kliennya AKAN Default Payment pada bulan selanjutnya')
        else:
            st.write('Kliennya TIDAK AKAN Default Payment pada bulan selanjutnya')