import streamlit as st
import math
import pandas as pd
from datetime import datetime

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Asisten Lab Dashboard",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS BARU — TEMA LAB KIMIA BIRU CERAH
# =========================================================
st.markdown("""
<style>

/* Background utama */
.stApp {
    background: linear-gradient(
        135deg,
        #38BDF8,
        #0EA5E9,
        #2563EB,
        #1E3A8A
    );

    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

/* Animasi background */
@keyframes gradientBG {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

/* Sidebar */
section[data-testid="stSidebar"] {

    background: rgba(255,255,255,0.15);

    backdrop-filter: blur(14px);

    border-right: 1px solid rgba(255,255,255,0.2);
}

/* Semua teks */
html, body, [class*="css"] {

    color: white !important;
}

/* Judul utama */
.main-title {

    font-size: 58px;

    font-weight: 900;

    text-align: center;

    color: white;

    text-shadow:
        0 0 10px rgba(255,255,255,0.8),
        0 0 20px rgba(255,255,255,0.5);

    animation: glow 2s ease-in-out infinite alternate;
}

/* Glow title */
@keyframes glow {

    from {
        text-shadow:
            0 0 10px rgba(255,255,255,0.7);
    }

    to {
        text-shadow:
            0 0 25px rgba(255,255,255,1);
    }
}

/* Subtitle */
.subtitle {

    text-align: center;

    font-size: 18px;

    color: #E0F2FE;

    margin-bottom: 35px;
}

/* Logo */
.logo-container {

    text-align: center;

    margin-bottom: 10px;
}

.logo-spin {

    font-size: 80px;

    display: inline-block;

    animation: spin 6s linear infinite;
}

@keyframes spin {

    100% {
        transform: rotate(360deg);
    }
}

/* Card metric */
[data-testid="stMetric"] {

    background: rgba(255,255,255,0.18);

    border-radius: 20px;

    padding: 18px;

    backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.25);

    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* Tombol */
.stButton > button {

    background: linear-gradient(
        90deg,
        #2563EB,
        #38BDF8
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 12px 18px;

    font-weight: bold;

    transition: 0.3s;

    box-shadow: 0 4px 20px rgba(255,255,255,0.25);
}

/* Hover tombol */
.stButton > button:hover {

    transform: scale(1.05);

    background: linear-gradient(
        90deg,
        #1D4ED8,
        #0EA5E9
    );
}

/* Input box */
.stTextInput input,
.stNumberInput input {

    background-color: rgba(255,255,255,0.18) !important;

    color: white !important;

    border-radius: 12px !important;

    border: 1px solid rgba(255,255,255,0.25) !important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {

    background-color: rgba(255,255,255,0.18) !important;

    border-radius: 12px !important;

    color: white !important;
}

/* Radio */
.stRadio label {

    color: white !important;
}

/* Progress bar */
.stProgress > div > div > div {

    background: linear-gradient(
        90deg,
        #FFFFFF,
        #BAE6FD
    );
}

/* Inventaris card */
.info-card {

    background: rgba(255,255,255,0.16);

    padding: 25px;

    border-radius: 22px;

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.25);

    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}

/* Molekul animasi */
.molecule {

    position: fixed;

    width: 14px;

    height: 14px;

    background: rgba(255,255,255,0.5);

    border-radius: 50%;

    animation: float 12s infinite linear;
}

/* Posisi molecule */
.molecule:nth-child(1) {
    left: 10%;
}

.molecule:nth-child(2) {
    left: 50%;
}

.molecule:nth-child(3) {
    left: 80%;
}

/* Animasi molecule */
@keyframes float {

    0% {
        transform: translateY(100vh);
    }

    100% {
        transform: translateY(-100vh);
    }
}

</style>

<div class="molecule"></div>
<div class="molecule"></div>
<div class="molecule"></div>

""", unsafe_allow_html=True)
# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown("## ⚙️ Pusat Kontrol Lab")

    menu_utama = st.radio(
        "Pilih Menu",
        [
            "💧 Pembuatan & Pengenceran",
            "🧬 Kalkulator pH",
            "📦 Inventaris Bahan Lab"
        ]
    )

    st.markdown("---")

    st.markdown("## 🤖 AI Kimia Mini")

    pertanyaan = st.text_input("Tanya Kimia")

    if pertanyaan:

        q = pertanyaan.lower()

        if "asam" in q:
            st.success("Asam menghasilkan ion H+")

        elif "basa" in q:
            st.success("Basa menghasilkan ion OH-")

        elif "ph" in q:
            st.success("pH menunjukkan tingkat keasaman")

        else:
            st.info("Database AI mini belum punya jawaban 😭")

# =========================================================
# HEADER BARU
# =========================================================
st.markdown("""

<div class="logo-container">
    <div class="logo-spin">🧪</div>
</div>

<div class="main-title">
Asisten Lab Dashboard
</div>

<div class="subtitle">
Sistem Analisis Parameter Laboratorium Kimia Interaktif
</div>

""", unsafe_allow_html=True)
# =========================================================
# FUNGSI
# =========================================================
def export_csv(data):

    df = pd.DataFrame(data)

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📁 Download CSV",
        csv,
        file_name=f"laporan_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# =========================================================
# MENU 1
# =========================================================
if menu_utama == "💧 Pembuatan & Pengenceran":

    st.markdown("## 💧 Pembuatan Larutan & Pengenceran")

    col1, col2 = st.columns(2)

    with col1:

        satuan = st.selectbox(
            "Satuan",
            [
                "Molaritas (M)",
                "Normalitas (N)",
                "ppm (mg/L)",
                "Persen Massa (%)"
            ]
        )

        metode = st.radio(
            "Metode",
            [
                "Membuat Larutan dari Padatan",
                "Pengenceran Cairan"
            ]
        )

        mr = st.number_input(
            "Mr Zat",
            min_value=0.1,
            value=40.0
        )

        if metode == "Membuat Larutan dari Padatan":

            volume = st.number_input(
                "Volume (mL)",
                min_value=1.0,
                value=100.0
            )

            if satuan == "Molaritas (M)":

                c = st.number_input(
                    "Konsentrasi (M)",
                    min_value=0.0001,
                    value=0.1,
                    format="%.4f"
                )

                if st.button("🚀 Hitung"):

                    massa = (c * mr * volume) / 1000

                    with col2:

                        st.metric(
                            "Massa Ditimbang",
                            f"{massa:.4f} gram"
                        )

                        st.success(
                            f"Timbang {massa:.4f} gram zat"
                        )

                        export_csv({
                            "Massa": [massa]
                        })

            elif satuan == "ppm (mg/L)":

                ppm = st.number_input(
                    "ppm",
                    min_value=0.1,
                    value=100.0
                )

                if st.button("🚀 Hitung"):

                    massa = (ppm * (volume/1000)) / 1000

                    with col2:

                        st.metric(
                            "Massa Ditimbang",
                            f"{massa:.4f} gram"
                        )

        else:

            c1 = st.number_input("C1", min_value=0.0001, value=10.0)
            c2 = st.number_input("C2", min_value=0.0001, value=1.0)
            v2 = st.number_input("V2", min_value=1.0, value=100.0)

            if st.button("🚀 Hitung Pengenceran"):

                if c1 <= c2:

                    st.error("C1 harus lebih besar dari C2")

                else:

                    v1 = (c2 * v2) / c1

                    with col2:

                        st.metric(
                            "Volume Stok",
                            f"{v1:.2f} mL"
                        )

                        st.success(
                            f"Ambil {v1:.2f} mL lalu encerkan hingga {v2:.0f} mL"
                        )

# =========================================================
# MENU 2
# =========================================================
elif menu_utama == "🧬 Kalkulator pH":

    st.markdown("## 🧬 Kalkulator pH")

    col1, col2 = st.columns(2)

    with col1:

        kategori = st.selectbox(
            "Jenis Larutan",
            [
                "Asam Kuat",
                "Basa Kuat",
                "Asam Lemah",
                "Basa Lemah"
            ]
        )

        konsentrasi = st.number_input(
            "Konsentrasi",
            min_value=1e-6,
            value=0.01,
            format="%.5f"
        )

        if "Kuat" in kategori:

            valensi = st.number_input(
                "Valensi",
                min_value=1,
                value=1
            )

        else:

            ka_kb = st.number_input(
                "Ka/Kb",
                min_value=1e-10,
                value=1.8e-5,
                format="%.2e"
            )

        proses = st.button("⚡ Hitung pH")

    with col2:

        if proses:

            if kategori == "Asam Kuat":
                ph = -math.log10(konsentrasi * valensi)

            elif kategori == "Basa Kuat":
                ph = 14 - (-math.log10(konsentrasi * valensi))

            elif kategori == "Asam Lemah":
                ph = -math.log10(math.sqrt(ka_kb * konsentrasi))

            else:
                ph = 14 - (-math.log10(math.sqrt(ka_kb * konsentrasi)))

            st.metric(
                "Nilai pH",
                f"{ph:.2f}"
            )

            st.progress(ph / 14)

            fig, ax = plt.subplots(figsize=(8,2))

            ax.plot([0,14],[0,14])

            ax.scatter(ph, ph, s=250)

            ax.set_xlim(0,14)
            ax.set_ylim(0,14)

            ax.set_xlabel("Skala pH")

            st.pyplot(fig)

            export_csv({
                "pH": [ph]
            })

# =========================================================
# MENU 3
# =========================================================
elif menu_utama == "📦 Inventaris Bahan Lab":

    st.markdown("## 📦 Inventaris Bahan Kimia")

    data_bahan = {

        "Etanol (C2H5OH)": {
            "Formula": "C2H5OH",
            "Mr": 46.07,
            "Sifat": "Pelarut organik",
            "Bahaya": "Mudah terbakar"
        },

        "NaOH": {
            "Formula": "NaOH",
            "Mr": 40.00,
            "Sifat": "Basa kuat",
            "Bahaya": "Korosif"
        },

        "HCl": {
            "Formula": "HCl",
            "Mr": 36.46,
            "Sifat": "Asam kuat",
            "Bahaya": "Korosif"
        },

        "KMnO4": {
            "Formula": "KMnO4",
            "Mr": 158.03,
            "Sifat": "Oksidator kuat",
            "Bahaya": "Toksik"
        },

        "AgNO3": {
            "Formula": "AgNO3",
            "Mr": 169.87,
            "Sifat": "Reagen analitik",
            "Bahaya": "Korosif"
        }
    }

    cari = st.text_input("🔍 Cari Bahan Kimia")

    hasil = []

    for bahan in data_bahan:

        if cari.lower() in bahan.lower():
            hasil.append(bahan)

    pilihan = st.selectbox(
        "Pilih Bahan",
        hasil if hasil else list(data_bahan.keys())
    )

    info = data_bahan[pilihan]

    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.08);
        padding:25px;
        border-radius:20px;
        backdrop-filter:blur(10px);
        box-shadow:0 8px 32px rgba(0,0,0,0.3);
        border:1px solid rgba(255,255,255,0.1);
    ">
        <h2>🔬 {pilihan}</h2>

        <p><b>Formula:</b> {info['Formula']}</p>

        <p><b>Mr:</b> {info['Mr']} g/mol</p>

        <p><b>Sifat:</b> {info['Sifat']}</p>

        <p><b>Bahaya:</b> {info['Bahaya']}</p>

    </div>
    """, unsafe_allow_html=True)

    export_csv({
        "Bahan": [pilihan],
        "Formula": [info['Formula']]
    })
