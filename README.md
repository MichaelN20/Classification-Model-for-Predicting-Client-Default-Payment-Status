# **Classification-Model-for-Predicting-Client-Default-Payment-Status**

### **URL:**

[Deployment](https://huggingface.co/spaces/michaeln20/Classification-Model-for-Predicting-Client-Default-Payment-Status)

### **Informasi Dataset:**

Dataset yang digunakan berisikan data-data mengenai kredit klien yang membantu kita memahami dan memprediksi kemampuan klien membayar kredit pada bulan berikutnya.

### **SMART framework:**

1. **Specific**: Membangun model klasifikasi untuk memprediksi status pembayaran kredit klien pada bulan berikutnya berdasarkan variabel-variabel seperti batas kredit, jenis kelamin, tingkat pendidikan, status pernikahan, usia, dan riwayat pembayaran sebelumnya.

2. **Measurable**: Menggunakan metrik evaluasi klasifikasi seperti akurasi, presisi, recall, dan F1-score untuk mengukur kinerja model.

3. **Achievable**: Menggunakan dataset dengan 2965 entri dan 24 kolom untuk melatih dan menguji model klasifikasi.

4. **Relevant**: Model ini relevan untuk memahami dan memprediksi kemampuan klien membayar kredit pada bulan berikutnya, memberikan wawasan yang berharga untuk manajemen risiko kredit.

5. **Time-Bound**: Menyelesaikan pengembangan model dan evaluasi kinerja dalam batas waktu yang ditentukan.

### **Objective:**

Tujuan utama proyek ini adalah mengembangkan model klasifikasi yang dapat memprediksi dengan akurat status pembayaran kredit klien pada bulan berikutnya. Evaluasi kinerja model dengan metrik akurasi, presisi, recall, dan F1-score. Optimasi model menggunakan GridSearchCV. Implementasi model untuk prediksi pada data klien baru. Penyusunan laporan hasil evaluasi dan wawasan terkait faktor-faktor risiko kredit.

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
