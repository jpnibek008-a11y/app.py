import streamlit as st

st.set_page_config(
    page_title="JON AI",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: radial-gradient(
        circle at top,
        #10285c,
        #050816 65%
    );
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
.stButton > button {
    background: linear-gradient(90deg, #007bff, #7b2cff);
    color: white;
    border: 1px solid #00d9ff;
    border-radius: 14px;
    padding: 12px 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("💎 JON AI")
st.caption("Sizning shaxsiy virtual yordamchingiz")

st.markdown("""
<div style="
text-align:center;
padding:30px 10px;
border:2px solid #00cfff;
border-radius:25px;
background:rgba(0,120,255,0.08);
box-shadow:0 0 25px #007bff;
">
<div style="font-size:100px;">🤖</div>
<h2>Salom! Men JON AI</h2>
<p>Virtual olamingizga xush kelibsiz!</p>
<p>Personajingizni o'zingiz tanlang.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

tanlov = st.radio(
    "Personaj yaratish usulini tanlang:",
    [
        "Tayyor personaj",
        "O'z suratidan yaratish"
    ]
)

if tanlov == "Tayyor personaj":
    personaj = st.selectbox(
        "Personajni tanlang:",
        ["JON AI", "Robot", "Multfilm uslubi"]
    )
    st.success(f"Siz {personaj} ni tanladingiz!")

else:
    surat = st.file_uploader(
        "Suratingizni yuklang",
        type=["png", "jpg", "jpeg"]
    )

    if surat:
        st.image(
            surat,
            caption="Yuklangan surat",
            use_container_width=True
        )
        st.info(
            "Surat qabul qilindi. "
            "Keyingi bosqichda uni AI yordamida "
            "yangi personajga aylantiramiz."
        )

st.divider()
st.subheader("💬 JON AI bilan suhbat")

xabar = st.chat_input("JON AI ga xabar yozing...")

if xabar:
    st.chat_message("user").write(xabar)
    st.chat_message("assistant").write(
        "Salom! Men JON AI. "
        "Hozir yangi imkoniyatlarimni ishlab chiqyapmiz!"
    )

