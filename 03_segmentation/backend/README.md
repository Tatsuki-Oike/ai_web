## 仮想環境の作成

```sh
cd ./03_segmentation/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## セグメンテーション関数のテスト

```sh
python3 segmentation.py
```

## セグメンテーションAPIのテスト

```sh
python3 api.py
```

新しいターミナル

```sh
cd ./03_segmentation/backend
source venv/bin/activate
python3 api_test.py
```