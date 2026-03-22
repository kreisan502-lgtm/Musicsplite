import streamlit as st
import time

# 1. Konfigurasi Halaman - Harus di baris pertama setelah import
st.set_page_config(
    page_title="HBD Sayang! ❤️",
    page_icon="🎂",
    layout="centered"
)

# 2. CSS Sederhana (Baris tunggal agar tidak error)
st.markdown("<style>.stApp {background-color: #fff5f5;} .stButton>button {width:100%; border-radius:20px; background-color:#ff4b4b; color:white;}</style>", unsafe_content_html=True)

# 3. Judul & Musik Latar (Placeholder)
st.markdown("<h1 style='text-align: center; color: #d32f2f;'>Happy Birthday! 🎂💖</h1>", unsafe_content_html=True)
st.markdown("<p style='text-align: center; color: #ff4b4b;'><i>\"Seseorang yang spesial sedang berulang tahun...\"</i></p>", unsafe_content_html=True)
st.divider()

# Audio Sample (Ganti ke musik romantis nanti)
st.write("🎵 **Putar musiknya:**")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 4. Foto Placeholder (Menggunakan gambar dari internet dulu)
st.write("")
st.image("https://images.unsplash.com/photo-1513151233558-d860c5398176?q=80&w=1000", 
         caption="Bayangkan ini foto kita berdua ✨", 
         use_container_width=True)

# 5. Pesan Romantis
st.write("")
st.info("""
Hai kamu! Di hari yang luar biasa ini, aku cuma mau bilang kalau aku sangat bersyukur 
memilikimu. Terima kasih sudah menjadi alasan di balik senyumku setiap hari.
""")

# 6. Tombol Kejutan
st.write("")
if st.button("KLIK UNTUK KEJUTAN! 🎁"):
    st.balloons()
    st.snow()
    
    # Pesan Rahasia (Audio Placeholder)
    st.success("Dengarkan pesan suara dariku... ❤️")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
    
    # Animasi teks penutup
    placeholder = st.empty()
    full_msg = "I Love You Today, Tomorrow, and Always! 🥂"
    for i in range(len(full_msg) + 1):
        placeholder.markdown(f"<h3 style='text-align: center; color: #ff4b4b;'>{full_msg[:i]}</h3>", unsafe_content_html=True)
        time.sleep(0.05)
        
