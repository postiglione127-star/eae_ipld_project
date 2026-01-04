# check_variables.py
# Questo script verifica se le variabili principali degli esercizi sono definite

# IMPORTS
import home

# Lista delle variabili richieste dal template Streamlit
required_vars = {
    "Ex 1.1": ["max_height", "max_width"],
    "Ex 1.2": ["crop_min_h", "crop_max_h", "crop_min_w", "crop_max_w"],
    "Ex 1.3": ["crop_arr"],
    "Ex 1.4": ["file_name", "crop_img"],
    "Ex 2.1": ["movies_df"],
    "Ex 2.2": ["min_year", "max_year"],
    "Ex 2.3": ["num_missing_directors"],
    "Ex 2.4": ["n_countries"],
    "Ex 2.5": ["avg_title_length"],
    "Ex 2.6": ["top_10_countries"],
    "Ex 2.7": ["movies_avg_duration_per_year"],
    "Ex 3.1": ["temps_df"],
    "Ex 3.2": ["temps_df"],  # perché la colonna nuova è dentro questo df
    "Ex 3.3": ["unique_countries_list"],
    "Ex 3.4": ["min_date", "max_date"],
    "Ex 3.5": ["min_temp", "max_temp", "min_temp_city", "min_temp_date", "max_temp_city", "max_temp_date"],
    "Ex 3.6": ["city_df_period"],  # dataframe finale filtrato
    "Ex 3.7": ["city_df_period"],  # dataframe finale filtrato
}

print("📝 Verifica delle variabili degli esercizi...\n")

# Ciclo su tutti gli esercizi
for ex, vars_list in required_vars.items():
    missing = []
    for var in vars_list:
        if var not in globals():
            missing.append(var)
    if missing:
        print(f"{ex}: ❌ Missing variables: {missing}")
    else:
        print(f"{ex}: ✅ All variables defined")

print("\n✅ Controllo completato.")


import streamlit as st

st.write("=== Debug: variabili esercizi ===")

# Ex 1.1
try:
    st.write("Ex 1.1:", max_height, max_width)
except NameError:
    st.write("Ex 1.1 missing")

# Ex 2.6
try:
    st.write("Ex 2.6:", top_10_countries)
except NameError:
    st.write("Ex 2.6 missing")

# Ex 3.1
try:
    st.write("Ex 3.1:", temps_df.head())
except NameError:
    st.write("Ex 3.1 missing")
