
import pandas as pd
import requests

url = "https://www.emag.hu/search-by-url"

headers = {
    "cookie": "",
    "Accept-Language": "en-GB,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "",
    "Referer": "https://www.emag.hu/laptop-notebook/brand/dell/c?ref=hp_menu_quick-nav_1_27&type=filter",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "accept": "application/json",
    "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": 'Windows',
    "x-app-module": "Paginator",
    "x-app-name": "photon-static",
    "x-request-source": "www",
    "x-requested-with": "XMLHttpRequest"
}

results = []
for page in range(1, 5):
    pagination = ''
    if page != 1:
        pagination = f"/p{page}"
    querystring = {"source_id": "7", "templates[]": "full", "is_eab344": "false", "sort[popularity_listing]": "desc",
                   "listing_display_id": "2", "page[limit]": "100", "page[offset]": "0",
                   "fields[items][image_gallery][fashion][limit]": "2", "fields[items][image][resized_images]": "1",
                   "fields[items][resized_images]": "720x720", "fields[items][flags]": "1",
                   "fields[items][offer][buying_options]": "1", "fields[items][offer][flags]": "1",
                   "fields[items][offer][bundles]": "1", "fields[items][offer][gifts]": "1",
                   "fields[items][characteristics]": "listing", "fields[quick_filters]": "1", "search_id": "",
                   "search_fraze": "", "search_key": "", "url": f"/laptop-notebook/brand/dell{pagination}/c"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    for item in data['data']['items']:
        results.append(item)

df = pd.json_normalize(results)

df.to_csv('results.csv')
