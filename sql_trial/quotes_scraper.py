def quotes_scraper():

    from next_page_getter import next_page_getter
    from items_scraper import items_scraper
    from soup_from_url import soup_from_url
    from store import store
    import mysql.connector
    from urllib.parse import urlparse
    import re
    import time
    # ----------------- SQL接続、DB作成 -------------------

    # URLをパース
    url = urlparse('mysql://dbuser:4649seisho@localhost:3306/quotesDB')
    # 接続を確立
    conn = mysql.connector.connect(host=url.hostname,
                                  port = url.port,
                                  user = url.username,
                                  password = url.password,
                                  database = url.path[1:],
                                 )
    # 操作するカーソルを取得
    cur = conn.cursor(buffered=True)

    # テーブルを作成
    cur.execute("CREATE TABLE IF NOT EXISTS quotes (\
    quote_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
    author VARCHAR(30),\
    quote VARCHAR(1500))")
    conn.commit()

    # -------------- ここからスクレイピング -----------------
    next_page_url = 'http://quotes.toscrape.com'
    count = 0
    while True:
        count += 1
        print(f'{count}ページ目をクロール中...\n')

        # クローリング

        # データ取得
        # soupを取得
        soup = soup_from_url(next_page_url)
         # 名言、作者、タグが格納された情報のブロックを取得
        blocks = soup.find_all('div', class_='quote')
        # 各ブロックについて2つの項目に関する情報を取得
        for block in blocks:
            quote, author = items_scraper(block)
            # 値を表示
            print(f'author: \n{author}\n')
            print(f'quote: \n{quote}\n\n\n')
             # MySQLを実行してDBに値を流し込む
            store(conn=conn, author=author, quote=quote)

        # 次のページを取得
        try:
            # 次のページリンクを取得
            next_page_url = next_page_getter(next_page_url)
            print(next_page_url)
        # 次のページが存在しない場合、AttributeErrorが帰ってくるので、例外処理をして安全に終了
        except AttributeError as A:
            print(f'エラーメッセージ: {A}')
            print('次のページはありません')
            # while ループを抜ける
            break

        # 2秒間隔を空ける
        time.sleep(2)

    # 後始末。DBを閉じる
    # curを閉じる
    cur.close()
    # connを閉じる
    conn.close()

quotes_scraper()
