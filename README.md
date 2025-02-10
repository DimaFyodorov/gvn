# GVN - GVN is Vector Notation.
It is a simple language for describing vector graphics.

## History
GVN is a small implementation of instructions from a computer science for grade 10 textbook written by me for fun while I was sick.
This pseudo language is used in as many as 2.5 tasks, in the first one you need to write it down in this language from an image (although I don't know how, since the dimensions are not given), and in the second one you need to build a picture from commands, as I suppose manually, but I had a lot of free time while I was sick, so I wrote an implementation of these instructions for fun. Moreover, since I am not one of those who requires a certificate from those who want to write in this (Hello 1C), there is support not only for Russian, but also for English for writing commands)))
Honestly, I don't know why you might need this thing, but below is described how to run it, what are the capabilities and limitations.

## Installation
You can download a ready-made build for Windows in 1 file, but it does not support vector formats, and I cannot guarantee that everything will be fine on your system.

1. Install [UV](https://github.com/astral-sh/uv), if you are not using it yet.
2. Install dependencies
```bash
uv sync
```
3. You can go to the src/ folder and run
```bash
uv run main.py
```

If you still use the .exe file, then instead of `uv run main.py <something>` write `gvn <something>`.

## Available commands
*Floating point numbers are indicated everywhere.
**Colors can be specified in hex format or by their names in English, if the color does not match, you will be warned about this.

`Set X Y`
Take 2 numbers and store them in memory for future use.

`Set_Draw_Color`
Sets the stroke color for shapes that will be created after this command.
If it is not written, the stroke color is black by default.

`Set_Fill_Color`
Sets the fill color for shapes that will be created after this command.
If it is not written, the fill color is None by default, i.e. transparent.

`Line_to X1 Y1`
Creates a line from the specified coordinates to the specified ones in memory. If `Set` has not been used before, the line will be brought to the point (0, 0).

`Line X1 Y1 X2 Y2`
Creates a line from (X1, Y1) to (X2, Y2).

`Circle X Y R`
Creates a circle with the center at point (X, Y) and radius R.

`Ellipse X1 Y1 X2 Y2`
Creates an ellipse inscribed in a rectangle with corners at points (X1, Y1) and (X2, Y2).

`Rectangle X1 Y1 X2 Y2`
Creates a rectangle with corners at points (X1, Y1) and (X2, Y2).

`Fill X Y color`
Changes the outline color of the shapes inside which the point (X, Y) is located.
It is important to note that the outline of **all** shapes inside which the specified point is located is changed.
A rather strange system, but it is what it is, as it was written in the textbook.

`Save file_name.extension`
Saves the described image to a file with the specified name and extension.

## Flags
The program supports a number of flags that can be used when transferring a file for processing.

`-h`
Shows help about the program.

`-r`
Tells the program to use Russian for processing commands.

`-c`
Outputs the program source code to the console in a "nicely" formatted view with highlighting.

`-g`
Adds a coordinate grid to the final image.
(*If I develop it, I need to transfer this feature to the code and let it be configured.)
`-s`
Enables interactive mode. After the program runs, a matplotlib window will open where you can see what you described.

## Examples
Will come a little later.
For now, they can be found in the example/ folder.


# На русском
GVN это простой язык для описания векторной графики.

## История
GVN это небольшая реализация инструкций из учебника по [информатике для 10 класса](https://informika-e.ru/S2/10_SEMAKIN.pdf)(стр.209) написанная мной ради шутки пока я болел.
Это псевдо язык используется в целых 2.5 заданиях, в первой надо по изображению записать его на этом языку (хотя хз как, ведь размеры не даны), а во втором построить по командам картинку, как предполагаю вручную, но у меня было много свободного времени пока болел по этому я и написал ради шутки реализацию этих инструкций. Причём так как я не из тех кто требует сертификат от тех кто хочет на этом писать (Привет 1С), есть поддержка не только русского, но ещё и английского языка для написания команд)))
Честно не знаю зачем вам может понадобиться это нечто, но ниже описано как запустить, какие есть возможности и ограничения.

## Установка
Можно скачать готовый билд для windows в 1 файле, но там отваливаеться поддержка векторных форматов, и я не могу гарантировать что всё будет хорошо именно на вашей системе.

1. Установите [UV](https://github.com/astral-sh/uv), если вы его ещё не используете.
2. Установите зависимости
   ```bash
   uv sync
   ```
3. Можно перейти в папку src/ и запустить
   ```bash
   uv run main.py
   ```

Если вы всё же используете .exe файл, то вместо `uv run main.py <что-то>` пишем `gvn <что-то>`.

## Доступные команды
*Везде указываются числа с плавающей точкой.
**Цвета можно указывать в hex формате или их именами по-английски, если цвет не подходят об этом предупредят. 

`Установить X Y`
Принимает 2 числа и запоминает их в памяти для использования в будущем.

`Цвет_Рисования цвет`
Устанавливает цвет обводки для фигур которые будут созданы после этой команды.
Если она не будет написано, то по умолчанию цвет обводки чёрный.

`Цвет_Закраски цвет`
Устанавливает цвет закраски для фигур которые будут созданы после этой команды.
Если она не будет написано, то по умолчанию цвет закраски None, то есть прозрачный.

`Линия_к X1 Y1`
Создаёт линию от указанных координат к указанным к памяти. Если до этого не применялась `Установить`, то линия будет приведена к точке (0, 0).

`Линия X1 Y1 X2 Y2`
Создаёт линию от (X1, Y1) до (X2, Y2).

`Окружность X Y R`
Создаёт окружность с центром в точке (X, Y) и радиусом R.

`Эллипс X1 Y1 X2 Y2`
Создаёт эллипс вписанный в прямоугольник с углами в точках (X1, Y1) и (X2, Y2).

`Прямоугольник X1 Y1 X2 Y2`
Создаёт прямоугольник с углами в точках (X1, Y1) и (X2, Y2).

`Закрасить X Y цвет`
Меняет цвет обводки фигур внутри которых находиться точка (X, Y).
Важно отметить что меняется обводка **всех** фигур внутри которых оказалась указанная точка.
Довольно странная система, но какая есть, так было написано в учебнике.

`Сохранить имя_файла.расширение`
Сохраняет описанное изображение в файл с указанным названием и расширением.

## Флаги
Программа поддерживает некоторое количество флагов которые можно использовать при передаче файла на обработку.

`-h`
Показывает справку о программе.

`-r`
Говорит программе использовать русский язык для обработки команд.

`-c`
Выводит в консоль исходный код программы в "красиво" отформатированном видел с подсветкой.

`-g`
Добавляет координатную сетку на итоговое изображение.
(*Если буду развивать надо перенести эту фичу в код и дать её настраивать.)

`-s`
Включает интерактивный режим. После работы программы откроется окно от matplotlib где можно будет увидеть то что вы описали.

## Примеры
Будет чуть позже.
Пока что их можно найти в папке example/ .
