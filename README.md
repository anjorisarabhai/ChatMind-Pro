# 🤖 ChatMind Pro

ChatMind Pro is an intelligent, file-aware, sentiment-sensitive chatbot web application built with Python and Flask. It can chat like a human, detect user emotions, read files like PDFs or Excel sheets, and respond smartly using free AI APIs like OpenAI GPT and Google Gemini.

---

## ✨ Features

✅ **User Authentication**  
Secure login and registration system with session support.

✅ **Chat Interface**  
A smooth web-based interface to interact with the chatbot.

✅ **Rule-based & Sentiment-aware Bot**  
Understands greetings and emotional tone using NLP tools like TextBlob/NLTK.

✅ **AI-Powered Responses**  
Integrates with OpenAI GPT API and Gemini API for realistic replies (via free tier).

✅ **File Upload Support**  
Reads `.txt`, `.pdf`, `.csv`, `.xlsx`, and even `.pptx` files. The bot can answer based on the file content.

✅ **Chat History**  
Stores previous user-chatbot conversations (optional feature).

✅ **Flashy & Responsive UI**  
Uses HTML, CSS, and JavaScript for a polished user experience.

---

## 🛠️ Tech Stack

| Area        | Technology         |
|-------------|--------------------|
| Backend     | Python, Flask      |
| Frontend    | HTML, CSS, JS      |
| Database    | SQLite             |
| AI/NLP      | TextBlob, NLTK, OpenAI API, Gemini API |
| File Parsing| PyMuPDF, pandas, python-pptx |
| Deployment  | GitHub + (optional Render, Replit) |

---

## 📂 Project Structure

```
chatmind-pro/
├── app.py                 # Flask backend
├── helpers.py             # Bot & file reading logic
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
├── .gitignore             # Ignore sensitive/data files
├── database/
│   └── chatbot.db         # SQLite database (auto-created)
├── static/
│   ├── styles.css         # CSS styling
│   └── script.js          # JS interactivity
├── templates/
│   ├── layout.html        # Base HTML
│   ├── login.html
│   ├── register.html
│   └── chat.html
├── uploads/               # Uploaded files by users
```

---

## 🚀 How to Run (Using Python 3.10)

> ⚠️ No virtual environment used. Ensure you have Python 3.10 installed and use it explicitly.

```bash
# Install Flask and dependencies
py -3.10 -m pip install flask textblob pandas python-pptx pymupdf

# Run the Flask app
py -3.10 app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the app.

---

## 🧠 Planned Upgrades

- [ ] Google Gemini API integration
- [ ] File-based chat context (like ChatGPT with PDFs)
- [ ] Conversation history viewer per user
- [ ] Admin dashboard to monitor users/chats
- [ ] Theme switcher (dark/light mode)

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 💡 Inspiration

This project was developed as part of **Harvard's CS50 final project**, with a goal to integrate multiple concepts: web development, Python, AI, NLP, and file processing.
