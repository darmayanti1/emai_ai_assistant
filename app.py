import streamlit as st
from services.email_generator import generate_email
from ui.layout import render_sidebar

st.set_page_config(
    page_title="AI Email Professional Assistant",
    page_icon="✉️",
    layout="wide"
)

# Custom CSS yang sudah diperbaiki
st.markdown("""
    <style>
    /* Background global */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e0f2fe 50%, #f1f5f9 100%);
    }
    
    /* Header styling */
    h1 {
        color: #1e293b;
        font-weight: 700;
        padding: 1rem 0;
        border-bottom: 4px solid #2563eb;
        margin-bottom: 1rem;
    }
    
    /* Input Area */
    .stTextArea > div > div > textarea {
        background-color: #ffffff;
        border: 2px solid #cbd5e1;
        border-radius: 0.75rem;
        font-size: 1rem;
        padding: 1rem;
        color: #334155;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }
    
    /* Tombol Utama */
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        padding: 0.8rem 2rem;
        border-radius: 0.75rem;
        border: none;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(37, 99, 235, 0.3);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Kotak Hasil (Code Block) */
    .stCodeBlock {
        background-color: #ffffff;
        border: 2px solid #e2e8f0;
        border-radius: 1rem;
        padding: 1rem;
    }

    /* Menghilangkan border kartu kosong bawaan streamlit jika ada */
    .element-container:empty {
        display: none;
    }
    
    h3 {
        color: #1e293b;
        font-weight: 700;
        border-left: 5px solid #16a34a;
        padding-left: 1rem;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✉️ AI Asisten Email Profesional")
st.markdown("Transformasikan poin-poin pikiran Anda menjadi draf email resmi dalam sekejap.")

# Memanggil Sidebar
tone, language = render_sidebar()

# Area Input
user_message = st.text_area(
    "Masukkan pesan / poin kasar Anda:",
    placeholder="Contoh: telat kirim laporan karena laptop rusak, sore ini baru dikirim.",
    height=200
)

# Tombol Generate
if st.button("🚀 GENERATE EMAIL"):
    if user_message.strip():
        with st.spinner("Mengevaluasi konteks dan merangkai kata..."):
            result = generate_email(user_message, tone, language)
            
            # Cek apakah hasil adalah error dari sistem Guardrail
            if result.startswith("FILTER_ERROR:"):
                # Menampilkan pesan error dengan box merah yang jelas
                clean_error = result.replace("FILTER_ERROR: ", "")
                st.error(f"Pesan Tidak Valid: {clean_error}")
            else:
                # Menampilkan hasil draf email
                st.subheader("📧 Hasil Draf Email")
                st.code(result, language="text")
                st.success("Draf email berhasil dibuat sesuai nada bicara Anda.")
    else:
        st.warning("⚠️ Mohon masukkan pesan terlebih dahulu.")