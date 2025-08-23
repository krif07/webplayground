from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.recipient} at {self.timestamp}"

    class Meta:
        ordering = ['-created']


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
   

def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None)
    print(instance, action, pk_set)

    false_pk_set = set()
    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print(f"Ups, ({msg.user}) no forma parte del hilo")
                false_pk_set.add(msg_pk)
    
    # Buscar los mensajes de false_pk_set qeu sí están en pk_set y se borran de pk_set
    pk_set.difference_update(false_pk_set)

m2m_changed.connect(messages_changed, sender=Thread.messages.through)