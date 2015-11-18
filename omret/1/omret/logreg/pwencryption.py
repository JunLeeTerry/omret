import hashlib

class pwEncryption(object):
    def encryptionByUser(self,user):
        return encryptionByPasswd(user.password)

    def encryptionByPasswd(self,password):
        encrypted_passwd = hashlib.sha1(password).hexdigest()
        return encrypted_passwd
