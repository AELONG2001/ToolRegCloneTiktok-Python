def getMailContent(mail_content):
    accounts = []
    for line in mail_content.splitlines():
        if "|" in line:
            username, password = line.split("|", 1)
            accounts.append((username.strip(), password.strip()))
    return accounts
