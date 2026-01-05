def email_prompt(user_message, tone, language):

    if language == "English":
        email_format = """
====================================
EMAIL FORMAT (MANDATORY):

Recipient   :
Subject     :

Dear Hiring Manager,

[Opening paragraph]

[Body paragraph 1]

[Body paragraph 2]

[Closing paragraph]

Sincerely,

[Full Name]
[Phone Number]
====================================
"""
    else:
        email_format = """
====================================
FORMAT EMAIL (WAJIB):

Penerima   :
Subjek     :

Kepada Yth.
Bapak/Ibu ...,

[Paragraf pembuka]

[Paragraf isi 1]

[Paragraf isi 2]

[Paragraf penutup]

Hormat saya,

[Nama Lengkap]
[No HP]
====================================
"""

    return f"""
Anda adalah asisten penulisan EMAIL PROFESIONAL.

TUGAS:
Ubah pesan informal menjadi EMAIL PROFESIONAL
DENGAN FORMAT WAJIB SEPERTI DI BAWAH INI.
JANGAN mengubah urutan format.

{email_format}

ATURAN:
- Gunakan bahasa {language}
- Nada bicara: {tone}
- Gunakan bahasa profesional & formal
- Jangan menggunakan bahasa gaul
- Jangan menambahkan penjelasan di luar email
- Tampilkan HASIL AKHIR EMAIL SAJA

PESAN ASLI USER:
\"\"\"{user_message}\"\"\"
"""
