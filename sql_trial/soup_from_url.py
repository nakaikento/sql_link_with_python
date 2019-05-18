def soup_from_url(url):
    import requests
    from bs4 import BeautifulSoup
    """URLからBeautifulSoupを取得する関数"""
    # 指定したurlのページ情報を取得
    r = requests.get(url)
    # soupを取得
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
