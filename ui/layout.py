import streamlit as st

# =========================
# SIDEBAR
# =========================
def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
            border-right: 2px solid #e2e8f0;
        }

        [data-testid="stSidebar"] h2 {
            color: #1e293b;
            font-weight: 700;
            font-size: 1.2rem;
            border-bottom: 3px solid #2563eb;
            padding-bottom: 0.4rem;
            margin-bottom: 1.2rem;
        }

        [data-testid="stSidebar"] label {
            font-weight: 700;
            font-size: 0.8rem;
            letter-spacing: 0.05em;
            color: #475569;
        }

        [data-testid="stSidebar"] .stSelectbox input {
            font-weight: 600 !important;
            color: #334155 !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.header("Pengaturan")

        tone = st.selectbox(
            "Format",
            ["Sangat Formal", "Formal", "Ramah & Sopan", "Tegas"],
            index=1,
            key="sidebar_tone"
        )

        language = st.selectbox(
            "Bahasa",
            ["Bahasa Indonesia", "English"],
            index=0,
            key="sidebar_language"
        )

        st.markdown("""
        #### 📌 Panduan
        - Tulis poin kasar
        - Pilih format & bahasa
        - Klik **Generate**
        """)

    return tone, language


# =========================
# EMAIL PREVIEW (GMAIL STYLE)
# =========================
def render_email_preview(email_text, language):
    if language == "English":
        receiver = "Recipient"
        subject = "Professional Email"
    else:
        receiver = "Penerima"
        subject = "Email Profesional"

    st.markdown("## 📧 Preview Email")

    st.markdown(f"""
    <div style="
        border:1px solid #e5e7eb;
        border-radius:10px;
        padding:20px;
        background:#ffffff;
        font-family: Arial, Helvetica, sans-serif;
        color:#111827;
    ">
        <div style="border-bottom:1px solid #e5e7eb; padding-bottom:10px; margin-bottom:15px;">
            <strong>{receiver}:</strong> <span style="color:#2563eb">example@email.com</span><br>
            <strong>Subject:</strong> {subject}
        </div>

        <div style="white-space:pre-wrap; line-height:1.7;">
            {email_text}
        </div>
    </div>
    """, unsafe_allow_html=True)
