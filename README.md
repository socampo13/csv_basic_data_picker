# 🧹 Data Cleaner App

A simple yet powerful web application to upload, clean, and filter CSV or Excel files directly from your browser.

Built with Python using Flask and Pandas.

---

## 🚀 Features

* 📂 Upload CSV or Excel (`.xlsx`) files
* 📊 Preview your data before processing
* ✅ Select specific columns to keep
* 🧹 Clean and normalize text data (optional)
* ⬇️ Download the processed file instantly
* 🎨 Modern UI with cards, tables, and responsive layout

---

## 🛠️ Tech Stack

* Python
* Flask
* Pandas
* Bootstrap (UI)

---

## 📁 Project Structure

```
csv_cleaner_app/
│
├── app.py
├── requirements.txt
├── uploads/
└── templates/
    ├── index.html
    └── select_columns.html
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/data-cleaner-app.git
cd data-cleaner-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open in your browser:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. Upload a CSV or Excel file
2. Preview the data
3. Select the columns you want
4. (Optional) Clean the data
5. Download the filtered file

---

## 🧹 Data Cleaning

The app can normalize text data by:

* Removing leading/trailing spaces
* Normalizing accents (á → a)
* Removing special characters
* Fixing multiple spaces

---

## 📌 Future Improvements

* 🔍 Column search/filter
* 📊 Data statistics (rows, duplicates, nulls)
* 📄 Multi-sheet Excel support
* ⚙️ Custom cleaning rules per column
* ☁️ Deployment (Render / Railway)
* 🔐 User authentication

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 💡 Author

Built by [Your Name]

---
