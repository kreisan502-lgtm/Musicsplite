import streamlit as st
import time

# 1. Konfigurasi Halaman (Wajib Paling Atas)
st.set_page_config(
    page_title="Happy Birthday! ❤️",
    page_icon="🎂",
    layout="centered"
)

# 2. Judul Sederhana (Menggunakan fungsi bawaan Streamlit agar aman)
st.title("Happy Birthday! 🎂💖")
st.subheader("Seseorang yang spesial sedang berulang tahun...")
st.divider()

# 3. Audio & Musik (Menggunakan Link Sampel)
st.write("🎵 **Putar musiknya di sini:**")
# Audio ini akan langsung muncul tanpa CSS tambahan
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 4. Foto Utama (Placeholder)
st.write("")
st.image("https://images.unsplash.com/photo-1513151233558-d860c5398176?q=80&w=1000", 
         caption="Momen indah untuk hari yang indah ✨", 
         use_container_width=True)

# 5. Pesan Romantis
st.write("")
st.info("""
Hai kamu! Di hari yang luar biasa ini, aku cuma mau bilang kalau aku sangat bersyukur 
memilikimu. Terima kasih sudah menjadi alasan di balik senyumku setiap hari.
""")

# 6. Tombol Kejutan
st.write("")
if st.button("KLIK UNTUK KEJUTAN! 🎁", use_container_width=True):
    # Efek Visual
    st.balloons()
    st.snow()
    
    # Pesan Suara (Placeholder)
    st.success("Dengarkan pesan rahasia dariku... ❤️")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
    
    # Animasi Teks Penutup Sederhana
    st.write("---")
    placeholder = st.empty()
    full_msg = "I Love You Today, Tomorrow, and Always! 🥂"
    for i in range(len(full_msg) + 1):
        placeholder.markdown(f"### {full_msg[:i]}")
        time.sleep(0.05)
