import streamlit as st
from deep_translator import GoogleTranslator

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="All-in-One Translator",
    page_icon="🌍",
    layout="centered"
)

# ================= SIDEBAR =================
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Choose Translator",
    [
        "🌍 Language Translator",
        "📡 Morse Code",
        "⠃ Braille Translator",
        "🏺 Ancient Scripts"
    ]
)

# =================================================
# 🌍 MODERN LANGUAGE TRANSLATOR
# =================================================
def language_translator():
    st.title("🌍 Language Translator")

    languages = {
        "English": "en",
        "Hindi": "hi",
        "Urdu": "ur",
        "Marathi": "mr",
        "Punjabi": "pa",
        "Bengali": "bn",
        "Assamese": "as",
        "Kannada": "kn",
        "Tamil": "ta",
        "Telugu": "te",
        "Malayalam": "ml",
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Russian": "ru",
        "Japanese": "ja",
        "Chinese": "zh-cn"
    }

    col1, col2 = st.columns(2)
    with col1:
        src = st.selectbox("From", languages.keys())
    with col2:
        tgt = st.selectbox("To", languages.keys())

    text = st.text_area("Enter text")

    if text:
        try:
            translated = GoogleTranslator(
                source=languages[src],
                target=languages[tgt]
            ).translate(text)
            st.success(translated)
        except:
            st.error("Translation failed. Please try again.")

# =================================================
# 📡 MORSE CODE TRANSLATOR
# =================================================
def morse_translator():
    st.title("📡 Morse Code Translator")

    MORSE = {
        'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
        'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
        'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---',
        'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
        'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--',
        'z':'--..', ' ':' / '
    }

    REVERSE = {v:k for k,v in MORSE.items()}

    mode = st.radio("Mode", ["English → Morse", "Morse → English"])
    text = st.text_input("Enter text")

    if text:
        if mode == "English → Morse":
            result = " ".join(MORSE.get(c.lower(), "") for c in text)
        else:
            result = "".join(REVERSE.get(c, "") for c in text.split())
        st.success(result)

# =================================================
# ⠃ BRAILLE TRANSLATOR
# =================================================
def braille_translator():
    st.title("⠃ Braille Translator")

    BRAILLE = {
        'a':'⠁','b':'⠃','c':'⠉','d':'⠙','e':'⠑',
        'f':'⠋','g':'⠛','h':'⠓','i':'⠊','j':'⠚',
        'k':'⠅','l':'⠇','m':'⠍','n':'⠝','o':'⠕',
        'p':'⠏','q':'⠟','r':'⠗','s':'⠎','t':'⠞',
        'u':'⠥','v':'⠧','w':'⠺','x':'⠭','y':'⠽',
        'z':'⠵',' ':' '
    }

    REVERSE = {v:k for k,v in BRAILLE.items()}

    mode = st.radio("Mode", ["English → Braille", "Braille → English"])
    text = st.text_input("Enter text")

    if text:
        if mode == "English → Braille":
            result = "".join(BRAILLE.get(c.lower(), "") for c in text)
        else:
            result = "".join(REVERSE.get(c, "") for c in text)
        st.success(result)

# =================================================
# 🏺 ANCIENT SCRIPTS (WITH REVERSE)
# =================================================
def ancient_translator():
    st.title("🏺 Ancient Script Translator")
    st.write("Scholarly transliteration with dependent & independent vowels")

    # ---------- BRAHMI ----------
    brahmi_iv = {"a":"𑀅","ā":"𑀆","i":"𑀇","ī":"𑀈","u":"𑀉","ū":"𑀊","e":"𑀏","o":"𑀑"}
    brahmi_dv = {"a":"", "ā":"𑀸","i":"𑀺","ī":"𑀻","u":"𑀼","ū":"𑀽","e":"𑀾","o":"𑁀"}
    brahmi_c = {"k":"𑀓","g":"𑀕","c":"𑀘","j":"𑀚","t":"𑀢","d":"𑀤","n":"𑀦","p":"𑀧","m":"𑀫","y":"𑀬","r":"𑀭","l":"𑀮","s":"𑀲","h":"𑀳"}
    rev_brahmi = {v:k for k,v in {**brahmi_iv, **brahmi_c}.items()}
    rev_brahmi.update({v:k for k,v in brahmi_dv.items() if v != ""})

    def eng_to_brahmi(word):
        i, out = 0, ""
        while i < len(word):
            if word[i] in brahmi_c:
                cons = brahmi_c[word[i]]
                v = "a"
                if i+1 < len(word) and word[i+1] in brahmi_dv:
                    v = word[i+1]
                    i += 1
                out += cons + brahmi_dv[v]
            elif word[i] in brahmi_iv:
                out += brahmi_iv[word[i]]
            else:
                out += word[i]
            i += 1
        return out

    def brahmi_to_eng(text):
        result = ""
        skip = False
        for i, ch in enumerate(text):
            if skip:
                skip = False
                continue
            if ch in brahmi_c.values() and i+1 < len(text) and text[i+1] in brahmi_dv.values():
                cons = [k for k,v in brahmi_c.items() if v==ch][0]
                dv = [k for k,v in brahmi_dv.items() if v==text[i+1]][0]
                result += cons + dv
                skip = True
            elif ch in rev_brahmi:
                result += rev_brahmi[ch]
            else:
                result += ch
        return result

    # ---------- KHAROSTHI ----------
    kharosthi_iv = {"a":"𐨀","i":"𐨁","u":"𐨂","e":"𐨅","o":"𐨆"}
    kharosthi_c = {"k":"𐨐","g":"𐨒","t":"𐨟","d":"𐨡","n":"𐨣","p":"𐨤","m":"𐨨","r":"𐨪","s":"𐨭","h":"𐨱"}
    rev_kharosthi = {v:k for k,v in {**kharosthi_iv, **kharosthi_c}.items()}

    def eng_to_kharosthi(word):
        return "".join(kharosthi_c.get(ch,kharosthi_iv.get(ch,ch)) for ch in word)

    def kharosthi_to_eng(text):
        return "".join(rev_kharosthi.get(ch,ch) for ch in text)

    # ---------- OTHER SCRIPTS ----------
    greek = {"a":"Α","b":"Β","g":"Γ","d":"Δ","e":"Ε"}
    rev_greek = {v:k for k,v in greek.items()}

    hebrew = {"a":"א","b":"ב","g":"ג","d":"ד","h":"ה"}
    rev_hebrew = {v:k for k,v in hebrew.items()}

    aramaic = {"a":"𐡀","b":"𐡁","g":"𐡂","d":"𐡃"}
    rev_aramaic = {v:k for k,v in aramaic.items()}

    tamil = {"a":"அ","ka":"க","na":"ந","ma":"ம","ra":"ர"}
    rev_tamil = {v:k for k,v in tamil.items()}

    latin = {chr(i): chr(i).upper() for i in range(97,123)}
    rev_latin = {v:k for k,v in latin.items()}

    scripts = ["Brahmi","Kharosthi","Greek","Hebrew","Aramaic","Tamil","Latin"]
    script = st.selectbox("Select Script", scripts)
    mode = st.radio("Mode", ["English → Ancient","Ancient → English"])
    text = st.text_input("Enter text")

    if text:
        if script == "Brahmi":
            st.success(eng_to_brahmi(text.lower()) if mode=="English → Ancient" else brahmi_to_eng(text))
        elif script == "Kharosthi":
            st.success(eng_to_kharosthi(text.lower()) if mode=="English → Ancient" else kharosthi_to_eng(text))
        elif script == "Greek":
            st.success("".join(greek.get(c,c) for c in text.lower()) if mode=="English → Ancient" else "".join(rev_greek.get(c,c) for c in text))
        elif script == "Hebrew":
            st.success("".join(hebrew.get(c,c) for c in text.lower()) if mode=="English → Ancient" else "".join(rev_hebrew.get(c,c) for c in text))
        elif script == "Aramaic":
            st.success("".join(aramaic.get(c,c) for c in text.lower()) if mode=="English → Ancient" else "".join(rev_aramaic.get(c,c) for c in text))
        elif script == "Tamil":
            st.success(" ".join(tamil.get(w,w) for w in text.lower().split()) if mode=="English → Ancient" else " ".join(rev_tamil.get(w,w) for w in text.split()))
        elif script == "Latin":
            st.success(text.upper() if mode=="English → Ancient" else "".join(rev_latin.get(c,c) for c in text))
