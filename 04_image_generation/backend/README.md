## 仮想環境の作成

```sh
cd ./04_image_generation/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 画像生成関数のテスト

```sh
python3 generation.py
```

## 画像生成APIのテスト

```sh
python3 api.py
```

新しいターミナル

```sh
cd ./04_image_generation/backend
source venv/bin/activate
python3 api_test.py
```