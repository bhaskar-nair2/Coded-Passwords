import hashlib
class data:
    def __init__(self,username,password):
        self.username=username
        self.hash=self.get_hash(password)

    def get_hash(self,password):
        for _ in range(0,9999999):
            head=(str(_)+self.username+password).encode()
            i=hashlib.sha3_256(head).hexdigest()
            if(i[:4]=='0000'):
                self.num=_
                return i
    def retrive(self,password):
        head = (str(self.num) + self.username + password).encode()
        i = hashlib.sha3_256(head).hexdigest()
        if(i==self.hash):
            return True
        else:
            return False


x= data("bhaskar","hahahaha")
print(x.hash)

while True:
    passw=input("Password- ")
    print(x.retrive(passw))