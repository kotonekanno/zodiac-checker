Read this in English: [README.md](READM.md)

# 星座判定アプリ

### 目次

- [概要](#概要)
- [実行方法](#実行方法)
  - [必要環境](#必要環境)
  - [Windows](#windows)
  - [macOS / Linux](#macos--linux)
- [ディレクトリ構成](#ディレクトリ構成)

## 概要

誕生日を入力することで星座を判定できる、簡単なWebアプリです。
PythonとFlaskを使って作成しており、ブラウザからアクセスできます。
PythonやWebアプリの練習用として作成しました。

## 実行方法

### 必要環境

- Python 3.10以上
- pip（Pythonに付属のパッケージ管理ツール）

### Windows

1. Pythonをインストール

   - [公式サイト](https://www.python.org/downloads/)から最新のPythonをダウンロードしてインストール
   - インストール時に"**Add Python to PATH**"にチェックを入れること

2. リポジトリをクローン

  ```powershell
  git clone https://github.com/kotonekanno/zodiac-checker
  cd zodiac-checker
  ```

3. 仮想環境を作成

  ```powershell
  py -m venv venv
  .\venv\Scripts\activate
  ```

4. Flaskをインストール

  ```powershell
  pip install flask
  ```

5. アプリを起動

  ```powershell
  py app.py
  ```

1. ブラウザでhttp://127.0.0.1:5000を開く


### macOS / Linux

1. Pythonをインストール
   - [公式サイト](https://www.python.org/downloads/)から最新のPython3をダウンロードしてインストール

2. リポジトリをクローン

  ```bash
  git clone https://github.com/kotonekanno/zodiac-checker
  cd zodiac-checker
  ```

3. 仮想環境を作成

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

4. Flaskをインストール

  ```bash
  pip install flask
  ```

5. アプリを起動

```bash
python app.py
```

1. ブラウザで(http://127.0.0.1:5000)を開く


## ディレクトリ構成

```
zodiac-checker/
├── static/          # 画像とCSS
├── templates/       # HTMLテンプレート
│   └── index.html  
├── app.py           # メインアプリ
├── README.en.md     
└── README.ja.md     # このファイル
```