import streamlit as st
import time

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Untuk Nurul Zakia ❤️",
    page_icon="🌹",
    layout="centered"
)

# 2. Judul & Header (Menggunakan fungsi standar Streamlit)
st.title("Barakallah Fii Umrik, Nurul Zakia ✨")
st.write("### *Semoga Allah senantiasa menjagamu dalam ketaatan dan kebahagiaan.*")
st.divider()

# 3. Musik Latar (Placeholder)
st.write("🎵 **Dengarkan ini sejenak ya...**")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 4. Foto (Placeholder)
st.write("")
st.image("https://images.unsplash.com/photo-1518199266791-739d6ff26ef0?q=80&w=1000", 
         caption="Terima kasih telah menjadi bagian dari ceritaku, Nurul Zakia. ❤️", 
         use_container_width=True)

# 5. Pesan Romantis & Islami
st.write("")
st.info("""
**Untukmu, Nurul Zakia...** 🌹

Di hari miladmu ini, aku memohon kepada Allah SWT agar setiap langkahmu selalu 
diberkahi, setiap urusanmu dimudahkan, dan hatimu selalu terpaut pada ridho-Nya.

Terima kasih telah menjadi sosok yang menginspirasiku untuk menjadi pribadi yang 
lebih baik. Semoga Allah menjaga ikatan kasih kita dalam naungan-Nya. 🤲✨
""")

# 6. Tombol Kejutan (Special Gift)
st.write("")
if st.button("KLIK UNTUK HADIAH RAHASIA! 🎁", use_container_width=True):
    # Efek Balon (Simbol perayaan)
    st.balloons()
    
    # Pesan Suara (Placeholder)
    st.success("Ada pesan suara khusus untukmu... ❤️")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
    
    st.divider()
    
    # Doa Penutup (Muncul perlahan tanpa HTML agar tidak error)
    placeholder = st.empty()
    doa_text = [
        "Barakallahu fii umrik... 🎂",
        "Semoga sehat walafiat selalu... 🤲",
        "Dimurahkan rezeki yang berkah... 💰",
        "Semoga kita selalu bersama hingga Jannah-Nya. 🌹",
        "Aamiin ya Rabbal 'Alamin. ❤️❤️❤️"
    ]
    
    for kalimat in doa_text:
        # Menggunakan .header() agar tulisan besar tapi tetap aman dari TypeError
        placeholder.header(kalimat)
        time.sleep(2.0)
        
