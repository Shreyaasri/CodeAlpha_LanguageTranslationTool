
import streamlit as st
from deep_translator import MyMemoryTranslator
import html

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Lingo — Language Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --primary: #6956E8;
    --dark: #211B45;
    --muted: #77758E;
    --surface: #FFFFFF;
}

.stApp {
    background: linear-gradient(135deg, #F7F6FF 0%, #F8FAFF 55%, #F1F4FF 100%);
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.hero {
    background: linear-gradient(120deg, #4030A8 0%, #7057E8 58%, #9B78F5 100%);
    padding: 36px 38px;
    border-radius: 25px;
    color: white;
    position: relative;
    overflow: hidden;
    box-shadow: 0 14px 35px rgba(83, 62, 180, 0.19);
    margin-bottom: 26px;
}

.hero h1 {
    color: white;
    font-size: clamp(28px, 4vw, 42px);
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 12px 0 8px 0;
}

.hero p {
    color: #ECE8FF;
    font-size: 15px;
    line-height: 1.7;
    margin-bottom: 0;
}

.eyebrow {
    display: inline-block;
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.22);
    color: white;
    border-radius: 30px;
    padding: 7px 13px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
}

.hero-icon {
    font-size: 50px;
    float: right;
    margin: 8px 8px 0 10px;
}

.section-title {
    color: #282344;
    font-size: 22px;
    font-weight: 800;
    margin: 12px 0 4px 0;
}

.section-subtitle {
    color: #77758E;
    font-size: 13px;
    margin-bottom: 20px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 1px solid #EAE7FA;
    border-radius: 20px;
    box-shadow: 0 7px 25px rgba(52, 39, 120, 0.055);
}

.stTextArea textarea {
    background: #FBFAFF !important;
    border: 1px solid #E5E0F8 !important;
    border-radius: 13px !important;
    color: #292443 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    line-height: 1.7 !important;
    padding: 15px !important;
}

.stTextArea textarea:focus {
    border-color: #8170EE !important;
    box-shadow: 0 0 0 2px rgba(105,86,232,0.10) !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #FBFAFF;
    border-radius: 11px;
    border-color: #E5E0F8;
}

.stButton > button {
    background: linear-gradient(100deg, #5D49D8, #8B68F0);
    color: white;
    border: none;
    border-radius: 12px;
    min-height: 47px;
    font-weight: 700;
    transition: all 0.2s ease;
    box-shadow: 0 6px 16px rgba(105,86,232,0.18);
}

.stButton > button:hover {
    color: white;
    border: none;
    transform: translateY(-2px);
    box-shadow: 0 9px 22px rgba(105,86,232,0.28);
}

.result-heading {
    color: #282344;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 12px;
}

.result-box {
    background: linear-gradient(135deg, #F6F3FF, #F5F8FF);
    border: 1px solid #E5DFFC;
    border-radius: 15px;
    padding: 22px;
    color: #292443;
    font-size: 16px;
    line-height: 1.9;
    min-height: 100px;
    overflow-wrap: anywhere;
    white-space: pre-wrap;
}

.feature-card {
    background: rgba(255,255,255,0.9);
    border: 1px solid #EAE7FA;
    border-radius: 16px;
    padding: 17px;
    height: 100%;
}

.feature-card .emoji {
    font-size: 25px;
    margin-bottom: 8px;
}

.feature-card h4 {
    color: #302750;
    font-size: 14px;
    margin: 0 0 6px 0;
}

.feature-card p {
    color: #77758E;
    font-size: 12px;
    line-height: 1.6;
    margin: 0;
}

.footer {
    text-align: center;
    color: #88849F;
    font-size: 12px;
    padding-top: 28px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

@media (max-width: 640px) {
    .hero {
        padding: 25px 22px;
    }
    .hero-icon {
        font-size: 34px;
    }
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO HEADER ----------------
st.markdown("""
<div class="hero">
    <span class="hero-icon">🌐</span>
    <span class="eyebrow">✦ SMART LANGUAGE ASSISTANT</span>
    <h1>Break Language Barriers.</h1>
    <p>
        Your words, in any language. Translate your text in seconds
        with a clean, simple and intuitive experience.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- LANGUAGE DATA ----------------

languages = {
    "English": "en-GB",
    "Hindi": "hi-IN",
    "French": "fr-FR",
    "Spanish": "es-ES",
    "German": "de-DE",
    "Japanese": "ja-JP",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar-SA",
    "Bengali": "bn-IN",
    "Gujarati": "gu-IN",
    "Italian": "it-IT",
    "Korean": "ko-KR",
    "Marathi": "mr-IN",
    "Portuguese": "pt-PT",
    "Russian": "ru-RU",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Urdu": "ur-PK"
}


def swap_languages():
    source = st.session_state.get("source_language", "English")
    target = st.session_state.get("target_language", "Hindi")

    st.session_state["source_language"] = target
    st.session_state["target_language"] = source
    st.session_state["translated_text"] = ""


# ---------------- MAIN LAYOUT ----------------
st.markdown('<div class="section-title">Translation Workspace</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Enter your message, choose your languages, and let Lingo do the rest.</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2, gap="large")

with left:
    with st.container(border=True):
        st.markdown("### 📝 Your text")
        st.caption("SOURCE LANGUAGE")

        source_language = st.selectbox(
            "Translate from",
            list(languages.keys()),
            index=0,
            label_visibility="collapsed",
            key="source_language"
        )

        input_text = st.text_area(
            "Enter your text",
            height=205,
            placeholder="Type or paste your text here...",
            max_chars=5000,
            key="input_text",
            label_visibility="collapsed"
        )

        st.caption(f"✍️ {len(input_text)} / 5000 characters")

with right:
    with st.container(border=True):
        st.markdown("### ✨ Translation")
        st.caption("TARGET LANGUAGE")

        target_language = st.selectbox(
            "Translate to",
            list(languages.keys()),
            index=1,
            label_visibility="collapsed",
            key="target_language"
        )

        st.markdown(
            '<div style="height: 10px"></div>',
            unsafe_allow_html=True
        )

        if "translated_text" not in st.session_state:
            st.session_state.translated_text = ""

        if "translation_history" not in st.session_state:
           st.session_state.translation_history = []

        if st.session_state.translated_text:
            st.markdown(
                '<div class="result-box">'
                + html.escape(st.session_state.translated_text)
                + '</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown("""
            <div class="result-box" style="color:#9690B0;">
                Your translated text will appear here...
                <br><br>
                <span style="font-size:35px;">💬</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("")
        if st.button("📋 Copy Translation", use_container_width=True):
           if st.session_state.translated_text:
              st.code(st.session_state.translated_text, language=None)
              st.info("Click the copy icon on the text box to copy your translation.")
        else:
            st.warning("Translate some text first.")


_, swap_col, _ = st.columns([1, 1, 1])

with swap_col:
    st.button(
        "🔄 Swap Languages",
        use_container_width=True,
        on_click=swap_languages
    )

# ---------------- TRANSLATE ACTION ----------------
st.markdown("")

if st.button("✨  Translate Now", use_container_width=True):
    if not input_text.strip():
        st.warning("Please enter some text before translating.")

    elif source_language == target_language:
        st.warning("Please choose two different languages.")

    else:
        try:
            with st.spinner("Translating your text..."):
                result = MyMemoryTranslator(
                   source=languages[source_language],
                   target=languages[target_language]
                ).translate(input_text.strip())

            st.session_state.translated_text = result
            
            st.session_state.translation_history.append({
                "source": source_language,
                "target": target_language,
                "input": input_text.strip(),
                "output": result
            })

            st.rerun()

        except Exception as e:
           st.error(f"Translation failed: {e}")

# ---------------- FEATURES ----------------
st.markdown("")
st.markdown('<div class="section-title">Made for effortless translation</div>',
            unsafe_allow_html=True)
st.markdown("")

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="emoji">⚡</div>
        <h4>Quick Translation</h4>
        <p>Translate text in just a few clicks with a simple workflow.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="emoji">🌍</div>
        <h4>Multiple Languages</h4>
        <p>Choose from a variety of languages for your translation needs.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="emoji">🔒</div>
        <h4>Simple & Easy</h4>
        <p>A clean interface designed to make everyday translation easier.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    🌐 Lingo Language Translator · Built with Python & Streamlit
    <br>
    Translation requires an internet connection.
</div>
""", unsafe_allow_html=True)


# ---------------- TRANSLATION HISTORY ----------------
st.markdown("## 🕘 Recent Translation History")

if st.button("🗑️ Clear History"):
    st.session_state.translation_history = []
    st.rerun()

if st.session_state.translation_history:
    for item in reversed(st.session_state.translation_history[-5:]):
        with st.container(border=True):
            st.caption(f"{item['source']} → {item['target']}")
            st.write("**Your text:**", item["input"])
            st.write("**Translation:**", item["output"])
else:
    st.info("Your recent translations will appear here.")
