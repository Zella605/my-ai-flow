import json
import time

def fetch_mock_data():
    # 模拟从 TikTok 抓取的高赞 AI 效果，现在包含了图片和链接
    current_time = int(time.time())
    new_ideas = [
        {
            "id": current_time, 
            "title": "AI 赛博佛系特效", 
            "likes": "98k", 
            "source": "TikTok", 
            "status": "pending",
            "url": "https://www.tiktok.com/@tiktok/video/7301072480679800000", # 模拟视频链接
            "imageUrl": "https://picsum.photos/400/300?random=1" # 模拟图片链接
        },
        {
            "id": current_time + 1, 
            "title": "3D 拟真纹身生成", 
            "likes": "45k", 
            "source": "Instagram", 
            "status": "pending",
            "url": "https://www.instagram.com/p/C0f90L9R3Y4/", # 模拟视频链接
            "imageUrl": "https://picsum.photos/400/300?random=2" # 模拟图片链接
        },
        {
            "id": current_time + 2, 
            "title": "情绪识别滤镜", 
            "likes": "62k", 
            "source": "TikTok", 
            "status": "pending",
            "url": "https://www.tiktok.com/@tiktok/video/7300300000000000000", 
            "imageUrl": "https://picsum.photos/400/300?random=3"
        }
    ]
    
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
            
    # 去重：只添加新的，并确保每个ID唯一
    existing_ids = {item['id'] for item in data}
    unique_new_ideas = [item for item in new_ideas if item['id'] not in existing_ids]

    data = unique_new_ideas + data
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data[:50], f, ensure_ascii=False, indent=4) # 保留最近50条

if __name__ == "__main__":
    fetch_mock_data()
    print("Successfully updated data.json with images and URLs!")
