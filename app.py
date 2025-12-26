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

# --- COSTANTI FISSE (Tutti i giorni tranne eccezioni) ---
colazione_std = "80g Fiocchi d'Avena (o Farina) OPPURE 4 Fette biscottate integrali + 200ml Albume (cotto) / 30g Whey / 150g Yogurt Greco 0% + 1 Banana media + 10g Mandorle o Noci"
spuntino_mattina_std = "1 Frutto (Mela/Pera/Pesca) + 20g Parmigiano OPPURE 15g Frutta Secca"
spuntino_pom_on = "4 Gallette di Riso + 60g Fesa di Tacchino o Bresaola"
spuntino_pom_off = "1 Yogurt Greco o 1 Frutto + 10 Mandorle"

# --- DATABASE DIETA (INSERITA SENZA MODIFICHE) ---
diet_plan = {
    "Lunedì": {
        "Type": "GYM A",
        "Colazione": colazione_std,
        "Spuntino_Mat": spuntino_mattina_std,
        "Pranzo": "120g Riso Basmati + 150g Petto di Pollo + Zucchine lesse + 1 cucchiaio Olio",
        "Spuntino_Pom": spuntino_pom_on,
        "Cena": "POST-WORKOUT (Ricarica): 400g Patate (Lesse/Forno) + 150g Manzo Magro (trita scelta) + Spinaci cotti + 1 cucchiaio Olio"
    },
    "Martedì": {
        "Type": "REST",
        "Colazione": colazione_std,
        "Spuntino_Mat": spuntino_mattina_std,
        "Pranzo": "100g Pasta (Integrale o Farro) + 110g Tonno al naturale (sgocciolato) + Fagiolini + 1 cucchiaio Olio",
        "Spuntino_Pom": spuntino_pom_off,
        "Cena": "LOW CARB (Digestivo): 200g Patate (o 60g Pane tostato) + 200g Merluzzo o Platessa + Carote lesse + 1 cucchiaio Olio"
    },
    "Mercoledì": {
        "Type": "GYM B",
        "Colazione": colazione_std,
        "Spuntino_Mat": spuntino_mattina_std,
        "Pranzo": "120g Riso Basmati + 150g Fesa di Tacchino (alla piastra) + Finocchi cotti (ottimi x stomaco) + 1 cucchiaio Olio",
        "Spuntino_Pom": spuntino_pom_on,
        "Cena": "POST-WORKOUT (Omega 3): 120g Riso Basmati (o Venere) + 150g Salmone (Fresco/Surgelato) + Zucchine grigliate + 1 cucchiaio Olio"
    },
    "Giovedì": {
        "Type": "REST",
        "Colazione": colazione_std,
        "Spuntino_Mat": spuntino_mattina_std,
        "Pranzo": "80g Farro o Orzo + 150g Lenticchie o Ceci (ben cotti) + Verdure miste + 1 cucchiaio Olio",
        "Spuntino_Pom": spuntino_pom_off,
        "Cena": "UOVA & VERDURE: 2 Uova intere + 100ml Albume (frittata) + 80g Pane integrale tostato + Verdure a foglia verde + 1 cucchiaio Olio"
    },
    "Venerdì": {
        "Type": "GYM A",
        "Colazione": colazione_std,
        "Spuntino_Mat": spuntino_mattina_std,
        "Pranzo": "120g Riso Basmati + 200g Orata o Branzino + Broccoli (se tollerati) o Carote + 1 cucchiaio Olio",
        "Spuntino_Pom": spuntino_pom_on,
        "Cena": "CARICO PRE-PARTITA: 120g Pasta (pomodoro leggero o olio) + 150g Pollo o Tacchino + Verdura cotta piccola porzione + 1 cucchiaio Olio"
    },
    "Sabato": {
        "Type": "CALCETTO (Ore 16:00)",
        "Colazione": colazione_std,
        "Spuntino_Mat": spuntino_mattina_std,
        "Pranzo": "NO FIBRE (Ore 12:30): 120g Riso Basmati (in bianco/olio) + 100g Pollo (cotto semplice) - ⛔ NIENTE VERDURE",
        "Spuntino_Pom": "MATCH DAY (Niente spuntino solito)",
        "Cena": "CENA LIBERA (Pizza): 1 Pizza Margherita o con Crudo. Niente fritti pesanti. (💊 DEPAKIN 2 ORE DOPO CENA)"
    },
    "Domenica": {
        "Type": "REST",
        "Colazione": colazione_std,
        "Spuntino_Mat": spuntino_mattina_std,
        "Pranzo": "PASTO LIBERO MODERATO: Es. Lasagna o Riso al forno + Secondo di carne + Verdura",
        "Spuntino_Pom": spuntino_pom_off,
        "Cena": "DETOX / RESET: Passato di verdure + 150g Nasello o Merluzzo + 50g Crostini pane + 1 cucchiaio Olio"
    }
}

# --- SOSTITUZIONI (UTILI MA NASCOSTE IN EXPANDER) ---
sostituzioni = {
    "Fonti Carboidrati": {
        "Riso (120g)": ["400g Patate", "100g Pasta/Farro", "120g Farina Avena", "120g Gallette (ca 14pz)"],
        "Patate (400g)": ["120g Riso", "350g Patate Dolci", "100g Cous Cous", "-"],
        "Pane (60g)": ["200g Patate", "50g Gallette", "50g Freselle", "-"]
    },
    "Fonti Proteiche": {
        "Pollo/Tacchino (150g)": ["150g Vitello Magro", "200g Pesce Bianco", "150g Gamberi", "6 Albumi + 1 Uovo"],
        "Manzo (150g)": ["150g Cavallo", "150g Salmone (no olio)", "120g Bresaola", "-"],
        "Tonno (110g)": ["150g Sgombro", "200g Merluzzo", "170g Fiocchi Latte", "-"]
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
    st.data_editor(scheda_a, hide_index=True, num_rows="fixed", use_container_width=True)
elif "GYM B" in tipo_oggi:
    st.error(f"🔥 OGGI: {tipo_oggi} - TRAZIONE & SCHIENA")
    st.data_editor(scheda_b, hide_index=True, num_rows="fixed", use_container_width=True)
elif "CALCETTO" in tipo_oggi:
    st.warning("⚽ OGGI: MATCH DAY (Ore 16:00). Niente palestra.")
else:
    st.success("💤 OGGI: REST DAY. Recupero attivo.")

# ==========================================
# SEZIONE 2: NUTRIZIONE (DIETA STRICT)
# ==========================================
st.divider()
st.header("🍽️ FUELING (Dieta)")

st.markdown("### 🥞 COLAZIONE (07:00-08:00)")
st.info(oggi_data['Colazione'])

st.markdown("### 🍏 SPUNTINO MATTINA (10:30)")
st.write(oggi_data['Spuntino_Mat'])

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🍚 PRANZO")
    # Evidenziamo se è il pranzo Pre-Partita del Sabato
    if "NO FIBRE" in oggi_data['Pranzo']:
        st.error(oggi_data['Pranzo'])
    else:
        st.write(oggi_data['Pranzo'])

with col2:
    st.markdown("### 🌙 CENA")
    st.write(oggi_data['Cena'])

st.markdown("---")
st.markdown("### 🥪 SPUNTINO POMERIGGIO (16:30)")
st.caption(f"Status oggi: {'ALLENAMENTO' if 'GYM' in tipo_oggi else 'RIPOSO/MATCH'}")
st.write(oggi_data['Spuntino_Pom'])

# Sostituzioni
with st.expander("🔄 TABELLA SOSTITUZIONI (Se manca qualcosa)"):
    st.table(pd.DataFrame(sostituzioni["Fonti Carboidrati"]))
    st.table(pd.DataFrame(sostituzioni["Fonti Proteiche"]))

st.divider()
st.caption("Protocollo V-Shape | Obiettivo 85kg | Coach Titan")
