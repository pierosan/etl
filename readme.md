# 🛠️ Proceso ETL - FOB Guard

Este repositorio contiene el código y los recursos necesarios para ejecutar un proceso **ETL** (Extract, Transform, Load) de manera local o mediante **Docker**.

---

## 🚀 Ejecutar el proceso ETL con Docker

Puedes ejecutar la imagen del contenedor directamente con:

```bash
docker run --name etl pierosan/etl_fob_guard:latest
```

---

## 🐍 Ejecutar el código ETL en Python

### 1. Clonar el repositorio

```bash
git clone https://github.com/pierosan/etl.git
cd etl
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

- **En Windows:**
  ```bash
  venv\Scripts\activate.bat
  ```
- **En Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el proceso ETL

```bash
python main.py
```

---

## ☁️ Desplegar infraestructura desde cero (GitHub Actions)

1. Ve a la pestaña **Actions** en GitHub.  
2. Busca el workflow llamado **"Creación de proceso ETL"**.  
3. Haz clic en **"Run workflow"** para desplegar la infraestructura completa desde cero.
