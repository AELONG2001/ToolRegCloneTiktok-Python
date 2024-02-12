# import requests
# import json
# from functions.transformApi.encrypt import encrypt
# from functions.transformApi.decrypt import decrypt


# def hdcklsfw(klsfw, mclsfw):
#     body = {
#         "klsfw": klsfw,
#         "mclsfw": mclsfw
#     }

#     key = b'BMGhq7VA9f2rY3Px6WdFtg5HmSUZLQeu'
    
#     json_data = json.dumps(body)
#     encrypted_data = encrypt(json_data, key)

#     req_data = {
#         "data": encrypted_data,
#     }

#     response = requests.post("https://longsoftware.vn/asdf234asdf8094awev.php", req_data).json()

#     decrypted_data = decrypt(response["data"], key)
#     return decrypted_data