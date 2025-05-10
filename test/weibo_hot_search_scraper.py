import requests
from bs4 import BeautifulSoup
import json

def get_weibo_hot_search():
    """
    爬取微博热搜榜并返回结果列表。
    """
    url = "https://s.weibo.com/top/summary/"
    headers = {
        # 模拟浏览器发送请求
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie": "SUB=_2AkMRX9exf8NxqwJRmfEcxVnlboV-zzDEieKlMyjXJRMyHRl-yD9jqhAHtRB6A7CVZDpSUnEYh1T2LNB7cQ4xZ7g7kS8Z;" # 请替换成你自己的有效Cookie
    }
    hot_searches = []

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 如果请求失败则抛出HTTPError错误
        response.encoding = response.apparent_encoding # 解决乱码问题

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 微博热搜榜的条目通常在 'tr' 标签中，并且有一个特定的类名或者在某个特定的 table/tbody下
        # 注意：微博的页面结构可能会变化，这里的选择器需要根据实际情况调整
        # 通过观察网页源码，热搜条目在 id="pl_top_realtimehot" 下的 tbody > tr
        
        # 查找包含热搜的表格或列表区域
        # 2024年6月观察，热搜条目在 `div#pl_top_realtimehot table tbody tr`
        # 标题在 td.td-02 > a
        # 热度在 td.td-02 > span (部分有)
        # 链接是 td.td-02 > a 的 href 属性，需要拼接 "https://s.weibo.com"
        
        rank = 0
        for item in soup.select('div#pl_top_realtimehot table tbody tr'):
            title_tag = item.select_one('td.td-02 > a')
            
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = "https://s.weibo.com" + title_tag['href']
                
                # 尝试获取热度值
                hotness_tag = item.select_one('td.td-02 > span')
                hotness = hotness_tag.get_text(strip=True) if hotness_tag else "N/A"

                # 过滤掉置顶的广告或推广（通常没有排名数字或排名为特殊字符）
                rank_tag = item.select_one('td.td-01')
                current_rank_text = rank_tag.get_text(strip=True) if rank_tag else ""

                if current_rank_text.isdigit(): # 只取有数字排名的
                    rank = int(current_rank_text)
                    hot_searches.append({
                        "rank": rank,
                        "title": title,
                        "link": link,
                        "hotness": hotness
                    })
                elif title and not hot_searches: # 处理可能存在的第一个非数字排名的置顶热搜（如“新时代”）
                    if current_rank_text and not current_rank_text.isdigit(): # 例如置顶的"新"字标
                         hot_searches.append({
                            "rank": current_rank_text, # 或者标记为 "置顶"
                            "title": title,
                            "link": link,
                            "hotness": hotness
                        })


        # 如果没有爬取到数据，可能是Cookie失效或页面结构变化
        if not hot_searches and soup.select_one('div.login_box'):
             print("检测到登录页面，Cookie可能已失效或需要更新。")
        elif not hot_searches:
            print("未能爬取到热搜数据，可能是页面结构已更新，请检查CSS选择器。")


    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
        
    return hot_searches

if __name__ == "__main__":
    print("正在爬取微博热搜...")
    hot_topics = get_weibo_hot_search()
    
    if hot_topics:
        print("\n微博热搜榜 (详细信息):")
        for index, topic in enumerate(hot_topics, 1):
            print(f"{index}. 排名: {topic['rank']}, 标题: {topic['title']}, 热度: {topic['hotness']}, 链接: {topic['link']}")
        
        # 你也可以选择将结果保存到文件，例如 JSON 文件
        # with open("weibo_hot_search.json", "w", encoding="utf-8") as f:
        #     json.dump(hot_topics, f, ensure_ascii=False, indent=4)
        # print("\n结果已保存到 weibo_hot_search.json")

        print("\n--- 主要数据汇总 (热搜名 + 热度) ---")
        for index, topic in enumerate(hot_topics, 1):
            print(f"{index}. 热搜名: {topic['title']}, 热度: {topic['hotness']}")
            
    else:
        print("未能获取到热搜数据。")