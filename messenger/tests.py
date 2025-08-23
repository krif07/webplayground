from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Thread


class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'password1')
        self.user2 = User.objects.create_user('user2', None, 'password2')
        self.user3 = User.objects.create_user('user3', None, 'password3')

        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(self.thread.users.count(), 2)

    def test_filter_threads_by_user(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread, threads.first())

    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertFalse(threads.exists())
        self.assertEqual(threads.count(), 0)

    def test_add_message_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hola, buenas tardes")
        message2 = Message.objects.create(user=self.user2, content="Todo OK!!")
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for message in self.thread.messages.all():
            print(f'({message.user}): {message.content}')

    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hola soy de aquí")
        message2 = Message.objects.create(user=self.user2, content="Hola yo también")
        message3 = Message.objects.create(user=self.user3, content="Hola estoy espiando")
        # user 3 is not part of the thread
        self.thread.messages.add(message1, message2, message3)
        # should be 2 not 3
        self.assertEqual(len(self.thread.messages.all()), 2)
