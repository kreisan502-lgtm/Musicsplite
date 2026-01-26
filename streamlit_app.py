import streamlit as st
import os
import subprocess
from groq import Groq

# Inisialisasi Groq (Untuk fitur tambahan seperti ringkasan lirik atau deskripsi musik)
client = Groq(api_key="ISI_API_KEY_GROQ_ANDA")

st.title("🎵 AI Audio Splitter (Stem Separator)")
st.write("Unggah musik Anda dan biarkan AI memisahkan instrumennya!")

uploaded_file = st.file_uploader("Pilih file audio...", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Simpan file sementara
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.audio("temp_audio.mp3", format='audio/mp3')

    if st.button("Mulai Pisahkan Instrumen"):
        with st.spinner("Sedang memproses... Ini mungkin memakan waktu beberapa menit."):
            try:
                # Menjalankan Demucs (Pemisah Audio) melalui command line
                # Ini akan membagi menjadi 4 bagian: Vocals, Drums, Bass, Other
                subprocess.run(["python", "-m", "demucs.separate", "temp_audio.mp3", "-o", "output"], check=True)
                
                st.success("Pemisahan Selesai!")

                # Folder output biasanya: output/htdemucs/temp_audio/
                output_path = "output/htdemucs/temp_audio"
                stems = ["vocals.wav", "drums.wav", "bass.wav", "other.wav"]

                for stem in stems:
                    file_path = os.path.join(output_path, stem)
                    if os.path.exists(file_path):
                        st.subheader(f"Download {stem.capitalize()}")
                        st.audio(file_path)
                        with open(file_path, "rb") as f:
                            st.download_button(label=f"Unduh {stem}", data=f, file_name=stem)

            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

---

## 🚀 Alur Kerja Sistem

1.  **Input:** User mengunggah file MP3 ke aplikasi Streamlit.
2.  **Processing:** Script memanggil library **Demucs** untuk membedah frekuensi audio.
3.  **Output:** File dipecah menjadi 4 jalur (track) terpisah.
4.  **Groq Integration:** Anda bisa menggunakan Groq untuk menganalisis lirik yang dihasilkan (setelah di-transcribe menggunakan Whisper di Groq) untuk memberikan makna lagu tersebut.

---

## 📝 Catatan Penting
1.  **Resource:** Proses pemisahan audio (*Demucs*) cukup berat untuk CPU/RAM. Jika Anda hosting di Streamlit Cloud versi gratis, mungkin akan terkena limit memori. Disarankan menjalankannya di laptop lokal terlebih dahulu.
2.  **API Groq:** Gunakan Groq untuk bagian "cerdasnya", misalnya setelah audio dipisah, Anda kirim transkrip vokalnya ke Groq untuk diterjemahkan atau dijelaskan maknanya.

**Langkah selanjutnya:** Apakah Anda ingin saya membantu membuatkan fungsi khusus untuk mengirim hasil transkrip liriknya ke Groq agar bot bisa menjelaskan makna lagunya?
