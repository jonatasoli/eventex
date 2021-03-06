from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Jonatas Oliveira', cpf='12345678901',
                email='jonatas@oliveira.com.br', phone='11-98765-4321')
        self.resp =  self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'jonatas@oliveira.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
                'Jonatas Oliveira',
                '12345678901',
                'jonatas@oliveira.com.br',
                '11-98765-4321',
                ]

        for content in contents:
            with  self.subTest():
                self.assertIn(content, self.email.body)
