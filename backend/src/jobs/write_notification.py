def write_notification(email: str, messsage=''):
    with open("log.txt", mode="w") as email_file:
        conteudo = f"Email: {email} - mgs: {messsage}\n"
        email_file.write(conteudo)