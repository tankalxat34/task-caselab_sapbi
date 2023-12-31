## Условие

Отдел бухгалтерского и налогового учета разрабатывает новый блок отчетов. В рамках этой задача необходимо разработать программу для автоматизированного поиска статей затрат предприятия. Статьи затрат пронумерованы (числовые значения) и организованы в иерархию. 

У каждой из статей затрат есть: 
- ее номер
- ссылка на статью-родителя
- две ссылки на статей-потомков. При этом в левой ссылке находятся статьи с меньшим номером, а в правом - с большим.

Задачи:
- Придумать алгоритм, который при вводе произвольной статьи затрат будет находить ближайшую к ней статью с бо́льшим номером. 
- Необходимо оформить алгоритм в виде технического задания к первой части задания для передачи сторонней организации на реализации.

## Запуск

1. Клонировать репозиторий
2. Запустить `interface.py` командой:

```powershell
python interface.py
```

Параметры запуска интерфейса:
1. `-g` - сгенерировать новую иерархию статей затрат в файл;
2. `-g -hard` - сгенерировать краевой случай;
3. Запуск без параметров считает существующую структуру;

## Тестирование

1. Клонировать репозиторий
2. В терминале запустить:

```powershell
python -m unittest discover tests
```

> ВНИАНИЕ! Есть трудоемкие тесты на миллионы и миллиарды! Может вылетать ошибка MemoryError