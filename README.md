# Russian Dirt Tongue  
## About
Модуль направлен на поиск русской ненормативной лексики в тексте.

Поиск слов происходит только с помощью регулярных выражений, в модуль заложен 
словарь плохих слов, но также можно создать свой.

## Usage

**Поиск стандартных слов:**

```python
>>>from dirt_tongue import is_dirt
>>>detector = is_dirt()
>>>detector("текст с матом")
True
>>>detector("текст")
False
```

**Поиск своих слов:**
```python
>>>from dirt_tongue import is_dirt
>>>detector = is_dirt("навальн|путин")
>>>detector("остро-политический текст")
True
>>>detector("текст")
False
```

## Installation

```bash
$ pip install dirt_tongue
```

## ToDo  
Модуль разрабатывался только для фильтрации сообщений, поэтому остаётся ещё несколько 
задач:
* Замена матерных слов
* Поиск всех матерных слов
* Создание и подключение словарей
* Что-нибудь ещё, что всплывёт в ходе использования
