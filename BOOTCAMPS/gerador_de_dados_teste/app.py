from asyncore import write
from fileinput import close
from posixpath import split
import random

class app():
    def __init__(self):
        self.list_names = ['joao','italo','jairo','adriao','lucas']
        self.list_phones = ['123456789','987654321','219327625','120984734','209878765']
        self.list_emails = ['teimuraz4891@uorak.com','ernesta4866@uorak.com','leszek9739@uorak.com','arquimedes40@uorak.com','jalisa4549@uorak.com']
        self.list_cities = ['camaragibe','recife','limoeiro','caruaru','carpina']
        self.list_states = ['sao paulo','rio de janeiro','pernambuco','mato grosso','amazonas']

    def outdoor(self):
        print('Escolha uma ou mais opcoes abaixo, separando-as por virgula, a serem geradas aleatoriamente ')
        print('[1]Nome \n[2]E-mail \n[3]Telefone \n[4]Cidade \n[5]Estado')

    def get_choice(self):
        choice = input(str('Escolha uma das opcoes acima:'))
        return choice

    def get_choice_archive(self):
        choice = input(str('Deseja salvar os dados em um arquivo ? (s/n):'))
        if choice == 's':
            return True
        else:
            return False

    def randomizer(self,choices: list):
        choice = random.choice(choices)
        return choice

    def set_choice(self,choice):
        list_choices = choice.split(',')
        if '1' in list_choices:
            self.name = self.randomizer(self.list_names)
        else:
            self.name = ''
        if '2' in list_choices:
            self.email = self.randomizer(self.list_emails)
        else:
            self.email = ''
        if '3' in list_choices:
            self.phone = self.randomizer(self.list_phones)
        else:
            self.phone = ''
        if '4' in list_choices:
            self.city = self.randomizer(self.list_cities)
        else:
            self.city = ''
        if '5' in list_choices:
            self.state = self.randomizer(self.list_states)
        else:
            self.state = ''
        return self.name,self.email,self.phone,self.city,self.state

    def printer(self,outputs,archive):
        print('Os dados gerados foram:')
        for i in outputs:
            if i == '':
                pass
            else:
                print(i)
                if archive:
                    self.save_archive(i)
                

    def save_archive(self,datas):
        with open('dados.txt','a') as dados:
            dados.write(datas + '\n')

    def initializer(self):
        while True:
            self.outdoor()
            choice = self.get_choice()
            if choice == 'parar':
                break
            archive = self.get_choice_archive()
            outputs = self.set_choice(choice)
            self.printer(list(outputs),archive)

app = app()
app.initializer()