import streamlit as st
import math

# --- KONFIGURASI TAMPILAN ---
st.set_page_config(
    page_title="Asisten Lab Dashboard ", 
    page_icon="🧪", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- STYLE CSS AGAR TIDAK MONOTON ---
st.markdown("""
    <style>
    .main-title { font-size:38px !important; font-weight: 800; color: #1E3A8A; text-align: center; margin-bottom: 0px; }
    .subtitle { font-size:16px !important; text-align: center; color: #6B7280; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR KONTROL ---
with st.sidebar:
    st.markdown("## ⚙️ Pusat Kontrol Lab")
    menu_utama = st.radio(
        "Pilih Menu Aplikasi:",
        ["💧 Pembuatan & Pengenceran", "🧬 Kalkulator pH ", "📦 Inventaris Bahan Lab"]
    )
    st.markdown("---")
    st.info("Aplikasi Tugas Akhir Logika & Pemrograman Komputer.")

# --- HEADER UTAMA ---
st.markdown("<div class='main-title'>🧪 Asisten Lab Dashboard </div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Sistem Analisis Parameter Laboratorium Kimia Interaktif</div>", unsafe_allow_html=True)
# =========================================================================
# MENU 1: KALKULATOR LARUTAN MULTI-SATUAN
# =========================================================================
if menu_utama == "💧 Pembuatan & Pengenceran":
    st.markdown("### 💧 Perhitungan Pembuatan Larutan & Pengenceran")
    col_in, col_out = st.columns(2, gap="large")
    
    with col_in:
        st.subheader("📥 Pengaturan Parameter")
        opsi_satuan = st.selectbox("Satuan Konsentrasi:", ["Molaritas (M)", "Normalitas (N)", "ppm (mg/L)", "Persen Massa (%)"])
        pilihan_sub = st.radio("Metode Pembuatan:", ["Membuat Larutan dari Padatan", "Pengenceran Cairan"])
        mr = st.number_input("Massa Molar / Mr Zat (g/mol):", min_value=0.1, value=40.0, step=0.1)
        
        if opsi_satuan == "Normalitas (N)":
            valensi_n = st.number_input("Valensi Zat (Ekivalen):", min_value=1, value=1, step=1)
            
        st.markdown("---")
        
        if pilihan_sub == "Membuat Larutan dari Padatan":
            volume_ml = st.number_input("Volume Larutan yang Ingin Dibuat (mL):", min_value=1.0, value=100.0)
            
            if opsi_satuan == "Molaritas (M)":
                c_m = st.number_input("Konsentrasi Molaritas (M):", min_value=0.0001, value=0.1000, format="%.4f")
                if st.button("🚀 Jalankan Komputasi", type="primary"):
                    massa = (c_m * mr * volume_ml) / 1000
                    with col_out:
                        st.subheader("📤 Hasil Analisis")
                        st.metric(label="Massa Harus Ditimbang", value=f"{massa:.4f} gram")
                        st.success(f"Timbang {massa:.4f} g zat, larutkan dalam labu takar {volume_ml:.0f} mL, homogenkan larutan.")
            
            elif opsi_satuan == "Normalitas (N)":
                c_n = st.number_input("Konsentrasi Normalitas (N):", min_value=0.0001, value=0.1000, format="%.4f")
                if st.button("🚀 Jalankan Komputasi", type="primary"):
                    be = mr / valensi_n
                    massa = (c_n * be * volume_ml) / 1000
                    with col_out:
                        st.subheader("📤 Hasil Analisis")
                        st.metric(label="Massa Harus Ditimbang", value=f"{massa:.4f} gram")
                        st.success(f"Timbang {massa:.4f} g zat, encerkan hingga {volume_ml:.0f} mL, homogenkan larutan.")
                        
            elif opsi_satuan == "ppm (mg/L)":
                c_ppm = st.number_input("Konsentrasi ppm (mg/L):", min_value=0.1, value=100.0)
                if st.button("🚀 Jalankan Komputasi", type="primary"):
                    massa = (c_ppm * (volume_ml / 1000)) / 1000
                    with col_out:
                        st.subheader("📤 Hasil Analisis")
                        st.metric(label="Massa Harus Ditimbang", value=f"{massa:.4f} gram")
                        st.info(f"Sama dengan {massa*1000:.2f} mg zat padat.")
                        
            elif opsi_satuan == "Persen Massa (%)":
                c_persen = st.number_input("Persen Massa Zat (% w/w):", min_value=0.01, max_value=100.0, value=5.0)
                rho = st.number_input("Massa Jenis Pelarut (g/mL):", min_value=0.1, value=1.0)
                if st.button("🚀 Jalankan Komputasi", type="primary"):
                    massa_total = volume_ml * rho
                    massa = (c_persen / 100) * massa_total
                    with col_out:
                        st.subheader("📤 Hasil Analisis")
                        st.metric(label="Massa Zat Terlarut", value=f"{massa:.2f} gram")
                        st.warning(f"Campurkan {massa:.2f} g zat dengan {massa_total - massa:.2f} g pelarut.")
        else:
            c1 = st.number_input("Konsentrasi Larutan Pekat (C1):", min_value=0.0001, value=10.0)
            c2 = st.number_input("Konsentrasi Diinginkan (C2):", min_value=0.0001, value=1.0)
            v2 = st.number_input("Volume Diinginkan (V2) dalam mL:", min_value=1.0, value=100.0)
            if st.button("🚀 Jalankan Komputasi", type="primary"):
                with col_out:
                    st.subheader("📤 Hasil Analisis")
                    if c1 <= c2:
                        st.error("Error: C1 harus lebih besar dari C2!")
                    else:
                        v1 = (c2 * v2) / c1
                        st.metric(label="Volume Stok Diambil (V1)", value=f"{v1:.2f} mL")
                        st.success(f"Ambil {v1:.2f} mL larutan pekat, encerkan hingga {v2:.0f} mL.")
# =========================================================================
# MENU 2: KALKULATOR pH 
# =========================================================================
elif menu_utama == "🧬 Kalkulator pH ":
    st.markdown("### 🧬 Simulator & Kalkulator pH Larutan Tingkat Lanjut")
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("📥 Input Data Larutan")
        kategori = st.selectbox("Klasifikasi Asam-Basa:", ["Asam Kuat", "Basa Kuat", "Asam Lemah", "Basa Lemah"])
        konsentrasi_ph = st.number_input("Konsentrasi Sistem (Molaritas):", min_value=1e-6, value=0.0100, format="%.5f")
        if "Kuat" in kategori:
            valensi_ph = st.number_input("Valensi Larutan (Jumlah Ion):", min_value=1, max_value=3, value=1)
        else:
            k_value = st.number_input("Konstanta Disosiasi (Ka/Kb):", min_value=1e-10, max_value=1.0, value=1.8e-5, format="%.2e")
        proses_ph = st.button("⚡ Hitung Nilai pH", type="primary")

    with col2:
        st.subheader("📊 Output & Indikator Skala")
        if proses_ph:
            if "Asam Kuat" == kategori:
                ph_akhir = -math.log10(konsentrasi_ph * valensi_ph)
            elif "Basa Kuat" == kategori:
                ph_akhir = 14 - (-math.log10(konsentrasi_ph * valensi_ph))
            elif "Asam Lemah" == kategori:
                ph_akhir = -math.log10(math.sqrt(k_value * konsentrasi_ph))
            elif "Basa Lemah" == kategori:
                ph_akhir = 14 - (-math.log10(math.sqrt(k_value * konsentrasi_ph)))
                
            st.metric(label="Nilai Real pH Terukur", value=f"{ph_akhir:.2f}")
            
            if ph_akhir < 3:
                st.markdown("<div style='background-color:#EF4444; color:white; padding:15px; border-radius:8px; text-align:center; font-weight:bold;'>🟥 ASAM KUAT</div>", unsafe_allow_html=True)
            elif ph_akhir < 7:
                st.markdown("<div style='background-color:#F59E0B; color:white; padding:15px; border-radius:8px; text-align:center; font-weight:bold;'>🟨 ASAM LEMAH</div>", unsafe_allow_html=True)
            elif ph_akhir == 7:
                st.markdown("<div style='background-color:#10B981; color:white; padding:15px; border-radius:8px; text-align:center; font-weight:bold;'>🟩 NETRAL</div>", unsafe_allow_html=True)
            elif ph_akhir <= 11:
                st.markdown("<div style='background-color:#3B82F6; color:white; padding:15px; border-radius:8px; text-align:center; font-weight:bold;'>🟦 BASA LEMAH</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div style='background-color:#8B5CF6; color:white; padding:15px; border-radius:8px; text-align:center; font-weight:bold;'>🟪 BASA KUAT</div>", unsafe_allow_html=True)
            st.progress(min(max(ph_akhir / 14.0, 0.0), 1.0))

# =========================================================================
# MENU 3: DATABASE INVENTARIS BAHAN LAB
# =========================================================================
elif menu_utama == "📦 Inventaris Bahan Lab":
    st.markdown("### 📦 Manajemen Informasi & Inventaris Bahan Laboratorium")
    data_bahan = {
        "Akuades (H2O)": {"Formula": "H2O", "Mr": 18.02, "Sifat": "Pelarut universal, netral.", "Bahaya": "Aman / Non-Hazardous", "Status": "Aman"},
        "Asam Klorida (HCl)": {"Formula": "HCl", "Mr": 36.46, "Sifat": "Asam kuat, cairan beruap cair.", "Bahaya": "Korosif, iritasi saluran pernapasan.", "Status": "Bahaya"},
        "Natrium Hidroksida (NaOH)": {"Formula": "NaOH", "Mr": 40.00, "Sifat": "Basa kuat, padatan pelet putih, higroskopis.", "Bahaya": "Korosif berat, menyebabkan luka bakar parah.", "Status": "Bahaya"},
        "Etanol (C2H5OH)": {"Formula": "C2H5OH", "Mr": 46.07, "Sifat": "Pelarut organik, mudah menguap.", "Bahaya": "Cairan mudah terbakar (Flammable).", "Status": "Bahaya"},
        "Asam Asetat (CH3COOH)": {"Formula": "CH3COOH", "Mr": 60.05, "Sifat": "Asam lemah, berbau menyengat tajam (cuka).", "Bahaya": "Korosif pada konsentrasi pekat, cairan mudah terbakar.", "Status": "Bahaya"},
        "Asam Sulfat (H2SO4)": {"Formula": "H2SO4", "Mr": 98.08, "Sifat": "Asam kuat bervalensi 2, cairan kental berenergi eksotermik tinggi.", "Bahaya": "Sangat korosif, destruktif pada jaringan kulit.", "Status": "Bahaya"},
        "Natrium Klorida (NaCl)": {"Formula": "NaCl", "Mr": 58.44, "Sifat": "Garam dapur, padatan kristal putih.", "Bahaya": "Aman pada konsentrasi normal.", "Status": "Aman"},
        "Aseton (CH3COCH3)": {"Formula": "CH3COCH3", "Mr": 58.08, "Sifat": "Pelarut organik polar, sangat mudah menguap.", "Bahaya": "Sangat mudah terbakar, iritasi mata.", "Status": "Bahaya"},
        "Tembaga(II) Sulfat (CuSO4)": {"Formula": "CuSO4", "Mr": 159.61, "Sifat": "Garam anorganik, umumnya berwarna biru (hidrat).", "Bahaya": "Toksik bagi lingkungan akuatik, berbahaya jika tertelan.", "Status": "Bahaya"},
    }
    cari_bahan = st.text_input("🔍 Cari Nama Bahan Kimia:", "")
    list_bahan = [b for b in data_bahan.keys() if cari_bahan.lower() in b.lower()]
    
    if list_bahan:
        pilihan_bahan = st.selectbox("Pilih Bahan Kimia:", list_bahan)
        info = data_bahan[pilihan_bahan]
        st.markdown(f"---")
        st.markdown(f"""
        <div style='background-color: #F8FAFC; padding: 20px; border-radius: 12px; border-left: 8px solid {info['Warna']};'>
            <h4>🔬 {pilihan_bahan}</h4>
            <p><b>Rumus:</b> {info['Formula']} | <b>Mr:</b> {info['Mr']} g/mol</p>
            <p><b>Sifat:</b> {info['Sifat']}</p>
            <p style='color:{info['Warna']}; font-weight:bold;'>⚠️ Bahaya: {info['Bahaya']}</p>
        </div>
        """, unsafe_allow_html=True)
