import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Titan Protocol", page_icon="🧬", layout="centered")

# --- LOGICA TEMPORALE ---
giorni_trad = {
    "Monday": "Lunedì", "Tuesday": "Martedì", "Wednesday": "Mercoledì",
    "Thursday": "Giovedì", "Friday": "Venerdì", "Saturday": "Sabato", "Sunday": "Domenica"
}
giorno_inglese = datetime.now().strftime("%A")
oggi = giorni_trad[giorno_inglese]

# --- DATI NUTRIZIONE (STRATEGIA RICHIESTA) ---
# Grammature stimate per Lean Bulk (Target ~2800kcal)
diet_plan = {
    "Lunedì": {
        "Type": "GYM A",
        "Pranzo": "120g Riso Basmati + 150g Pollo + Zucchine a piacere",
        "Cena": "HIGH CARB: 400g Patate + 150g Manzo Magro + Spinaci"
    },
    "Martedì": {
        "Type": "REST",
        "Pranzo": "120g Pasta Integrale + 160g Tonno (sgocciolato) + Verdure",
        "Cena": "LOW CARB: 200g Pesce Bianco + Verdure Cotte + 50g Pane tostato"
    },
    "Mercoledì": {
        "Type": "GYM B",
        "Pranzo": "120g Riso + 150g Tacchino + Finocchi (Digeribili)",
        "Cena": "HIGH CARB: 100g Riso Basmati + 150g Salmone + Verdure"
    },
    "Giovedì": {
        "Type": "REST",
        "Pranzo": "80g Cereali (Farro/Orzo) + 200g Legumi decorticati (o passati)",
        "Cena": "LOW CARB: Frittata (2 Uova + 150ml Albume) + Verdure + 50g Pane"
    },
    "Venerdì": {
        "Type": "GYM A (No Gambe Pesanti)",
        "Pranzo": "200g Pesce Bianco + 300g Patate Lesse + Carote",
        "Cena": "CARICO PRE-MATCH: 120g Pasta o Riso + 150g Pollo/Pesce Magro (Niente fibre/verdure pesanti)"
    },
    "Sabato": {
        "Type": "CALCETTO",
        "Pranzo": "100g Riso in bianco + 100g Bresaola/Pollo (No Verdure per evitare gonfiore in campo)",
        "Cena": "PIZZA / LIBERO (No Alcol, No Fritti pesanti)"
    },
    "Domenica": {
        "Type": "REST",
        "Pranzo": "Pasto Libero Moderato (es. Lasagna casalinga)",
        "Cena": "DETOX: Passato di verdure + 150g Merluzzo/Nasello"
    }
}

# --- SOSTITUZIONI (LISTA INTELLIGENTE) ---
sostituzioni = {
    "Fonti Carboidrati": {
        "Riso (100g)": ["400g Patate", "100g Pasta di Riso/Mais", "100g Farina Avena", "100g Gallette (ca 12 pz)"],
        "Patate (400g)": ["100g Riso", "350g Patate Dolci", "100g Cous Cous"],
        "Pane (50g)": ["150g Patate", "40g Gallette", "40g Freselle"]
    },
    "Fonti Proteiche": {
        "Pollo/Tacchino (150g)": ["150g Vitello Magro", "200g Pesce Bianco", "150g Gamberi", "6 Albumi + 1 Uovo"],
        "Manzo (150g)": ["150g Cavallo", "150g Salmone (ma togli l'olio dal pasto)", "120g Bresaola"],
        "Tonno (160g)": ["150g Sgombro", "200g Merluzzo", "170g Fiocchi di Latte"]
    },
    "Verdure": "Se hai gastrite, evita: Broccoli, Cavolfiori, Peperoni. Preferisci: Zucchine, Carote, Finocchi, Spinaci, Valeriana."
}

# --- INTERFACCIA ---
st.title(f"🧬 TITAN PROTOCOL: {oggi}")
oggi_data = diet_plan[oggi]

# ==========================================
# SEZIONE 1: ALLENAMENTO (PRIORITÀ VISIVA)
# ==========================================
st.header("🏋️ WAR ROOM (Scheda)")

# Definiamo le schede
scheda_a = pd.DataFrame({
    "Esercizio": ["Goblet Squat", "Panca Inclinata Manubri", "Alzate Laterali", "Face Pull"],
    "Serie": ["4", "4", "5", "4"],
    "Reps": ["8-10", "8-10", "12-15", "15"],
    "Recupero": ["90''", "90''", "60''", "60''"],
    "Carico (kg)": [0.0, 0.0, 0.0, 0.0] 
})

scheda_b = pd.DataFrame({
    "Esercizio": ["Lat Machine (o Trazioni)", "Pulley Basso", "Alzate 90°", "Curl Manubri"],
    "Serie": ["4", "4", "4", "4"],
    "Reps": ["8-10", "10-12", "15", "12"],
    "Recupero": ["90''", "90''", "60''", "60''"],
    "Carico (kg)": [0.0, 0.0, 0.0, 0.0]
})

# Logica di visualizzazione basata sul giorno
tipo_oggi = oggi_data['Type']

if "GYM A" in tipo_oggi:
    st.error(f"🔥 OGGI: {tipo_oggi} - SPINTA & V-SHAPE")
    if "Gambe Pesanti" in tipo_oggi: # Venerdì
         st.info("ℹ️ Nota: Riduci il carico o il volume sulle gambe in vista del calcetto.")
    st.data_editor(scheda_a, hide_index=True, num_rows="fixed", use_container_width=True)
    
elif "GYM B" in tipo_oggi:
    st.error(f"🔥 OGGI: {tipo_oggi} - TRAZIONE & SCHIENA")
    st.data_editor(scheda_b, hide_index=True, num_rows="fixed", use_container_width=True)
    
elif "CALCETTO" in tipo_oggi:
    st.warning("⚽ OGGI: MATCH DAY. Niente palestra. Focus Idratazione.")
    
else:
    st.success("💤 OGGI: REST DAY. Recupero attivo (Stretching / Vacuum).")


# ==========================================
# SEZIONE 2: NUTRIZIONE
# ==========================================
st.divider()
st.header("🍽️ FUELING (Dieta)")

col1, col2 = st.columns(2)
with col1:
    st.info("**PRANZO**")
    st.write(oggi_data['Pranzo'])

with col2:
    st.success("**CENA**")
    st.write(oggi_data['Cena'])

# Sostituzioni (Menu a tendina)
with st.expander("🔄 TABELLA SOSTITUZIONI (Clicca per aprire)"):
    st.write("**Carboidrati:**")
    st.table(pd.DataFrame(sostituzioni["Fonti Carboidrati"]).transpose())
    st.write("**Proteine:**")
    st.table(pd.DataFrame(sostituzioni["Fonti Proteiche"]).transpose())
    st.write(f"**Verdure:** {sostituzioni['Verdure']}")

st.divider()
st.caption("Protocollo V-Shape | Obiettivo 85kg | No Scuse.")
