from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age
        UrTube.users[self.nickname] = self.password

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return False
class UrTube:
    users = {}
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = hash(str(password))
        if self.nickname in self.users:
            if self.password == self.users[nickname]:
                UrTube.current_user = self.nickname
            else:
                print('Неправильный пароль')

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age
        if self.nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
            # another_pass = input(f'Введите пароль для {nickname} ')     # возможность войти в аккаунт для созданного
            # self.log_in(nickname, another_pass)                         # пользователя
        else:
            self.users[self.nickname] = self.password
            self.log_in(nickname, password)

    def log_out(self):
        print(f'Вы вышли из аккаунта {self.current_user}')
        UrTube.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)
            else:
                pass

    def get_videos(self, find_word):
        found_videos = []
        for video in self.videos:
            if find_word.lower() in video.title.lower():
                found_videos.append(video)
        return found_videos

    def watch_video(self, video_name):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            if self.age >= 18:
                for video in self.videos:
                    if video.title == video_name:
                        for i in range(1, video.duration + 1):
                            print(i, end=' ')
                            sleep(1)
                        print('Конец видео')
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
