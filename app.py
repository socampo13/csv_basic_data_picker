from flask import Flask, render_template, request, send_file
import pandas as pd
import os
import unicodedata
import re
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Save temporary dataframes
dataframes = {}

# -----------------------------
# Load file
# -----------------------------

def load_file(filepath):
    if filepath.endswith(".csv"):
        return pd.read_csv(
            filepath,
            on_bad_lines="skip",
            encoding="utf-8",
            engine="python"
        )
    elif filepath.endswith(".xlsx"):
        return pd.read_excel(filepath)
    return None

# -----------------------------
# Text cleaning
# -----------------------------

def clean_text(value):
    if isinstance(value, str):
        value = value.strip()
        
        value = unicodedata.normalize('NFKD', value)\
            .encode('ascii', 'ignore')\
            .decode('utf-8')

        value = re.sub(r'[^a-zA-Z0-9\s@._-]', '', value)
        value = re.sub(r'\s+', ' ', value)
    
        return value
    return value

# ------------------------
# 🏠 Home
# ------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        
        if not file:
            return "No file found"
        
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)
        
        df = load_file(filepath)
        
        if df is None:
            return "File format is not supported, only upload CSV or XLSX"
        
        dataframes[file.filename] = df
        
        preview_data = df.head(10).to_html(index=False)
        
        return render_template(
            "select_columns.html",
            columns=df.columns.tolist(),
            filename=file.filename,
            preview=preview_data
        )
    return render_template("index.html")

# ------------------------
# Processing files
# ------------------------
@app.route("/process", methods=["POST"])
def process():
    filename = request.form.get("filename")
    selected_columns = request.form.getlist("columns")
  # clean_data = request.form.get("clean_data")
    
    df = dataframes.get(filename)
    
    if df is None:
        return "File not found"
    
    if not selected_columns:
        return "Choose at lease 1 column"
    
    new_df = df[selected_columns]
    
    # Optional cleaning
    csv_buffer = BytesIO()
    new_df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    return send_file(
        csv_buffer,
        mimetype="text/csv",
        as_attachment=True,
        download_name="filtered.csv"
    )
    

# ------------------------
# ▶️ Run
# ------------------------

if __name__ == "__main__":
    app.run(debug=True)