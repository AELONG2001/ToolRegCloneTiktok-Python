import os
import json

def handleSaveDataInputUser(kzlsfw, value):
    # Kiểm tra sự tồn tại của tệp JSON
    if os.path.exists("configs_account.json"):
        try:
            # Đọc dữ liệu từ tệp JSON hiện có
            with open("configs_account.json", "r") as json_file:
                data = json.load(json_file)
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}  # Tạo một dictionary mới nếu tệp chưa tồn tại

    data[f"{kzlsfw}"] = value

    # Ghi lại toàn bộ dictionary vào tệp JSON
    with open("configs_account.json", "w") as json_file:
        json.dump(data, json_file, indent=4)