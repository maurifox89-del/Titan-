import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Coach Titan App", page_icon="🧬")

# --- PROFILO ATLETA ---
USER_WEIGHT_START = 75
USER_TARGET = 85
MEDS = {
    "Mattina": "Eutirox 75mcg + Tiroide Secca (WAIT 30 MIN!)",
    "Colazione": "Cipralex 10mg",
    "Sera": "Depakin 500mg (Cena finita 2h prima!)"
}

# --- INTERFACCIA ---
st.title("🧬 PROTOCOLLO TITAN")
st.write(f"Obiettivo: {USER_TARGET}kg | Attuale: {st.session_state.get('peso_attuale', USER_WEIGHT_START)}kg")

# --- SEZIONE CHECK-IN MATTUTINO (CRITICO) ---
st.header("1. Check-In Farmacologico")
col1, col2 = st.columns(2)
with col1:
    eutirox = st.checkbox("Eutirox Preso?")
with col2:
    wait_zone = st.checkbox("Wait Zone 30' (Posture)?")

if eutirox and not wait_zone:
    st.warning("⚠️ FERMO! Devi fare i 30 minuti di Vacuum/Elastici prima di mangiare.")
elif eutirox and wait_zone:
    st.success("✅ Procedi con Colazione + Cipralex.")

# --- SEZIONE ALLENAMENTO (LOGICA MESE 1) ---
st.header("2. War Room (Allenamento)")
giorno = st.selectbox("Cosa facciamo oggi?", ["Rest Day", "Scheda A (Spinta)", "Scheda B (Trazione)", "Calcetto"])

if giorno == "Scheda A (Spinta)":
    st.info("🔥 FOCUS: V-SHAPE & SPALLE. Proteggi la Lordosi.")
    
    # Esempio Tabella interattiva per inserire i carichi
    exercises_a = {
        "Esercizio": ["Goblet Squat", "Panca Inclinata Manubri", "Alzate Laterali", "Face Pull (Non saltare!)"],
        "Serie": ["4", "4", "5", "4"],
        "Reps": ["8-10", "8-10", "12-15", "15"],
        "Carico (kg)": [0.0, 0.0, 0.0, 0.0] # Qui l'utente inserisce i dati
    }
    df_a = pd.DataFrame(exercises_a)
    edited_df = st.data_editor(df_a, num_rows="dynamic")
    
    if st.button("Salva Workout"):
        st.success("Dati salvati! (Logica database da implementare)")

elif giorno == "Calcetto":
    st.warning("⚽ ATTENZIONE: Domani ridurre volume gambe del 30%. Idratazione Extra.")

# --- SEZIONE NUTRIZIONE ---
st.header("3. Fueling (Nutrizione)")
st.info("Target: 2800 Kcal - Focus Digeribilità (Gastrite)")

pasto = st.radio("Pasto Corrente", ["Colazione", "Pranzo", "Spuntino", "Cena Post-WO"])

if pasto == "Cena Post-WO":
    st.markdown("""
    * **Fonte**: Riso o Patate (Indice Glicemico Alto)
    * **Proteina**: Pesce bianco o Pollo
    * **Regola**: *Hai finito di mangiare 2 ore prima del Depakin?*
    """)

# --- PROGRESSO PESO ---
st.divider()
nuovo_peso = st.number_input("Aggiorna Peso Corporeo (kg)", min_value=70.0, max_value=90.0, step=0.1)
if st.button("Aggiorna Peso"):
    st.session_state['peso_attuale'] = nuovo_peso
    st.balloons()
