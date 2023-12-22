## 仮想環境の作成

```sh
cd ./02_object_detection/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 物体検出関数のテスト

```sh
python3 detection.py
```

## 物体検出APIのテスト

```sh
python3 api.py
```

新しいターミナル

```sh
cd ./02_object_detection/backend
source venv/bin/activate
python3 api_test.py
```