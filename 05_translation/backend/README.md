## 仮想環境の作成

```sh
cd ./05_translation/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 翻訳関数のテスト

```sh
python3 translation.py
```

## 翻訳APIのテスト

```sh
python3 api.py
```

新しいターミナル

```sh
cd ./05_translation/backend
source venv/bin/activate
python3 api_test.py
```