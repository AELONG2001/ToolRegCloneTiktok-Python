def readMailFile(file_path):
    with open(file_path, "r") as file:
        mail_content = file.read()
        return mail_content
