import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Titan Protocol", page_icon="🧬", layout="centered")

# --- CSS CUSTOM ---
st.markdown("""
<style>
    .stProgress > div > div > div > div { background-color: #00B4D8; }
    .kcal-box {
        background-color: #ffebee; color: #b71c1c; padding: 15px;
        border-radius: 10px; text-align: center; font-weight: bold;
        font-size: 20px; margin-top: 20px; border: 2px solid #b71c1c;
    }
    .stButton > button { width: 100%; border-radius: 10px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- LOGICA TEMPORALE ---
giorni_list = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
giorni_trad = {
    "Monday": "Lunedì", "Tuesday": "Martedì", "Wednesday": "Mercoledì",
    "Thursday": "Giovedì", "Friday": "Venerdì", "Saturday": "Sabato", "Sunday": "Domenica"
}
giorno_reale_inglese = datetime.now().strftime("%A")
giorno_reale_ita = giorni_trad[giorno_reale_inglese]
oggi_data_breve = datetime.now().strftime("%Y-%m-%d")

# --- TITOLO & SELETTORE ---
st.title("🧬 TITAN PROTOCOL")
selected_day = st.selectbox("📅 Visualizza Piano del Giorno:", giorni_list, index=giorni_list.index(giorno_reale_ita))

# --- GESTIONE DATABASE (FILE CSV) ---
FILE_PESO = "progressi_peso.csv"
FILE_ESERCIZI = "storico_esercizi.csv"

if not os.path.exists(FILE_PESO):
    pd.DataFrame(columns=["Data", "Peso"]).to_csv(FILE_PESO, index=False)
df_peso = pd.read_csv(FILE_PESO)

if not os.path.exists(FILE_ESERCIZI):
    pd.DataFrame(columns=["Data", "Esercizio", "Carico", "Reps"]).to_csv(FILE_ESERCIZI, index=False)
df_esercizi = pd.read_csv(FILE_ESERCIZI)

# --- IDRATAZIONE ---
if 'water_level' not in st.session_state: st.session_state.water_level = 0.0
if 'last_access' not in st.session_state: st.session_state.last_access = datetime.now().day
if st.session_state.last_access != datetime.now().day:
    st.session_state.water_level = 0.0
    st.session_state.last_access = datetime.now().day

# --- DEFINIZIONI COLAZIONI ---
pancake = "🥞 PANCAKE: 80g Farina Avena + 200ml Albume + 1 Banana + 10g Noci"
bowl = "🥣 BOWL: 150g Yogurt Greco + 4 Fette Bisc. + Frutto"
shake = "🥤 SHAKE (Liquid): 300ml Acqua/Latte + 30g Whey + 80g Avena Istantanea + 1 Banana + 15g Burro Arachidi"

# --- LOGICA SABATO DINAMICO ---
is_match_day = True 
if selected_day == "Sabato":
    st.write("---")
    col_check, col_void = st.columns([2,1])
    with col_check:
        mode = st.radio("⚽ Hai la partita oggi?", ["SÌ, MATCH DAY", "NO, RIPOSO"], horizontal=True)
        is_match_day = True if mode == "SÌ, MATCH DAY" else False

# --- DIET PLAN (BUDGET FRIENDLY: TONNO/SGOMBRO/SALMONE) ---
diet_plan = {
    "Lunedì": {
        "Type": "GYM A", "Kcal": "2850", 
        "Colazione": (pancake, "Alt: " + shake),
        "Spuntino_Mat": ("1 Frutto + 20g Parmigiano", "Alt: 15g Frutta Secca"), 
        "Pranzo": ("120g Riso + 150g Pollo + Zucchine", "Alt: 400g Patate + 112g Tonno (2 scatolette)"), 
        "Spuntino_Pom": ("4 Gallette + 60g Fesa", "Alt: Banana + Whey"), 
        "Cena": ("POST-WO: 400g Patate + 150g Manzo + Spinaci", "Alt: 120g Riso + 100g Salmone Affumicato")
    },
    "Martedì": {
        "Type": "REST", "Kcal": "2600", 
        "Colazione": (bowl, "Alt: " + shake),
        "Spuntino_Mat": ("1 Frutto + 15g Mandorle", "Alt: Yogurt"), 
        "Pranzo": ("100g Pasta Int. + 112g Tonno (sgocciolato) + Fagiolini", "Alt: Farro + 125g Sgombro"), 
        "Spuntino_Pom": ("Yogurt + 10 Mandorle", "Alt: Frutto + Parmigiano"), 
        "Cena": ("LOW CARB: 200g Patate + 125g Sgombro al Naturale", "Alt: 60g Pane + 100g Salmone Affumicato")
    },
    "Mercoledì": {
        "Type": "GYM B", "Kcal": "2850", 
        "Colazione": (shake, "Alt: " + pancake),
        "Spuntino_Mat": ("Frutto + Parmigiano", "-"), 
        "Pranzo": ("120g Riso + 150g Tacchino + Finocchi", "Alt: Patate + 112g Tonno"), 
        "Spuntino_Pom": ("4 Gallette + Bresaola", "Alt: Banana + Whey"), 
        "Cena": ("POST-WO: 120g Riso Venere + 100g Salmone Affumicato + Zucchine", "Alt: Patate Dolci + Manzo")
    },
    "Giovedì": {
        "Type": "REST", "Kcal": "2600", 
        "Colazione": (bowl, "Alt: " + shake), 
        "Spuntino_Mat": ("Frutto + Noci", "-"), 
        "Pranzo": ("80g Farro + 150g Legumi", "Alt: Pasta + 2 Uova"), 
        "Spuntino_Pom": ("Yogurt + Pera", "-"), 
        "Cena": ("Frittata (2 Uova) + 80g Pane", "Alt: 112g Tonno + Patate")
    },
    "Venerdì": {
        "Type": "GYM A", "Kcal": "2900", 
        "Colazione": (pancake, "Alt: " + shake), 
        "Spuntino_Mat": ("Frutto + Parmigiano", "-"), 
        "Pranzo": ("120g Riso Basmati + 125g Sgombro (Scatola) + Carote", "Alt: 400g Patate + 100g Salmone Affumicato"), 
        "Spuntino_Pom": ("4 Gallette + Fesa", "-"), 
        "Cena": ("PRE-MATCH: 120g Pasta + 150g Pollo", "Alt: Riso + 112g Tonno")
    },
    "Sabato": {
        "Type": "CALCETTO" if is_match_day else "REST", 
        "Kcal": "Match Day" if is_match_day else "2600",
        "Colazione": (pancake, "Alt: " + shake),
        "Spuntino_Mat": ("Frutto + Noci", "-"),
        "Pranzo": ("NO FIBRE: 120g Riso Bianco + 100g Pollo" if is_match_day else "120g Riso + 112g Tonno + Verdure", "Alt: Pasta in bianco + Tonno"), 
        "Spuntino_Pom": ("Banana Pre-Match" if is_match_day else "Yogurt + Noci", "-"), 
        "Cena": ("PIZZA / LIBERO", "-")
    },
    "Domenica": {
        "Type": "REST", "Kcal": "Detox", 
        "Colazione": ("Fette Bisc + Miele + Albume", "Alt: " + shake), 
        "Spuntino_Mat": ("Frutto", "-"), 
        "Pranzo": ("LIBERO MODERATO", "-"), 
        "Spuntino_Pom": ("Yogurt", "-"), 
        "Cena": ("Passato Verdure + 100g Salmone Affumicato (o Tonno)", "-")
    }
}

oggi_data = diet_plan[selected_day]
tipo_oggi = oggi_data['Type']

# ==========================================
# 💧 IDRATAZIONE
# ==========================================
st.markdown("### 💧 IDRATAZIONE (3.5L)")
col_w1, col_w2, col_w3 = st.columns([3, 1, 1])
with col_w1: st.progress(min(st.session_state.water_level / 3.5, 1.0))
with col_w2: 
    if st.button("+0.5L"): st.session_state.water_level += 0.5; st.rerun()
with col_w3: st.write(f"**{st.session_state.water_level}L**")
st.divider()

# ==========================================
# ⚖️ PESO CORPOREO (SOLO LUNEDÌ)
# ==========================================
with st.expander("⚖️ PESO CORPOREO & PROGRESSI", expanded=(giorno_reale_ita == "Lunedì")):
    if giorno_reale_ita == "Lunedì":
        st.info("📅 È Lunedì. Giorno di Check-In.")
        c1, c2 = st.columns([2,1])
        with c1: nuovo_peso = st.number_input("Inserisci Peso (kg)", 60.0, 100.0, step=0.1)
        with c2: 
            st.write("")
            st.write("")
            if st.button("Salva Peso"):
                nuova = pd.DataFrame({"Data": [oggi_data_breve], "Peso": [nuovo_peso]})
                df_peso = pd.concat([df_peso, nuova], ignore_index=True)
                df_peso.to_csv(FILE_PESO, index=False)
                st.success("Salvato!")
                st.rerun()
    else:
        st.write(f"📅 Oggi è {giorno_reale_ita}. Il check del peso è attivo solo di Lunedì.")

    if not df_peso.empty:
        st.line_chart(df_peso.set_index("Data"))
        st.caption(f"Ultimo peso: {df_peso.iloc[-1]['Peso']} kg")

# ==========================================
# 🏋️ WAR ROOM
# ==========================================
st.header(f"🏋️ WAR ROOM: {tipo_oggi}")

scheda_a_raw = {
    "✅": [False]*6,
    "Esercizio": ["Goblet Squat", "Rematore Manubrio", "Panca Inclinata", "Lat Machine", "Face Pull", "Plank"],
    "Set x Reps": ["3 x 10", "3 x 10", "3 x 10", "3 x 12", "4 x 15", "3 x 45''"],
    "Rec": ["90''", "60''", "90''", "60''", "60''", "45''"],
    "Note": ["Gomiti stretti.", "Schiena piatta.", "Discesa 3 sec.", "No dondolare.", "Ruota polsi.", "No lombare curva."],
    "Carico (kg)": [0.0]*6
}
scheda_b_raw = {
    "✅": [False]*7,
    "Esercizio": ["Affondi Manubri", "Pulley Basso", "Shoulder Press", "Lat Pulldown", "Alzate Laterali", "Push Down", "Vacuum"],
    "Set x Reps": ["3 x 10xlato", "3 x 12", "3 x 10", "3 x 10", "4 x 15", "3 x 12", "5 x 20''"],
    "Rec": ["90''", "60''", "90''", "60''", "45''", "60''", "30''"],
    "Note": ["Passi controllati.", "Allungati avanti.", "Schiena appoggiata.", "Presa neutra.", "Gomiti alti.", "Gomiti fissi.", "A vuoto."],
    "Carico (kg)": [0.0]*7
}

if "GYM" in tipo_oggi:
    df_active = pd.DataFrame(scheda_a_raw) if "GYM A" in tipo_oggi else pd.DataFrame(scheda_b_raw)
    st.info("Inserisci i carichi e spunta ✅ quando hai finito.")
    
    edited_df = st.data_editor(
        df_active,
        hide_index=True,
        use_container_width=True,
        column_config={
            "✅": st.column_config.CheckboxColumn("Fatto", default=False),
            "Esercizio": st.column_config.TextColumn("Ex", width="medium"),
            "Note": st.column_config.TextColumn("Note", width="small"),
            "Carico (kg)": st.column_config.NumberColumn("Kg", min_value=0, max_value=200, step=0.5)
        }
    )

    col_save, col_info = st.columns([1, 1])
    with col_save:
        if st.button("💾 SALVA SESSIONE COMPLETA"):
            completed_exercises = edited_df[edited_df["✅"] == True]
            if not completed_exercises.empty:
                new_records = []
                today_date_str = datetime.now().strftime("%Y-%m-%d")
                for index, row in completed_exercises.iterrows():
                    if row["Carico (kg)"] > 0:
                        new_records.append({
                            "Data": today_date_str,
                            "Esercizio": row["Esercizio"],
                            "Carico": row["Carico (kg)"],
                            "Reps": row["Set x Reps"] 
                        })
                if new_records:
                    df_new = pd.DataFrame(new_records)
                    df_esercizi = pd.concat([df_esercizi, df_new], ignore_index=True)
                    df_esercizi.to_csv(FILE_ESERCIZI, index=False)
                    st.toast(f"Salvato storico per {len(new_records)} esercizi!", icon="🦍")
                else:
                    st.warning("Hai spuntato ma carico = 0.")
            else:
                st.warning("Spunta almeno un esercizio.")

    st.write("")
    with st.expander("📈 VEDI STORICO ESERCIZIO (Grafico)", expanded=False):
        if not df_esercizi.empty:
            lista_es = df_esercizi["Esercizio"].unique()
            if len(lista_es) > 0:
                scelta_es = st.selectbox("Seleziona Esercizio:", lista_es)
                dati_es = df_esercizi[df_esercizi["Esercizio"] == scelta_es]
                if not dati_es.empty:
                    st.line_chart(dati_es.set_index("Data")["Carico"])
                    ult_carico = dati_es.iloc[-1]["Carico"]
                    st.caption(f"Ultimo carico: **{ult_carico} kg**")
                else:
                    st.write("Nessun dato.")
            else:
                 st.write("Nessun esercizio salvato.")
        else:
            st.write("Database vuoto.")

elif "CALCETTO" in tipo_oggi:
    st.warning("⚽ MATCH DAY (16:00) - Focus Idratazione")
else:
    st.success("💤 REST DAY - Recupero Attivo")

# ==========================================
# 🍽️ FUELING
# ==========================================
st.divider()
st.header("🍽️ FUELING")
def show_meal(t, d, i):
    st.markdown(f"**{i} {t}**")
    st.info(d[0]); 
    if d[1] != "-": st.caption(f"Opz: {d[1]}")
    st.write("---")

show_meal("COLAZIONE", oggi_data['Colazione'], "🥞")
show_meal("SPUNTINO", oggi_data['Spuntino_Mat'], "🍏")
show_meal("PRANZO", oggi_data['Pranzo'], "🍚")
show_meal("MERENDA", oggi_data['Spuntino_Pom'], "🥪")
show_meal("CENA", oggi_data['Cena'], "🌙")

st.markdown(f"<div class='kcal-box'>🔥 OBIETTIVO: {oggi_data['Kcal']} Kcal</div>", unsafe_allow_html=True)

with st.expander("📚 SOSTITUZIONI BUDGET"):
    st.table(pd.DataFrame({
        "Carbo": ["Riso 120g -> Patate 400g", "Pane 60g -> Gallette 50g"],
        "Proteine Economiche": ["Pesce Fresco 200g -> Tonno/Sgombro 112g (2 scat. piccole)", "Manzo 150g -> Salmone Affumicato 100g"]
    }))
