# ✍️ AI Writing Assistant with Tone Control

A purpose-built, locally running AI writing tool that generates content in different tones using prompt engineering. Built with Python, Flask, Ollama, and vanilla JavaScript.

---

## 🧩 What It Does

- Takes a topic as input and generates well-structured written content
- Lets you control **tone** (Formal, Casual, Persuasive, Friendly, Technical, Creative)
- Lets you control **length**, **format** (paragraphs, bullets, email, LinkedIn post), and **target audience**
- Runs 100% on your local machine — no internet, no API key, no cost
- Auto-detects all Ollama models you have installed

---

## 🤔 Why This — Not Just ChatGPT or Claude?

- **Offline first** — nothing leaves your machine; ChatGPT and Claude send every prompt to the cloud
- **Baked-in tone control** — no need to re-explain the tone every time; system prompts handle it automatically in the background
- **Purpose-built UI** — one screen, one job, no chat history, no distractions
- **You own everything** — the prompts, the model, the logic; swap any part without asking anyone's permission
- **Embeddable** — this is designed as a layer, not a standalone app; drop it into any product (CMS, CRM, browser extension, internal tool) without rebuilding from scratch
- **Teachable** — building this gives you real experience with prompt engineering, REST APIs, and local LLM deployment — skills companies actively hire for

---

## 🔌 Use as an Embedded Layer in Other Products

This assistant is not just a standalone tool — the Flask backend is a reusable API that can be dropped into any product to add AI writing capabilities.

**Examples of where you can embed it:**

- **CMS / Blog platform** — add a "Generate Draft" button that uses the user's post title as the topic
- **CRM / Sales tool** — auto-generate follow-up emails or cold outreach in the right tone per customer segment
- **Chrome extension** — highlight any text on a webpage, right-click, rewrite it in a chosen tone
- **Internal HR tool** — generate job descriptions, offer letters, or announcements in the company's preferred tone
- **E-commerce dashboard** — generate product descriptions for listings in bulk, formatted for different platforms
- **Student platform** — let students pick a topic and get a writing scaffold to start from

**How embedding works:**
- The Flask `/generate` endpoint is a standard REST API — any product that can make an HTTP POST request can call it
- Pass `topic`, `tone`, `length`, `format`, `audience` as JSON
- Get back the generated content as plain text
- The frontend (HTML/CSS/JS) is completely optional — your product's own UI can call the same backend directly

---

## ✨ Features at a Glance

- 6 tones — Formal · Casual · Persuasive · Friendly · Technical · Creative
- 3 length options — Short · Medium · Long
- 4 format options — Paragraphs · Bullets · Email · LinkedIn Post
- 4 audience options — General · Students · Professionals · Executives
- Auto model detection from Ollama
- One-click copy to clipboard
- Clean loading state and error handling

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| Frontend | HTML, CSS, Vanilla JS |
| Backend | Python, Flask, Flask-CORS |
| AI Engine | Ollama (local LLM) |
| Default Model | Llama 3.2 |

---

## 🚀 How to Run

**Prerequisites:** Python 3.8+, [Ollama](https://ollama.com) installed

```bash
# 1. Pull a model (one time only)
ollama pull llama3.2

# 2. Install dependencies
pip install -r requirements.txt

# 3. Terminal 1 — start Ollama
ollama serve

# 4. Terminal 2 — start Flask
python app.py

# 5. Open index.html in your browser
```

---

## 🔄 Alternatives to Ollama (Free Cloud APIs)

If you want to skip local setup, replace the Ollama logic in `app.py` with any of these — frontend stays untouched:

| Provider | Free Tier | Speed | How to swap |
|---|---|---|---|
| **Google Gemini** ⭐ | ~1B tokens/month, no card | Fast | `pip install google-generativeai` → replace `ollama.chat()` with `genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)` · Key at [aistudio.google.com](https://aistudio.google.com) |
| **Groq** | Daily limits, no card | Very fast | `pip install groq` → use `Groq(api_key).chat.completions.create()` with `llama-3.3-70b-versatile` · Key at [console.groq.com](https://console.groq.com) |
| **OpenRouter** | 50+ free models | Fast | `pip install openai` → point OpenAI client at `https://openrouter.ai/api/v1` · use any `model:free` · Key at [openrouter.ai](https://openrouter.ai) |
| **GitHub Models** | Free for GitHub users | Fast | `pip install openai` → point client at `https://models.github.ai/inference` · use your GitHub PAT as the key |

> In every case: only the API client and model name change. The prompt builder, Flask routes, and frontend are identical.

---

## 🗂️ Project Structure

```
ai-writing-assistant/
├── app.py            # Flask backend — prompt builder + Ollama/API connection
├── index.html        # Frontend — controls and output panel
├── style.css         # Styling
├── requirements.txt  # Dependencies
└── README.md
```

---

## 🧠 What I Learned

- Prompt engineering — how system prompt wording changes LLM output completely
- Building REST APIs with Flask — routes, JSON handling, error responses
- Frontend ↔ backend communication — fetch, CORS, async/await
- Local LLM deployment with Ollama
- Thinking in layers — separating UI, logic, and AI so each part is swappable

---

## 🔭 Roadmap

- [ ] Streaming output — text appears word by word
- [ ] Generation history — save and revisit past outputs
- [ ] Custom tone builder — let users define their own system prompt
- [ ] Export as `.txt` / `.docx`
- [ ] Deploy backend to Railway or Render for a shareable link
- [ ] Multi-language support

---

## 👤 Author

**Kirti** — built as a hands-on project for learning prompt engineering and LLM integration.
Fork it, extend it, embed it in something bigger.
