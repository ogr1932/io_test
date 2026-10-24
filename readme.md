# JSONファイル入出力

`json_file_io.py` は、PythonのデータをJSONファイルに保存し、あとから読み込むサンプルです。

## 実行方法

Python 3 がインストールされている状態で、ターミナルから次のコマンドを実行します。

```powershell
python json_file_io.py
```

実行すると、アカウント番号をキーにした辞書を `account.json` に保存し、保存した内容を読み込んで表示します。`account.json` は実行時の作業フォルダーに作られます。初めて実行するとき、ファイルがまだ無ければ空の辞書 `{}` から始めます。

## 関数の使い方

```python
from json_file_io import read_json, write_json

data = {"account_number": "A001", "visits": 3}
write_json("account.json", data)       # JSONファイルへ書き込む
loaded_data = read_json("account.json")  # JSONファイルを読み込む
print(loaded_data["visits"])             # 3
```

- `write_json(file_name, data)`: ファイル名と辞書型データを受け取り、JSONファイルに書き込みます。既存のファイルがあれば上書きします。一時ファイルに書いてから置き換えます。
- `read_json(file_name)`: ファイル名を受け取り、JSONファイルを辞書型として返します。ファイルが無ければ空の辞書 `{}` を返し、内容が辞書型でない場合はエラーになります。
- 日本語が `\uXXXX` の形にならないよう、UTF-8と `ensure_ascii=False` を使っています。

自分で全部書けるようになりたいものですね...