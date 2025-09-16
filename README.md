# 起動の仕方
まず、cloneしてくる。

git clone url 

クローンしてきたら、.envを作る

.envの内容はdiscordに書いてます。

.envの準備が終わったら、dockerを起動する

起動した状態で、ターミナルを開いて

docker compose up -d

と入力すると、dbとfastapiが起動する。


# マイグレーション
modelファイルに書いたテーブルをdbに反映させる

## 手順
1.models配下にmodelを書く
2.env.pyでそのmodel classをimportしてくる
3.uv run alembic revision --autogenerate -m "マイグレーションメッセージ"
4.uv run alembic upgrade head
