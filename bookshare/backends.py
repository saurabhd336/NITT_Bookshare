import imaplib
from django.contrib.auth.models import User
from bookshare.models import Student

class MyBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            temp = imaplib.IMAP4("webmail.nitt.edu")
            temp.login(username, password)
            try:
                user = User.objects.get(username = username)
                new_student = Student.objects.get(user = user)
            except User.DoesNotExist:
                user = User(username = username, password = 'nope')
                user.save()
                new_student = Student(user = user)
                new_student.save()
            return new_student
        except Exception, e:
            print e
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id).student
        except User.DoesNotExist:
            return None