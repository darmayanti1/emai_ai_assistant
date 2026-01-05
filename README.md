# ✉️ AI Email Professional Assistant

AI Email Professional Assistant adalah aplikasi berbasis web yang dibangun menggunakan **Python** dan **Streamlit** dengan dukungan **Large Language Model (Google Gemini)**.  
Aplikasi ini berfungsi untuk mengubah pesan informal atau poin kasar menjadi **draf email profesional** dengan format resmi dan bahasa yang dapat disesuaikan.

---

## 🎯 Tujuan Aplikasi
- Membantu pengguna menyusun email profesional dengan cepat
- Mengurangi kesalahan tata bahasa dan struktur email
- Menyesuaikan format email berdasarkan **bahasa** dan **nada bicara**
- Memberikan tampilan preview email yang rapi dan formal

---

## 🚀 Fitur Utama
- ✍️ Konversi pesan informal menjadi email profesional
- 🌐 Pilihan bahasa: **Bahasa Indonesia** dan **English**
- 🎨 Pilihan nada bicara: Sangat Formal, Formal, Ramah & Sopan, Tegas
- 📧 Format email resmi (header, isi, penutup)
- 🖥️ Antarmuka berbasis Streamlit
- 🔐 Keamanan API Key menggunakan file `.env`

---

## 🧠 Teknologi yang Digunakan
- Python 3.10+
- Streamlit
- Google Gemini API
- Prompt Engineering
- HTML & CSS (Streamlit Styling)

---

## 📁 Struktur Folder
```
emai_ai_assistant/
│
├── app.py
├── services/
│   └── email_generator.py
├── ui/
│   └── layout.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalasi & Menjalankan Aplikasi

### 1️⃣ Clone Repository
```bash
git clone code
cd email-ai_assistant
```

### 2️⃣ Buat Virtual Environment (Opsional)
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variable
Buat file `.env` di root folder:
```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```



---

## ▶️ Menjalankan Aplikasi
```bash
streamlit run app.py
```

---

## 🧪 Contoh Penggunaan
**Input:**
```
mau ngelamar admin, fresh graduate, pernah ikut bem, siap kerja
```

**Output:**
- Email profesional
- Struktur resmi
- Bahasa & format sesuai pilihan pengguna

---



## 📜 Lisensi
Proyek ini dibuat untuk keperluan **akademik dan pembelajaran**.
