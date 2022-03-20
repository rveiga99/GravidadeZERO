from faker import Faker
fake = Faker()

import bcrypt

def get_hashed_pass(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(8))
    return  hashed

def users_to_insert_db():
    return [
        factory_user('login'),
        factory_user('be_geek'),
        factory_user('short_desc'),
        factory_user('long_desc'),
        factory_user('req_fields')
    ]

def factory_user(target):
    
    data = {
        'faker': {
            'name': fake.first_name(),
            'lastname': fake.last_name(),
            'email': fake.free_email(),
            'password': '123456789qq'
        },
        'wrong_email': {
            'name': 'Pedro',
            'lastname': 'De Lara',
            'email': 'teste$gmail.com',
            'password': 'teste999'
        },
        'login': {
            'name': 'Rafael',
            'lastname': 'Veiga',
            'email':'rafael88@gmail.com',
            'password': 'rafa123'
        },
        'be_geek': {
            'name': 'Kim',
            'lastname':'Dotcom',
            'email': 'kim@dot.com',
            'password':'teste999',
            'geek_profile': {
                'whats': '11999999999',
                'desc': 'Seu computador está lento? Reiniciando do nada? Talvez seja um vírus ou algum hardware com defeito. Posso fazer a manutenção no seu PC, formatando, reinstalando o SO, trocando algum componente físico e porque não remover o baidu ou qualquer outro malware.',
                'printer_repair':'Sim',
                'work':'Remoto',
                'cost':'100'
            }
        },
        'short_desc': {
            'name': 'Kim',
            'lastname':'Dotcom Short',
            'email': 'teste_short@dot.com',
            'password':'teste999',
            'geek_profile': {
                'whats': '11999999999',
                'desc': 'Formato o seu PC',
                'printer_repair':'Sim',
                'work':'Remoto',
                'cost':'100'
            }
        },
        'long_desc': {
            'name': 'Kim',
            'lastname':'Dotcom Long',
            'email': 'teste_long@dot.com',
            'password':'teste999',
            'geek_profile': {
                'whats': '11999999999',
                'desc': 'Seu computador está lento? Reiniciando do nada? Talvez seja um vírus ou algum hardware com defeito. Posso fazer a manutenção no seu PC, formatando, reinstalando o SO, trocando algum componente físico e porque não remover o baidu ou qualquer outro malware e etc',
                'printer_repair':'Sim',
                'work':'Remoto',
                'cost':'100'
            }
        },
        'req_fields':{
            'name': 'Kim',
            'lastname':'Dotcom Fields',
            'email': 'teste_fields@dot.com',
            'password':'teste999',
            'geek_profile': {
                'whats': '11999999999',
                'desc': 'Seu computador está lento? Reiniciando do nada? Talvez seja um vírus ou algum hardware com defeito. Posso fazer a manutenção no seu PC, formatando, reinstalando o SO, trocando algum componente físico e porque não remover o baidu ou qualquer outro malware e etc',
                'printer_repair':'Sim',
                'work':'Remoto',
                'cost':'100'
            }
        }
    }
    
    return data[target]


    