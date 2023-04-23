# Soccer chat

このサイトではサッカーに関する掲示板を作ることができ、またその掲示板に対してコメントをすることができる。他にもサッカーチームに関する基本情報を見ることがきる。

レスポンシブには対応していません。
## イメージ図
- ホーム画面
![ホーム画面](https://user-images.githubusercontent.com/115523429/233838131-416398ea-66e7-4bd9-9e14-4af0febf3e20.png)
- 掲示板詳細画面
![ホーム画面](https://user-images.githubusercontent.com/115523429/233838117-efbd79b3-4df7-4ac8-939d-b8858d0bb8f5.png)
- チーム一覧画面
![ホーム画面](https://user-images.githubusercontent.com/115523429/233838106-0e2feb6e-a679-4c85-b258-06dd6e39f14a.png)
- チーム詳細画面
![ホーム画面](https://user-images.githubusercontent.com/115523429/233838113-51f87c38-f8fd-4da9-8158-0b786ee63dd3.png)
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

## ER図
![er](https://user-images.githubusercontent.com/115523429/233841887-1ba2e535-45b3-441d-a897-311722dd4f86.png)
