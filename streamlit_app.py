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
    st.write("Daftar referensi sifat fisis, massa molar, dan klasifikasi bahaya GHS bahan kimia.")
    
    # Perluasan database dengan variasi bahan kimia laboratorium terpopuler
    data_bahan = {
        # --- KELOMPOK PELARUT & UTALITAS ---
        "Akuades (H2O)": {"Formula": "H2O", "Mr": 18.02, "Sifat": "Pelarut universal, cairan jernih, netral.", "Bahaya": "Aman / Non-Hazardous", "Warna": "#10B981"},
        "Etanol (C2H5OH)": {"Formula": "C2H5OH", "Mr": 46.07, "Sifat": "Pelarut organik, alkohol, sangat mudah menguap.", "Bahaya": "Cairan mudah terbakar (Flammable).", "Warna": "#F59E0B"},
        "Aseton (CH3COCH3)": {"Formula": "CH3COCH3", "Mr": 58.08, "Sifat": "Pelarut organik polar, pembersih alat gelas.", "Bahaya": "Sangat mudah terbakar, iritasi mata.", "Warna": "#F59E0B"},
        "Metanol (CH3OH)": {"Formula": "CH3OH", "Mr": 32.04, "Sifat": "Pelarut alkohol sederhana, cairan beracun.", "Bahaya": "Mudah terbakar, sangat toksik jika tertelan.", "Warna": "#EF4444"},
        
        # --- KELOMPOK ASAM ---
        "Asam Klorida (HCl)": {"Formula": "HCl", "Mr": 36.46, "Sifat": "Asam mineral kuat, berasap pada konsentrasi pekat.", "Bahaya": "Sangat Korosif, iritasi saluran pernapasan.", "Warna": "#EF4444"},
        "Asam Sulfat (H2SO4)": {"Formula": "H2SO4", "Mr": 98.08, "Sifat": "Asam kuat kental, dehidrator berat, eksotermik tinggi.", "Bahaya": "Sangat korosif, destruktif pada jaringan kulit.", "Warna": "#EF4444"},
        "Asam Nitrat (HNO3)": {"Formula": "HNO3", "Mr": 63.01, "Sifat": "Asam kuat pengoksidasi, agen nitrasi.", "Bahaya": "Korosif berat, oksidator kuat.", "Warna": "#EF4444"},
        "Asam Asetat (CH3COOH)": {"Formula": "CH3COOH", "Mr": 60.05, "Sifat": "Asam organik lemah, berbau menyengat (cuka glasial).", "Bahaya": "Korosif pada kadar tinggi, cairan mudah terbakar.", "Warna": "#F59E0B"},
        "Asam Oksalat (H2C2O4)": {"Formula": "H2C2O4", "Mr": 90.03, "Sifat": "Asam organik lemah, padatan kristal putih.", "Bahaya": "Berbahaya jika terkena kulit, toksik.", "Warna": "#F59E0B"},
        
        # --- KELOMPOK BASA ---
        "Natrium Hidroksida (NaOH)": {"Formula": "NaOH", "Mr": 40.00, "Sifat": "Basa kuat, padatan pelet putih, higroskopis.", "Bahaya": "Korosif berat, menyebabkan luka bakar parah.", "Warna": "#EF4444"},
        "Kalium Hidroksida (KOH)": {"Formula": "KOH", "Mr": 56.11, "Sifat": "Basa kuat, kaustik, melepaskan panas saat larut.", "Bahaya": "Sangat korosif, toksisitas akut.", "Warna": "#EF4444"},
        "Amonia (NH4OH)": {"Formula": "NH4OH", "Mr": 35.05, "Sifat": "Basa lemah, larutan gas amonia dalam air, bau menyengat.", "Bahaya": "Korosif, sangat toksik bagi organisme air.", "Warna": "#EF4444"},
        
        # --- KELOMPOK GARAM & INDIKATOR ---
        "Natrium Klorida (NaCl)": {"Formula": "NaCl", "Mr": 58.44, "Sifat": "Garam halida standar, padatan kristal putih.", "Bahaya": "Aman pada penggunaan normal laboratorium.", "Warna": "#10B981"},
        "Tembaga(II) Sulfat (CuSO4)": {"Formula": "CuSO4", "Mr": 159.61, "Sifat": "Garam anorganik, berwarna biru cerah (bentuk hidrat).", "Bahaya": "Toksik bagi lingkungan akuatik, iritan kuat.", "Warna": "#EF4444"},
        "Kalsium Karbonat (CaCO3)": {"Formula": "CaCO3", "Mr": 100.09, "Sifat": "Kapur, padatan serbuk putih, sukar larut air.", "Bahaya": "Aman / Risiko iritasi sangat rendah.", "Warna": "#10B981"},
        "Kalium Permanganat (KMnO4)": {"Formula": "KMnO4", "Mr": 158.03, "Sifat": "Garam mangan, kristal ungu gelap, agen titrasi redoks.", "Bahaya": "Oksidator kuat, korosif, toksik.", "Warna": "#EF4444"}
    }
    
    # Kolom Input Pencarian dengan Fitur Autocomplete Otomatis
    cari_bahan = st.text_input("🔍 Ketik Nama Bahan Kimia untuk Mencari:", "")
    
    # Logika Python List Comprehension untuk filter pencarian
    list_bahan = [b for b in data_bahan.keys() if cari_bahan.lower() in b.lower()]
    
    if list_bahan:
        pilihan_bahan = st.selectbox("Pilih Bahan Kimia dari Hasil Pencarian:", list_bahan)
        info = data_bahan[pilihan_bahan]
        
        st.markdown("---")
        # Visualisasi data berbasis Kotak Informasi (Card Web Interaktif)
        st.markdown(f"""
        <div style='background-color: #F8FAFC; padding: 25px; border-radius: 12px; border-left: 8px solid {info['Warna']}; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);'>
            <h3 style='margin-top:0px; color:#1E293B;'>🔬 {pilihan_bahan}</h3>
            <p style='margin-bottom:8px;'><b>Rumus Kimia:</b> <code style='font-size:16px; background-color:#E2E8F0; padding:2px 6px; border-radius:4px;'>{info['Formula']}</code></p>
            <p style='margin-bottom:8px;'><b>Massa Molar (Mr):</b> <span style='color:#1E3A8A; font-weight:bold;'>{info['Mr']} g/mol</span></p>
            <p style='margin-bottom:8px;'><b>Karakteristik Fisik & Sifat:</b> {info['Sifat']}</p>
            <hr style='border-color:#E2E8F0; margin: 15px 0;'>
            <h5 style='margin:0 0 5px 0; color:{info['Warna']};'>⚠️ Regulasi Keselamatan Kerja & Bahaya (GHS):</h5>
            <p style='color:#475569; font-weight:500; margin:0;'>{info['Bahaya']}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Bahan kimia tidak terdaftar di database. Periksa kembali ejaan Anda.")
