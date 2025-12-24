from flask import Flask, redirect, jsonify
import random
import os
import json
from pathlib import Path

app = Flask(__name__)

# 問卷 URLs
SURVEYS = {
    "hotel": "https://tassel.syd1.qualtrics.com/jfe/form/SV_cCtJgUMGbUGfyxE",
    "medical": "https://tassel.syd1.qualtrics.com/jfe/form/SV_1TXCuW7dGUxH7Aa"
}

# 計數檔案路徑
COUNTS_FILE = "survey_counts.json"


def load_counts():
    """讀取分派計數"""
    if Path(COUNTS_FILE).exists():
        with open(COUNTS_FILE, 'r') as f:
            return json.load(f)
    return {"hotel": 0, "medical": 0}


def save_counts(counts):
    """保存分派計數"""
    with open(COUNTS_FILE, 'w') as f:
        json.dump(counts, f)


def get_balanced_survey():
    """取得平衡分派的問卷類型"""
    counts = load_counts()
    
    # 如果計數完全相同，隨機選擇
    if counts["hotel"] == counts["medical"]:
        return random.choice(list(SURVEYS.keys()))
    
    # 分派到計數較少的問卷
    return "hotel" if counts["hotel"] < counts["medical"] else "medical"


def increment_survey_count(survey_type):
    """增加分派計數"""
    counts = load_counts()
    counts[survey_type] += 1
    save_counts(counts)


@app.route('/')
def index():
    """首頁 - 顯示說明"""
    counts = load_counts()
    return jsonify({
        "message": "問卷隨機分派系統 - 公平分派版本",
        "usage": "訪問 /survey 來獲得隨機分派的問卷",
        "distribution_method": "平衡分派 - 自動確保兩份問卷數量相近",
        "surveys": {
            "hotel": "飯店問卷",
            "medical": "醫療問卷"
        },
        "current_distribution": {
            "hotel": counts["hotel"],
            "medical": counts["medical"],
            "total": counts["hotel"] + counts["medical"]
        }
    })


@app.route('/survey')
def random_survey():
    """平衡分派問卷並重定向"""
    survey_type = get_balanced_survey()
    survey_url = SURVEYS[survey_type]
    
    # 記錄分派結果
    increment_survey_count(survey_type)
    app.logger.info(f"Assigned survey: {survey_type}")
    
    return redirect(survey_url)


@app.route('/survey/info')
def survey_info():
    """顯示將被分派的問卷資訊（不重定向）"""
    survey_type = get_balanced_survey()
    
    return jsonify({
        "survey_type": survey_type,
        "survey_name": "飯店問卷" if survey_type == "hotel" else "醫療問卷",
        "survey_url": SURVEYS[survey_type]
    })


@app.route('/survey/stats')
def stats():
    """顯示分派統計"""
    counts = load_counts()
    total = counts["hotel"] + counts["medical"]
    
    return jsonify({
        "total_assigned": total,
        "hotel": {
            "count": counts["hotel"],
            "percentage": round(counts["hotel"] / total * 100, 1) if total > 0 else 0
        },
        "medical": {
            "count": counts["medical"],
            "percentage": round(counts["medical"] / total * 100, 1) if total > 0 else 0
        }
    })


@app.route('/survey/reset')
def reset_stats():
    """重置統計（需謹慎使用）"""
    save_counts({"hotel": 0, "medical": 0})
    return jsonify({"message": "統計已重置"})


@app.route('/survey/<survey_type>')
def specific_survey(survey_type):
    """訪問特定問卷"""
    if survey_type not in SURVEYS:
        return jsonify({"error": "問卷類型不存在"}), 404
    
    increment_survey_count(survey_type)
    return redirect(SURVEYS[survey_type])


@app.route('/health')
def health():
    """健康檢查端點"""
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0')
