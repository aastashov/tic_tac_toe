# Tic Tac Toe

Игра крестики-нолики

### TODO

- [x] 🐞 Создать последовательность ходов (сейчас пользователь может ходить дважды)
- [ ] 🐞 Починить Concurrency в момент подключения к игре (Python async Lock)
- [ ] 👯 Нужно создать комнаты для большего кол-ва игр
- [ ] 🚶 Реализовать лобби и очередь подключений (Python async Queue)
- [x] ⏱️ Отображать кто сейчас ходит на доске
- [ ] 👾 CI/CD
- [ ] 💔 Тесты
- [ ] 🫙 SqLite хранилище
- [ ] 🏆 Статистика по играм
- [ ] 💅 Красивые баджики для Readme.md
- [x] 💖 Линтеры
- [ ] 🤖 Простой бот
- [ ] 💽 Сохранение игры
- [ ] 🤡 Сложный бот (ML)

### Bot
Бот знает о всех выигрышных позициях, перебирает позиции и старается поставить свой маркер на не занятую
 клетку из выигрышной позиции.

### MLBot
Пощупать ML для создания бота

### Development

Install JS packages

```shell
make install-js
```

Install Python packages

```shell
make install-python
```

Or use common install

```shell
make install
```

Build JS

```shell
make build-js
```

Run Python server

```shell
make run-dev
```

Run JS server for development without Python server.

```shell
make run-dev-js
```

Run tests

```shell
make tests
```

Run linter and formatter

```shell
make lint
make format
```