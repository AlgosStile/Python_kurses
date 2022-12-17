
**Методы** и **Описание**
==============================================

**Базовые команды Python**
>## pip
>>Менеджер пакетов Python. Команда pip install используется для установки 
любого программного пакета из онлайн-репозитория общедоступных пакетов 
или Индекса пакетов Python (PyPI, Python Package Index).

pip install имя-пакета

>## print
>>Команда для печати сообщений на экране или другом стандартном устройстве
вывода. Команда print может использоваться для печати любого типа 
объекта — целого числа, строки, списка, кортежа и других.

print(объект)
>## class
>>Команда для создания классов. 
Python поддерживает объектно-ориентированное программирование
и позволяет пользователям создавать классы и инициализировать объекты. 
Класс может состоять из переменных с модификаторами доступа, 
функций с возвращаемыми типами и даже других классов (вложенный класс). 
Синтаксис выглядит class так:

>## type
>>Команда для проверки типа или класса объекта.

type(объект)
>## range
>>Команда для генерации последовательности целых чисел, начиная с 0 по 
умолчанию и заканчивая n, где n не включено в сгенерированные числа. 
Эта команда в основном используется в циклах for.

range(start, stop, step)

В приведенном синтаксисе:

* start — начало диапазона (опционально; по умолчанию — 0);
* stop — номер, перед которым нужно остановиться (обязательно);
* step — счетчик приращений (опционально; по умолчанию — 1).

>>Важно. Если функции range() будут даны только два параметра, она всегда 
будет рассматривать их как (start, stop), а не как (stop, step).

>## round
>>Команда для округления числа до заданной точности в десятичных разрядах. 
Позволяет сократить количество цифр после запятой в числе с плавающей 
запятой до указанного значения.

round(number, digits)
В приведенном синтаксисе:

* number — число с плавающей запятой;
* digits — количество цифр после десятичной точки (опционально; 
по умолчанию — 0).
>## input
>>Команда для получения ввода от пользователя. Исполнение программы будет 
остановлено до тех пор, пока пользователь не введет какое-либо значение, 
которое будет преобразовано функцией input() в строку. Если в качестве 
входных данных нужно взять целое число, его нужно преобразовать явно.

>## def
>>Команда определения функции Python дает возможность оборачивать повторно 
используемый код внутри функций, чтобы вызваны его позже, когда это 
необходимо. Функция def позволяет свести к минимуму избыточность кода.

def имя_функции (параметры):
"""строка документации"""
состояние(я)
>## len
>>Команда len или функция len() используются для подсчёта количества 
> элементов в объекте. Если объект является строкой, то функция len() 
> возвращает количество присутствующих в ней символов. 
> Если объект представляет собой список или кортеж, он вернет количество 
> элементов, присутствующих в этом списке или кортеже. 
> При попытке передать len() целочисленное значение, функция выдает ошибку.



## Циклические команды
>>В Python есть две простейшие команды цикла (loop commands) — 
**while** и **for**. 
>>* Команда while используется для выполнения набора операторов, 
если заданное условие истинно.
*while condition:
statements
update iterator*
>>* Команда цикла for используется для выполнения набора операторов путем 
повторения последовательности. Эта последовательность может быть списком, 
кортежем, строкой, словарем и т. д.

*for x in sequence:
statements*
## Команды Python среднего уровня
### Строковые команды
Наиболее важные функции и методы строк в Python — 
* isalnum(), 
* capitalize(), 
* find(), 
* count() 
* center().

>## isalnum()
>>Команда isalnum() проверяет, являются ли все символы данной строки 
буквенно-цифровыми или нет. Он возвращает логическое значение.

stringname.isalnum()
>## capitalize()
>>Строковая функция capitalize() возвращает строку, изменяя ее первый символ 
на верхний регистр, а остальные переводя в нижний. Если первый символ уже в 
верхнем регистре, а также представляет собой целое число или любой 
специальный символ, команда ничего не делает.

stringname.capitalize()
>## find()
>>Команда find() используется для поиска подстроки в строке. 
Если таковая найдена, find() возвращает индекс первого вхождения подстроки, 
в противном случае возвращает -1.

string.find(substring)
В приведенном синтаксисе:

* string — строка, где будет выполняться поиск.
* substring — подстрока, значение которой нужно найти.
* 
>## count()
>>Строковая функция count() возвращает количество вхождений подстроки 
в строковый объект.

stringname.count(substring, start, end)
В приведенном синтаксисе:

* stringname — строка, где будет выполняться поиск.
* substring — подстрока, значение которой нужно найти.
* start — начальный индекс в строке, с которого начинается поиск (опционально).
* end — конечный индекс в строке, где заканчивается поиск (опционально).

>## center()
>>Команда center() используется для выравнивания строки по центру с 
заполнением указанным символом.

string.center(length, character)
В приведенном синтаксисе:

* string — строка, которую нужно выровнять по центру.
* length — полная длина новой строки.
* character — символ для заполнения пропущенного места 
с каждой стороны. По умолчанию — « » (пробел).

## Команды для объектов списка
Списки используются для хранения нескольких элементов с различными 
типами данных в одном объекте. Наиболее важные методы списков 
Python — append(), copy(), insert(), pop(), reverse() и sort().

>## append()
>>Команда списка append() используется для добавления элемента 
в конец списка.

list.append(element)
В приведенном синтаксисе:

* list — объект списка, в который нужно добавить элемент.
* element — новый элемент, который добавляется в список.
>## copy()
>>Команда copy() создает новую копию объекта списка. Она возвращает 
новый объект списка.

list.copy()
>## insert()
Команда insert() добавляет элемент в указанное место в объекте списка.

listname.insert(position, element)
В приведенном синтаксисе:

* position — позиция, в которую нужно вставить новый элемент. 
Если указанная позиция превышает количество элементов в списке, 
* элемент будет 
вставляться в конец.
* element — новый элемент, который необходимо добавить.

>## pop()
>>Метод pop() используется для удаления элемента из указанной позиции 
> в списке. 
Он возвращает элемент после удаления его из списка.

listname.pop(position)
В приведенном синтаксисе: position — позиция откуда нужно удалить элемент.

>## reverse()
>>Метод reverse() изменяет порядок всех элементов в списке. Команда 
> изменяет 
исходный объект списка и ничего не возвращает.
> 
list.reverse()

>## sort()
Метод sort() по умолчанию используется для сортировки элементов списка 
в порядке возрастания.

list.sort()
## Команды кортежа
>>Кортеж (tuple) — встроенный тип данных, который используется 
для хранения нескольких элементов в одной переменной. 
Объекты кортежа упорядочены и неизменны. В Python есть два встроенных
метода кортежа — count() и index().

>## count()
>>Метод count() используется для подсчета вхождений элемента в кортеже.

tuple.count(элемент)
>## index()
>>Метод index() используется для поиска индекса первого вхождения 
> элемента. Если элемент не найден во всем кортеже, будет выведена 
> ошибка «ValueError».

tuple.index(элемент)
## Продвинутые команды Python
### Команды множества
Встроенный тип множество (set) в Python используется для хранения 
нескольких элементов в одном объекте. Этот тип объектов не допускает 
дублирования или изменения элементов, только добавление новых или удаление
существующих.
Множества неупорядочены и неиндексированы, поэтому при попытке отобразить
все элементы set, они будут выведены в случайном порядке.

>## add()
>>Команда add() позволяет добавить новый элемент в множество.
setname.add(element)
В приведенном синтаксисе:

* setname — имя переменной set, в которую нужно добавить новый элемент.
* element — элемент, который необходимо добавить.
>## clear ()
>>Функция clear () удаляет все элементы set. Она не принимает никаких 
параметров.

setname.clear()
>## discard()
Команда discard() позволяет удалить указанный элемент из набора. 
Если элемент не найден в наборе, она не выдаст ошибку.

setname.discard(element)
В приведенном синтаксисе:

* setname — имя переменной set, из которой нужно удалить элемент.
* element — элемент, который необходимо удалить.

>## remove()
>>Команда remove() также используется для удаления указанного элемента 
из множества. От команды discard() она отличается сообщением об ошибке, 
которое выводится, если указанный элемент не найден.

setname.remove(element)
В приведенном синтаксисе:

* setname — имя переменной множества, из которой нужно удалить элемент.
* element — элемент, который необходимо удалить.

>## difference()
>>Метод difference() используется для получения множества, 
содержащего разность двух множеств. В нем будут только те элементы, 
которые присутствуют только в одном множестве и отсутствуют в другом. 
Например, difference() для множеств setA {1,2,3} и setB {2, 4, 6} 
будет {1,3}.

setA.difference(setB)
>## difference_update()
>>Метод difference_update() позволяет получить набор элементов, 
> которые присутствуют в первом множестве и не являются общими для обоих. 
> Это означает, что difference_update() удаляет элементы, существующие 
> в обоих множествах. Он не возвращает новый set, а просто удаляет общие 
> элементы из первого множества.

setA.difference_update(setB)
>## intersection()
>>Метод intersection() отображает множество, содержащее элементы, 
> которые существуют во всех указанных множествах.

set.intersection(set1, set2, … setn)
>## issubset()
>>Метод issubset() проверяет, все ли элементы множества setA присутствуют
> в setB. Команда возвращает логическое значение.

setA.issubset(setB)
>## symmetric_difference()
>>Метод symmetric_difference() возвращает симметричную разность двух 
> множеств, содержащую все элементы, за исключением общих.

setA.symmetric_difference(setB)
>## union()
>>Метод union() возвращает все элементы из обоих множеств, 
> кроме повторяющихся.

setA.union(setB)
>## if, elif, else
>>Эти операторы Python, также называемые операторами ветвления или 
> операторами условного управления, позволяют изменять ход выполнения 
> программы в зависимости от условий.

* Команда if оценивает выражение и, если оно истинно (true), выполняет операторы под ним.
* Команда elif (else if) предоставляет другое выражение, которое оценивается, если предыдущий оператор if возвращает отрицательное значение «false».
* Если никакие предыдущие операторы (if или elif) не возвращают положительное значение «true», вычисляется выражение, предоставленное командой else.

**Обратите внимание. В одном блоке кода может быть несколько операторов
if и elif.**

## Команды словаря
>>Словарь (dictionary) — встроенный тип объектов в Python, 
> который используется для хранения пар ключ-значение. 
> Он упорядочен, модифицируем и не допускает дублирования значения ключей.
> Среди основных встроенных методов словаря в Python 
> выделяются следующие:
 * fromkeys(), 
 * get(), 
 * items(), 
 * keys(), 
 * values(), 
 * pop(), 
 * popitem()
 * setdefault().

>## fromkeys()
>>Метод fromkeys() используется для создания словаря с указанными ключами 
> и значением.

dict.fromkeys(keys, value)
В приведенном синтаксисе:

>## keys 
>>— кортеж или список ключевых элементов.
>## value 
>>— значение, которое будет связано со всеми указанными ключами.
>## get()
>> Метод get() позволяет получить значения указанного ключа. 
Если ключ не найден в словаре, get() ничего не вернет, 
если что-то не будет указано в параметрах.

dictionary.get(key, value)

В приведенном синтаксисе:

* dictionary — имя объекта словаря, в котором нужно выполнить поиск.
* key — ключ, который нужно найти в словаре.
* value — значение, которое будет возвращено, если ключ не будет найден
* в словаре.
>## items()
>>Метод items() используется для отображения всех элементов словаря. 
> Он возвращает объект представления, который будет содержать все пары 
> ключ-значение в виде кортежей в списке. items() не принимает никаких 
> параметров.

dictionary.items()
>## keys()
>>Метод keys() используется для получения всех ключей, присутствующих
> в словаре. Он возвращает объект представления, содержащий все ключи 
> словаря в виде списка. keys() не принимает никаких параметров.

dictionary.keys()
>## values()
>>Метод values() позволяет получить всех значения в словаре. 
> Он возвращает объект представления, содержащий все значения словаря 
> в виде списка. values() не принимает никаких параметров.

dictionary.values()
>## pop()
>>Метод pop() используется для удаления пары ключ-значение из словаря путем 
указания ключа. Он возвращает значение пары ключ-значение, 
которую необходимо удалить.

dictionary.pop(ключ)
>> Команда popitem () позволяет удалить последнюю вставленную пару из словаря. Она не принимает никаких параметров. popitem () возвращает удаленную пару в виде кортежа.

>## dictionary.popitem()
>>Метод setdefault() используется для получения значения указанного ключа. Если ключ не существует, он вставит ключ со значением, переданным в качестве параметра. Если значение не будет указано, setdefault() вставит ключ со значением «None».

dictionary.setdefault(key, value)
## Магические команды IPython
 «Магические команды» (magic commands) или магические методы
 Python — одно из важнейших дополнений, сделанных к оригинальной 
 оболочке Python Shell в процессе создания ядра IPython и его 
 официальной реализации Jupyter Notebook. Эти встроенные команды 
 IPython упрощают решение задач по анализу данных с помощью Python, 
 а также обеспечивают упрощенное взаимодействие «змеиного языка» с 
 операционными системами, другими языками программирования или ядрами.

**Магические команды Python делятся на 2 типа:**

* Строчные (line magics) — обычно начинаются с символа % и работают только в одной строке, Строчные магические команды могут использоваться как выражения, а их возвращаемое значение может быть присвоено переменной.
* Ячеечные (cell magics) — обозначаются двойным префиксом %% и работают во всей ячейке. Они могут вносить произвольные изменения в получаемые входные данные, которые необязательно должны быть кодом Python.
>## %lsmagic
>>Команда, которая выводит список всех магических функций, доступных 
> на данный момент.

>## %quickref
>>Это команда-шпаргалка, похожая на %lsmagic. Он отображает краткую 
> справку со списком возможностей каждой магической функции.

>## %who
Позволяет вам увидеть список всех ранее определенных переменных. 
Вместе с %who используются 2 производные от нее магические команды:

* %whos, которая дает дополнительную информацию о каждой переменной;
* %who_ls — возвращает отсортированный список текущих переменных.
>## %xdel
>>Удаляет переменную и любые ссылки на нее из механизма IPython.

>## %time
>>Возвращает время выполнения инструкции или выражения Python. 
Эту команду можно использовать для измерения времени необходимого среде 
IPython для выполнения выражения Python.

>## %pinfo
>>Эта волшебная команда Jupyter Notebook позволяет получить информацию
> об объекте.

>## %run
>>Функция запускает файл Python как программу в Jupyter Notebook. 
> Это может быть особенно полезно, если нужно применить функции, 
> хранящиеся во внешних файлах Python.

%run [имя файла]
В приведенном синтаксисе аргумент «имя файла» должен быть либо 
скриптом Python (с расширением .py), либо файлом с пользовательским 
синтаксисом IPython.

>## %load
>>Волшебная функция очень похожая на %run. Она загружает код файла в 
текущий интерфейс Jupyter Notebook. Источником может быть имя файла в 
каталоге используемого документа (Notebook), URL-адрес или макрос.

%load [имя файла]
В приведенном синтаксисе аргумент «имя файла» должен быть либо скриптом 
Python (с расширением .py), либо файлом с пользовательским синтаксисом 
IPython.

Более функциональным аналогом %load служит магическая команда %pycat, 
которая показывает код внешнего файла Python с подсветкой синтаксиса.

>## %%writefile
>>Копирует содержимое ячейки во внешний файл. Магическая команда полезна, 
если нужно быстро создать файл с кодом в Jupyter Notebook с помощью 
экспорта всего содержимого указанной ячейки.

Для выполнения экспорта нужно просто добавить %%writefile перед кодом. 
Команда создаст новый файл, если он не существует. В противном случае 
файл будет перезаписываться, пока после команды не будет добавлено -a.

>## %paste
>>Команда одновременно вводит и выполняет код, делая функцию готовой к 
использованию. Команда с аналогичным функционалом %cpaste открывает 
интерактивную многострочную подсказку, в которую можно вставить один 
или несколько фрагментов кода для выполнения в пакете.

### Команды рабочего каталога:
>## %pwd
>>Волшебная функция %pwd отображает текущий путь к рабочему каталогу.

>## %cd
>>Команда %cd позволяет сменить каталог, если после нее указать новый путь.
Ее можно использовать несколькими способами:

* %cd <dir> — изменяет текущий рабочий каталог на <dir>;
* % cd .. — изменяет текущий каталог на родительский;
* %cd — изменяет текущий каталог на последний посещенный. 

>## %history
>>Команда %history отображает все предыдущие команды в текущем сеансе. 
Увидеть подобный список команд и функций может быть полезно, если была 
случайно удалена команда и ее результат.

>## %dhist
>>Волшебная команда %dhist выводит все каталоги, посещенные в текущем 
сеансе. Каждый раз, когда используется команда %cd, этот список обновляется в переменной «dh».

>## %env
>>Магическая функция используется для получения, установки и перечисления 
переменных среды. Запуск команды без аргументов отобразит список всех 
переменных среды. Также можно ввести имя переменной среды, за которой 
следует команда, и она вернет ее значение:

%env HOMEDRIVE
или использовать %env для установки значения переменной окружения:

%env: HOMEDRIVE=F:
>## %edit
>>Эта волшебная команда вызывает текстовый редактор, используемый 
по умолчанию в текущей ОС (например, «Блокнот» Windows) для редактирования 
скрипта Python. Скрипт выполняется при закрытии редактора.

>## %autocall
>>Эта волшебная команда позволяет автоматически вызывать функцию 
без использования круглых скобок.

%autocall [режим]
>>Для приведенного синтаксиса доступно 3 аргумента режима:

* 0 — выключено;
* 1 — smart-режим (по умолчанию);
* 2 — всегда включен.


>## %automagic
Позволяет вводить магические команды без префикса «%», 
если установлено значение «1». Без аргументов функция 
включается/выключается. Для деактивации нужно установить значение «0».

>## %matplotlib
Магическая функция активирует интерактивную поддержку 
matplotlib во время сеанса IPython. Однако она не импортирует 
библиотеку matplotlib.

>## %notebook
Эта функция преобразует текущую историю IPython в файл «блокнота» 
IPython с расширением ipynb.

>## %recall
При выполнении без каких-либо параметров эта функция выполняет 
предыдущую команду. При указании номера ячейки (%recall n) после команды, 
вызывается команда в этой ячейке (n).

>## %gui [GUINAME]
При использовании без аргумента команда включает или отключает 
интеграцию цикла событий IPython GUI. С аргументом GUINAME магическая функция заменяет наборы инструментов GUI, используемые по умолчанию, на указанный.
