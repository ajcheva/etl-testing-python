import pandas as pd

# Dataset: usuarios.csv
df_usuarios_raw = pd.read_csv("data/usuarios.csv")

def test_columnas_obligatorias_en_usuarios():
    columnas_esperadas = {"id", "nombre", "email"}
    columnas_presentes = set(df_usuarios_raw.columns)
    assert columnas_esperadas.issubset(columnas_presentes), \
        f"Faltan columnas obligatorias: {columnas_esperadas - columnas_presentes}"

def test_ids_no_nulos():
    assert df_usuarios_raw["id"].notnull().all(), "Hay valores nulos en la columna 'id'"

def test_ids_unicos():
    assert df_usuarios_raw["id"].is_unique, "La columna 'id' contiene duplicados"

def test_emails_con_arroba():
    emails = df_usuarios_raw["email"].dropna().astype(str)
    assert emails.str.contains("@").all(), "Hay correos electrónicos sin '@'"
