import random
import threading
from time import sleep


class Bank:
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            num_plus = random.randint(50, 500)
            self.balance += num_plus
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {num_plus}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            num_min = random.randint(50, 500)
            print(f'запрос на {num_min}')
            if num_min <= self.balance:
                self.balance -= num_min
                print(f'снятие: {num_min}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')