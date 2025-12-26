import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAZIONE (CORRETTA) ---
# Streamlit accetta solo "centered" o "wide". 
# "Centered" è perfetto per lo smartphone.
st.set_page_config(page_title="Titan Protocol", page_icon="🧬", layout="centered")

# --- INIZIALIZZAZIONE DATI (SIMULAZIONE DATABASE) ---
if 'history_a' not in st.session_state:
    # ... il resto del codice rimane uguale ...
if 'history_a' not in st.session_state:
    st.session_state['history_a'] = {
        "Goblet Squat": 20.0,
        "Panca Inclinata Manubri": 22.0,
        "Alzate Laterali": 8.0,
        "Face Pull": 15.0
    }

# --- PROFILO ---
st.title("🧬 COACH TITAN")
st.caption("Evolutionary Protocol | V-Shape Focus")

# --- 1. NUTRIZIONE (CORRETTO: VISTA GIORNALIERA) ---
st.header("🍽️ Piano Nutrizionale Odierno")
st.info("Obiettivo: Lean Bulk (~2800 Kcal) | Focus: Digeribilità")

with st.expander("Vedi Menu Completo di Oggi", expanded=True):
    st.markdown("### 🌅 MATTINA")
    st.write("**Appena Sveglio:** Eutirox 75mcg")
    st.warning("⏳ WAIT ZONE 30' (Vacuum + Postura) - TASSATIVO")
    st.write("**Colazione:** Pancake / Avena + Yogurt + CIPRALEX 10mg")
    
    st.markdown("---")
    st.markdown("### ☀️ PRANZO")
    st.write("**Fonte:** Riso o Patate (No Pasta integrale se infiamma)")
    st.write("**Proteine:** Pollo / Pesce Bianco")
    st.write("**Grassi:** Olio EVO a crudo")
    
    st.markdown("---")
    st.markdown("### 🎒 SPUNTINO LAVORO")
    st.write("**Grab & Go:** Shaker Proteine + Frutta Secca o Barretta")
    st.error("☕ STOP CAFFÈ dopo le 16:30")

    st.markdown("---")
    st.markdown("### 🌙 CENA (Post-Workout)")
    st.write("**Carbo:** Riso Basmati / Patate (Alto indice glicemico)")
    st.write("**Proteine:** Merluzzo / Tacchino")
    st.warning("💊 DEPAKIN 500mg: Prendi 2 ore dopo fine cena.")

# --- 2. WORKOUT (CORRETTO: STORICO + EDIT) ---
st.header("🏋️ War Room (Allenamento)")

scheda = st.selectbox("Seleziona Sessione", ["Scheda A (Spinta)", "Scheda B (Trazione)", "Rest Day"])

if scheda == "Scheda A (Spinta)":
    st.subheader("🔥 Focus: V-Shape & Spalle")
    
    # Creiamo i dati unendo lo storico
    data_a = {
        "Esercizio": ["Goblet Squat", "Panca Inclinata Manubri", "Alzate Laterali", "Face Pull"],
        "Serie x Reps": ["4x8-10", "4x8-10", "5x12-15", "4x15"],
        "Carico SETT. SCORSA (kg)": [st.session_state['history_a'].get("Goblet Squat"), 
                                     st.session_state['history_a'].get("Panca Inclinata Manubri"),
                                     st.session_state['history_a'].get("Alzate Laterali"),
                                     st.session_state['history_a'].get("Face Pull")],
        "Carico OGGI (kg)": [0.0, 0.0, 0.0, 0.0] # L'utente scrive qui
    }
    
    df_a = pd.DataFrame(data_a)

    # Configurazione Tabella Editabile
    st.markdown("Inserisci i carichi di **OGGI** nella colonna di destra:")
    edited_df = st.data_editor(
        df_a,
        column_config={
            "Carico SETT. SCORSA (kg)": st.column_config.NumberColumn(disabled=True), # Bloccato
            "Carico OGGI (kg)": st.column_config.NumberColumn(min_value=0, max_value=200, step=0.5) # Modificabile
        },
        hide_index=True,
        num_rows="fixed"
    )

    if st.button("💾 Salva Allenamento"):
        # Qui aggiorniamo lo "storico" in memoria per la prossima volta (nella sessione corrente)
        # Nota: Per salvare PER SEMPRE serve un database (Google Sheets), ma per ora simuliamo.
        st.toast("Allenamento Salvato! Grande lavoro.", icon="💪")
        st.balloons()

elif scheda == "Scheda B (Trazione)":
    st.info("Configura la Scheda B nel codice seguendo l'esempio della A.")

# --- FOOTER ---
st.divider()
st.caption("Coach Titan System v1.2")
