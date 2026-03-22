import streamlit as st
import time

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Barakallah Fii Umrik, Nurul Zakia ❤️",
    page_icon="✨",
    layout="centered"
)

# 2. Header & Judul
st.title("Barakallah Fii Umrik, Nurul Zakia ✨")
st.subheader("Semoga Allah senantiasa menjagamu dalam ketaatan dan kebahagiaan.")
st.divider()

# 3. Audio & Musik (Ganti dengan nasyid atau lagu instrumen lembut nanti)
st.write("🎵 **Dengarkan ini sejenak...**")
# Audio ini menggunakan link sampel instrumen lembut
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 4. Foto Utama (Placeholder)
st.write("")
st.image("https://images.unsplash.com/photo-1518199266791-739d6ff26ef0?q=80&w=1000", 
         caption="Terima kasih telah menjadi bagian dari ceritaku, Nurul Zakia.", 
         use_container_width=True)

# 5. Pesan Romantis & Islami
st.write("")
st.info("""
**Untukmu, Nurul Zakia...**

Di hari miladmu ini, aku memohon kepada Allah SWT agar setiap langkahmu selalu 
diberkahi, setiap urusanmu dimudahkan, dan hatimu selalu terpaut pada ridho-Nya.

Terima kasih telah menjadi sosok yang menginspirasiku untuk menjadi pribadi yang 
lebih baik. Semoga Allah menjaga ikatan kasih kita dalam naungan-Nya.
""")

# 6. Tombol Kejutan (Special Gift)
st.write("")
if st.button("KLIK UNTUK HADIAH RAHASIA! 🎁", use_container_width=True):
    # Efek Visual (Banyak Salju agar suasana tenang dan indah)
    st.snow()
    
    # Pesan Suara (Ganti dengan rekaman doamu nanti)
    st.success("Ada pesan suara khusus untukmu... ❤️")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
    
    # Doa Penutup (Muncul perlahan)
    st.write("---")
    placeholder = st.empty()
    doa_text = [
        "Barakallahu fii umrik...",
        "Semoga sehat walafiat selalu...",
        "Dimurahkan rezeki yang berkah...",
        "Dan semoga kita selalu bersama hingga Jannah-Nya.",
        "Aamiin ya Rabbal 'Alamin. ❤️"
    ]
    
    for kalimat in doa_text:
        placeholder.markdown(f"<h3 style='text-align: center; color: #d32f2f;'>{kalimat}</h3>", unsafe_content_html=True)
        time.sleep(2.0) # Jeda agar bisa dibaca satu per satu
    
