import json
import os
from datetime import datetime


def write_json(file_name, data):
    """ファイル名と辞書型を受け取り、JSON形式で保存する。

    一時ファイルに書いてから置き換えるため、書き込み中に止まっても
    保存済みのファイルが壊れにくくなります。
    """
    if not isinstance(data, dict):
        raise TypeError("data は辞書型（dict）を指定してください")

    temp_name = file_name + ".tmp"
    with open(temp_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    os.replace(temp_name, file_name)


def read_json(file_name):
    """ファイル名を受け取り、JSONファイルを辞書型で返す。

    ファイルがまだ無い場合は、初回起動用に空の辞書 {} を返します。
    """
    if not os.path.exists(file_name):
        return {}

    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise TypeError(f"{file_name} の中身が辞書型ではありません")
    return data


if __name__ == "__main__":
    file_name = "account.json"

    # アカウント番号をキーにして、複数人分を保存する例
    accounts = read_json(file_name)
    print("読み込み:", accounts)

    if "A001" not in accounts:
        accounts["A001"] = {"visits": 0, "history": []}

    accounts["A001"]["visits"] += 1
    accounts["A001"]["history"].append(datetime.now().astimezone().isoformat(timespec="seconds"))

    write_json(file_name, accounts)

    loaded_data = read_json(file_name)
    print("保存後:", loaded_data)
    print("A001の来場回数:", loaded_data["A001"]["visits"])
