from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    category = data.get("category")
    month = data.get("month")
    
    prediction = 5000000  # 더미 예측값

    return jsonify({
        "category": category,
        "month": month,
        "predicted_amount": int(prediction)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
