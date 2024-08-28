# 定义请求头部
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'Content-Type': 'application/json',
    'Cookie': 'LF_ID=c674524-4bb6910-3a5751c-2546032; GCID=e0ae0bf-acfc951-9139342-f30208b; GRID=e0ae0bf-acfc951-9139342-f30208b; GCESS=BgsCBgAEBACNJwAFBAAAAAAKBAAAAAABCHaiJAAAAAAACQEBBwRoNHMsDAEBCAEDDQEBAgRYn7VmBgSLnPJgAwRYn7Vm; tfstk=fzDxgz1-NUYciJOihmOuITiKggxkZxn4wqoCIP4c143-SVk0oomgfb3IJj2D_IlOWz3zjq2jSVQto40T_nzg5P3ifjxkKpmq0Ry1BevHK0uA-hgTcR6fFhZ3fN6EtyHK0Ry6rkiuE0oqJHLR7Ie628ZgDlw_1Ot8Vl45hl6bfat8bza_CS6jVTZQbNa_ltGVXFU5cPXt1mMrI_C8CO6shRPbJE474ok8DSUBLzBsDYEYMyij3DQmfuMoeWVljU2SYb0b2JpA8ohSv-ZtQH1TW5H4ez3pdOrrGqH76Yxwdm2YXWw_wG6s28UzNxwBdaErNmcs3qIOCokmK5UUwh6as8M3OXgAbHo7hlgaTAYF3risYvl3pKQUDbiLegyxKvHYawXBSstJ215aGufB6TbkbJU4RuUHDdCN_7-z2yxJ215aGur8-nLA_1Py4; mantis5539=9f6ffa3b91a04db499e16731d265778e@5539; MEIQIA_TRACK_ID=2kPIayyCUBPSeJ1gnb9m647yGWr; MEIQIA_VISIT_ID=2kPIaytyuDVPpTwBdhySUlbvqO1; _tea_utm_cache_20000743={%22utm_source%22:%22geektime_search%22%2C%22utm_medium%22:%22geektime_search%22%2C%22utm_campaign%22:%22geektime_search%22%2C%22utm_term%22:%22geektime_search%22%2C%22utm_content%22:%22geektime_search%22}; gksskpitn=426c2ca1-9677-4140-9d3c-ee89f00b7290; __tea_cache_tokens_20000743={%22web_id%22:%227400996621225687819%22%2C%22user_unique_id%22:%222400886%22%2C%22timestamp%22:1724850249595%2C%22_type_%22:%22default%22}; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1724850250|1724850248'
}
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
r = requests.post('https://time.geekbang.org/serv/v4/pvip/product_list', headers=headers, json=data)
datas = r.json()
name = datas['data']["info"][0]["author"]["name"]
print(name)
