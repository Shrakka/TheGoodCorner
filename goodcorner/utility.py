from .models import Announce, User
from django.utils import timezone
from django.core.mail import send_mail


# FETCH A USER IN THE DB AND IF DOES NOT EXIST, CREATE ONE
def createOrGetUser(surname, email):
    try:
        user = User.objects.get(email=email)
        user.surname = surname
    except User.DoesNotExist:
        user = User(surname=surname, email=email)
    
    user.save()
    print("userID=", user.id)
    return user

# CREATE AND SAVE AN ANNOUNCE IN DB
def createAnnounce(title, description, user):
    announce = user.announce_set.create(title=title, description=description, creation_date=timezone.now())
    print("announceID=", announce.id)
    return announce


def sendCreationMail(user, announce):
    subject = "Your announce was created with success"
    message = "Hello " + user.surname + "!\nYour announce was created with succes!\nYou can view and modify it here:\nlocalhost:8000/edit/" + str(announce.hashurl)
    author = "GoodCornerDoNotReply@django.test"
    send_mail(subject, message, author, [user.email], fail_silently=False)

def sendContactMail(email, message, announce):
    subject = "Someone is interested in your announce!"
    author = "GoodCornerDoNotReply@django.test"
    messageToSend = "Hello " + announce.user.surname + ",\nSomeone is interested in your add: \n<"+ announce.title + ">\nThis person sent you a message:\n<"+ message +">\nFeel free to contact this person at: \n<" + email
    send_mail(subject, messageToSend, 'GoodCornerDoNotReply@django.test', [announce.user.email], fail_silently=False)

def updateAnnounce(pk, newTitle, newDescription):
    Announce.objects.filter(pk=pk).update(title=newTitle, description=newDescription, creation_date=timezone.now())