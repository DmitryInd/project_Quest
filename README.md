# project_Quest
Создатель: Инденбом Дмитрий

Этот квест создаётся на питоне в качестве проекта для университета. 

Как состоит файл сюжета:
1. Количество локаций (вершин у графа)
2. Json-строка со словарём "Edges",
   где соответственно определены все переходы в строгом порядке 
3. Дальше идут последовательно (нумерация сверху вниз) json-строки с описанием локаций:
   1. Название* локации ("name")
   2. Изображение, которое будет выводится на локации
      (когда будет графический интерфейс) ("image")
   3. Текст, который будет выводится на локации ("text")
   4. Переходы (в том же порядке, что и во втором пункте) ("choices"):
      1. Условия отображения выбора ("condition")
         (в формате python но без if и пока только с целыми числами)
      2. Текст выбора ("text")
      3. Изменение количества предметов в инвентаре ("gifts")
           (Можно написать сложную функцию, обазаначая в ней
           кол-во предметов из инвентаря их именами -- в строке
           или просто число, которое прибавится к уже имеющемуся кол-ву)
           
*Название заключающего слайда должно начинаться с @end@. При его достижении программа стирает автосохрнанение.

У любого сюжета обязан быть инвентарь с расширением json в той же папке:
  1. В нём три словаря: c видимыми предметами ("Visible") и невидимыми ("Not visible") и всегда видимыми ("Always visible"):
     1. Количество видимых предметов игрок может посмотеть в инвентаре (если оно не равно нулю)
     2. Количество невидимых предметов игрок не может посмотеть
     3. Всегда видимые показываются вместе с описанием локации при любом количестве

Чтобы игра сама определяла ваш сценарий, вам нужно:
1. Добавить его в папку "Information" (которая должна находится в папке с кодом) 
2. Добавить туда же инвентарь
3. Понять имя инвентаря на "*Имя файла с сюжетом* _Inventory.json" (Это нужно в любом месте)

Для ввода своего адреса у игры появился отдельный экран,
он также проверяет наличие нужных файлов.

P.S. Поддерживаются русские буквы
