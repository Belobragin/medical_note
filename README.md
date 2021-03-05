Тестовая задача: SQLAlchemy

Модули:
- hardcode.py :: константы. ВНИМАНИЕ: следует изменить параметры базы на используемые в соотв. среде.
- models.py :: модели
- tests_Belobragin.py :: тесты
- htask_Belobragin.py :: основной модуль
Пояснения в тексте модулей.
Для простоты модули в пакет не собирались, используется простой импорт.

Последовательность решения задачи:
1. создать базу, если не создана
2. создать таблицы в базе
3. заполнить таблицы
4. результат выполнения заданной функции

При решении сделаны следующие допущения (по пунктам):
п. 1. Модель в соответствии с п. 1 не может имет древовидную 5-ти уровневую структуру. Соответствующая модель ModelTable создана.
Для решения задачи в п. 2 - 5 добавлена модель TaskTable с 5ю доп. полями, что позволяет реализовать древовидную структуру.

п. 2. Заполнена, функция populate_tables()

п. 3:
	- Параметр depth непонятен: 
		Результатом сортировки является совокупность элементов (строк) таблицы. Возможно имелось в виду использование having?  
		Что является "прямыми потомками", если у нас одна таблица, иерархическая структура данных, один несвязанный внешний ключ и 				нет требований к содержанию полей? 			
		Непонятно.
	- Искомая функция OurSweatFoo(args), пояснения в тексте модуля htask_Belobragin


п. 4 Тесты реализованы на unittest, что для меня несколько привычнее.

Набор тестов:
1. Корректное создание базы
2. корректное создание таблиц
3. выбор корректного значения элементов
4. корректная сортировка