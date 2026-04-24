from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 模擬課表資料
courses = {
    "114": "114年度應修科目：機器學習、巨量資料分析、數位行銷、企業創新",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"]

    # 校區平面圖
    if "校區" in msg or "平面圖" in msg:
        return jsonify({
            "reply": "這是致理科技大學校區平面圖，請參考下方的位置說明。",
            "image": "/static/images.svg"
        })

    # 系辦位置
    if "所辦" in msg:
        return jsonify({
            "reply": "所辦在綜合大學2樓。",
            "image": "/static/images.svg"
        })

    # 研究室
    elif "研究室" in msg:
        return jsonify({
            "reply": "商務科技智慧與創新研究所在綜合教學大樓3樓的E32教室。",
            "image": "/static/images.svg"
        })

    # 商務科技智慧與創新研究所
    elif "研究所" in msg or "商務科技" in msg:
        return jsonify({
            "reply": "商務科技智慧與創新研究所在綜合教學大樓2樓。",
            "image": "/static/images.svg"
        })

    # 課表
    elif "課表" in msg or "應修" in msg:
        return jsonify({
            "reply": "114年度應修科目：機器學習、巨量資料分析、數位行銷、企業創新。詳細內容請參考下方的應修科目表。",
            "image": "/static/114級應修科目表.pdf"
        })

    # 年度判斷
    elif msg in courses:
        return jsonify({
            "reply": courses[msg],
            "image": "/static/114級應修科目表.pdf"
        })

    # 其他問題
    else:
        return jsonify({
            "reply": "請聯絡系辦秘書  02-2257-6167分機1137，",
            "image": None
        })

if __name__ == "__main__":
    app.run(debug=True)