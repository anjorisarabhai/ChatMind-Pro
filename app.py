from flask import Flask, render_template, request
from helpers import detect_sentiment, rule_based_reply, get_gpt_response, get_gemini_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    user_message = bot_reply = sentiment = gpt_reply = gemini_reply = None

    if request.method == "POST":
        user_message = request.form.get("message")

        # Sentiment analysis
        sentiment = detect_sentiment(user_message)

        # Rule-based
        bot_reply = rule_based_reply(user_message)

        # GPT fallback
        gpt_reply = get_gpt_response(user_message) if not bot_reply else None

        # Gemini fallback (if both above fail)
        if not bot_reply and not gpt_reply:
            gemini_reply = get_gemini_response(user_message)

    return render_template("chat.html", user=user_message, sentiment=sentiment, bot=bot_reply, gpt=gpt_reply, gemini=gemini_reply)

if __name__ == "__main__":
    app.run(debug=True)