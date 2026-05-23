import streamlit as st
import math
from streamlit_option_menu import option_menu

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="ChemAssist Dashboard",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS MODERN
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

    backdrop-filter: blur(16px);

    border-right: 1px solid rgba(255,255,255,0.2);
}

/* Semua teks */
html, body, [class*="css"] {
    color: white !important;
}

/* Header */
.main-title {

    font-size: 58px;

    font-weight: 900;

    text-align: center;

    color: white;

    text-shadow:
        0 0 12px rgba(255,255,255,0.8),
        0 0 20px rgba(255,255,255,0.5);

    animation: glow 2s ease-in-out infinite alternate;
}

/* Glow */
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

.stButton > button:hover {

    transform: scale(1.05);
}

/* Metric */
[data-testid="stMetric"] {

    background: rgba(255,255,255,0.18);

    border-radius: 20px;

    padding: 18px;

    backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.25);

    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* Input */
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

    color: black !important;
}

/* Card */
.info-card {

    background: rgba(255,255,255,0.18);

    padding: 25px;

    border-radius: 22px;

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.25);

    box-shadow: 0 8px 24px rgba(0,0,0,0.15);

    color: white;
}

/* Molekul */
.molecule {

    position: fixed;

    width: 14px;

    height: 14px;

    background: rgba(255,255,255,0.5);

    border-radius: 50%;

    animation: float 12s infinite linear;
}

.molecule:nth-child(1) {
    left: 10%;
}

.molecule:nth-child(2) {
    left: 50%;
}

.molecule:nth-child(3) {
    left: 80%;
}

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
# HEADER
# =========================================================
st.markdown("""

<div class="logo-container">
    <div class="logo-spin">🧪</div>
</div>

<div class="main-title">
ChemAssist Dashboard
</div>

<div class="subtitle">
Sistem Analisis Parameter Laboratorium Kimia Interaktif
</div>

""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    selected = option_menu(
        menu_title="✨ ChemAssist Menu",

        options=[
            "Home",
            "Larutan",
            "pH",
            "Informasi Bahan Kimia",
            "Tentang"
        ],

        icons=[
            "house",
            "droplet",
            "eyedropper",
            "clipboard-data",
            "info-circle"
        ],

        menu_icon="stars",

        default_index=0,

        styles={

            "container": {
                "padding": "12px",
                "background-color": "rgba(255,255,255,0.12)",
                "border-radius": "20px",
            },

            "icon": {
                "color": "#0F172A",
                "font-size": "22px"
            },

            "menu-title": {
                "color": "#0F172A",
                "font-size": "28px",
                "font-weight": "bold",
            },

            "nav-link": {

                "font-size": "20px",

                "text-align": "left",

                "margin": "10px",

                "padding": "14px",

                "border-radius": "16px",

                "background-color": "rgba(255,255,255,0.35)",

                "color": "#0F172A",

                "font-weight": "600",

                "--hover-color": "rgba(255,255,255,0.55)",
            },

            "nav-link-selected": {

                "background": "linear-gradient(90deg,#38BDF8,#2563EB)",

                "color": "#FFFFFF",

                "font-weight": "bold",

                "box-shadow": "0 4px 15px rgba(37,99,235,0.45)"
            },
        }
    )

# =========================================================
# HOME
# =========================================================
if selected == "Home":

    st.markdown("## 🏠 Selamat Datang")

    st.markdown("""
    <div class="info-card">

    <h2>🧪 ChemAssist Dashboard</h2>

    <p>
    Aplikasi laboratorium kimia modern untuk membantu:
    </p>

    <ul>
    <li>💧 Perhitungan larutan</li>
    <li>🧬 Kalkulator pH</li>
    <li>📦 Informasi bahan kimia</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MENU LARUTAN
# =========================================================
elif selected == "Larutan":

    st.markdown("## 💧 Smart Solution Maker")

    col1, col2 = st.columns(2)

    with col1:

        mr = st.number_input(
            "Mr Senyawa",
            min_value=0.1,
            value=40.0
        )

        molaritas = st.number_input(
            "Konsentrasi (M)",
            min_value=0.0001,
            value=0.1
        )

        volume = st.number_input(
            "Volume (mL)",
            min_value=1.0,
            value=100.0
        )

        hitung = st.button("🚀 Hitung Massa")

    with col2:

        if hitung:

            massa = (molaritas * mr * volume) / 1000

            st.metric(
                "Massa Ditimbang",
                f"{massa:.4f} gram"
            )

            st.success(
                f"Timbang {massa:.4f} gram zat"
            )

# =========================================================
# MENU pH
# =========================================================
elif selected == "pH":

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

        proses = st.button("⚡ Hitung pH")

    with col2:

        if proses:

            if kategori == "Asam Kuat":

                ph = -math.log10(konsentrasi)

            elif kategori == "Basa Kuat":

                ph = 14 - (-math.log10(konsentrasi))

            elif kategori == "Asam Lemah":

                ph = -math.log10(math.sqrt(1.8e-5 * konsentrasi))

            else:

                ph = 14 - (-math.log10(math.sqrt(1.8e-5 * konsentrasi)))

            st.metric(
                "Nilai pH",
                f"{ph:.2f}"
            )

            st.progress(ph / 14)

# =========================================================
# INFORMASI BAHAN KIMIA
# =========================================================
elif selected == "Informasi Bahan Kimia":

    st.markdown("## 📦 Informasi Bahan Kimia")

    data_bahan = {

        "Asam Klorida (HCl)": {
            "Formula": "HCl",
            "Mr": 36.46,
            "Bahaya": "Korosif"
        },

        "NaOH": {
            "Formula": "NaOH",
            "Mr": 40.00,
            "Bahaya": "Korosif"
        },

        "KMnO4": {
            "Formula": "KMnO4",
            "Mr": 158.03,
            "Bahaya": "Oksidator kuat"
        },

        "Etanol": {
            "Formula": "C2H5OH",
            "Mr": 46.07,
            "Bahaya": "Mudah terbakar"
        }
    }

    pilihan = st.selectbox(
        "Pilih Bahan Kimia",
        list(data_bahan.keys())
    )

    info = data_bahan[pilihan]

    st.markdown(f"""
    <div class="info-card">

    <h2>🧪 {pilihan}</h2>

    <p><b>Formula:</b> {info['Formula']}</p>

    <p><b>Mr:</b> {info['Mr']} g/mol</p>

    <p><b>Bahaya:</b> {info['Bahaya']}</p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# TENTANG
# =========================================================
elif selected == "Tentang":

    st.markdown("## ℹ️ Tentang Aplikasi")

    st.markdown("""
    <div class="info-card">

    <h2>🧪 ChemAssist Dashboard</h2>

    <p>
    Dibuat menggunakan Python & Streamlit
    untuk membantu analisis laboratorium kimia.
    </p>

    <p>
    ✨ Tema modern glassmorphism
    </p>

    </div>
    """, unsafe_allow_html=True)
