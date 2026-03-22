import streamlit as st
import time

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Happy Birthday! ❤️",
    page_icon="🎂",
    layout="centered"
)

# 2. Custom UI dengan CSS (Warna Pastel Romantis)
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f5;
    }
    .main-title {
        color: #d32f2f;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #ff4b4b;
        text-align: center;
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 1.2rem;
        margin-top: 0px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #d32f2f;
        border: none;
        color: white;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_content_html=True)

# --- BAGIAN 1: HEADER ---
st.markdown('<p class="main-title">Happy Birthday! 🎂</p>', unsafe_content_html=True)
st.markdown('<p class="sub-title">"Untuk seseorang yang paling spesial..."</p>', unsafe_content_html=True)
st.divider()

# --- BAGIAN 2: AUDIO PLACEHOLDER ---
# Menggunakan audio sampel agar kamu bisa tes UI-nya dulu
st.write("🎵 **Putar musiknya di sini:**")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") 
st.caption("_(Nanti ini akan diganti dengan lagu pilihanmu)_")

# --- BAGIAN 3: FOTO PLACEHOLDER ---
st.write("")
# Menggunakan gambar estetik dari Unsplash sebagai contoh tampilan
st.image("https://images.unsplash.com/photo-1530103862676-fa8c9d343165?q=80&w=1000", 
         caption="Bayangkan ini adalah foto favorit kalian ✨", 
         use_container_width=True)

# --- BAGIAN 4: PESAN ---
st.write("")
st.markdown("""
    <div style="background-color: white; padding: 25px; border-radius: 20px; box-shadow: 2px 2px 15px rgba(0,0,0,0.05);">
        <h4 style="color: #d32f2f; margin-top: 0;">Dear Kamu, ❤️</h4>
        <p style="color: #5d4037; line-height: 1.6;">
            "Hari ini adalah hari yang luar biasa karena seseorang yang luar biasa lahir ke dunia. 
            Terima kasih telah memberikan warna dalam hidupku. Semoga tahun ini penuh dengan 
            kebahagiaan yang tak henti-hentinya."
        </p>
    </div>
    """, unsafe_content_html=True)

# --- BAGIAN 5: TOMBOL KEJUTAN ---
st.write("")
st.write("👇 **Ada kejutan kecil buat kamu:**")

if st.button("KLIK UNTUK KEJUTAN! 🎁"):
    # Efek Balon
    st.balloons()
    
    # Suara Kejutan (Placeholder)
    st.success("Dengarkan pesan rahasia ini... ❤️")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
    
    # Animasi Teks Penutup
    msg_area = st.empty()
    final_text = "I Love You Today, Tomorrow, and Always! ✨"
    for i in range(len(final_text) + 1):
        msg_area.markdown(f"<h3 style='text-align: center; color: #ff4b4b;'>{final_text[:i]}</h3>", unsafe_content_html=True)
        time.sleep(0.05)
    
    # Tambahan Snow/Salju agar lebih meriah
    st.snow()
    
