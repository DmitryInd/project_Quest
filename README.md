# project_Quest
Этот квест создаётся на питоне в качестве проекта для университета. 

Как состоит файл сюжета:
1. Количество локаций (вершин у графа)
2. Json-строка со словарём "Edges",
   где соответственно определены все переходы в строгом порядке 
3. Дальше идут последовательно (нумерация сверху вниз) json-строки с описанием локаций:
   1) Название локации ("name")
   2) Изображение, которое будет выводится на локации
      (когда будет графический интерфейс) ("image")
   3) Текст, который будет выводится на локации ("text"),
   4) Переходы (в том же порядке, что и во втором пункте) ("choices"):
      4.1) Условия отображения выбора ("condition")
           (в формате python но без if и пока только с целыми числами)
      4.2) Текст выбора ("text")
      4.3) Изменение количества предметов в инвентаре ("gifts")
           (Можно написать сложную функцию, обазаначая в ней
           кол-во предметов из инвентаря их именами -- в строке
           или просто число, которое прибавится к уже имеющемуся кол-ву)

У любого сюжета обязан быть инвентарь с расширением json в той же папке:
  1. В нём два словаря: c видимыми предметами ("Visible") и невидимыми ("Not visible"):
     1.1) Количество видимых предметов игрок может посмотеть
     1.2) Количество невидимых предметов игрок не может посмотеть

Чтобы игра сама определяла ваш сценарий, вам нужно:
1. Добавить его в папку "Information" (которая должна находится в папке с кодом) 
2. Добавить туда же инвентарь
3. Понять имя инвентаря на "*Имя файла с сюжетом* _Inventory.json" (Это нужно в любом месте)

Если же вы вводите неверный адрес сюжета, то сейчас игра просто выдаст ошбику (вылетит)

P.S. Поддерживаются русские буквы
