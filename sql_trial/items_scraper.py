def items_scraper(block: 'bs4.element.Tag'):
    """bs4.element.Tagを引数にとり、名言(text), 作者(author)、タグのリスト(tag_list)を返す"""
    import re
    # 名言を抽出
    quote = block.find('span', class_='text').text
    # クォートを空文字に変換
    quote = re.sub(r'(“|”)', '', quote)
    # ダブルクォーテーションをクォートに変換
    quote = re.sub(r'"', '“', quote)
    # 作者を抽出
    author = block.find('small', class_='author').text

    return quote, author
