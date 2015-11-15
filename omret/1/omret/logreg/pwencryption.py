class pwEncryption():
    def encryptionByUser(user):
        return encryptionByPasswd(user.password)

    def encryptionByPasswd(password):
        encrypted_passwd = hashlib.sha1(password)
        return encrypted_passwd
