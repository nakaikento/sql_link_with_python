def next_page_getter(url):
    import requests
    from bs4 import BeautifulSoup
    """URLを引数として該当ページの次のページリンクを取得する関数"""
    url_format = 'http://quotes.toscrape.com'
    # 指定したurlのページ情報を取得
    r = requests.get(url)
    # soupを取得
    soup = BeautifulSoup(r.text, 'html.parser')
    # 次のページのURLを取得
    next_page_url =  url_format + soup.find('li', class_='next').a.get('href')
    return next_page_url
