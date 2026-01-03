import streamlit as st

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
        "📡 Morse Code",
        "⠃ Braille Translator",
        "🏺 Ancient Scripts"
    ]
)

# =================================================
# 📡 MORSE CODE
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

    REVERSE = {v: k for k, v in MORSE.items()}

    mode = st.radio("Mode", ["English → Morse", "Morse → English"])
    text = st.text_input("Enter text")

    if text:
        if mode == "English → Morse":
            result = " ".join(MORSE.get(c.lower(), "") for c in text)
        else:
            result = "".join(REVERSE.get(c, "") for c in text.split())
        st.success(result)

# =================================================
# ⠃ BRAILLE
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

    REVERSE = {v: k for k, v in BRAILLE.items()}

    mode = st.radio("Mode", ["English → Braille", "Braille → English"])
    text = st.text_input("Enter text")

    if text:
        if mode == "English → Braille":
            result = "".join(BRAILLE.get(c.lower(), "") for c in text)
        else:
            result = "".join(REVERSE.get(c, "") for c in text)
        st.success(result)

# =================================================
# 🏺 ANCIENT SCRIPTS
# =================================================
def ancient_translator():
    st.title("🏺 Ancient Script Translator")

    # ---------------- BRAHMI ----------------
    brahmi_independent_vowels = {
        "a":"𑀅","ā":"𑀆","i":"𑀇","ī":"𑀈",
        "u":"𑀉","ū":"𑀊","e":"𑀏","ai":"𑀐","o":"𑀑","au":"𑀒"
    }
    brahmi_dependent_vowels = {
        "a":"", "ā":"𑀸","i":"𑀺","ī":"𑀻",
        "u":"𑀼","ū":"𑀽","e":"𑀾","ai":"𑀿","o":"𑁀","au":"𑁁"
    }
    brahmi_consonants = {
        "k":"𑀓","kh":"𑀔","g":"𑀕","gh":"𑀖","ṅ":"𑀗",
        "c":"𑀘","ch":"𑀙","j":"𑀚","jh":"𑀛","ñ":"𑀜",
        "ṭ":"𑀝","ṭh":"𑀞","ḍ":"𑀟","ḍh":"𑀠","ṇ":"𑀡",
        "t":"𑀢","th":"𑀣","d":"𑀤","dh":"𑀥","n":"𑀦",
        "p":"𑀧","ph":"𑀨","b":"𑀩","bh":"𑀪","m":"𑀫",
        "y":"𑀬","r":"𑀭","l":"𑀮","v":"𑀯",
        "ś":"𑀰","ṣ":"𑀱","s":"𑀲","h":"𑀳"
    }

    # ---------------- KHAROSTHI ----------------
    kharosthi_independent_vowels = {
        "a":"𐨀","i":"𐨁","u":"𐨂","e":"𐨅","o":"𐨆"
    }
    kharosthi_dependent_vowels = {
        "a":"", "i":"𐨁","u":"𐨂","e":"𐨅","o":"𐨆"
    }
    kharosthi_consonants = {
        "ka":"𐨐","kha":"𐨑","ga":"𐨒","gha":"𐨓",
        "ca":"𐨕","ja":"𐨗",
        "ṭa":"𐨙","ḍa":"𐨛",
        "ta":"𐨟","da":"𐨡","na":"𐨣",
        "pa":"𐨤","ba":"𐨦","ma":"𐨨",
        "ya":"𐨩","ra":"𐨪","la":"𐨫","sa":"𐨭","ha":"𐨱"
    }

    # ---------------- GREEK ----------------
    greek_independent_vowels = {"a":"Α","e":"Ε","i":"Ι","o":"Ο","u":"Υ","ō":"Ω","ē":"Η"}
    greek_consonants = {"b":"Β","g":"Γ","d":"Δ","z":"Ζ","th":"Θ","k":"Κ","l":"Λ","m":"Μ","n":"Ν","x":"Ξ","p":"Π","r":"Ρ","s":"Σ","ph":"Φ","ch":"Χ","ps":"Ψ"}

    # ---------------- HEBREW ----------------
    hebrew_independent_vowels = {"a":"א","e":"א","i":"י","o":"ו","u":"ו"}
    hebrew_consonants = {"b":"ב","g":"ג","d":"ד","h":"ה","w":"ו","z":"ז","ḥ":"ח","ṭ":"ט","y":"י","k":"כ","l":"ל","m":"מ","n":"נ","s":"ס","ʿ":"ע","p":"פ","ṣ":"צ","q":"ק","r":"ר","š":"ש","t":"ת"}

    # ---------------- ARAMAIC ----------------
    aramaic_independent_vowels = {"a":"𐡀","e":"𐡀","i":"𐡉","o":"𐡅","u":"𐡅"}
    aramaic_consonants = {"b":"𐡁","g":"𐡂","d":"𐡃","h":"𐡄","w":"𐡅","z":"𐡆","ḥ":"𐡇","ṭ":"𐡈","y":"𐡉","k":"𐡊","l":"𐡋","m":"𐡌","n":"𐡍","s":"𐡎","ʿ":"𐡏","p":"𐡐","ṣ":"𐡑","q":"𐡒","r":"𐡓","š":"𐡔","t":"𐡕"}

    # ---------------- TAMIL ----------------
    tamil_independent_vowels = {"a":"அ","ā":"ஆ","i":"இ","ī":"ஈ","u":"உ","ū":"ஊ","e":"எ","ē":"ஏ","ai":"ஐ","o":"ஒ","ō":"ஓ","au":"ஔ"}
    tamil_consonants = {"ka":"க","ṅa":"ங","ca":"ச","ña":"ஞ","ṭa":"ட","ṇa":"ண","ta":"த","na":"ந","pa":"ப","ma":"ம","ya":"ய","ra":"ர","la":"ல","va":"வ","ḻa":"ழ","ḷa":"ள","ṟa":"ற","ṉa":"ன"}

    # ---------------- LATIN ----------------
    latin = {chr(i): chr(i).upper() for i in range(97,123)}

    ancient_scripts = {
        "Brahmi": (brahmi_independent_vowels, brahmi_dependent_vowels, brahmi_consonants),
        "Kharosthi": (kharosthi_independent_vowels, kharosthi_dependent_vowels, kharosthi_consonants),
        "Greek": (greek_independent_vowels, {}, greek_consonants),
        "Hebrew": (hebrew_independent_vowels, {}, hebrew_consonants),
        "Aramaic": (aramaic_independent_vowels, {}, aramaic_consonants),
        "Tamil": (tamil_independent_vowels, {}, tamil_consonants),
        "Latin": (latin, {}, {})
    }

    script = st.selectbox("Select Ancient Script", ancient_scripts.keys())
    text = st.text_input("Enter text (space-separated for English → Ancient)")

    mode = st.radio("Mode", ["English → Ancient", "Ancient → English"])

    if text:
        independent, dependent, consonants = ancient_scripts[script]
        result = ""
        words = text.lower().split()

        if mode == "English → Ancient":
            for word in words:
                i = 0
                out = ""
                while i < len(word):
                    matched = False
                    # independent vowels
                    for v in independent:
                        if word[i:].startswith(v):
                            out += independent[v]
                            i += len(v)
                            matched = True
                            break
                    if matched:
                        continue
                    # consonants + dependent vowels
                    for c in consonants:
                        if word[i:].startswith(c):
                            cons = consonants[c]
                            i += len(c)
                            vowel = "a"
                            for v in dependent:
                                if word[i:].startswith(v):
                                    vowel = v
                                    i += len(v)
                                    break
                            out += cons + dependent.get(vowel,"")
                            matched = True
                            break
                    if not matched:
                        out += word[i]
                        i += 1
                result += out + " "
        else:
            # Ancient → English
            rev_consonants = {v: k for k, v in consonants.items()}
            rev_independent = {v: k for k, v in independent.items()}
            rev_dependent = {v: k for k, v in dependent.items() if v != ""}
            for word in words:
                i = 0
                out = ""
                while i < len(word):
                    char = word[i]
                    if char in rev_independent:
                        out += rev_independent[char]
                        i += 1
                        continue
                    if char in rev_consonants:
                        out += rev_consonants[char]
                        i += 1
                        if i < len(word) and word[i] in rev_dependent:
                            out += rev_dependent[word[i]]
                            i += 1
                        continue
                    out += char
                    i += 1
                result += out + " "
        st.success(result.strip())

# =================================================
# ROUTER
# =================================================
if page == "📡 Morse Code":
    morse_translator()
elif page == "⠃ Braille Translator":
    braille_translator()
elif page == "🏺 Ancient Scripts":
    ancient_translator()
