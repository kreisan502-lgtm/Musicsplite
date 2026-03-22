import streamlit as st
import time

# 1. Konfigurasi Halaman (Harus paling atas)
st.set_page_config(
    page_title="Happy Birthday! ❤️",
    page_icon="🎂",
    layout="centered"
)

# 2. Ambil Secrets dengan pengecekan manual
if "LINK_FOTO" not in st.secrets:
    st.error("Error: 'LINK_FOTO' tidak ditemukan di Secrets!")
    st.stop()

# 3. Custom CSS (Disederhanakan untuk menghindari TypeError)
st.markdown("<style> .stApp {background-color: #fff5f5;} </style>", unsafe_content_html=True)

# 4. Header & Musik
st.markdown("<h1 style='text-align: center; color: #d32f2f;'>Happy Birthday, Sayang! 🎂💖</h1>", unsafe_content_html=True)
st.divider()

# Memutar lagu latar
st.audio(st.secrets["LINK_LAGU"], format="audio/mp3")
st.caption("🎵 Nyalakan volumenya ya...")

# 5. Foto Utama
st.write("")
st.image(st.secrets["LINK_FOTO"], use_container_width=True, caption="Momen favorit kita ✨")

# 6. Pesan Romantis
st.write("")
st.info("""
Hai kamu! Di hari yang luar biasa ini, aku cuma mau bilang kalau aku sangat bersyukur 
memilikimu. Terima kasih sudah menjadi alasan di balik senyumku setiap hari.
""")

# 7. Tombol Kejutan
st.write("")
if st.button("KLIK UNTUK KEJUTAN! 🎁"):
    st.balloons()
    st.success("Dengarkan pesan suara dariku... ❤️")
    st.audio(st.secrets["LINK_VOICE"])
    
    # Animasi teks sederhana
    placeholder = st.empty()
    full_msg = "I Love You Today, Tomorrow, and Always! 🥂"
    for i in range(len(full_msg) + 1):
        placeholder.subheader(full_msg[:i])
        time.sleep(0.05)
        
