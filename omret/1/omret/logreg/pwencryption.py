import hashlib

class pwEncryption(object):
    def encryptionByPasswd(self,password):
        encrypted_passwd = hashlib.sha1(password).hexdigest()
        return encrypted_passwd

