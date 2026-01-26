import streamlit as st
import os
import subprocess
from groq import Groq

# Inisialisasi Groq menggunakan Secrets yang sudah kamu simpan
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("API Key tidak ditemukan. Pastikan sudah memasukkan GROQ_API_KEY di menu Secrets.")

st.set_page_config(page_title="AI Music Splitter", page_icon="🎵")

st.title("🎵 AI Music Splitter & Lyric Analyzer")
st.write("Unggah musik untuk memisahkan Vokal dan Instrumen menggunakan AI.")

# Upload File
uploaded_file = st.file_uploader("Pilih file audio (MP3/WAV)...", type=["mp3", "wav"])

if uploaded_file is not None:
    # 1. Simpan file yang diunggah secara lokal
    input_path = "input_audio.mp3"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.audio(input_path, format='audio/mp3')

    if st.button("Mulai Proses Pemisahan"):
        with st.spinner("Sedang memproses... Ini mungkin memakan waktu beberapa menit."):
            try:
                # 2. Proses Pemisahan menggunakan Demucs (2 stems: vokal & non-vokal)
                # Catatan: Ini membutuhkan resource CPU/RAM yang besar
                subprocess.run([
                    "python", "-m", "demucs.separate", 
                    "--two-stems", "vocals", 
                    input_path, 
                    "-o", "output"
                ], check=True)
                
                # Path hasil output (default demucs)
                path_vokal = "output/htdemucs/input_audio/vocals.wav"
                path_instrumen = "output/htdemucs/input_audio/no_vocals.wav"

                # 3. Tampilkan Hasil
                st.success("Pemisahan Selesai!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("🎤 Vokal")
                    if os.path.exists(path_vokal):
                        st.audio(path_vokal)
                        with open(path_vokal, "rb") as f:
                            st.download_button("Unduh Vokal", f, file_name="vokal.wav")

                with col2:
                    st.subheader("🎹 Instrumen")
                    if os.path.exists(path_instrumen):
                        st.audio(path_instrumen)
                        with open(path_instrumen, "rb") as f:
                            st.download_button("Unduh Instrumen", f, file_name="instrumen.wav")

                # 4. Integrasi Groq: Transkripsi & Analisis
                st.divider()
                st.subheader("📝 Analisis Lirik (Powered by Groq)")
                with open(path_vokal, "rb") as audio_file:
                    # Menggunakan model Whisper di Groq untuk transkripsi cepat
                    transcription = client.audio.transcriptions.create(
                        file=(path_vokal, audio_file.read()),
                        model="whisper-large-v3",
                        response_format="text"
                    )
                    
                    # Mintalah model Llama 3 di Groq untuk menjelaskan makna liriknya
                    completion = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "system", "content": "Kamu adalah ahli musik. Jelaskan makna dari lirik lagu berikut dalam Bahasa Indonesia."},
                            {"role": "user", "content": transcription}
                        ]
                    )
                    
                    st.write("**Transkrip Lirik:**")
                    st.info(transcription)
                    st.write("**Makna Lagu:**")
                    st.success(completion.choices[0].message.content)

            except Exception as e:
                st.error(f"Terjadi kesalahan teknis: {e}")
                st.warning("Tips: Streamlit Cloud gratis memiliki batas RAM. Jika error, coba gunakan file audio yang durasinya sangat pendek (di bawah 1 menit).")
                
