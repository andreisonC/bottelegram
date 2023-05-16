#App api_id: 25191819
#App api_hash: cdc2820167b5e479674895fd11badf97

import requests
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, pyfiglet
from colorama import init, Fore
import os, random
from time import sleep

init()

lg = Fore.LIGHTGREEN_EX
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
r = Fore.RED
n = Fore.RESET
colors = [lg, r, w, cy, ye]

def banner():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('Telegram')
    print(f'{random.choice(colors)}{banner}{n}')
    print(f' Moded by: {r}Andre :D{w}\n')


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    #print(r)
    banner()
    #print(n)
    print(lg+'[1] Adcionar nova conta'+n)
    print(lg+'[2] Filtrar todas as contas banidas'+n)
    print(lg+'[3] Lista de todas as contas'+n)
    print(lg+'[4] Deletar um conta'+n)
    #print(lg+'[5] Update your Genisys'+n)
    print(lg+'[5] Sair')
    a = int(input(f'\nEnter your choice: {r}'))
    if a == 1:
        with open('vars.txt', 'ab') as g:
            newly_added = []
            while True:
                a = int(input(f'\n{lg}Adcionar API ID: {r}'))
                b = str(input(f'{lg}Adcionar API Hash: {r}'))
                c = str(input(f'{lg}Adcionar Numero de Telefone: {r}'))
                p = ''.join(c.split())
                pickle.dump([a, b, p], g)
                newly_added.append([a, b, p])
                ab = input(f'\nDeseja adcionar mais alguma conta?[y/n]: ')
                if 'y' in ab:
                    pass
                else:
                    print('\n'+lg+'[i] Todas as contas salvaz em: vars.txt'+n)
                    g.close()
                    sleep(3)
                    clr()
                    print(lg + '[*] Fazendo login a partir de novas contas...\n')
                    for added in newly_added:
                        c = TelegramClient(f'sessão/{added[2]}', added[0], added[1])
                        try:
                            c.start()
                            print(f'n\n{lg}[+] Logando como - {added[2]}')
                            c.disconnect()
                        except PhoneNumberBannedError:
                            print(f'{r}[!] {added[2]} Foi banido! Filtre usando a opção 2')
                            continue
                        print('\n')
                    input(f'\n{lg}Aperte enter para voltar ao menu...')
                    break
        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Não há contas adcionadas ! Adcione uma e tente novamente')
            sleep(3)
        else:
            for account in accounts:
                api_id = int(account[0])
                api_hash = str(account[1])
                phone = str(account[2])
                client = TelegramClient(f'sessão\\{phone}', api_id, api_hash)
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        client.sign_in(phone, input('[+] Entre o codigo: '))
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' foi banida!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Parabens! conta não banida')
                input('\nAperte enter para voltar ao menu...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Id = a[0]
                        Hash = a[1]
                        Phone = a[2]
                        pickle.dump([Id, Hash, Phone], k)
                k.close()
                print(lg+'[i] Todas as contas banidas foram removidas!'+n)
                input('\nAperte enter para voltar ao menu...')
    elif a == 3:
        display = []
        j = open('vars.txt', 'rb')
        while True:
            try:
                display.append(pickle.load(j))
            except EOFError:
                break
        j.close()
        print(f'\n{lg}')
        print(f'API ID  |            API Hash              |    Numero')
        print(f'==========================================================')
        i = 0
        for z in display:
            print(f'{z[0]} | {z[1]} | {z[2]}')
            i += 1
        print(f'==========================================================')
        input('\nAperte enter para voltar ao menu...')

    elif a == 4:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Escolha uma conta para deletar\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[2]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Escolha uma opção: {n}'))
        phone = str(accs[index][2])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Conta deletada{n}')
        input(f'{lg}Aperte enter para voltar ao menu...{n}')
        f.close()
    elif a == 5:
        clr()
        banner()
        quit()