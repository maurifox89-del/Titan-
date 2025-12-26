import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Titan Protocol", page_icon="🧬", layout="centered")

# --- LOGICA TEMPORALE & SELETTORE GIORNO ---
giorni_list = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
giorni_trad = {
    "Monday": "Lunedì", "Tuesday": "Martedì", "Wednesday": "Mercoledì",
    "Thursday": "Giovedì", "Friday": "Venerdì", "Saturday": "Sabato", "Sunday": "Domenica"
}

# Calcola il giorno reale di oggi per il default
giorno_reale_inglese = datetime.now().strftime("%A")
giorno_reale_ita = giorni_trad[giorno_reale_inglese]
oggi_data_breve = datetime.now().strftime("%Y-%m-%d")

# --- TITOLO & SELETTORE ---
st.title("🧬 TITAN PROTOCOL")
# Il selettore parte di default sul giorno di OGGI, ma puoi cambiarlo
selected_day = st.selectbox("📅 Visualizza Piano del Giorno:", giorni_list, index=giorni_list.index(giorno_reale_ita))

# --- FILE SALVATAGGIO PESO ---
FILE_DATI = "progressi_peso.csv"
if not os.path.exists(FILE_DATI):
    pd.DataFrame(columns=["Data", "Peso"]).to_csv(FILE_DATI, index=False)
df_peso = pd.read_csv(FILE_DATI)

# --- DATABASE DIETA ---
diet_plan = {
    "Lunedì": {
        "Type": "GYM A",
        "Colazione": ("80g Avena + 200ml Albume + 1 Banana + 10g Noci", 
                      "Alt: 4 Fette Biscottate + 30g Whey o 150g Yogurt Greco"),
        "Spuntino_Mat": ("1 Frutto + 20g Parmigiano", 
                         "Alt: 1 Frutto + 15g Frutta Secca"),
        "Pranzo": ("120g Riso Basmati + 150g Pollo + Zucchine + Olio", 
                   "Alt: 400g Patate / 100g Pasta Riso + 200g Pesce Bianco"),
        "Spuntino_Pom": ("4 Gallette Riso + 60g Fesa Tacchino", 
                         "Alt: 1 Banana + 30g Whey Protein"),
        "Cena": ("POST-WO: 400g Patate + 150g Manzo Magro + Spinaci", 
                 "Alt: 120g Riso + 150g Cavallo o Salmone (senza olio)")
    },
    "Martedì": {
        "Type": "REST",
        "Colazione": ("4 Fette Biscottate + 150g Yogurt Greco + Banana + Noci", 
                      "Alt: Pancake (80g Avena + 150ml Albume)"),
        "Spuntino_Mat": ("1 Frutto + 15g Mandorle", "Alt: 1 Yogurt Greco"),
        "Pranzo": ("100g Pasta Integrale + 110g Tonno + Fagiolini", 
                   "Alt: 100g Farro + 150g Sgombro/Salmone"),
        "Spuntino_Pom": ("1 Yogurt Greco + 10 Mandorle", "Alt: 1 Frutto + Parmigiano"),
        "Cena": ("LOW CARB: 200g Patate + 200g Merluzzo + Carote", 
                 "Alt: 60g Pane Tostato + 150g Pollo + Verdure")
    },
    "Mercoledì": {
        "Type": "GYM B",
        "Colazione": ("Cream of Rice (100g) + 30g Whey + 10g Cioccolato", 
                      "Alt: 80g Avena + 200ml Albume"),
        "Spuntino_Mat": ("1 Frutto + 20g Parmigiano", "Alt: Shake Proteico"),
        "Pranzo": ("120g Riso + 150g Tacchino + Finocchi", 
                   "Alt: 400g Patate + 150g Vitello"),
        "Spuntino_Pom": ("4 Gallette + 60g Bresaola", "Alt: 1 Banana + Whey"),
        "Cena": ("POST-WO: 120g Riso Venere + 150g Salmone + Zucchine", 
                 "Alt: 400g Patate Dolci + 150g Manzo")
    },
    "Giovedì": {
        "Type": "REST",
        "Colazione": ("100g Avena + 200g Yogurt Greco + Frutti Bosco", 
                      "Alt: 5 Fette Biscottate + 30g Whey"),
        "Spuntino_Mat": ("1 Frutto + 15g Noci", "Alt: Barretta Proteica"),
        "Pranzo": ("80g Farro/Orzo + 150g Legumi + Verdure", 
                   "Alt: 80g Pasta Integrale + 2 Uova Sode"),
        "Spuntino_Pom": ("1 Yogurt Greco + 1 Pera", "Alt: 20g Parmigiano + Frutto"),
        "Cena": ("LOW CARB: Frittata (2 Uova + 100ml Albume) + 80g Pane", 
                 "Alt: 200g Pesce Bianco + 200g Patate")
    },
    "Venerdì": {
        "Type": "GYM A",
        "Colazione": ("80g Avena + 200ml Albume + Banana", "Alt: Pancake Proteici"),
        "Spuntino_Mat": ("1 Frutto + 20g Parmigiano", "Alt: Yogurt Greco"),
        "Pranzo": ("120g Riso Basmati + 200g Orata + Carote", 
                   "Alt: 400g Patate + 150g Pollo"),
        "Spuntino_Pom": ("4 Gallette + 60g Fesa", "Alt: Shake Whey + Banana"),
        "Cena": ("PRE-MATCH: 120g Pasta olio/pomodoro + 150g Pollo", 
                 "Alt: 120g Riso + 200g Merluzzo (No Verdure Fibrose)")
    },
    "Sabato": {
        "Type": "CALCETTO",
        "Colazione": ("Pancake (80g Farina + 150ml Albume) + Marmellata", "Alt: Fette Biscottate + Miele + Whey"),
        "Spuntino_Mat": ("1 Frutto + 15g Noci", "-"),
        "Pranzo": ("NO FIBRE: 120g Riso Bianco + 100g Pollo", "Alt: 120g Pasta in bianco + 100g Tacchino"),
        "Spuntino_Pom": ("MATCH DAY: Solo acqua o banana pre-partita", "-"),
        "Cena": ("LIBERA: Pizza Margherita/Crudo (No fritti pesanti)", "Alt: Hamburger fatto in casa con pane")
    },
    "Domenica": {
        "Type": "REST",
        "Colazione": ("Fette Biscottate + Miele + Albume strapazzato", "Alt: Yogurt Greco + Frutta + Avena"),
        "Spuntino_Mat": ("1 Frutto", "-"),
        "Pranzo": ("LIBERO MODERATO: Lasagna o Riso al forno", "Alt: Pasta al ragù"),
        "Spuntino_Pom": ("Yogurt o Frutto", "-"),
        "Cena": ("DETOX: Passato Verdure + 150g Nasello", "Alt: Minestrone + 100g Pollo")
    }
}

# --- DATI SCHEDE ---
scheda_a_raw = {
    "✅": [False]*6,
    "Esercizio": ["Goblet Squat", "Rematore Manubrio", "Panca Inclinata", "Lat Machine", "Face Pull", "Plank"],
    "Set x Reps": ["3 x 10", "3 x 10", "3 x 10", "3 x 12", "4 x 15", "3 x 45''"],
    "Rec": ["90''", "60''", "90''", "60''", "60''", "45''"],
    "Note Tecniche": ["Gomiti stretti. Venerdì: Buffer 2 reps.", "Schiena piatta. Tira all'anca.", "Discesa 3 sec. Focus petto alto.", "Non dondolare. Petto fuori.", "Ruota polsi. Fondamentale cifosi.", "Strizza glutei. No lombare curva."],
    "Carico (kg)": [0.0]*6
}

scheda_b_raw = {
    "✅": [False]*7,
    "Esercizio": ["Affondi Manubri", "Pulley Basso", "Shoulder Press", "Lat Pulldown", "Alzate Laterali", "Push Down", "Vacuum"],
    "Set x Reps": ["3 x 10xlato", "3 x 12", "3 x 10", "3 x 10", "4 x 15", "3 x 12", "5 x 20''"],
    "Rec": ["90''", "60''", "90''", "60''", "45''", "60''", "30''"],
    "Note Tecniche": ["Busto dritto. Passi controllati.", "Allungati avanti, chiudi scapole.", "Macchina protegge schiena.", "Presa neutra/stretta. V-Shape.", "Gomiti alti. No slanci.", "Gomiti incollati ai fianchi.", "A vuoto. Risucchia ombelico."],
    "Carico (kg)": [0.0]*7
}

# --- RECUPERO DATI GIORNO SELEZIONATO ---
oggi_data = diet_plan[selected_day]
tipo_oggi = oggi_data['Type']

# ==========================================
# 📈 SEZIONE PROGRESSI
# ==========================================
with st.expander("📈 REGISTRO PESO & GRAFICO", expanded=False):
    col_in, col_btn = st.columns([2, 1])
    with col_in:
        nuovo_peso = st.number_input("Peso (kg)", 60.0, 100.0, step=0.1)
    with col_btn:
        st.write("") 
        st.write("") 
        if st.button("Salva"):
            nuova_riga = pd.DataFrame({"Data": [oggi_data_breve], "Peso": [nuovo_peso]})
            df_peso = pd.concat([df_peso, nuova_riga], ignore_index=True)
            df_peso.to_csv(FILE_DATI, index=False)
            st.rerun()

    if not df_peso.empty:
        st.line_chart(df_peso.set_index("Data"))
        st.caption(f"Ultimo: {df_peso.iloc[-1]['Peso']} kg")

# ==========================================
# 🏋️ WAR ROOM (ALLENAMENTO)
# ==========================================
st.header(f"🏋️ WAR ROOM: {tipo_oggi}")

if "GYM" in tipo_oggi:
    # Selezione Scheda in base al tipo di giornata
    df_active = pd.DataFrame(scheda_a_raw) if "GYM A" in tipo_oggi else pd.DataFrame(scheda_b_raw)
    
    st.info("Spunta le caselle quando completi l'esercizio.")
    edited_df = st.data_editor(
        df_active,
        hide_index=True,
        use_container_width=True,
        column_config={
            "✅": st.column_config.CheckboxColumn("Fatto", default=False),
            "Esercizio": st.column_config.TextColumn("Esercizio", width="medium"),
            "Set x Reps": st.column_config.TextColumn("Set/Reps", width="small"),
            "Rec": st.column_config.TextColumn("Rec", width="small"),
            "Note Tecniche": st.column_config.TextColumn("💡 Note Coach", width="large"),
            "Carico (kg)": st.column_config.NumberColumn("Carico", min_value=0, max_value=200, step=0.5, format="%.1f kg")
        }
    )
    # Barra Progresso
    fatti = edited_df["✅"].sum()
    totali = len(edited_df)
    progresso = fatti / totali
    st.progress(progresso, text=f"Completamento: {int(progresso*100)}%")
    if progresso == 1.0:
        st.balloons()
        st.success("GRANDE. RECUPERA E MANGIA.")

elif "CALCETTO" in tipo_oggi:
    st.warning("⚽ MATCH DAY (16:00)")
    st.markdown("""
    * **Pranzo:** Solo Riso e Pollo (Zero Fibre).
    * **Acqua:** 1.5L prima del match.
    """)

else:
    st.success("💤 REST DAY - Recupero Attivo & Stretching")

# ==========================================
# 🍽️ FUELING (DIETA ORDINATA)
# ==========================================
st.divider()
st.header("🍽️ FUELING")

def show_meal_box(title, data, icon):
    st.markdown(f"#### {icon} {title}")
    st.info(f"**{data[0]}**") # Opzione principale
    if data[1] != "-":
        st.caption(f"🔄 *Oppure: {data[1]}*") # Alternativa
    st.write("---") # Separatore visivo

# SEQUENZA ORDINATA
show_meal_box("1. COLAZIONE (07:00-08:00)", oggi_data['Colazione'], "🥞")
show_meal_box("2. SPUNTINO MATTINA (10:30)", oggi_data['Spuntino_Mat'], "🍏")
show_meal_box("3. PRANZO (13:00-14:00)", oggi_data['Pranzo'], "🍚")
show_meal_box("4. MERENDA POMERIGGIO (16:30)", oggi_data['Spuntino_Pom'], "🥪")
show_meal_box("5. CENA (Post-WO/Relax)", oggi_data['Cena'], "🌙")

# ==========================================
# 🔄 TABELLA SOSTITUZIONI
# ==========================================
with st.expander("📚 TABELLA SOSTITUZIONI (Consultare se necessario)"):
    sostituzioni = {
        "Fonti Carboidrati": {
            "Riso (120g)": ["400g Patate", "100g Pasta/Farro", "120g Avena", "120g Gallette"],
            "Patate (400g)": ["120g Riso", "350g Patate Dolci", "100g Cous Cous", "-"],
            "Pane (60g)": ["200g Patate", "50g Gallette", "50g Freselle", "-"]
        },
        "Fonti Proteiche": {
            "Pollo/Tacchino (150g)": ["150g Vitello", "200g Pesce Bianco", "150g Gamberi", "7 Albumi"],
            "Manzo (150g)": ["150g Cavallo", "150g Salmone (no olio)", "120g Bresaola", "-"],
            "Tonno (110g)": ["150g Sgombro", "200g Merluzzo", "170g Fiocchi Latte", "-"]
        }
    }
    st.write("**Carboidrati**")
    st.table(pd.DataFrame(sostituzioni["Fonti Carboidrati"]))
    st.write("**Proteine**")
    st.table(pd.DataFrame(sostituzioni["Fonti Proteiche"]))

st.caption("Protocollo V-Shape | Obiettivo 85kg | Coach Titan")
