from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)  # Allows the HTML frontend to talk to this server

# =============================================
# TONE SYSTEM PROMPTS
# =============================================
TONE_PROMPTS = {
    "formal": """You are a professional business writer. Use precise, structured language.
Write in a formal register with clear, well-organized paragraphs.
Avoid contractions, slang, or casual expressions. Be authoritative and objective.""",

    "casual": """You are a friendly, relaxed writer. Write like you're talking to a friend.
Use contractions (it's, you'll, we're). Keep sentences short and punchy.
Be warm, conversational, and approachable. Avoid jargon.""",

    "persuasive": """You are a skilled copywriter and persuasion expert.
Use compelling arguments, emotional appeal, and rhetorical techniques.
Include a strong opening hook, supporting points, and a clear call-to-action.""",

    "friendly": """You are a warm, encouraging communicator.
Write with empathy, positivity, and a supportive tone.
Use inclusive language like 'we' and 'together'. Make the content feel welcoming.""",

    "technical": """You are a technical writer with deep domain expertise.
Use precise terminology, structured explanations, and logical flow.
Write for an audience that values accuracy and depth over simplicity.""",

    "creative": """You are a creative writer with a vivid, imaginative style.
Use metaphors, storytelling, and expressive language.
Make the content memorable and emotionally resonant.""",
}

LENGTH_MAP = {
    "short":  "1 to 2 paragraphs",
    "medium": "3 to 4 paragraphs",
    "long":   "5 or more paragraphs",
}

FORMAT_MAP = {
    "paragraph": "flowing paragraphs",
    "bullets":   "a clear bullet-point list",
    "email":     "a professional email with subject line, greeting, body, and sign-off",
    "linkedin":  "an engaging LinkedIn post with a hook, body, and hashtags",
}

AUDIENCE_MAP = {
    "general":       "a general audience",
    "students":      "students or young learners",
    "professionals": "working professionals",
    "executives":    "senior executives and decision-makers",
}


def build_prompt(topic, tone, length, format, audience):
    system_instruction = TONE_PROMPTS.get(tone, TONE_PROMPTS["formal"])
    return (
        f"{system_instruction}\n\n"
        f"Write content about the following topic:\n\"{topic}\"\n\n"
        f"Requirements:\n"
        f"- Length: {LENGTH_MAP.get(length, '3 to 4 paragraphs')}\n"
        f"- Format: {FORMAT_MAP.get(format, 'flowing paragraphs')}\n"
        f"- Target audience: {AUDIENCE_MAP.get(audience, 'a general audience')}\n\n"
        f"Write only the content. Do not include any explanation or meta-commentary."
    )


# =============================================
# API ENDPOINT: /generate
# =============================================
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    topic    = data.get("topic", "").strip()
    tone     = data.get("tone", "formal")
    length   = data.get("length", "medium")
    fmt      = data.get("format", "paragraph")
    audience = data.get("audience", "general")
    model    = data.get("model", "llama3.2")  # change to any model you've pulled

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    prompt = build_prompt(topic, tone, length, fmt, audience)

    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        result = response["message"]["content"]
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================================
# ENDPOINT: /models — list available models
# =============================================
@app.route("/models", methods=["GET"])
def list_models():
    try:
        models = ollama.list()
        names = [m["name"] for m in models.get("models", [])]
        return jsonify({"models": names})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================================
# RUN THE SERVER
# =============================================
if __name__ == "__main__":
    print("🚀 Server running at http://localhost:5000")
    print("📦 Make sure Ollama is running: ollama serve")
    app.run(debug=True, port=5000)