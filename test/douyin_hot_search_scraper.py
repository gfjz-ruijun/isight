import requests
import json

def get_douyin_hot_search():
    """
    尝试爬取抖音热搜榜并返回结果列表。
    抖音的API和页面结构变化较快，此脚本可能需要随之更新。
    """
    # 一个已知的抖音热搜API接口，可能会变化
    url = "https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/"
    # 尝试使用更通用的热榜接口
    # url = "https://aweme.snssdk.com/aweme/v1/hot/search/list/?aid=1128&version_code=100700" # 这个可能需要更多参数或签名

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        # "Accept": "application/json, text/plain, */*",
        # "Referer": "https://www.douyin.com/hot", # 有时需要Referer
    }
    hot_searches = []

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 如果请求失败则抛出HTTPError错误
        
        data = response.json()
        
        # 根据API返回的JSON结构提取数据
        # 对于 "https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/"
        if "word_list" in data:
            for item in data["word_list"]:
                title = item.get("word")
                hotness = item.get("hot_value", "N/A") # 热度值字段可能是 hot_value 或 view_count 等
                # 抖音热搜通常没有直接的链接到搜索结果页，这里可以省略或构造一个
                # link = f"https://www.douyin.com/search/{requests.utils.quote(title)}"
                
                if title:
                    hot_searches.append({
                        "title": title,
                        "hotness": hotness
                    })
        # 如果是其他API，例如 aweme.snssdk.com，其结构可能是 data -> word_list
        elif "data" in data and isinstance(data["data"], list) and data["data"] and "word" in data["data"][0]: # 这是一个非常粗略的判断
             for item in data["data"]:
                title = item.get("word")
                hotness = item.get("hot_value") or item.get("view_count", "N/A")
                if title:
                    hot_searches.append({
                        "title": title,
                        "hotness": hotness
                    })
        elif "data" in data and "word_list" in data["data"]: # 另一种可能的结构
            for item in data["data"]["word_list"]:
                title = item.get("word")
                hotness = item.get("hot_value", "N/A")
                if title:
                    hot_searches.append({
                        "title": title,
                        "hotness": hotness
                    })
        else:
            print("未能从API响应中找到预期的热搜数据结构。请检查API返回内容。")
            print("API原始返回:", response.text[:500]) # 打印部分返回内容帮助调试

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
    except json.JSONDecodeError:
        print("解析JSON响应失败。API可能返回了非JSON内容或页面结构已更改。")
        print("API原始返回:", response.text[:500])
    except Exception as e:
        print(f"发生未知错误: {e}")
        
    return hot_searches

if __name__ == "__main__":
    print("正在爬取抖音热搜...")
    hot_topics = get_douyin_hot_search()
    
    if hot_topics:
        print("\n--- 抖音热搜榜 (热搜名 + 热度) ---")
        for index, topic in enumerate(hot_topics, 1):
            print(f"{index}. 热搜名: {topic['title']}, 热度: {topic['hotness']}")
        
        # 你也可以选择将结果保存到文件
        # with open("douyin_hot_search.json", "w", encoding="utf-8") as f:
        #     json.dump(hot_topics, f, ensure_ascii=False, indent=4)
        # print("\n结果已保存到 douyin_hot_search.json")
    else:
        print("未能获取到抖音热搜数据。可能是API已更改、需要更复杂的请求头或网络问题。")