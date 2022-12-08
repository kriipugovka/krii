import codecs
import os

class Car(object):

    def __init__(self, num, name, year, lights, doors):
        self.num = num
        self.name = name
        self.year = year
        self.lights = lights
        self.doors = doors

    def param_print(self,p_type):
        if p_type == 'Название':
            print(self.name)
        elif p_type == 'Год выпуска':
            print(self.year)
        elif p_type == 'Состояние фар':
            print(self.lights)
        elif p_type == 'Состояние дверей':
            print(self.doors)

    def p_repl(self,p_type,text):
        with codecs.open('cars\car'+str(self.num)+'.txt', encoding = 'utf-8') as car_file:
            p_array = list(car_file.readlines())
        array_normal = []
        for word in p_array:
            if '\r\n' in word:
                word = word.replace('\r\n','',1)
            if '\n' in word:
                word = word.replace('\n','',1)
            array_normal.append(word)
        if p_type == 'Название':
            if len(text) > 50:
                return 'Название слишком длинное'
            if car_search(text) != None:
                return 'Машина с таким названием уже существует, введите другое название'
            if text == 'Выход':
                return 'Название машины не может быть "Выход"'
            else:
                fwrite_arr = []
                fwrite_arr.append(text)
                fwrite_arr.append(array_normal[1])
                fwrite_arr.append(array_normal[2])
                fwrite_arr.append(array_normal[3])
                self.name = text
        elif p_type == 'Год выпуска':
            if int(text) > 2022 or int(text) < 1800:
                return 'Год указан некорректно'
            else:
                fwrite_arr = []
                fwrite_arr.append(array_normal[0])
                fwrite_arr.append(text)
                fwrite_arr.append(array_normal[2])
                fwrite_arr.append(array_normal[3])
                self.year = text
        elif p_type == 'Состояние фар':
            lights_array = ['Включены','Выключены']
            if not text in lights_array:
                return 'Неверно указано состояние фар. Доступные состояния: "Включены", "Выключены"'
            else:
                fwrite_arr = []
                fwrite_arr.append(array_normal[0])
                fwrite_arr.append(array_normal[1])
                fwrite_arr.append(text)
                fwrite_arr.append(array_normal[3])
                self.lights = text
        elif p_type == 'Состояние дверей':
            doors_array = ['Открыты','Закрыты']
            if not text in doors_array:
                return 'Неверно указано состояние дверей. Доступные состояния: "Открыты", "Закрыты"'
            else:
                fwrite_arr = []
                fwrite_arr.append(array_normal[0])
                fwrite_arr.append(array_normal[1])
                fwrite_arr.append(array_normal[2])
                fwrite_arr.append(text)
                self.doors = text
        try:
            with codecs.open('cars\car'+str(self.num)+'.txt', 'w+', encoding = 'utf-8') as car_file:
                for line in fwrite_arr:
                    car_file.write(line + '\n')
            return 'Параметр изменён'
        except:
            pass

    def p_del(self,p_type):
        with codecs.open('cars\car'+str(self.num)+'.txt', encoding = 'utf-8') as car_file:
            p_array = list(car_file.readlines())
        array_normal = []
        for word in p_array:
            if '\r\n' in word:
                word = word.replace('\r\n','',1)
            if '\n' in word:
                word = word.replace('\n','',1)
            array_normal.append(word)
        if p_type == 'Название':
            return 'Название машины нельзя удалить'
        elif p_type == 'Год выпуска':
            fwrite_arr = []
            fwrite_arr.append(array_normal[0])
            fwrite_arr.append('None')
            fwrite_arr.append(array_normal[2])
            fwrite_arr.append(array_normal[3])
            self.year = 'None'
        elif p_type == 'Состояние фар':
            fwrite_arr = []
            fwrite_arr.append(array_normal[0])
            fwrite_arr.append(array_normal[1])
            fwrite_arr.append('None')
            fwrite_arr.append(array_normal[3])
            self.lights = 'None'
        elif p_type == 'Состояние дверей':
            fwrite_arr = []
            fwrite_arr.append(array_normal[0])
            fwrite_arr.append(array_normal[1])
            fwrite_arr.append(array_normal[2])
            fwrite_arr.append('None')
            self.doors = 'None'
        try:
            with codecs.open('cars\car'+str(self.num)+'.txt', 'w+', encoding = 'utf-8') as car_file:
                for line in fwrite_arr:
                    car_file.write(line + '\n')
            return 'Параметр удалён'
        except:
            pass

def car_add(name):
    global car_count
    lines = [name, 'None', 'None', 'None']
    new_car_file = codecs.open('cars\car'+str(car_count)+'.txt','w+',encoding = 'utf-8')
    for line in lines:
        new_car_file.write(line + '\n')
    new_car_file.close()
    print('Создана новая машина')
    car_count += 1

def cars_list():
    car_number = 0
    while True:
        try:
            with codecs.open('cars\car'+str(car_number)+'.txt', encoding = 'utf-8') as f:
                text = list(f.readlines())
            text1 = []
            for word in text:
                if '\r\n' in word:
                    word = word.replace('\r\n','',1)
                if '\n' in word:
                    word = word.replace('\n','',1)
                text1.append(word)
            print(text1[0])
        except FileNotFoundError:
            break
        car_number += 1

def car_del(num):
    os.remove('cars\car'+str(num)+'.txt')

def isnum(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def car_debug():
    global chosen_car
    chosen_car = car.name

def pr_checker(name):
    p_array = ['Название','Год выпуска','Состояние фар','Состояние дверей']
    if name in p_array:
        return name
    else:
        return False

def car_search(name):
    global chosen_car
    car_number = 0
    while True:
        try:
            with codecs.open('cars\car'+str(car_number)+'.txt', encoding = 'utf-8') as f:
                text = list(f.readlines())
            text1 = []
            for word in text:
                if '\r\n' in word:
                    word = word.replace('\r\n','',1)
                if '\n' in word:
                    word = word.replace('\n','',1)
                text1.append(word)
            if name == text1[0]:
                chosen_car = name
                return car_number
                break
        except FileNotFoundError:
            break
            print('Машины с таким названием не существует')
        car_number += 1

def create(num):
    global car
    with codecs.open('cars\car'+str(num)+'.txt', encoding = 'utf-8') as f:
        text = list(f.readlines())
    text1 = []
    for word in text:
        if '\r\n' in word:
            word = word.replace('\r\n','',1)
        if '\n' in word:
            word = word.replace('\n','',1)
        text1.append(word)
    name = text1[0]
    year = text1[1]
    lights = text1[2]
    doors = text1[3]
    car = Car(num, name, year, lights, doors)

running = True
car_count = 0
car_num = None
chosen_car = None
while True:
    try:
        f = open('cars\car'+str(car_count)+'.txt')
        car_count += 1
        f.close()
    except FileNotFoundError:
        break
while running:
    if car_count == 0:
        print('Для начала работы создайте новую машину')
        print('Введите название первой машины или введите "Выход" для выхода из программы')
        inp = input()
        while len(inp) > 50 and not inp == 'Выход':
            print('Длина названия не может быть больше 50 символов')
            inp = input()
        if not inp == 'Выход':
            car_add(inp)
        if inp == 'Выход':
            running = False
    else:
        if car_num == None:
            print('Машин в базе:',str(car_count)+',','введите название машины, чтобы отредактировать её')
            print('Чтобы создать новую машину, введите "Новая машина", затем введите название')
            print('Чтобы выйти из консоли, введите "Выход"')
            print('Чтобы вывести список со всеми машинами, введите "Список"')
            inp = input()
            if inp == 'Новая машина':
                print('Название:')
                inp = input()
                while inp == 'Новая машина':
                    print('Машина не может иметь название "Новая машина"')
                    inp = input()
                existing_car_num = None
                existing_car_num = car_search(inp)
                while not existing_car_num == None:
                    print('Машина с таким названием уже существует')
                    inp = input()
                    existing_car_num = car_search(inp)
                car_add(inp)
            elif inp == 'Выход':
                running = False
            elif inp == 'Список':
                cars_list()
            else:
                car_num = car_search(inp)
                while car_num == None:
                    print('Машина не найдена, попробуйте ещё раз')
                    inp = input()
                    while inp == 'Новая машина':
                        print('Машина не может иметь название "Новая машина"')
                        inp = input()
                    car_num = car_search(inp)
        if car_num != None:
            try:
                del car
            except:
                pass
            create(car_num)
            car_debug()
            print('Текущая машина имеет номер:',str(car_num)+',','название:',chosen_car)
            print('Для выхода из режима редактирования параметров машины, введите "Выход"')
            print('Для удаления машины введите "Удалить", для взаимодействия с параметрами, введите название параметра')
            print('Возможные параметры: Название, Год выпуска, Состояние фар, Состояние дверей')
            inp = input()
            if inp == 'Выход':
                print('Вы вышли из режима редактирования параметров')
                car_num = None
            elif inp == 'Удалить':
                car_del(car_num)
                car_count -= 1
                car_num = None
                chosen_car = None
                i = 0
                search_err = 0
                folder = []
                while True:
                    try:
                        f = codecs.open('cars\car'+str(i)+'.txt', 'r', encoding = 'utf-8')
                        f.close()
                        fname = 'car'+str(i)+'.txt'
                        folder.append(fname)
                    except:
                        search_err += 1
                    i += 1
                    if search_err >= 3:
                        break
                for i in range(0, len(folder)):
                    try:
                        os.rename('cars\\'+folder[i], 'cars\car'+str(i)+'.txt')
                    except:
                        pass
                print('Машина удалена')
            else:
                print('Вы находитесь в режиме редактирования машины, чтобы выйти из него, введите "Выход"')
                ch_quit = False
                while not ch_quit:
                    param_search_repl = pr_checker(inp)
                    while not bool(param_search_repl):
                        print('Такого параметра нет')
                        inp = input()
                        if inp != 'Выход':
                            param_search_repl = pr_checker(inp)
                        else:
                            ch_quit = True
                            print('Вы вышли из режима изменения машины')
                    if not ch_quit:
                        print('Вы выбрали параметр:',str(inp)+',','введите "Вывод", чтобы вывести его значение, "Изменить", чтобы изменить его или "Удалить", чтобы удалить параметр')
                        print('Чтобы выбрать другой параметр, введите "Выбор", если хотите покинуть режим редактирования параметров, введите "Выход"')
                        inp = input()
                        while not (inp == 'Вывод' or inp == 'Изменить' or inp == 'Выбор' or inp == 'Удалить' or inp == 'Выход'):
                            print('Такой команды нет')
                            inp = input()
                        if inp == 'Вывод':
                            car.param_print(param_search_repl)
                            print('Для замены параметра введите "Изменить", для удаления введите "Удалить", для выбора другого параметра введите "Выбор", для выхода введите "Выход"')
                            inp = input()
                            while not (inp == 'Изменить' or inp == 'Удалить' or inp == 'Выбор' or inp == 'Выход'):
                                print('Такой команды нет')
                                inp = input()
                            if inp == 'Выход':
                                ch_quit = True
                                print('Вы вышли из режима редактирования машины')
                            else:
                                if inp == 'Изменить':
                                    print('Введите новое значение изменяемого параметра')
                                    inp = input()
                                    while not ch_quit and param_search_repl == 'Год выпуска' and not inp.isdigit():
                                        print('Год выпуска должен являться числом')
                                        inp = input()
                                        if inp == 'Выход':
                                            ch_quit = True
                                            print('Вы вышли из режима редактирования машины')
                                    if not inp == 'Выход':
                                        ret = car.p_repl(param_search_repl,inp)
                                        if ret == 'Параметр изменён':
                                            print(ret)
                                    while not ret == 'Параметр изменён' and not ch_quit:
                                        if inp == 'Выход':
                                            ch_quit = True
                                            print('Вы вышли из режима редактирования машины')
                                        elif not inp == 'Выход' and not ch_quit:
                                            ret = car.p_repl(param_search_repl,inp)
                                            if ret == 'Параметр изменён':
                                                print(ret)
                                                ch_quit = True
                                            else:
                                                print(ret)
                                                print('Попробуйте ещё раз или введите "Выход", чтобы покинуть режим изменения этого параметра')
                                                inp = input()
                                        car_debug()
                                    ch_quit = True
                                if inp == 'Выбор':
                                    print('Введите название другого параметра')
                                    inp = input()
                                if inp == 'Удалить':
                                    print(car.p_del(param_search_repl))
                                    ch_quit = True
                        elif inp == 'Изменить':
                            print('Введите новое значение изменяемого параметра')
                            inp = input()
                            while not ch_quit and param_search_repl == 'Год выпуска' and not inp.isdigit():
                                print('Год выпуска должен являться числом')
                                inp = input()
                                if inp == 'Выход':
                                    ch_quit = True
                                    print('Вы вышли из режима редактирования машины')
                            if not inp == 'Выход':
                                ret = car.p_repl(param_search_repl,inp)
                                if ret == 'Параметр изменён':
                                    print(ret)
                            while not ret == 'Параметр изменён' and not ch_quit:
                                if inp == 'Выход':
                                    ch_quit = True
                                    print('Вы вышли из режима редактирования машины')
                                elif not inp == 'Выход' and not ch_quit:
                                    ret = car.p_repl(param_search_repl,inp)
                                    if ret == 'Параметр изменён':
                                        print(ret)
                                        ch_quit = True
                                    else:
                                        print(ret)
                                        print('Попробуйте ещё раз или введите "Выход", чтобы покинуть режим изменения этого параметра')
                                        inp = input()
                                car_debug()
                            ch_quit = True
                            if inp == 'Выбор':
                                print('Введите название другого параметра')
                                inp = input()
                            if inp == 'Удалить':
                                print(car.p_del(param_search_repl))
                                ch_quit = True
                        elif inp == 'Удалить':
                            print(car.p_del(param_search_repl))
                            ch_quit = True
                        elif inp == 'Выбор':
                            print('Введите название другого параметра')
                            inp = input()
                        elif inp == 'Выход':
                            ch_quit = True
                            print('Вы вышли из режима редактирования машины')
