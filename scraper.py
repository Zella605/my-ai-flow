import json
import time

def fetch_mock_data():
    # 模拟从 TikTok 抓取的高赞 AI 效果
    new_ideas = [
        {"id": int(time.time()), "title": "AI 赛博佛系特效", "likes": "98k", "source": "TikTok", "status": "pending"},
        {"id": int(time.time())+1, "title": "3D 拟真纹身生成", "likes": "45k", "source": "Instagram", "status": "pending"}
    ]

    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = []

    data = new_ideas + data

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data[:50], f, ensure_ascii=False, indent=4) # 保留最近50条

if __name__ == "__main__":
    fetch_mock_data()
    print("Successfully updated data.json!")
