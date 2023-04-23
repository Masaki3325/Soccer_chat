# Soccer chat

このサイトではサッカーに関する掲示板を作ることができ、またその掲示板に対してコメントをすることができる。他にもサッカーチームに関する基本情報を見ることがきる。

レスポンシブには対応していません。
## 使用技術

- Django 4.1
- Python 3.9
- psycopg2-binary
- django-environ
- Pillow
- googlemaps
- Docker/docker-compose
- Google Maps JavaScript API

## 機能一覧
- ユーザー登録、ログイン、ログアウト
- 掲示板作成、作成者のみ削除
- コメント
- チーム一覧、各チームのホームスタジアム場所を取得するAPI
- チームごとの投稿の表示
