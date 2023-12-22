## 仮想環境の作成

```sh
cd ./06_chat/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## チャット関数のテスト

```sh
python3 chat.py
```

## チャットAPIのテスト

```sh
python3 api.py
```

新しいターミナル

```sh
cd ./06_chat/backend
source venv/bin/activate
python3 api_test.py
```