import streamlit as st
from google import genai
from google.genai import types

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="JON AI",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top, #10285c, #050816 70%);
        color: white;
    }
    [data-testid="stSidebar"] {
        background: #080f25;
        border-right: 1px solid #00d9ff;
    }
    h1, h2, h3, p, label {
        color: white !important;
    }
    .stButton > button {
        width: 100%;
        min-height: 45px;
        color: white;
        background: linear-gradient(90deg, #0066ff, #7928ca);
        border: 1px solid #00d9ff;
        border-radius: 14px;
    }
    .stTextInput input, .stTextArea textarea {
        background: #0b1633;
        color: white;
        border: 1px solid #00d9ff;
        border-radius: 12px;
    }
    .hero {
        text-align: center;
        padding: 28px 12px;
        border: 1px solid #00d9ff;
        border-radius: 24px;
        background: rgba(0, 100, 255, 0.10);
        box-shadow: 0 0 22px rgba(0, 180, 255, 0.20);
    }
    .robot { font-size: 85px; }
    .card {
        padding: 18px;
        margin: 8px 0;
        background: rgba(20, 40, 80, 0.55);
        border: 1px solid #174b87;
        border-radius: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Gemini setup
# -----------------------------
MODEL_NAME = "gemini-2.5-flash"
SYSTEM_INSTRUCTION = (
    "You are JON AI, a helpful, friendly personal assistant. "
    "Respond in the same language as the user unless they request another language. "
    "Be clear, accurate, and honest. Do not invent facts."
)

@st.cache_resource
def get_gemini_client(api_key: str):
    return genai.Client(api_key=api_key)

def get_api_key():
    """Read the API key from Streamlit Cloud Secrets or a local .env-style environment."""
    try:
        key = st.secrets.get("GEMINI_API_KEY", "")
    except Exception:
        key = ""
    return key or ""

def ask_gemini(prompt: str, history=None, system_instruction=SYSTEM_INSTRUCTION) -> str:
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY topilmadi. Streamlit Cloud → Settings → Secrets "
            "bo‘limiga GEMINI_API_KEY = \"API_KEYINGIZ\" qo‘shing."
        )

    client = get_gemini_client(api_key)
    contents = []

    # Gemini history must use 'user' and 'model' roles.
    for item in history or []:
        role = "user" if item["role"] == "user" else "model"
        contents.append(
            types.Content(
                role=role,
                parts=[types.Part.from_text(text=item["content"])],
            )
        )

    contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        )
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.7,
            max_output_tokens=2048,
        ),
    )

    answer = getattr(response, "text", None)
    if not answer:
        raise RuntimeError("Gemini javob qaytarmadi. Boshqa savol bilan urinib ko‘ring.")
    return answer.strip()

def show_ai_result(prompt: str, system_instruction: str, key: str):
    if not prompt.strip():
        st.warning("Iltimos, avval matn kiriting.")
        return
    with st.spinner("JON AI javob tayyorlamoqda..."):
        try:
            result = ask_gemini(prompt, system_instruction=system_instruction)
            st.markdown(result)
        except Exception as exc:
            st.error(f"AI so‘rovi bajarilmadi: {exc}")

# -----------------------------
# Session state
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "personaj" not in st.session_state:
    st.session_state.personaj = "JON AI"
if "bolim" not in st.session_state:
    st.session_state.bolim = "💬 AI bilan suhbat"
if "ism" not in st.session_state:
    st.session_state.ism = ""
if "til" not in st.session_state:
    st.session_state.til = "O‘zbekcha"

# -----------------------------
# Sidebar navigation
# -----------------------------
st.sidebar.markdown("# 💎 JON AI")
st.sidebar.caption("Sizning virtual yordamchingiz")

menu_items = [
    "🏠 Bosh sahifa",
    "💬 AI bilan suhbat",
    "🤖 Personaj",
    "✍️ Matn yozish",
    "🌐 Tarjimon",
    "💡 Maslahatlar",
    "⚙️ Sozlamalar",
]
selected = st.sidebar.radio(
    "MENYU",
    menu_items,
    index=menu_items.index(st.session_state.bolim)
    if st.session_state.bolim in menu_items else 1,
)
st.session_state.bolim = selected

if st.sidebar.button("🗑️ Suhbatni tozalash"):
    st.session_state.messages = []
    st.rerun()

with st.sidebar.expander("API holati"):
    if get_api_key():
        st.success("Gemini API kaliti topildi.")
    else:
        st.warning("GEMINI_API_KEY sozlanmagan.")

# -----------------------------
# Home
# -----------------------------
if selected == "🏠 Bosh sahifa":
    st.title("💎 JON AI")
    st.caption("Kelajak bilan muloqot")
    st.markdown(
        """
        <div class="hero">
            <div class="robot">🤖</div>
            <h2>Salom! Men JON AI</h2>
            <p>Sizning shaxsiy virtual yordamchingiz.</p>
            <p>Yangi g‘oyalar. Yangi imkoniyatlar. Yangi olam.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.subheader("✨ Imkoniyatlar")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h3>💬 Suhbat</h3><p>Savollaringizga AI javob beradi.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>✍️ Matn yozish</h3><p>She’r, hikoya, insho va rasmiy xatlar.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>🤖 Personaj</h3><p>Yordamchi ko‘rinishini tanlang.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>🌐 Tarjima</h3><p>Matnlarni turli tillarga tarjima qiling.</p></div>', unsafe_allow_html=True)
    st.info("Boshlash uchun chap tomondagi menyudan kerakli bo‘limni tanlang.")

# -----------------------------
# Chat
# -----------------------------
elif selected == "💬 AI bilan suhbat":
    st.title("💬 JON AI bilan suhbat")
    st.caption("Gemini orqali ishlaydi")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    xabar = st.chat_input("Xabaringizni yozing...")
    if xabar:
        st.session_state.messages.append({"role": "user", "content": xabar})
        with st.chat_message("user"):
            st.markdown(xabar)

        with st.chat_message("assistant"):
            with st.spinner("JON AI o‘ylayapti..."):
                try:
                    # Send previous messages except the just-added latest user message.
                    history = st.session_state.messages[:-1]
                    javob = ask_gemini(xabar, history=history)
                    st.markdown(javob)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": javob}
                    )
                except Exception as exc:
                    st.error(f"AI so‘rovi bajarilmadi: {exc}")

# -----------------------------
# Character
# -----------------------------
elif selected == "🤖 Personaj":
    st.title("🤖 Personajni sozlash")
    st.session_state.personaj = st.selectbox(
        "Personajni tanlang",
        ["JON AI", "Futuristik robot", "Do‘stona yordamchi", "Multfilm personaji"],
        index=["JON AI", "Futuristik robot", "Do‘stona yordamchi", "Multfilm personaji"].index(
            st.session_state.personaj
        ) if st.session_state.personaj in ["JON AI", "Futuristik robot", "Do‘stona yordamchi", "Multfilm personaji"] else 0,
    )
    st.markdown(
        f'<div class="hero"><div class="robot">🤖</div><h2>{st.session_state.personaj}</h2>'
        '<p>Siz tanlagan virtual personaj</p></div>',
        unsafe_allow_html=True,
    )
    surat = st.file_uploader("O‘z rasmingizni yuklang", type=["png", "jpg", "jpeg"])
    if surat:
        st.image(surat, caption="Tanlangan rasm", use_container_width=True)
        st.caption("Rasm ko‘rsatiladi; uni o‘zgartirish yoki yangi rasm yaratish alohida xizmatni talab qiladi.")

# -----------------------------
# Writing assistant
# -----------------------------
elif selected == "✍️ Matn yozish":
    st.title("✍️ Matn yozish yordamchisi")
    mavzu = st.text_area("Nima haqida matn kerak?")
    tur = st.selectbox("Matn turi", ["She’r", "Hikoya", "Insho", "Tabrik", "Rasmiy xat", "Boshqa"])
    uslub = st.selectbox("Uslub", ["Oddiy va tushunarli", "Rasmiy", "Ijodiy", "Batafsil"])
    if st.button("Matn tayyorlash"):
        prompt = f"Mavzu: {mavzu}\nMatn turi: {tur}\nUslub: {uslub}\nMatnni tayyorlab ber."
        show_ai_result(
            prompt,
            "You are a skilled writing assistant. Write the requested text in the user's language. Follow the requested type and style.",
            "writing",
        )

# -----------------------------
# Translator
# -----------------------------
elif selected == "🌐 Tarjimon":
    st.title("🌐 Tarjimon")
    matn = st.text_area("Tarjima qilinadigan matnni kiriting")
    til = st.selectbox("Qaysi tilga tarjima qilinsin?", ["O‘zbek tili", "Ingliz tili", "Rus tili", "Turk tili", "Arab tili"])
    if st.button("Tarjima qilish"):
        prompt = f"Translate the following text into {til}. Preserve the meaning and tone. Return only the translation unless a brief clarification is essential.\n\nText:\n{matn}"
        show_ai_result(
            prompt,
            "You are a professional multilingual translator. Preserve meaning, tone, names, and formatting. Do not summarize.",
            "translation",
        )

# -----------------------------
# Advice
# -----------------------------
elif selected == "💡 Maslahatlar":
    st.title("💡 JON AI maslahatchi")
    savol = st.text_area("Qanday masala bo‘yicha maslahat kerak?")
    if st.button("Maslahat olish"):
        show_ai_result(
            savol,
            "You are a thoughtful, practical personal assistant. Give balanced, actionable advice. If a topic is high-stakes, clearly state limitations and encourage qualified professional help when appropriate.",
            "advice",
        )

# -----------------------------
# Settings
# -----------------------------
elif selected == "⚙️ Sozlamalar":
    st.title("⚙️ Sozlamalar")
    ism = st.text_input("Ismingiz", value=st.session_state.ism, placeholder="Ismingizni kiriting")
    til = st.selectbox("Ilova tili", ["O‘zbekcha", "English", "Русский"], index=["O‘zbekcha", "English", "Русский"].index(st.session_state.til))
    if st.button("Sozlamalarni saqlash"):
        st.session_state.ism = ism
        st.session_state.til = til
        st.success("Sozlamalar saqlandi!")
    st.write("Tanlangan personaj:", st.session_state.personaj)
    st.caption("JON AI • Gemini API bilan ishlaydi")

st.caption("JON AI • Kelajak bilan muloqot")
