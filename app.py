import streamlit as st
from services.email_generator import generate_email
from ui.layout import render_sidebar

st.set_page_config(
    page_title="AI Email Professional Assistant",
    page_icon="✉️",
    layout="wide"
)

# Custom CSS tetap sama sesuai permintaan Anda
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e0f2fe 50%, #f1f5f9 100%);
    }
    h1 {
        color: #1e293b;
        font-weight: 700;
        padding: 1.5rem 0;
        border-bottom: 4px solid #2563eb;
        margin-bottom: 1rem;
    }
    .stMarkdown p {
        color: #475569;
        font-size: 1.1rem;
        font-weight: 500;
    }
    .stTextArea > div > div > textarea {
        background-color: #f8fafc;
        border: 2px solid #cbd5e1;
        border-radius: 0.5rem;
        font-size: 1rem;
        padding: 1rem;
        font-weight: 500;
        color: #334155;
    }
    .stTextArea > div > div > textarea:focus {
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        font-weight: 700;
        font-size: 1rem;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        border: none;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
        transition: all 0.2s;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8 0%, #1e40af 100%);
        box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3);
        transform: translateY(-2px);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        border-right: 1px solid #e2e8f0;
    }
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: #f8fafc;
        border: 2px solid #cbd5e1;
        border-radius: 0.5rem;
        font-weight: 500;
    }
    .stCodeBlock {
        background-color: #f8fafc;
        border: 2px solid #cbd5e1;
        border-radius: 0.5rem;
        padding: 1.5rem;
    }
    .stAlert {
        border-radius: 0.5rem;
        border-left: 4px solid #2563eb;
    }
    .stSpinner > div {
        border-top-color: #2563eb;
    }
    h3 {
        color: #1e293b;
        font-weight: 700;
        padding: 0.5rem 0;
        border-left: 4px solid #16a34a;
        padding-left: 1rem;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✉️ AI Asisten Email Profesional")
st.markdown("Ubah pesan santai menjadi email profesional sesuai format resmi.")

tone, language = render_sidebar()

user_message = st.text_area(
    "Masukkan pesan / poin kasar:",
    placeholder="contoh: mau ngelamar admin, fresh graduate, pernah ikut bem",
    height=200
)

if st.button("Generate Email"):
    if user_message.strip():
        with st.spinner("Mengevaluasi dan menyusun email..."):
            result = generate_email(user_message, tone, language)
            
            # Cek apakah hasil adalah error dari filter gibberish
            if result.startswith("FILTER_ERROR:"):
                # Menghilangkan tag FILTER_ERROR agar user hanya melihat pesannya
                clean_error = result.replace("FILTER_ERROR: ", "")
                st.warning(f"⚠️ {clean_error}")
            else:
                st.subheader("📧 Hasil Draf Email")
                st.code(result, language="text")
    else:
        st.warning("Pesan tidak boleh kosong.")