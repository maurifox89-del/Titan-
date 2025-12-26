import streamlit as st
import pandas as pd
import os
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
oggi_data_breve = datetime.now().strftime("%Y-%m-%d")

# --- GESTIONE SALVATAGGIO PESO (MEMORIA) ---
FILE_DATI = "progressi_peso.csv"

# Se il file non esiste, lo creiamo vuoto
if not os.path.exists(FILE_DATI):
    df_init = pd.DataFrame(columns=["Data", "Peso"])
    df_init.to_csv(FILE_DATI, index=False)

# Carichiamo i dati esistenti
df_peso = pd.read_csv(FILE_DATI)

# --- COSTANTI DIETA ---
colazione_std = "80g Fiocchi d'Avena (o Farina) OPPURE 4 Fette biscottate integrali + 200ml Albume (cotto) / 30g Whey / 150g Yogurt Greco 0% + 1 Banana media + 10g Mandorle o Noci"
spuntino_mattina_std = "1 Frutto (Mela/Pera/Pesca) + 20g Parmigiano OPPURE 15g Frutta Secca"
spuntino_pom_on = "4 Gallette di Riso + 60g Fesa di Tacchino o Bresaola"
spuntino_pom_off = "1 Yogurt Greco o 1 Frutto + 10 Mandorle"

# --- DATABASE DIETA ---
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

# --- SOSTITUZIONI ---
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
tipo_oggi = oggi_data['Type']

# ==========================================
# 📈 SEZIONE PROGRESSI
# ==========================================
with st.expander("📈 REGISTRO PESO & GRAFICO", expanded=False):
    col_in, col_btn = st.columns([2, 1])
    with col_in:
        nuovo_peso = st.number_input("Peso di oggi (kg)", min_value=60.0, max_value=100.0, step=0.1, key="input_peso")
    with col_btn:
        st.write("") 
        st.write("") 
        if st.button("Salva Peso"):
            nuova_riga = pd.DataFrame({"Data": [oggi_data_breve], "Peso": [nuovo_peso]})
            df_peso = pd.concat([df_peso, nuova_riga], ignore_index=True)
            df_peso.to_csv(FILE_DATI, index=False)
            st.success(f"Salvato: {nuovo_peso}kg")
            st.rerun()

    if not df_peso.empty:
        st.subheader("Andamento verso 85kg")
        st.line_chart(df_peso.set_index("Data"))
        st.caption(f"Ultimo peso: {df_peso.iloc[-1]['Peso']} kg")

# ==========================================
# SEZIONE 1: WAR ROOM
# ==========================================
st.header("🏋️ WAR ROOM")

with st.expander("ℹ️ METODO & REGOLE (Leggi Prima)", expanded=False):
    st.markdown("""
    * **METODO TUT 3-1-1:** 3 secondi a scendere, 1 fermo, 1 a salire.
    * **PROGRESSIONE:** Aumenta carico (2.5%) SOLO se chiudi le reps con tecnica perfetta.
    * **DOLORE:** Se senti dolore articolare -> STOP.
    """)

scheda_a_data = {
    "Esercizio": ["1. Goblet Squat", "2. Rematore Manubrio", "3. Panca Inclinata Manubri", "4. Lat Machine Avanti", "5. Face Pull", "6. Plank Statico"],
    "Serie": ["3", "3", "3", "3", "4", "3"],
    "Reps": ["10", "10", "10", "12", "15", "45''"],
    "Recupero": ["90''", "60''", "90''", "60''", "60''", "45''"],
    "Note Tecniche": [
        "Gomiti STRETTI. Manubrio al petto. VENERDÌ: Buffer 2 reps (risparmia gambe).",
        "Mano su panca. Schiena piatta. Tira verso l'anca.",
        "Panca 30°. Scendi in 3 SECONDI. Focus clavicole.",
        "Petto in fuori. NON dondolare.",
        "Cavo fronte. Ruota polsi. CRITICO per cifosi.",
        "Strizza glutei. Non inarcare la lombare."
    ],
    "Carico (kg)": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
}

scheda_b_data = {
    "Esercizio": ["1. Affondi Manubri", "2. Pulley Basso", "3. Shoulder Press Macchina", "4. Lat Pulldown (Neutra)", "5. Alzate Laterali", "6. Push Down (Tricipiti)", "7. Vacuum Addominale"],
    "Serie": ["3", "3", "3", "3", "4", "3", "5"],
    "Reps": ["10xlato", "12", "10", "10", "15", "12", "20''"],
    "Recupero": ["90''", "60''", "90''", "60''", "45''", "60''", "30''"],
    "Note Tecniche": [
        "Busto dritto. Controllo totale.",
        "Usa triangolo. Allungati bene avanti, chiudi scapole tirando.",
        "Proteggi schiena (meglio dei manubri). Non inarcare.",
        "Presa stretta/neutra. Tira al petto alto. Focus V-Shape.",
        "Carico basso. Gomiti altezza spalle. No slanci.",
        "Gomiti incollati ai fianchi.",
        "A stomaco vuoto. Risucchia ombelico."
    ],
    "Carico (kg)": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
}

if "GYM A" in tipo_oggi:
    st.error(f"🔥 OGGI: {tipo_oggi} - SPESSORE & CORE")
    if "Venerdì" in oggi:
        st.warning("⚽ PRE-CALCETTO: Nel Goblet Squat lascia 2 ripetizioni di riserva!")
    st.data_editor(pd.DataFrame(scheda_a_data), hide_index=True, use_container_width=True, column_config={"Note Tecniche": st.column_config.TextColumn(width="medium")})

elif "GYM B" in tipo_oggi:
    st.error(f"🔥 OGGI: {tipo_oggi} - V-SHAPE & AMPIEZZA")
    st.data_editor(pd.DataFrame(scheda_b_data), hide_index=True, use_container_width=True, column_config={"Note Tecniche": st.column_config.TextColumn(width="medium")})

elif "CALCETTO" in tipo_oggi:
    st.warning("⚽ OGGI: MATCH DAY (Ore 16:00).")
    st.info("Ricorda: Niente fibre a pranzo.")

else:
    st.success("💤 OGGI: REST DAY. Recupero attivo.")

# ==========================================
# SEZIONE 2: NUTRIZIONE (ORDINE CRONOLOGICO)
# ==========================================
st.divider()
st.header("🍽️ FUELING (Menu del Giorno)")

# 1. COLAZIONE
st.markdown("### 🥞 1. COLAZIONE (07:00-08:00)")
st.info(oggi_data['Colazione'])

# 2. SPUNTINO MATTINA
st.markdown("### 🍏 2. SPUNTINO MATTINA (10:30)")
st.write(oggi_data['Spuntino_Mat'])

# 3. PRANZO
st.markdown("### 🍚 3. PRANZO (13:00-14:00)")
if "NO FIBRE" in oggi_data['Pranzo']:
    st.error(oggi_data['Pranzo'])
else:
    st.write(oggi_data['Pranzo'])

# 4. SPUNTINO POMERIGGIO
st.markdown("### 🥪 4. SPUNTINO POMERIGGIO (16:30)")
st.write(oggi_data['Spuntino_Pom'])

# 5. CENA
st.markdown("### 🌙 5. CENA (Post-Workout/Relax)")
st.success(oggi_data['Cena'])

# SOSTITUZIONI
st.divider()
with st.expander("🔄 TABELLA SOSTITUZIONI (Se manca qualcosa)"):
    st.table(pd.DataFrame(sostituzioni["Fonti Carboidrati"]))
    st.table(pd.DataFrame(sostituzioni["Fonti Proteiche"]))

st.caption("Protocollo V-Shape | Obiettivo 85kg | Coach Titan")
