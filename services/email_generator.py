from prompts.email_prompt import email_prompt
from config.gemini_config import load_model

def generate_email(user_message, tone, language):
    model = load_model()
    
    # --- LAPISAN FILTER 1: Validasi Teknis Sederhana ---
    # Mencegah input satu kata seperti "saya" atau "halo" diproses sebagai email panjang
    if len(user_message.strip().split()) < 2:
        return "FILTER_ERROR: Pesan terlalu singkat. Mohon masukkan minimal beberapa kata atau poin pesan agar asisten bisa memahami konteksnya."

    # --- LAPISAN FILTER 2: Validasi Makna via LLM ---
    # Meminta Gemini memeriksa apakah input memiliki maksud atau hanya gibberish/karakter acak
    validation_prompt = f"""
    Analyze the intent of this text: "{user_message}"
    
    Decision Criteria:
    - 'VALID': The text contains clear information, a request, or a context for an email (even if informal).
    - 'INVALID': The text is random characters, repetitive gibberish, or a single word without any context.
    
    Answer only with one word: VALID or INVALID.
    """
    
    try:
        check_response = model.generate_content(validation_prompt)
        is_valid = check_response.text.strip().upper()

        # Jika Gemini mendeteksi input tidak bermakna
        if "INVALID" in is_valid:
            return "FILTER_ERROR: Input tidak dikenali sebagai informasi yang bermakna. Mohon masukkan poin-poin pesan yang lebih jelas agar draf tidak melantur."

        # --- PROSES GENERATE EMAIL (Hanya jika lolos filter) ---
        prompt = email_prompt(user_message, tone, language)
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"FILTER_ERROR: Terjadi kesalahan pada sistem koneksi AI: {str(e)}"