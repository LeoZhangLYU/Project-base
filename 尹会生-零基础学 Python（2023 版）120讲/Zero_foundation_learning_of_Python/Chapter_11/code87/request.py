import requests

# 定义请求头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'Content-Type': 'application/json',
}

# 定义请求数据
data = {
    "tag_ids": [
        12
    ],
    "product_type": 0,
    "product_form": 0,
    "pvip": 0,
    "prev": 0,
    "size": 20,
    "sort": 8,
    "with_articles": True
}

# 发送 POST 请求
r = requests.post('https://time.geekbang.org/serv/v4/pvip/product_list', headers=headers, json=data)

# 检查请求是否成功
if r.status_code == 200:
    datas = r.json()
    name = datas['data']["info"][0]["author"]["name"]
    print(name)
else:
    print(f"请求失败，状态码: {r.status_code}")
