import streamlit as st
from datetime import datetime
import pandas as pd

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Titan Protocol", page_icon="🧬", layout="centered")

# --- LOGICA TEMPORALE (IL CERVELLO) ---
# Dizionario per tradurre i giorni in Italiano
giorni_trad = {
    "Monday": "Lunedì", "Tuesday": "Martedì", "Wednesday": "Mercoledì",
    "Thursday": "Giovedì", "Friday": "Venerdì", "Saturday": "Sabato", "Sunday": "Domenica"
}

# Ottieni il giorno corrente
giorno_inglese = datetime.now().strftime("%A")
oggi = giorni_trad[giorno_inglese]

# --- DATABASE DIETA (GRAMMATURE PER 2800 KCAL) ---
# N.B. Basato su tolleranza Gastrite (Riso/Patate > Pasta)
diet_plan = {
    "Lunedì": {
        "Focus": "Training Day (High Carbs)",
        "Colazione": "100g Avena (Porridge) + 200ml Albume + 1 Banana + 20g Mandorle",
        "Pranzo": "140g Riso Basmati + 150g Petto di Pollo + 10g Olio EVO + Zucchine cotte",
        "Spuntino": "50g Gallette Riso + 30g Whey (o 80g Fesa Tacchino) + 1 Mela",
        "Cena": "130g Riso (o 500g Patate lesse) + 150g Merluzzo + 10g Olio EVO"
    },
    "Martedì": {
        "Focus": "Rest Day (Recupero SNC)",
        "Colazione": "3 Pancake (80g Farina Avena + 1 Uovo + 100ml Albume) + 20g Burro Arachidi",
        "Pranzo": "120g Riso Venere/Basmati + 150g Tacchino + 10g Olio EVO + Finocchi",
        "Spuntino": "1 Yogurt Greco (0%) + 20g Noci + 1 Pera",
        "Cena": "400g Patate Dolci (Americane) + 150g Salmone (o Pesce grasso) + Verdure cotte"
    },
    "Mercoledì": {
        "Focus": "Training Day (Spinta)",
        "Colazione": "100g Crema di Riso + 30g Whey + 10g Cioccolato Fondente",
        "Pranzo": "140g Riso Basmati + 150g Macinato Magro (Manzo) + 10g Olio EVO",
        "Spuntino": "1 Banana + Shaker Proteine (30g)",
        "Cena": "130g Basmati + 150g Platessa + 10g Olio EVO + Carote lesse"
    },
    "Giovedì": {
        "Focus": "Calcetto / Cardio",
        "Colazione": "100g Avena + 200g Yogurt Greco + Frutti di Bosco",
        "Pranzo": "130g Riso + 2 Uova sode + 100g Albume + 10g Olio EVO",
        "Spuntino": "Barretta Proteica (senza polialcoli se gastrite) + 1 Frutto",
        "Cena": "120g Riso + 150g Pollo + 10g Olio EVO (Idratazione Extra!)"
    },
    "Venerdì": {
        "Focus": "Training Day (Trazione)",
        "Colazione": "100g Avena + 200ml Albume + 20g Mandorle",
        "Pranzo": "140g Pasta di Riso/Mais (No Glutine) + 150g Tonno al naturale + 10g Olio",
        "Spuntino": "50g Gallette + 80g Bresaola",
        "Cena": "500g Patate al forno (senza grassi in cottura) + 150g Orata + 10g Olio a crudo"
    },
    "Sabato": {
        "Focus": "Rest Day Attivo",
        "Colazione": "Pancake (80g Farina + 150ml Albume) + Marmellata light",
        "Pranzo": "120g Riso + 150g Pollo + Insalata mista + 15g Olio EVO",
        "Spuntino": "Frullato (1 Banana + 200ml Latte senza lattosio + 30g Whey)",
        "Cena": "Cheat Meal controllato (Es. Pizza marinara/semplice - Occhio alla gastrite!)"
    },
    "Domenica": {
        "Focus": "Reset Gastrico",
        "Colazione": "Fette biscottate (5/6) + Miele + 200ml Albume strapazzato",
        "Pranzo": "120g Riso in bianco + 150g Nasello bollito + 10g Olio + Limone",
        "Spuntino": "1 Mela cotta + Yogurt Greco",
        "Cena": "Vellutata di patate/verdure + 150g Tacchino"
    }
}

# --- INTERFACCIA UTENTE ---
st.title(f"🧬 TITAN PROTOCOL: {oggi}")
st.caption("Obiettivo: 85kg | Cibo = Carburante")

# --- 1. CHECK FARMACI (SEMPRE VISIBILE) ---
st.warning("⚠️ **PROTOCOLLO SICUREZZA MATTINA**")
st.markdown("""
* **Sveglia:** Eutirox 75mcg
* 🛑 **WAIT ZONE:** Devi aspettare **30 minuti** precisi prima di mangiare.
* *In questo tempo: Fai Vacuum addominale + Elastici spalle.*
""")

# --- 2. MENU DEL GIORNO AUTOMATICO ---
menu_oggi = diet_plan[oggi]

st.header(f"🍽️ Fueling di {oggi}")
st.info(f"Target Odierno: **{menu_oggi['Focus']}**")

# Visualizzazione Tabellare Pulita
col1, col2 = st.columns([1, 3])

with st.container():
    st.markdown("### 🥞 COLAZIONE")
    st.write(f"👉 {menu_oggi['Colazione']}")
    st.markdown(f"💊 *Assumere Cipralex 10mg ora*")
    
    st.markdown("---")
    
    st.markdown("### 🍚 PRANZO")
    st.write(f"👉 {menu_oggi['Pranzo']}")
    
    st.markdown("---")
    
    st.markdown("### 🎒 SPUNTINO")
    st.write(f"👉 {menu_oggi['Spuntino']}")
    st.error("☕ *Ultimo caffè entro le 16:30*")
    
    st.markdown("---")
    
    st.markdown("### 🌙 CENA (Post-Workout)")
    st.write(f"👉 {menu_oggi['Cena']}")
    st.warning("💊 *DEPAKIN 500mg: Assumere 2 ore dopo aver finito di cenare.*")

# --- 3. SEZIONE ALLENAMENTO RAPIDO ---
st.divider()
st.header("🏋️ Check Allenamento")
if "Rest" in menu_oggi['Focus']:
    st.success("✅ OGGI RIPOSO / CARDIO LEGGERO. Fai solo stretching.")
else:
    st.error("🔥 OGGI SI SPINGE. Apri la scheda di allenamento.")
    # Qui potremmo reinserire la logica di inserimento pesi se vuoi
