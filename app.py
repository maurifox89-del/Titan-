import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Titan Pro UI", page_icon="🧬", layout="centered")

# --- CSS INJECTION (IL TRUCCO PER L'ESTETICA) ---
# Qui forziamo lo stile per farlo assomigliare alla tua foto
st.markdown("""
<style>
    /* Sfondo generale più pulito */
    .stApp {
        background-color: #F8F9FA;
    }
    
    /* Stile per i Container (Le "Carte" bianche) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #E0E0E0;
    }

    /* Bottoni Rossi (Stile Titan) */
    .stButton > button {
        background-color: #B71C1C; /* Rosso Scuro */
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #D32F2F; /* Rosso più chiaro al passaggio */
        color: white;
    }

    /* Bottoni Secondari (Bianchi con bordo rosso) */
    .secondary-btn > button {
        background-color: white !important;
        color: #B71C1C !important;
        border: 2px solid #B71C1C !important;
    }

    /* Input Fields (Arrotondati) */
    .stNumberInput > div > div > input {
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
    }
    
    /* Nascondere etichette inutili */
    label {
        font-weight: bold;
        color: #333;
    }
    
    /* Titoli grandi */
    h1, h2, h3 {
        font-family: 'Helvetica', sans-serif;
        color: #212121;
    }
</style>
""", unsafe_allow_html=True)

# --- DATI ESERCIZIO (SIMULATI) ---
esercizio_corrente = {
    "Nome": "A. Lat Machine",
    "Target_Serie": 4,
    "Target_Reps": "10-8-6-5",
    "Recupero": 90,
    "History_Pesi": [40, 45, 50, 55] # Ultimi pesi usati
}

# Inizializza lo stato se vuoto
if "serie_log" not in st.session_state:
    st.session_state["serie_log"] = [
        {"Set": 1, "Kg": 40.0, "Reps": 10},
        {"Set": 2, "Kg": 45.0, "Reps": 8},
        {"Set": 3, "Kg": 50.0, "Reps": 6},
        {"Set": 4, "Kg": 55.0, "Reps": 5}
    ]

# ==========================================
# 📱 INTERFACCIA MOBILE REPLICA
# ==========================================

# 1. HEADER ESERCIZIO
st.subheader(esercizio_corrente["Nome"])

# 2. INFO RAPIDE (ICONE)
col_info1, col_info2, col_info3 = st.columns(3)
with col_info1:
    st.markdown(f"<div style='text-align:center; color:#B71C1C; font-size:24px;'>🔄</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center;'><b>{esercizio_corrente['Target_Serie']}</b><br><span style='font-size:12px; color:grey'>Serie</span></div>", unsafe_allow_html=True)
with col_info2:
    st.markdown(f"<div style='text-align:center; color:#B71C1C; font-size:24px;'>🏋️</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center;'><b>{esercizio_corrente['Target_Reps']}</b><br><span style='font-size:12px; color:grey'>Reps Target</span></div>", unsafe_allow_html=True)
with col_info3:
    st.markdown(f"<div style='text-align:center; color:#B71C1C; font-size:24px;'>⏳</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center;'><b>{esercizio_corrente['Recupero']}''</b><br><span style='font-size:12px; color:grey'>Recupero</span></div>", unsafe_allow_html=True)

st.markdown("---")

# 3. BOTTONI AZIONE (ESECUZIONE / STORICO)
c1, c2 = st.columns(2)
with c1:
    st.button("▶️ Esecuzione VIDEO")
with c2:
    # Usiamo un trucco CSS per rendere questo bottone diverso se volessimo, 
    # ma per ora lo lasciamo standard rosso
    st.button("📈 Storico Pesi") 

st.write("") # Spazio

# 4. IL "CARD" DEGLI INPUT (Cuore dell'interfaccia)
# Usiamo st.container con border=True per creare la scatola bianca
with st.container(border=True):
    st.markdown("### Serie")
    
    # Intestazioni Colonne
    h1, h2, h3 = st.columns([0.5, 2, 2])
    h2.markdown("<div style='text-align:center; color:grey; font-size:14px'>Peso (Kg)</div>", unsafe_allow_html=True)
    h3.markdown("<div style='text-align:center; color:grey; font-size:14px'>Ripetizioni</div>", unsafe_allow_html=True)
    
    # GENERAZIONE RIGHE DINAMICHE
    for i, serie in enumerate(st.session_state["serie_log"]):
        c_num, c_kg, c_reps = st.columns([0.5, 2, 2])
        
        # Numero Serie (Rosso e Grassetto)
        with c_num:
            st.markdown(f"<div style='padding-top: 35px; color: #B71C1C; font-weight: bold; font-size: 20px;'>{serie['Set']}</div>", unsafe_allow_html=True)
        
        # Input Peso
        with c_kg:
            nuovo_kg = st.number_input(
                f"kg_{i}", 
                value=float(serie['Kg']), 
                step=1.25, 
                label_visibility="collapsed",
                key=f"w_{i}"
            )
            
        # Input Reps
        with c_reps:
            nuove_reps = st.number_input(
                f"reps_{i}", 
                value=int(serie['Reps']), 
                step=1, 
                label_visibility="collapsed",
                key=f"r_{i}"
            )
            
        # Aggiorniamo lo stato in tempo reale
        st.session_state["serie_log"][i]["Kg"] = nuovo_kg
        st.session_state["serie_log"][i]["Reps"] = nuove_reps

    st.write("") # Spazio
    
    # BOTTONI DI SERVIZIO DENTRO LA CARD
    if st.button(f"⏱️ AVVIA RECUPERO: {esercizio_corrente['Recupero']}''"):
        with st.spinner("Recupero in corso... Respira profondo."):
            time.sleep(2) # Simulazione timer
        st.success("Recupero Finito! SPINGI!")

    if st.button("➕ Aggiungi Serie (Drop Set)"):
        nuovo_set = len(st.session_state["serie_log"]) + 1
        st.session_state["serie_log"].append({"Set": nuovo_set, "Kg": 0.0, "Reps": 0})
        st.rerun()

# 5. BOTTONE FINALE GIGANTE
st.write("")
st.write("")
st.button("✅ TERMINA ALLENAMENTO", type="primary")

# --- FOOTER SIMULATO (NAVBAR) ---
st.markdown("---")
nav1, nav2, nav3, nav4 = st.columns(4)
with nav1: st.markdown("<div style='text-align:center; color:grey'>🏠<br>Home</div>", unsafe_allow_html=True)
with nav2: st.markdown("<div style='text-align:center; color:#B71C1C; font-weight:bold'>🏋️<br>Workout</div>", unsafe_allow_html=True)
with nav3: st.markdown("<div style='text-align:center; color:grey'>🍽️<br>Nutrizione</div>", unsafe_allow_html=True)
with nav4: st.markdown("<div style='text-align:center; color:grey'>💬<br>Chat</div>", unsafe_allow_html=True)

