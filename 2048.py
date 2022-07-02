bgs={0:"#FFFFF0",2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", 32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61",
    512:"#edc850", 1024:"#edc53f", 2048:"#edc22e"}# Шестнадцатеричное значение цвета
mp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]# Как двумерный массив для записи изменений 4 * 4 квадратов
vis=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]# Используется для обозначения того, какие позиции квадратов 4 * 4 имеют значения
newmp=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]# Использовать в качестве промежуточного массива
vc=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]# Определите, есть ли данные в каждом месте


# Случайно найти координату в пустом пространстве и присвоить значение 2 или 4
def random_num():
    while True:
        x1=random.randint(0,3)  # Диапазон целых данных 0-3
        y1=random.randint(0,3)
        if vis[x1][y1]==0:
            mp[x1][y1]=random.choice([2,4,2,2])  # Случайно принимать значение от 2 до 4
            vis[x1][y1]=1
            return


# Инициализировать newmp, vis
def init():
    for i in range(4):
        for j in range(4):
            newmp[i][j]=0
            vis[i][j]=0


# Начальная мп
def init_mp():
    for i in range(4):
        for j in range(4):
            mp[i][j]=0


# Изменить интерфейс
def print_interface():
    for i in range(4):
        for j in range(4):
            cs=bgs[mp[i][j]]
            c1.create_rectangle(j*100,i*100,j*100+100,i*100+100,fill="%s"%(cs))
            if mp[i][j]!=0:  #Control 0 output
                c1.create_text((j*100+100)-50,(i*100+100)-50,text="%d"%(mp[i][j]),font=(«Курсив»,30))


# Оцените, закончилось ли это
def gameover():
    if vis==vc and panduan()==False:  # Если в каждом бите есть данные, а номер каждого элемента и смежные позиции не равны, игра будет выведена на интерфейс для завершения игры.
        c1.create_oval(100,150,300,250,fill="#FF4500")
        c1.create_text(200,200,text="игра закончена")


# Решите, можете ли вы продолжить операцию
def panduan ():
    movex=[-1,1,0,0]
    movey=[0,0,-1,1]
    for i in range(4):  # Оценить окружение каждого элемента
        for j in range(4):
            for l in range(4):
                newx=int(i+movex[l])
                newy=int(j+movey[l])
                if (newx<0 or newx>3)or(newy<0 or newy>3):
                    continue
                else:
                    if mp[i][j]==mp[newx][newy]:
                        return True
    return False


#UP
def put_up():
    init()  # Инициализация, newmp, vis
    for i in range(4):  # Объединить, удалить сетку 0
        l=0
        for j in range(4):
            if mp[j][i]==0:
                continue
            else:
                newmp[l][i]=mp[j][i]
                l+=1
    for i in range(4):  # Начиная со второго, сравнивать только с предыдущим числом, если оно равно, добавить его и сделать эту позицию равной 0
        for j in range(1,4):
            if newmp[j][i]==0:
                break
            else:
                if newmp[j][i]==newmp[j-1][i]:
                    newmp[j-1][i]=newmp[j][i]+newmp[j-1][i]
                    newmp[j][i]=0
    if newmp==mp:  # Если после слияния вверх и добавления соседней позиции, такой же, как предыдущая без изменений, это означает, что направление не может быть изменено и выскочить напрямую
        return
    init_mp()  # Инициализировать mp, объединить добавленное значение снова и передать его в mp
    for i in range(4):
        l=0
        for j in range(4):
            if newmp[j][i]==0:
                continue
            else:
                mp[l][i]=newmp[j][i]
                vis[l][i]=1
                l+=1
    random_num()  # 2 или 4 генерируется случайным образом после слияния
    print_interface()  # Модифицировать интерфейс и отображение
    gameover()  # Первый судья, закончился ли он
    return


#вниз
def put_down():
    init()
    for i in range(4):
        l=3
        j=3
        while j>=0:
            if mp[j][i]==0:
                j-=1
                continue
            else:
                newmp[l][i]=mp[j][i]
                l-=1
                j-=1
    for i in range(4):
        j=2
        while j>=0:
            if newmp[j][i]==0:
                break
            else:
                if newmp[j][i]==newmp[j+1][i]:
                    newmp[j+1][i]=newmp[j][i]+newmp[j+1][i]
                    newmp[j][i]=0
            j-=1
    if newmp==mp:
        return
    init_mp()
    for i in range(4):
        l=3
        j=3
        while j>=0:
            if newmp[j][i]==0:
                j-=1
                continue
            else:
                mp[l][i]=newmp[j][i]
                vis[l][i]=1
                l-=1
            j-=1
    random_num()
    print_interface()
    gameover()  # Первый судья, закончился ли он
    return


#осталось
def put_left():
    init()
    for i in range(4):
        l=0
        for j in range(4):
            if mp[i][j]==0:
                continue
            else:
                newmp[i][l]=mp[i][j]
                l+=1
    for i in range(4):
        for j in range(1,4):
            if newmp[i][j]==0:
                break
            else:
                if newmp[i][j]==newmp[i][j-1]:
                    newmp[i][j-1]=newmp[i][j]+newmp[i][j-1]
                    newmp[i][j]=0
    if newmp==mp:
        return
    init_mp()
    for i in range(4):
        l=0
        for j in range(4):
            if newmp[i][j]==0:
                continue
            else:
                mp[i][l]=newmp[i][j]
                vis[i][l]=1
                l+=1
    random_num()
    print_interface()
    gameover()  # Первый судья, закончился ли он
    return


#Направо
def put_right():
    init()
    for i in range(4):
        l=3
        j=3
        while j>=0:
            if mp[i][j]==0:
                j-=1
                continue
            else:
                newmp[i][l]=mp[i][j]
                l-=1
                j-=1
    for i in range(4):
        j=2
        while j>=0:
            if newmp[i][j]==0:
                break
            else:
                if newmp[i][j]==newmp[i][j+1]:
                    newmp[i][j+1]=newmp[i][j]+newmp[i][j+1]
                    newmp[i][j]=0
            j-=1
    if newmp==mp:
        return
    init_mp()
    for i in range(4):
        l=3
        j=3
        while j>=0:
            if newmp[i][j]==0:
                j-=1
                continue
            else:
                mp[i][l]=newmp[i][j]
                vis[i][l]=1
                l-=1
            j-=1
    random_num()
    print_interface()
    gameover()  # Первый судья, закончился ли он
    return


# Основной раздел функций
import random  # Библиотека случайных чисел
import tkinter  # Библиотека форм
t1=tkinter.Tk()  # Создать форму объекта
t1.geometry("650x400")  # Размер формы
t1.title("2048")  # Заголовок формы
btn1=tkinter.Button(t1,text=«Вверх»,font=(«Курсив»,11),fg="black",command=put_up)  # Первая кнопка и события, которые произойдут после нажатия (команда)
btn2=tkinter.Button(t1,text="вниз",font=(«Курсив»,11),fg="black",command=put_down)  # Вторая кнопка и событие
btn3=tkinter.Button(t1,text="осталось",font=(«Курсив»,11),fg="black",command=put_left)
btn4=tkinter.Button(t1,text="Направо",font=(«Курсив»,11),fg="black",command=put_right)
btn4.pack(side="right",padx="2m",anchor="e")  # Позиция, которая должна быть размещена, е означает средний правый
btn3.pack(side="right",padx="2m",anchor="e")
btn2.pack(side="right",padx="2m",anchor="e")
btn1.pack(side="right",padx="2m",anchor="e")
t1['background']='#F4A460'  # Формировать цвет фона
c1=tkinter.Canvas(t1,width=400,height=400)  # Создание и определение размера формы холста
c1.pack(side="left")  # Установите холст с выравниванием по левому краю на форме
random_num()  # Произвольно генерировать 2 или 4 в позиции, где нет номера
for i in range(4):  #for интерфейс вывода цикла
    for j in range(4):
        cs=bgs[mp[i][j]]
        c1.create_rectangle(j*100,i*100,j*100+100,i*100+100,fill="%s"%(cs))  # Создайте квадрат на холсте, четыре значения - это левая вершина и нижняя правая вершина квадрата
        if mp[i][j]!=0:
            c1.create_text((j*100+100)-50,(i*100+100)-50,text="%d"%(mp[i][j]),font=(«Курсив»,30))  # Заполните соответствующий номер в поле
t1.mainloop()  # Запустить значение функции цикла сообщения формы