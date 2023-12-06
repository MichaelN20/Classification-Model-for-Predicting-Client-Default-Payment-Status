# **Classification-Model-for-Predicting-Client-Default-Payment-Status**

### **Informasi Dataset:**

Dataset yang digunakan berisikan data-data mengenai kredit klien yang membantu kita memahami dan memprediksi kemampuan klien membayar kredit pada bulan berikutnya.

### **SMART framework:**

1. **Specific**: Membangun model Regresi Linear untuk memprediksi harga perjalanan pada layanan ride-hailing Uber dan Lyft di Boston, Massachusetts, berdasarkan berbagai faktor seperti jenis layanan, lokasi, jarak, cuaca, dll.

2. **Measurable**: Menilai kinerja model menggunakan metrik seperti Mean Squared Error (MSE) dan R-squared untuk mengukur tingkat akurasi dalam memprediksi harga perjalanan.

3. **Achievable**: Memanfaatkan dataset yang disediakan yang berisi informasi perjalanan ride-hailing untuk membangun dan melatih model Regresi Linear untuk prediksi tarif.

4. **Relevant**: Model ini menangani kebutuhan praktis untuk memprediksi dengan akurat harga perjalanan ride-hailing, memberikan wawasan berharga bagi pengguna dan perusahaan ride-hailing.

5. **Time-Bound**: Bertujuan untuk menyelesaikan pengembangan model dan evaluasi dalam batas waktu tertentu, memastikan pengiriman wawasan dan prediksi yang berguna untuk implementasi praktis.

### **Objective:**

Tujuan dari penelitian ini adalah mengembangkan dan menerapkan model Regresi Linear untuk memprediksi harga perjalanan pada layanan ride-hailing di Boston, Massachusetts, dengan mempertimbangkan variabel-variabel seperti jenis layanan, lokasi, jarak, dan kondisi cuaca. Penelitian ini menggunakan dataset yang disediakan oleh Uber dan Lyft. Fokus utama adalah meningkatkan akurasi prediksi harga perjalanan, dengan harapan memberikan wawasan yang berharga bagi pengguna dan perusahaan ride-hailing.

### **Conceptual Problems:**
1. Sebutkan dan jelaskan asumsi yang dipakai oleh Linear Regression ! (Gunakan bahasa anda sendiri)
2. Tunjukkan dan tafsirkan arti dari slope dan intercept yang didapat dari model yang telah Anda bangun !

### **Tools:**
- **Data Retrieval:** SQL
- **Data Manipulation:** Python, Pandas, Numpy
- **Statistical Analysis:** Scipy, Statsmodels
- **Visualization:** Matplotlib, Seaborn
- **Feature Engineering:** Phik, Variance Inflation Factor (VIF), Winsorizer
- **Machine Learning:** Scikit-Learn (LogisticRegression, KNeighborsClassifier, SVC, GridSearchCV)
- **Model Evaluation:** Classification Report, Confusion Matrix, ConfusionMatrixDisplay, F1 Score, Accuracy Score, Precision Score, Recall Score
- **Preprocessing:** RobustScaler, Winsorizer
- **Data Splitting:** train_test_split
- **Pipeline:** make_pipeline
- **Column Transformation:** make_column_transformer
- **Model Persistence:** pickle
