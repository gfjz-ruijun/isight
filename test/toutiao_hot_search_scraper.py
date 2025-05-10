import requests
import json

def get_toutiao_hot_search():
    """
    尝试爬取今日头条热榜数据。
    头条的API和页面结构变化较快，此脚本可能需要随之更新。
    """
    # 一个常用的今日头条热榜API接口
    url = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc"
    # 备选或旧版API，可能已失效:
    # url = "https://i.snssdk.com/hotboard/feed? કોઈ特定参数"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01", # 明确接受JSON
        "Referer": "https://www.toutiao.com/", # 有时需要Referer
    }
    hot_searches = []

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # 根据API返回的JSON结构提取数据
        # 对于 "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc"
        # 数据通常在 'data' 键下
        if "data" in data and isinstance(data["data"], list):
            for item in data["data"]:
                title = item.get("Title")
                hotness_label = item.get("HotValue", "N/A") # 热度值，可能带有单位如 "万"
                # 头条热搜的链接通常是其内容页
                # link = item.get("Url") 
                
                if title:
                    hot_searches.append({
                        "title": title,
                        "hotness": hotness_label 
                        # "link": link
                    })
        else:
            print("未能从API响应中找到预期的热搜数据结构 ('data' 列表)。请检查API返回内容。")
            print("API原始返回:", response.text[:500])

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
    except json.JSONDecodeError:
        print("解析JSON响应失败。API可能返回了非JSON内容或页面结构已更改。")
        print("API原始返回:", response.text[:500])
    except Exception as e:
        print(f"发生未知错误: {e}")
        
    return hot_searches

if __name__ == "__main__":
    print("正在爬取今日头条热搜...")
    hot_topics = get_toutiao_hot_search()
    
    if hot_topics:
        print("\n--- 今日头条热搜榜 (热搜名 + 热度标签) ---")
        for index, topic in enumerate(hot_topics, 1):
            print(f"{index}. 热搜名: {topic['title']}, 热度: {topic['hotness']}")
        
        # 你也可以选择将结果保存到文件
        # with open("toutiao_hot_search.json", "w", encoding="utf-8") as f:
        #     json.dump(hot_topics, f, ensure_ascii=False, indent=4)
        # print("\n结果已保存到 toutiao_hot_search.json")
    else:
        print("未能获取到今日头条热搜数据。可能是API已更改、需要更复杂的请求头或网络问题。")