import pandas as pd

# 1. Leer el dataset original
df_usuarios_raw = pd.read_csv("data/usuarios.csv")
print("📋 Dataset original:")
print(df_usuarios_raw)

# 2. Filtrar usuarios que tengan nombre y email válidos
df_usuarios_cleaned = df_usuarios_raw.dropna(subset=["nombre", "email"])

# 3. Filtrar emails que contengan "@"
df_usuarios_cleaned = df_usuarios_cleaned[df_usuarios_cleaned["email"].str.contains("@")]

print("\n✅ Dataset filtrado (usuarios válidos):")
print(df_usuarios_cleaned)

# 4. Guardar el resultado en un nuevo archivo CSV
df_usuarios_cleaned.to_csv("data/usuarios_filtrados.csv", index=False)
print("\n💾 Archivo 'usuarios_filtrados.csv' guardado en /data/")
