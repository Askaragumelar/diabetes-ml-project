Nama: Syahya Agung Pratama
Npm: 2441010
UAS Machine Learning




# Aplikasi Prediksi Penyakit Diabetes Berbasis Machine Learning

Aplikasi ini merupakan sistem prediksi penyakit diabetes menggunakan metode *Machine Learning* yang diintegrasikan dengan **FastAPI** sebagai backend dan **HTML, CSS, JavaScript** sebagai frontend.  
Aplikasi ini bertujuan untuk membantu memberikan **prediksi awal** berdasarkan data kesehatan pasien.

> Catatan: Hasil prediksi **bukan diagnosis medis**, melainkan alat bantu berbasis data.

---

## Latar Belakang
Diabetes merupakan salah satu penyakit kronis yang jumlah penderitanya terus meningkat.  
Dengan memanfaatkan Machine Learning, data kesehatan pasien dapat dianalisis untuk memberikan prediksi risiko diabetes secara cepat dan efisien.

---

##  Dataset & Fitur
Dataset yang digunakan mengacu pada data kesehatan dengan beberapa parameter utama, antara lain:

- Jumlah Kehamilan
- Kadar Glukosa (mg/dL)
- Tekanan Darah (mmHg)
- Ketebalan Kulit
- Insulin
- BMI (Body Mass Index)
- Riwayat Diabetes Keluarga
- Usia

---

##  Model Machine Learning
- Model dilatih menggunakan dataset kesehatan
- Model disimpan dalam format `.pkl`
- Backend menggunakan **FastAPI**
- Endpoint API menerima data JSON dan mengembalikan hasil prediksi

---

## Teknologi yang Digunakan
**Backend:**
- Python
- FastAPI
- Scikit-learn
- Uvicorn

**Frontend:**
- HTML
- CSS
- JavaScript
- Chart.js (Visualisasi Grafik)

---

## Cara Menjalankan Aplikasi

### Clone Repository
```bash
git clone https://github.com/username/diabetes-ml-project.git
cd diabetes-ml-project