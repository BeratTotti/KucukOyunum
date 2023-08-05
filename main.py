import turtle
import random

screen = turtle.Screen()
screen.bgcolor("#98f5ff")
screen.title("Kamlumbağayı Yakala")

turtle_instance = turtle.Turtle()
turtle_instance.hideturtle()
Turtle_List = []
skor = 0



# turtle ile yazı yazma

#score_turtle
score_turtle=turtle.Turtle()
#coutndownturtle
countdown_turtle = turtle.Turtle()
# gameover
gameover = False


font= ("Times",30 ,"normal")
def turtle_ayarları():
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.hideturtle()
    score_turtle.color("black")

    score_turtle.penup()
    score_turtle.setposition(0,340)
    score_turtle.write(arg="Score : 0 ",move=False,align="center",font=font)
turtle_ayarları()


def make_turtle(x,y):

    def get_mouse_click(x,y ):
        global skor
        skor += + 1
        score_turtle.clear()
        score_turtle.write(arg="Score : {}".format(skor),move=False,align="center",font=font)





        #print(x,y)
    t = turtle.Turtle()
    t.shape("turtle")
    t.shapesize(2)
    t.color("green")
    t.penup()
    t.onclick(get_mouse_click)
    t.goto(x * 10 , y * 10 )
    Turtle_List.append(t)


# 10 ile çarpmamızın nedeni turtle' mızı farklı yere götürmek için 3 basamaklı sayılar girceğimizzden 10 ile çarp dersek
# eğer, öyle çok büyük sayılar girmemize gerek kalmıycak fonkisyon içine.

def turtle_kısayol():

    x_koordinat = [30,20,10,0,-30,-20,-10]
    y_koordinat = [30,20,10,0,-30,-20,-10]

    for x in x_koordinat:
        for y in y_koordinat:
            make_turtle(x,y)

def hide_turtle():
    for t in Turtle_List:
        t.hideturtle()

def show_turtle_random():
    if not gameover:
        hide_turtle()
        random.choice(Turtle_List).showturtle(),
        screen.ontimer(show_turtle_random, 300)
        hide_turtle()




def countdown(time):
    global gameover
    countdown_turtle.hideturtle()
    countdown_turtle.color("red")

    countdown_turtle.penup()
    countdown_turtle.setposition(0, 300)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time : {} ".format(time), move=False, align="center", font=font)
        screen.ontimer(lambda : countdown(time - 1),1000)
    else:
        gameover = True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write(arg="Game Over!! ", move=False, align="center", font=font)
        hide_turtle()




def start_up_turtle():# yapıp bir fonksiyon içine alıp kolay bi şekilde bu fonksiyonu çalıştırdığımızda direkt başlatma
    turtle.tracer(0)  # fonksiyonlarının hepsi çalışır.Daha derli toplu olur :)

    turtle_ayarları()
    turtle_kısayol()
    hide_turtle()
    countdown(10)
    show_turtle_random()

    turtle.tracer(1)

start_up_turtle()









turtle.mainloop()