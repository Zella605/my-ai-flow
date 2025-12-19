import json
import requests
import os
import time

def fetch_tiktok_trends():
    # 1. 从 GitHub Secrets 安全读取 API Key
    api_key = os.getenv("RAPIDAPI_KEY")
    if not api_key:
        print("Error: RAPIDAPI_KEY not found in environment secrets.")
        return

    # 2. 配置 API 请求 (使用 RapidAPI 上的常用 TikTok 数据接口)
    # 搜索关于 'AI Filter' 或 'AI Effect' 的最新高赞视频
    url = "https://tiktok-all-in-one.p.rapidapi.com/search"
    querystring = {"keywords": "AI Filter Effect", "count": "12"}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "tiktok-all-in-one.p.rapidapi.com"
    }

    try:
        print("🚀 Connecting to TikTok API...")
        response = requests.get(url, headers=headers, params=querystring, timeout=15)
        response.raise_for_status()
        res_data = response.json()
        
        # 3. 结构化解析数据
        # 兼容不同 API 的返回格式，提取视频列表
        raw_videos = res_data.get("data", [])
        if not raw_videos and "items" in res_data: raw_videos = res_data.get("items", [])

        real_ideas = []
        for v in raw_videos:
            # 提取核心字段：视频ID、描述、点赞、作者、封面
            video_id = v.get("video_id") or v.get("aweme_id")
            author_name = v.get("author", {}).get("unique_id") or v.get("author", {}).get("nickname", "Creator")
            
            real_ideas.append({
                "id": str(video_id),
                "title": v.get("desc") or v.get("title") or "Trending AI Effect",
                "likes": format_likes(v.get("statistics", {}).get("digg_count", 0)),
                "source": "TikTok",
                "url": f"https://www.tiktok.com/@{author_name}/video/{video_id}",
                "imageUrl": v.get("video", {}).get("cover", {}).get("url_list", [""])[0] or v.get("cover_data", {}).get("dynamic_1", ""),
                "status": "pending",
                "type": "hotspot",
                "timestamp": int(time.time())
            })

        # 4. 写入文件
        if real_ideas:
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(real_ideas, f, ensure_ascii=False, indent=4)
            print(f"✅ Success! Captured {len(real_ideas)} real AI trends.")
        else:
            print("⚠️ No data found in API response. Check keywords or API quota.")

    except Exception as e:
        print(f"❌ Scraper failed: {str(e)}")

def format_likes(count):
    """格式化数字，如 1200000 变为 1.2M"""
    try:
        num = int(count)
        if num >= 1000000: return f"{num/1000000:.1f}M"
        if num >= 1000: return f"{num/1000:.1f}K"
        return str(num)
    except:
        return "0"

if __name__ == "__main__":
    fetch_tiktok_trends()
