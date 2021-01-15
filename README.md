# fastapi_websocket

`docker build -t backend-api ./backend/`

`docker run --rm -d -p 8080:8080 --name backend-fast-api backend-api`


`docker build -t frontend-api ./frontend/`

`docker run --rm -d -p 8501:8501 --name frontend-streamlit frontend-api`

## TODO
ログイン認証
Authで認証する
requirements.txtで

websocketで処理結果がくるまでまつ


DB接続：firebaseに
mlflow接続

GUIテスト


mongoでkey指定して出力できるようにする
csv化してダウンロードできるようにする