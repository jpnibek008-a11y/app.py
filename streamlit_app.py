import streamlit as st

st.set_page_config(
    page_title="JON AI",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(
            circle at top,
            #10285c,
            #050816 70%
        );
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
    background: linear-gradient(
        90deg,
        #0066ff,
        #7928ca
    );
    border: 1px solid #00d9ff;
    border-radius: 14px;
}

.stTextInput input,
.stTextArea textarea {
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

.robot {
    font-size: 85px;
}

.card {
    padding: 18px;
    margin: 8px 0;
    background: rgba(20, 40, 80, 0.55);
    border: 1px solid #174b87;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "personaj" not in st.session_state:
    st.session_state.personaj = "JON AI"

st.sidebar.markdown("# 💎 JON AI")
st.sidebar.caption("Sizning virtual yordamchingiz")

bolim = st.sidebar.radio(
    "MENYU",
    [
        "🏠 Bosh sahifa",
        "💬 AI bilan suhbat",
        "🤖 Personaj",
        "✍️ Matn yozish",
        "🌐 Tarjimon",
        "💡 Maslahatlar",
        "⚙️ Sozlamalar"
    ]
)

if st.sidebar.button("🗑️ Suhbatni tozalash"):
    st.session_state.messages = []
    st.rerun()

if bolim == "🏠 Bosh sahifa":

    st.title("💎 JON AI")
    st.caption("Kelajak bilan muloqot")

    st.markdown("""
    <div class="hero">
        <div class="robot">🤖</div>
        <h2>Salom! Men JON AI</h2>
        <p>Sizning shaxsiy virtual yordamchingiz.</p>
        <p>Yangi g‘oyalar. Yangi imkoniyatlar. Yangi olam.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("✨ Imkoniyatlar")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>💬 Suhbat</h3>
        <p>Savollaringizni yozing.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>✍️ Matn yozish</h3>
        <p>She’r, hikoya va matnlar.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🤖 Personaj</h3>
        <p>O‘zingizga mos personaj tanlang.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>🌐 Tarjima</h3>
        <p>Turli tillardagi matnlar.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "Boshlash uchun chap tomondagi menyudan "
        "kerakli bo‘limni tanlang."
    )

elif bolim == "💬 AI bilan suhbat":

    st.title("💬 JON AI bilan suhbat")
    st.caption("Suhbat oynasi")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    xabar = st.chat_input("Xabaringizni yozing...")

    if xabar:
        st.session_state.messages.append({
            "role": "user",
            "content": xabar
        })

        with st.chat_message("user"):
            st.write(xabar)

        javob = (
            "Xabaringiz qabul qilindi! "
            "Haqiqiy AI javoblarini olish uchun "
            "keyingi bosqichda AI API xizmatini ulaymiz."
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": javob
        })

        with st.chat_message("assistant"):
            st.write(javob)

elif bolim == "🤖 Personaj":

    st.title("🤖 Personajni sozlash")

    personaj = st.selectbox(
        "Personajni tanlang",
        [
            "JON AI",
            "Futuristik robot",
            "Do‘stona yordamchi",
            "Multfilm personaji"
        ]
    )

    st.session_state.personaj = personaj

    st.markdown(
        f'<div class="hero">'
        f'<div class="robot">🤖</div>'
        f'<h2>{personaj}</h2>'
        f'<p>Siz tanlagan virtual personaj</p>'
        f'</div>',
        unsafe_allow_html=True
    )

    surat = st.file_uploader(
        "O‘z rasmingizni yuklang",
        type=["png", "jpg", "jpeg"]
    )

    if surat:
        st.image(
            surat,
            caption="Tanlangan rasm",
            use_container_width=True
        )

        st.info(
            "Rasm yuklandi. Uni haqiqiy AI personajiga "
            "aylantirish uchun alohida rasm yaratish "
            "xizmati kerak bo‘ladi."
        )

elif bolim == "✍️ Matn yozish":

    st.title("✍️ Matn yozish yordamchisi")

    mavzu = st.text_input(
        "Nima haqida matn kerak?"
    )

    tur = st.selectbox(
        "Matn turi",
        [
            "She’r",
            "Hikoya",
            "Insho",
            "Tabrik",
            "Rasmiy xat",
            "Boshqa"
        ]
    )

    if st.button("Matn tayyorlash"):
        if mavzu.strip():
            st.info(
                "Tanlangan tur: " + tur +
                "\n\nMavzu: " + mavzu +
                "\n\nHaqiqiy matn yaratish uchun "
                "AI xizmatini ulash keyingi bosqichda "
                "amalga oshiriladi."
            )
        else:
            st.warning("Avval mavzuni kiriting.")

elif bolim == "🌐 Tarjimon":

    st.title("🌐 Tarjimon")

    matn = st.text_area(
        "Tarjima qilinadigan matnni kiriting"
    )

    til = st.selectbox(
        "Qaysi tilga tarjima qilinsin?",
        [
            "O‘zbek tili",
            "Ingliz tili",
            "Rus tili",
            "Turk tili",
            "Arab tili"
        ]
    )

    if st.button("Tarjima qilish"):
        if matn.strip():
            st.info(
                "Matn qabul qilindi. "
                "Tarjima natijasini olish uchun "
                "AI xizmatini ulashimiz kerak."
            )
        else:
            st.warning("Avval matn kiriting.")

elif bolim == "💡 Maslahatlar":

    st.title("💡 JON AI maslahatchi")

    savol = st.text_area(
        "Qanday masala bo‘yicha maslahat kerak?"
    )

    if st.button("Maslahat olish"):
        if savol.strip():
            st.info(
                "Savolingiz qabul qilindi. "
                "Shaxsiylashtirilgan javoblar uchun "
                "keyingi bosqichda AI xizmatini ulaymiz."
            )
        else:
            st.warning("Savolingizni kiriting.")

elif bolim == "⚙️ Sozlamalar":

    st.title("⚙️ Sozlamalar")

    st.write("JON AI ilovasini sozlang.")

    ism = st.text_input(
        "Ismingiz",
        placeholder="Ismingizni kiriting"
    )

    til = st.selectbox(
        "Ilova tili",
        ["O‘zbekcha", "English", "Русский"]
    )

    if st.button("Sozlamalarni saqlash"):
        st.session_state.ism = ism
        st.session_state.til = til
        st.success("Sozlamalar saqlandi!")

    st.write("Tanlangan personaj:", st.session_state.personaj)

    st.caption("JON AI — ishlab chiqilayotgan loyiha.")
