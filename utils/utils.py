import random
import string
from time import sleep
import os
import shutil

def random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def wait(min_time, max_time):
    delay = random.uniform(min_time, max_time)
    sleep(delay)

def generate_random_name(length=10):
    characters = string.ascii_letters + string.digits
    
    random_name = ''.join(random.choices(characters, k=length))
    
    return random_name

def generate_password():
    # Dãy ký tự chứa các chữ in hoa, chữ thường, số và ký tự đặc biệt
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "@"  # Chọn ký tự đặc biệt là '@' hoặc '.'

    # Tạo một mật khẩu ngẫu nhiên có ít nhất một ký tự của mỗi loại
    password = (
        random.choice(uppercase_letters) +
        random.choice(lowercase_letters) +
        random.choice(digits) +
        random.choice(special_characters)
    )

    # Hoàn thành mật khẩu với 4 ký tự ngẫu nhiên khác
    remaining_characters = (
        uppercase_letters + lowercase_letters + digits + special_characters
    )

    for _ in range(4):
        password += random.choice(remaining_characters)

    # Trộn các ký tự để tạo một mật khẩu cuối cùng
    password_list = list(password)
    random.shuffle(password_list)
    password_account = ''.join(password_list)

    return password_account

def delete_all_subfolders(parent_folder):
    subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]

    for subfolder in subfolders:
        try:
            shutil.rmtree(subfolder)
            print(f'Thư mục con {subfolder} đã được xóa.')
        except Exception as e:
            print(f"Không thể xóa thư mục con {subfolder}. Lỗi: {e}")