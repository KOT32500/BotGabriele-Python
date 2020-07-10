# Габриэль
Габриэль это бот для Дискорд сервера, в его возможности входят как технический, так и развлекательный контент

## Возможности

* [Разговор](#dialogue)  
* [Создание голосовых комнат](#Rooms) 
* Википедия
* [Игра](#Game) 

<a name="dialogue">Разговор</a>
Габриэль имеет функции чтобы поддерживать общение
Она автоматически запоминает все слова сказанные на сервере, и уже после начинает общаться используя этот словарный запас
###### В скорем времени можно будет настроить исключительно каких каналов нужно запоминать сообщения
Разговаривает она автоматически, но если Вы вдруг решите чтобы она что либо сказала прямо сейчас, воспользуйтесь командой

![Команда G](https://i.imgur.com/QIP1G25.png)

В таком случае Габриэль скажет что либо.
Команда принимает в себя необязательный атрибут. С атрибутом Габриэль использует строго то количество слов, которые вы ей задали

![Команда G с Атрибутом](https://i.imgur.com/iaioEZO.png)

В моем случае, я поставил 5 слов, и как видим, она отправила 5 слов
(Эмоджи тоже считаются словами)

![Ответ Габриэль](https://i.imgur.com/ZIY4OEj.png)

<a name="Rooms"><h2>Создание голосовых комнат</h2></a>
Габриэль может создавать голосовые каналы, для каждого игрока, если это будет необходимо.
Но для этого вам требуется создать канал, в который когда пользователи будут заходить, их будет перекидывать на в собственные комнаты.

![Создание канала](https://i.imgur.com/Mfs0MeO.png)
![Выбор и переименовывание](https://i.imgur.com/vfuodDY.png)

После этого, когда пользователи зайдут в этот канал, им автоматически присвоиться комната, с их именем, если они до этого не переименовывали комнату

Давайте создадим первую комнату, и проверим как она работает

![Создалась комната](https://i.imgur.com/cZVhc24.png)

![Голосовая комната](https://i.imgur.com/NY4xvLD.png)

![Создалась комната](https://i.imgur.com/ptXXHUP.png)

Как видим, наша первая голосовая комната готова, её могут создать все участники.

Теперь давайте настроим комнату, делается это совершенно так же, как и обычно

![Процесс создания комнаты](https://i.imgur.com/xVvj3IV.png)
![Процесс создания комнаты](https://i.imgur.com/ANFCC9c.png)
![Процесс создания комнаты](https://i.imgur.com/ETOaNmN.png)
![Процесс создания комнаты](https://i.imgur.com/2ygHf7c.png)

Габриэль автоматически запоминает все изменения в комнате, начиная от переименовывания, заканчивая правами всех кто в ней находиться
Это означает что если вы однажды сделали так, чтобы пользователь не мог зайти в комнату, пока вы не уберете это, он никогда не сможет в неё зайти
Даже если вы создали новую комнату. Ведь новая комната = старой комнате

Если из комнаты вышли все участники, она автоматически удаляется

![Удаление комнаты](https://i.imgur.com/qmFjd0J.png)

![Удаление комнаты](https://i.imgur.com/AYqxNeR.png)

![Удаление комнаты](https://i.imgur.com/cZVhc24.png)

<a name="Game">Игра</a>
Габриэль овладает мини игрой, которой можно развлекаться, пока ожидаете друзей
#### Об игре
У игры нет сюжета, ваша единственная задача стать сильнее, побеждая Боссов и других игроков, получая новые предметы, и открывая новые таланты.

* [Обучение](#Start) 
* [Механика](#Mekaniks) 
* [Где взять золото?](#GetGold) 
* [Что такое Сила Ловкость и Интеллект?](#Whatisit) 
* [Что такое Навыки?](#TalantsIT) 

<a name="Start">Обучение</a>
У вас есть собственный профиль, о котором можно узнать все необходимое
Изначально он выглядит страшно, но его можно изменить, начиная с аватарки, заканчивая задним фоном

Чтобы Габриэль показала вам профиль, существует команда 

![Команда](https://i.imgur.com/rvh3MMu.png)

В итоге она отправит нечно похожее на это

![Профиль](https://i.imgur.com/iR6AtNZ.png)

Делается это всего 2 командами

| Команда       | Атрибут   |      Что делает     |
| ------------- |:---------:| -------------------:|
| New_Avatar    | URL       | Устанавливает аватар|
| New_BackGround| URL       | Устанавливает фон   |

<a name="Mekaniks"><h2>Механика</h2></a>
Каждое ваше сообщение добавляет вам 1 ед. опыта.
Собирая необходимое количество опыта, вы получаете уровень
Уровень повышает характеристики

Характеристики нужны чтобы побеждать боссов

![Информация о боссе ](https://i.imgur.com/GCfppvl.png)

Тут мы видим количество здоровье у босса, а так же его сложность
От сложности зависит сила предметов, которые можно получить победив босса.
Атаковать босса на ранних этапах игры опасно, ведь победить его сложно, с шанс того что победите его именно вы, ещё меньше
Поэтому изначально игрокам нужно скупить рынок, и прокачать персанажа в плане урона и здоровье, однако где взять золото?

<a name="GetGold"><h2>Где взять золото?</h2></a>
Каждое 5 ваше сообщение, дает вам 1 золотую. За них уже, можно купить необходимые характеристики в магазине.
Так же, золото можно выиграть на скачках, или побеждая боссов

<a name="Whatisit">Что такое Сила Ловкость и Интеллект?</a>

Сила : Умнажает ваш урон. Изначально сила = 1 ед.
Это означает что ваш урон не умнажается.

Ловкость : За каждую единицу ловкости, вы можете атаковать 2 раза, так же за каждые 10 ед. увеличивает награду в скачках на 10%

Интеллект : Увеличивает скорость получения навыков

<a name="TalantsIT">Что такое Навыки?</a>
Навыки это то, что усиливает вашего героя.
Они улучшаются со временем, и Интеллект поможет вам получить их быстрее
