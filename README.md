# 🎬 AI YouTube Script Generator

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?logo=openai&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

> A Python AI automation tool that generates complete YouTube content packages — scripts, titles, descriptions, and hashtags — from a single topic input. Powered by the OpenAI API.

---

## 📸 Screenshots

> _Add your screenshots here after running the project._
>
> **CLI version** — paste a screenshot of the terminal output.  
> **Streamlit UI** — paste a screenshot of the browser UI.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎬 Full YouTube Script | Documentary-style script with HOOK, INTRO, MAIN CONTENT, and OUTRO |
| 📌 5 Title Ideas | Click-worthy, SEO-optimized title options |
| 📋 Video Description | SEO-optimized description with chapters and CTA |
| 🏷️ 10 Hashtags | Mix of broad and niche hashtags for maximum reach |
| 💾 Auto Save | Results automatically saved to a timestamped `.txt` file |
| 🌐 Web UI | Optional Streamlit browser interface |
| ⌨️ CLI Mode | Clean terminal interface, no browser required |

---

## 🛠️ Technology Stack

- **Python 3.11**
- **OpenAI API** (GPT-4o-mini)
- **Streamlit** (optional web UI)
- **python-dotenv** (secure API key management)

---

## 📁 Project Structure

```
ai-youtube-script-generator/
│
├── main.py                 # CLI entry point
├── app.py                  # Streamlit web UI
├── script_generator.py     # Generates the full YouTube script
├── title_generator.py      # Generates titles + video description
├── hashtag_generator.py    # Generates hashtags
│
├── requirements.txt        # Python dependencies
├── .env.example            # Template for your API key
├── .gitignore              # Files excluded from Git
└── README.md               # This file
```

---

## 🚀 Getting Started

### Step 1 — Install Python

Download and install Python 3.11 from the official website:  
👉 https://www.python.org/downloads/

During installation on Windows, **check the box** that says **"Add Python to PATH"**.

Verify the installation:

```bash
python --version
# Expected output: Python 3.11.x
```

---

### Step 2 — Clone the Repository

```bash
git clone https://github.com/Umar-Software-House/ai-youtube-script-generator.git
cd ai-youtube-script-generator
```

---

### Step 3 — Create a Virtual Environment

A virtual environment keeps project dependencies isolated.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You will see `(venv)` appear at the start of your terminal prompt — this means the virtual environment is active.

---

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `openai` — connects to the OpenAI API
- `python-dotenv` — reads your secret API key from the `.env` file
- `streamlit` — powers the optional web UI

---

### Step 5 — Get Your OpenAI API Key

1. Go to 👉 https://platform.openai.com/api-keys
2. Sign in or create a free account
3. Click **"Create new secret key"**
4. Copy the key (starts with `sk-...`)

> ⚠️ **Keep it secret.** Never share your API key or commit it to GitHub.

---

### Step 6 — Configure the `.env` File

Copy the example file:

**Windows:**
```bash
copy .env.example .env
```

**Mac / Linux:**
```bash
cp .env.example .env
```

Open the `.env` file in VS Code and replace the placeholder with your real key:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

---

## ▶️ Running the Project

### Option A — Command Line Interface (CLI)

```bash
python main.py
```

You will be prompted to enter a topic:

```
📝  Your topic: Apple vs Samsung rivalry history
```

The script will generate all content and display it in the terminal.  
Results are also saved automatically to `output_script_YYYYMMDD_HHMMSS.txt`.

---

### Option B — Streamlit Web UI (Recommended for Portfolio)

```bash
streamlit run app.py
```

Your browser will open automatically at `http://localhost:8501`.

1. Enter your OpenAI API key in the sidebar (if not set in `.env`)
2. Type your topic in the text box
3. Click **Generate Content**
4. View results in tabs: Titles · Description · Hashtags · Full Script
5. Click **Download All Results as .txt** to save the file

---

## 📄 Example Output

**Topic:** `Apple vs Samsung rivalry history`

**Titles generated:**
```
1. The $100 Billion War: How Apple vs Samsung Changed Tech Forever
2. Apple vs Samsung: The Untold Story of the Greatest Tech Rivalry
3. Who Really Won? The Apple Samsung Battle That Shocked the World
4. The Secret History Behind Apple vs Samsung's Epic Legal War
5. How Two Companies Changed the World: Apple vs Samsung Explained
```

**Hashtags generated:**
```
#AppleVsSamsung #TechHistory #SmartphoneWar #Apple #Samsung
#iPhoneVsGalaxy #TechRivalry #TechNews #MobileTech #TechDocumentary
```

**Output file:** `output_script_20260311_143022.txt`

---

## 🔑 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `OPENAI_API_KEY` | Your OpenAI secret API key | ✅ Yes |

---

## 🧠 How It Works

```
User enters topic
       │
       ▼
main.py / app.py  ──► OpenAI API (GPT-4o-mini)
       │
       ├── script_generator.py   → Full YouTube script
       ├── title_generator.py    → 5 titles + description
       └── hashtag_generator.py  → 10 hashtags
       │
       ▼
Display in terminal / Streamlit UI
       │
       ▼
Save to output_script_TIMESTAMP.txt
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| `OPENAI_API_KEY not found` | Make sure your `.env` file exists and contains the key |
| `AuthenticationError` | Your API key is invalid or expired — generate a new one |
| `RateLimitError` | You have hit your OpenAI usage limit — wait or upgrade your plan |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` inside your activated `venv` |
| Streamlit not opening | Try `http://localhost:8501` manually in your browser |

---

## 📤 Uploading to GitHub

```bash
# 1. Initialise a Git repository
git init

# 2. Add all files
git add .

# 3. Make the first commit
git commit -m "Initial commit: AI YouTube Script Generator"

# 4. Create the repo on GitHub at:
#    https://github.com/new
#    Name it: ai-youtube-script-generator

# 5. Link your local repo to GitHub
git remote add origin https://github.com/Umar-Software-House/ai-youtube-script-generator.git

# 6. Push to GitHub
git branch -M main
git push -u origin main
```

---

## 👤 Author

**Muhammad Umar Malik**  
AI Automation Engineer (Learning Phase)

- 🌐 Portfolio: [muhammadumarmalik.me](https://muhammadumarmalik.me)
- 🐙 GitHub: [@Umar-Software-House](https://github.com/Umar-Software-House)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

> _Built with ❤️ to demonstrate real-world AI automation skills._
