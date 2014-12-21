from django.contrib.auth.models import User

def updatePwd():
    user = User.objects.get(username="admin")
    user.set_password('123456')
    user.save()



class a(object):
    i = 0
    def __init__(self,i,j):
#         self.i = i
        self.i = i
        self.b()

    def b(self):
        self.i =3


    
c = []
c.append(1)

print c