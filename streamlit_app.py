import streamlit as st
import time

# Konfigurasi Halaman agar tampil cantik di HP maupun Laptop
st.set_page_config(
    page_title="Happy Birthday! ❤️",
    page_icon="🎂",
    layout="centered"
)

# Custom CSS untuk tampilan romantis tanpa ribet
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #fff5f5, #ffe0e0);
    }
    .main-title {
        color: #d32f2f;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 2.5rem;
        margin-top: 20px;
    }
    .love-text {
        color: #5d4037;
        text-align: center;
        font-style: italic;
    }
    </style>
    """, unsafe_content_html=True)

# --- LOADING DATA DARI SECRETS ---
# Pastikan nama di st.secrets[] sama dengan yang diisi di dashboard Streamlit Cloud
try:
    URL_FOTO = st.secrets["LINK_FOTO"]
    URL_LAGU = st.secrets["LINK_LAGU"]
    URL_VOICE = st.secrets["LINK_VOICE"]
except:
    st.error("Waduh! Sepertinya link rahasia belum diatur di Streamlit Secrets.")
    st.stop()

# --- BAGIAN 1: HEADER & MUSIK ---
st.markdown('<h1 class="main-title">Happy Birthday, Sayang! 🎂💖</h1>', unsafe_content_html=True)
st.write("---")

# Memutar lagu latar secara otomatis
st.audio(URL_LAGU, format="audio/mp3")
st.caption("🎵 *Tekan play untuk memulai suasana romantis...*")

# --- BAGIAN 2: FOTO UTAMA ---
st.write("")
col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
with col2:
    # Foto diambil dari Google Drive via Secrets
    st.image(URL_FOTO, use_container_width=True, caption="Setiap momen bersamamu adalah favoritku ✨")

# --- BAGIAN 3: PESAN ---
st.write("")
st.markdown("""
    <div style="background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #ff4b4b;">
        <p style="font-size: 1.1rem; line-height: 1.6; color: #333;">
            "Hai kamu! Di hari yang luar biasa ini, aku cuma mau bilang kalau aku sangat bersyukur 
            memilikimu. Terima kasih sudah menjadi alasan di balik senyumku setiap hari. 
            Semoga semua impianmu tercapai, dan aku bisa terus ada di sampingmu untuk merayakannya."
        </p>
    </div>
    """, unsafe_content_html=True)

# --- BAGIAN 4: TOMBOL KEJUTAN ---
st.write("")
st.write("👇 **Ada sesuatu buat kamu, klik tombol di bawah:**")

if st.button("KLIK UNTUK KEJUTAN! 🎁"):
    # Efek Balon Terbang
    st.balloons()
    
    # Menampilkan pesan suara dari Secrets
    st.success("Dengarkan pesan suara dariku ya... ❤️")
    st.audio(URL_VOICE)
    
    # Animasi teks penutup
    msg = st.empty()
    full_msg = "I Love You Today, Tomorrow, and Always! 🥂✨"
    for i in range(len(full_msg) + 1):
        msg.markdown(f"<h2 style='text-align: center; color: #ff4b4b;'>{full_msg[:i]}</h2>", unsafe_content_html=True)
        time.sleep(0.08)
        
