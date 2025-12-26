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

# --- DATI NUTRIZIONE COMPLETI (2800 KCAL) ---
diet_plan = {
    "Lunedì": {
        "Type": "GYM A",
        "Colazione": "100g Avena (Porridge) + 200ml Albume + 1 Banana + 15g Mandorle",
        "Pranzo": "120g Riso Basmati + 150g Pollo + Zucchine a piacere",
        "Spuntino": "Shaker Proteine (30g) + 1 Mela + 3 Gallette",
        "Cena": "HIGH CARB: 400g Patate + 150g Manzo Magro + Spinaci"
    },
    "Martedì": {
        "Type": "REST",
        "Colazione": "3 Pancake (80g Farina Avena + 150ml Albume) + 20g Burro Arachidi",
        "Pranzo": "120g Pasta Integrale + 160g Tonno (sgocciolato) + Verdure",
        "Spuntino": "1 Yogurt Greco (0%) + 15g Noci",
        "Cena": "LOW CARB: 200g Pesce Bianco + Verdure Cotte + 50g Pane tostato"
    },
    "Mercoledì": {
        "Type": "GYM B",
        "Colazione": "100g Crema di Riso + 30g Whey + 10g Cioccolato Fondente",
        "Pranzo": "120g Riso + 150g Tacchino + Finocchi (Digeribili)",
        "Spuntino": "1 Banana + Shaker Proteine (30g)",
        "Cena": "HIGH CARB: 100g Riso Basmati + 150g Salmone + Verdure"
    },
    "Giovedì": {
        "Type": "REST",
        "Colazione": "100g Avena + 200g Yogurt Greco + Frutti di Bosco",
        "Pranzo": "80g Cereali (Farro/Orzo) + 200g Legumi decorticati (o passati)",
        "Spuntino": "Barretta Proteica (o 50g Parmigiano) + 1 Pera",
        "Cena": "LOW CARB: Frittata (2 Uova + 150ml Albume) + Verdure + 50g Pane"
    },
    "Venerdì": {
        "Type": "GYM A (No Gambe Pesanti)",
        "Colazione": "100g Avena + 200ml Albume + 20g Mandorle",
        "Pranzo": "200g Pesce Bianco + 300g Patate Lesse + Carote",
        "Spuntino": "50g Gallette + 80g Bresaola/Fesa",
        "Cena": "CARICO PRE-MATCH: 120g Pasta o Riso + 150g Pollo/Pesce Magro (Niente verdure fibrose)"
    },
    "Sabato": {
        "Type": "CALCETTO",
        "Colazione": "Pancake (80g Farina + 150ml Albume) + Marmellata",
        "Pranzo": "100g Riso in bianco + 100g Bresaola/Pollo (No Verdure)",
        "Spuntino": "Banana (Pre-Partita)",
        "Cena": "PIZZA / LIBERO (No Alcol, No Fritti pesanti)"
    },
    "Domenica": {
        "Type": "REST",
        "Colazione": "Fette biscottate (5/6) + Miele + 200ml Albume strapazzato",
        "Pranzo": "Pasto Libero Moderato (es. Lasagna casalinga)",
        "Spuntino": "1 Mela cotta + Yogurt",
        "Cena": "DETOX: Passato di verdure + 150g Merluzzo/Nasello"
    }
}

# --- SOSTITUZIONI (LUNGHEZZA FISSA 4) ---
sostituzioni = {
    "Fonti Carboidrati": {
        "Riso (100g)": ["400g Patate", "100g Pasta Riso/Mais", "100g Farina Avena", "100g Gallette (12pz)"],
        "Patate (400g)": ["100g Riso", "350g Patate Dolci", "100g Cous Cous", "-"],
        "Pane (50g)": ["150g Patate", "40g Gallette", "40g Freselle", "-"]
    },
    "Fonti Proteiche": {
        "Pollo/Tacchino (150g)": ["150g Vitello Magro", "200g Pesce Bianco", "150g Gamberi", "6 Albumi + 1 Uovo"],
        "Manzo (150g)": ["150g Cavallo", "150g Salmone (no olio)", "120g Bresaola", "-"],
        "Tonno (160g)": ["150g Sgombro", "200g Merluzzo", "170g Fiocchi Latte", "-"]
    },
    "Colazione/Spuntino": {
        "Avena (100g)": ["100g Crema di Riso", "80g Fette Biscottate", "100g Pane Integrale", "80g Corn Flakes"],
        "Albume (200ml)": ["30g Whey Protein", "200g Yogurt Greco", "80g Affettato Magro", "-"],
        "Yogurt": ["Fiocchi di Latte", "Kefir", "Budino Proteico", "-"]
    }
}

# --- INTERFACCIA ---
st.title(f"🧬 TITAN PROTOCOL: {oggi}")
oggi_data = diet_plan[oggi]

# ==========================================
# SEZIONE 1: ALLENAMENTO
# ==========================================
st.header("🏋️ WAR ROOM (Scheda)")

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

tipo_oggi = oggi_data['Type']

if "GYM A" in tipo_oggi:
    st.error(f"🔥 OGGI: {tipo_oggi} - SPINTA & V-SHAPE")
    if "Gambe Pesanti" in tipo_oggi:
         st.info("ℹ️ Nota: Riduci il carico gambe del 30% pre-calcetto.")
    st.data_editor(scheda_a, hide_index=True, num_rows="fixed", use_container_width=True)
    
elif "GYM B" in tipo_oggi:
    st.error(f"🔥 OGGI: {tipo_oggi} - TRAZIONE & SCHIENA")
    st.data_editor(scheda_b, hide_index=True, num_rows="fixed", use_container_width=True)
    
elif "CALCETTO" in tipo_oggi:
    st.warning("⚽ OGGI: MATCH DAY. Niente palestra. Focus Idratazione.")
    
else:
    st.success("💤 OGGI: REST DAY. Recupero attivo.")

# ==========================================
# SEZIONE 2: NUTRIZIONE (COMPLETA)
# ==========================================
st.divider()
st.header("🍽️ FUELING (Dieta)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🥞 COLAZIONE")
    st.info(oggi_data['Colazione'])
    
    st.markdown("### 🍚 PRANZO")
    st.info(oggi_data['Pranzo'])

with col2:
    st.markdown("### 🎒 SPUNTINO")
    st.success(oggi_data['Spuntino'])
    
    st.markdown("### 🌙 CENA")
    st.success(oggi_data['Cena'])

# Sostituzioni
with st.expander("🔄 TABELLA SOSTITUZIONI (Clicca per aprire)"):
    st.markdown("### 🍞 Carboidrati")
    st.table(pd.DataFrame(sostituzioni["Fonti Carboidrati"]))
    
    st.markdown("### 🍗 Proteine")
    st.table(pd.DataFrame(sostituzioni["Fonti Proteiche"]))

    st.markdown("### 🥛 Colazione & Snack")
    st.table(pd.DataFrame(sostituzioni["Colazione/Spuntino"]))

st.divider()
st.caption("Protocollo V-Shape | Obiettivo 85kg | No Scuse.")
