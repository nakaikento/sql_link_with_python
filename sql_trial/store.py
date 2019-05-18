def store(conn, author, quote):
    # 操作するカーソルを取得
    cur = conn.cursor(buffered=True)
    query = f"INSERT into quotes\
    (author, quote)\
    VALUES\
    (\"{author}\", \"{quote}\");"
    cur.execute(query)
    # 変更をコミットする
    conn.commit()
