## 仮想環境の作成

```sh
cd ./01_image_recognition/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## 画像認識関数のテスト

```sh
python3 recognition.py
```

## 画像認識APIのテスト

```sh
python3 api.py
```

新しいターミナル

```sh
cd ./01_image_recognition/backend
source venv/bin/activate
python3 api_test.py
```