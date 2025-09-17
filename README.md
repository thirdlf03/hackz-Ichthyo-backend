# 起動の仕方
1. git clone する
2. uv syncする
3. .envを作って、discordの内容をコピーする
4. uv run main.pyでmain.pyを実行

# マイグレーション
modelファイルに書いたテーブルをdbに反映させる

## 手順
1.models配下にmodelを書く
2.env.pyでそのmodel classをimportしてくる
3.uv run alembic revision --autogenerate -m "マイグレーションメッセージ"
4.uv run alembic upgrade head


