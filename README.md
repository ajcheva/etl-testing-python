# 🧪 Proyecto de ETL Testing con Python, pytest y Great Expectations

Este repositorio contiene un ejemplo completo de flujo ETL (Extract-Transform-Load) con foco en la validación de calidad de datos utilizando `pytest` y la librería `Great Expectations`.

## 📁 Estructura del proyecto

```
etl_testing/
├── .venv/                         ← Entorno virtual (ignorado por .gitignore)
├── data/
│   ├── usuarios.csv               ← Datos originales (crudos)
│   └── usuarios_filtrados.csv     ← Datos validados y limpios
├── main.py                        ← Script que carga, filtra y guarda los datos
├── test_datos.py                  ← Pruebas automatizadas con pytest
├── requirements.txt               ← Dependencias necesarias
├── gx/
│   ├── checkpoints/               ← Checkpoints de validación de GE
│   ├── expectations/              ← Suites de expectativas definidas
│   ├── validations/               ← Resultados de validación generados
│   └── uncommitted/               ← Archivos temporales de ejecución
├── .gitignore                     ← Exclusiones para mantener el repo limpio
└── README.md                      ← Este archivo
```

## 🛠️ Requisitos

- Python 3.10 o superior
- Virtualenv activado:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate  # En Unix/Mac
  .venv\Scripts\activate   # En Windows
  ```
- Instalación de dependencias:
  ```bash
  pip install -r requirements.txt
  ```

## ✅ Validación de datos con Great Expectations

Se definió una `Expectation Suite` llamada `usuarios_suite` para validar el contenido del archivo `usuarios_filtrados.csv`. Las expectativas incluyen:

- El campo `id` debe ser único y no nulo.
- El campo `nombre` no debe ser nulo.
- El campo `email` debe cumplir con un formato válido usando expresión regular.

Además, los resultados de validación se registran en un reporte HTML interactivo generado con los Data Docs de Great Expectations.

