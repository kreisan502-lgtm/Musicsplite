import streamlit as st
import os
import subprocess
import librosa
import numpy as np
from groq import Groq

# Inisialisasi Groq
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Masukkan GROQ_API_KEY di Secrets!")

st.set_page_config(page_title="Ultra AI Music Splitter", layout="wide")
st.title("🎸 Ultra AI Music Splitter & Analyzer")
st.write("Memisahkan Vokal, Drum, Bass, Gitar, Piano, & Lainnya.")

uploaded_file = st.file_uploader("Upload Musik (Gunakan durasi pendek < 30 detik untuk Cloud)", type=["mp3", "wav"])

if uploaded_file:
    with open("input.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.audio("input.mp3")

    if st.button("Mulai Pisahkan Semua Instrumen"):
        with st.spinner("AI sedang bekerja keras membedah musik..."):
            try:
                # Menggunakan model 6-stems untuk kepekaan maksimal
                # vokal, drum, bass, gitar, piano, other
                subprocess.run([
                    "python", "-m", "demucs.separate", 
                    "-n", "htdemucs_6s", 
                    "input.mp3", "-o", "output"
                ], check=True)
                
                output_dir = "output/htdemucs_6s/input"
                stems = ["vocals", "drums", "bass", "guitar", "piano", "other"]
                
                cols = st.columns(3)
                for i, stem in enumerate(stems):
                    file_path = f"{output_dir}/{stem}.wav"
                    if os.path.exists(file_path):
                        with cols[i % 3]:
                            st.write(f"🎧 **{stem.capitalize()}**")
                            st.audio(file_path)

                # ANALISIS VOKAL MENGGUNAKAN GROQ & LIBROSA
                st.divider()
                st.subheader("🧐 Analisis Karakteristik Vokal")
                
                vocal_path = f"{output_dir}/vocals.wav"
                if os.path.exists(vocal_path):
                    # Transkripsi Vokal dengan Whisper Groq
                    with open(vocal_path, "rb") as af:
                        transcript = client.audio.transcriptions.create(
                            file=(vocal_path, af.read()),
                            model="whisper-large-v3",
                            response_format="text"
                        )
                    
                    # Mintalah Groq menganalisis apakah ada humming atau backing vocal
                    analysis = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "system", "content": "Kamu adalah asisten audio expert."},
                            {"role": "user", "content": f"Berdasarkan lirik ini: '{transcript}', apakah kamu bisa mendeteksi suasana lagu dan kemungkinan adanya backing vocal/humming?"}
                        ]
                    )
                    
                    st.write("**Lirik Terdeteksi:**")
                    st.info(transcript)
                    st.write("**Analisis AI:**")
                    st.success(analysis.choices[0].message.content)

            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Saran: Gunakan file yang sangat pendek atau jalankan di komputer lokal.")
                
