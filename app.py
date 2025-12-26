import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Titan App", page_icon="🧬", layout="centered")

# --- CSS OTTIMIZZATO PER MOBILE ---
st.markdown("""
<style>
    /* Rimuove margini inutili per guadagnare spazio su mobile */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }
    
    /* Stile Bottoni Rossi TITAN */
    .stButton > button {
        background-color: #B71C1C !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: bold !important;
        height: 50px;
        width: 100%;
    }
    
    /* Stile Input (Pesi e Reps) più grandi per le dita */
    .stNumberInput input {
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #B71C1C;
    }
    
    /* Nasconde freccette input su mobile per pulizia */
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button { 
        -webkit-appearance: none; 
        margin: 0; 
    }
</style>
""", unsafe_allow_html=True)

# --- INIZIALIZZAZIONE STATO (LA MEMORIA) ---
# Questo blocco assicura che i dati non spariscano quando clicchi
if "workout_data" not in st.session_state:
    st.session_state.workout_data = [
        {"set": 1, "kg": 40.0, "reps": 10},
        {"set": 2, "kg": 45.0, "reps": 8},
        {"set": 3, "kg": 50.0, "reps": 6},
        {"set": 4, "kg": 55.0, "reps": 5}
    ]

# --- FUNZIONI DI GESTIONE (LOGICA) ---
def aggiungi_serie():
    nuovo_set = len(st.session_state.workout_data) + 1
    # Copiamo il peso dell'ultima serie per comodità
    ultimo_peso = st.session_state.workout_data[-1]["kg"] if st.session_state.workout_data else 0.0
    st.session_state.workout_data.append({"set": nuovo_set, "kg": ultimo_peso, "reps": 0})

def rimuovi_serie():
    if len(st.session_state.workout_data) > 0:
        st.session_state.workout_data.pop()

# --- INTERFACCIA UTENTE ---

# 1. HEADER
col_title, col_hist = st.columns([3, 1])
with col_title:
    st.title("A. Lat Machine")
    st.caption("Focus: Schiena / V-Shape")
with col_hist:
    st.markdown("## 📈") # Placeholder per bottone storico

# 2. TARGET E INFO
with st.container(border=True):
    c1, c2, c3 = st.columns(3)
    c1.metric("Serie", "4")
    c2.metric("Reps", "10-8-6-5")
    c3.metric("Recupero", "90''")

st.divider()

# 3. CARD INPUT (IL CUORE DELL'APP)
st.subheader("📝 Registra Serie")

# Intestazioni (Per capire cosa inserire)
h1, h2, h3 = st.columns([0.7, 2, 2])
h1.write("#")
h2.markdown("**Kg**")
h3.markdown("**Reps**")

# CICLO DI RENDERING SERIE
for i, row in enumerate(st.session_state.workout_data):
    # Layout colonne ottimizzato per mobile: 1 piccola, 2 grandi uguali
    c1, c2, c3 = st.columns([0.7, 2, 2])
    
    with c1:
        # Numero serie (Centrato verticalmente col padding vuoto)
        st.markdown(f"<h3 style='text-align: center; color: #B71C1C; margin-top: 10px;'>{row['set']}</h3>", unsafe_allow_html=True)
    
    with c2:
        # Input Peso - Collegato direttamente allo stato tramite KEY
        val_kg = st.number_input(
            "Kg", 
            value=float(row['kg']), 
            step=1.0, 
            key=f"kg_{i}", 
            label_visibility="collapsed"
        )
        # Aggiornamento immediato dello stato
        st.session_state.workout_data[i]["kg"] = val_kg

    with c3:
        # Input Reps - Collegato direttamente allo stato tramite KEY
        val_reps = st.number_input(
            "Reps", 
            value=int(row['reps']), 
            step=1, 
            key=f"reps_{i}", 
            label_visibility="collapsed"
        )
        # Aggiornamento immediato dello stato
        st.session_state.workout_data[i]["reps"] = val_reps

# 4. BOTTONI DI CONTROLLO
st.write("")
col_add, col_del = st.columns([2, 1])

with col_add:
    # Callback: quando clicchi, esegue la funzione PRIMA di ricaricare
    st.button("➕ AGGIUNGI SERIE", on_click=aggiungi_serie)

with col_del:
    st.button("🗑️", on_click=rimuovi_serie)

# 5. TIMER RECUPERO
st.write("")
if st.button("⏱️ AVVIA RECUPERO (90'')"):
    with st.spinner("Recupero in corso..."):
        time.sleep(2) # Simulazione breve per demo
    st.toast("Recupero Finito! Torni a spingere.", icon="🔥")

# 6. SALVATAGGIO FINALE
st.markdown("---")
if st.button("✅ TERMINA & SALVA ESERCIZIO"):
    # Qui salveremmo su CSV/Database
    df_result = pd.DataFrame(st.session_state.workout_data)
    st.success("Dati Salvati con Successo!")
    st.dataframe(df_result, hide_index=True) # Feedback visivo di cosa ha salvato
    # Reset opzionale
    # st.session_state.workout_data = [] 

# --- FOOTER ---
st.caption("Coach Titan System v2.0 Mobile")
