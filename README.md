# 🧪 Proyecto de ETL Testing con Python y pytest

Este repositorio contiene un ejemplo de flujo ETL (Extract-Transform-Load) centrado en la validación de calidad de datos usando Python y `pytest`.

## 📁 Estructura del proyecto

```
etl_testing/
├── .venv/                   ← Entorno virtual (ignorado por .gitignore)
├── data/
│   ├── usuarios.csv         ← Datos originales (crudos)
│   └── usuarios_filtrados.csv ← Datos validados y limpios
├── main.py                 ← Script que carga, filtra y guarda
├── test_datos.py           ← Pruebas automatizadas con pytest
├── requirements.txt        ← Dependencias del entorno
├── .gitignore              ← Exclusiones para mantener el repo limpio
└── README.md               ← Este archivo
```

## 🛠️ Requisitos

- Python 3.10 o superior
- Entorno virtual (`python3 -m venv .venv`)
- Instalación de dependencias:

```bash
pip install -r requirements.txt
```
