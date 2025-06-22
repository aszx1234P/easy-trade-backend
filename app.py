
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "TTB Backend Running ✅"

@app.route("/api/signals")
def signals():
    return jsonify([
        {
            "id": 1,
            "asset": "RELIANCE.BSE",
            "action": "buy",
            "entry": 2845.3,
            "stopLoss": 2800.5,
            "target": 2900.0,
            "time": "10:45 AM"
        }
    ])

@app.route("/api/report/1")
def report():
    return jsonify({
        "roi": "16.5%",
        "win_rate": "70%",
        "drawdown": "4.3%",
        "trades": 18
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
