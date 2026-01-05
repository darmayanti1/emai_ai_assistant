from prompts.email_prompt import email_prompt
from config.gemini_config import load_model

def generate_email(user_message, tone, language):
    model = load_model()
    
    # --- LAPISAN FILTER (VALIDASI INPUT) ---
    # Meminta Gemini memeriksa apakah input adalah pesan bermakna atau karakter acak
    validation_prompt = f"""
    Analyze the following text: "{user_message}"
    
    Is this text a meaningful message (even if informal, slang, or short) or is it just random gibberish/characters?
    
    Answer only with one word:
    'VALID' if it has meaning.
    'INVALID' if it is random gibberish or has no clear intent.
    """
    
    check_response = model.generate_content(validation_prompt)
    is_valid = check_response.text.strip().upper()

    # Jika hasil validasi adalah INVALID, kembalikan pesan peringatan khusus
    if "INVALID" in is_valid:
        return "FILTER_ERROR: Input tidak dikenali sebagai pesan yang bermakna. Mohon masukkan poin-poin pesan yang jelas."

    # --- PROSES GENERATE EMAIL (JIKA VALID) ---
    prompt = email_prompt(user_message, tone, language)
    response = model.generate_content(prompt)
    return response.text