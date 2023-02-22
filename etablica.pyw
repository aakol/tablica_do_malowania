import tkinter
import tkinter as tk
from tkinter import *
import codecs
from random import random
import ftplib
from ftplib import *
from tkinter import messagebox
a =int(random()*1000000)
nazwa = "etable"+str(a)+".html"

listax =[]
listay =[]
kolor =  []

okno = tkinter.Tk()
okno.title("eTablica  - "+nazwa)
okno.configure(background="#669900")
width_e =okno.winfo_screenwidth()*0.95
height_e =okno.winfo_screenheight()*0.45
#okno.geometry(str(width_e)+"x"+str(height_e-20))

print()
frame = Frame(okno)

frame.pack()

def ftpa():
    przycisk1.configure(state="disabled")
    ftpi = FTP()
    #ftpi.set_debuglevel(2)
    try:
        ftpi.connect(serwer.get(), 21, timeout=25)
    except ftplib.all_errors as e:
        messagebox.showinfo("connect error", "serwer niedostępny lub błąd nazwy\n"+str(e))
        return 0
    try:
        ftpi.login(login.get(),halo.get())
    except ftplib.all_errors as e:

        print(str(e))
        #print("zły login lub haslo")
        messagebox.showinfo("login lub hasło", "raczej może to być nieprawidłowe hasło lub login\n"+str(e))
        return 0
    try:
        file = open(nazwa,"rb")
    except:
        #print("plik niedostępnyt")
        messagebox.showinfo("plik", "brak dostępu do pliku na dysku")
        return 0
    try:
        ftpi.cwd(kat.get())
    except ftplib.all_errors as e:

        messagebox.showinfo("bląd w czwartym oknie", "bład katalogu\n"+str(e))
        return 0
    ftpi.storbinary('STOR ' +nazwa , file)          # send the file
    file.close()                                    # close file and FTP
    ftpi.quit()
    print("zakończone wysyłanie")
    messagebox.showinfo("transfer zakończony", "prawie na pewno transfer pliku został zakończony prawidłowo plik "+ nazwa +" z dużą pewnością znajduje się na serwerze PAMIĘTAJ najpierw GENERATE potem SEND")
    przycisk1.configure(state="active")
def wysylanie():
    przycisk.configure(state="disabled")
    aaa=tekst.index('end').split(".")
    bbb=int(aaa[0])
    des=tekst.get("1.0","4.0")
    try:
        plik = codecs.open(nazwa, 'w', 'utf-8')
    except:
        print("nie mogę otworzyć pliku")
        return 0

    #print("otwarcie pliku")
    plik.write('<html><head><meta charset="utf-8" /><title>eTablica - eTable</title><meta http-equiv="refresh" content="300"></head><body bgcolor="white"><center><canvas id="rysunek" width="'+str(width_e)+ '" height="'+str(height_e)+'" style="border:1px solid #d3d3d3; background-color: white;">Twoja przeglądarka nie obsłoguje "Canvas" więc nie wyświetlą się rysunki, rozwiązanie zainstalować inna przeglądarkę</canvas></center> <script> var x='+str(listax))


    plik.write('\n;var y='+str(listay)+'\n;var k='+str(kolor)+'\n;var i;var c = document.getElementById("rysunek");var ctx = c.getContext("2d");for (i = 0; i <x.length; i++) {if(k[i]=="blue"){ctx.beginPath();ctx.arc(x[i], y[i], 1, 0, 2 * Math.PI, false);ctx.closePath();ctx.strokeStyle = k[i];ctx.lineWidth = 3;ctx.stroke();}else if(k[i] == "magenta"){ctx.beginPath();ctx.arc(x[i], y[i], 1, 0, 2 * Math.PI, false);ctx.closePath();ctx.strokeStyle = k[i];ctx.lineWidth = 3;ctx.stroke();}else if(k[i] == "white"){ctx.beginPath();ctx.arc(x[i], y[i], 1, 0, 2 * Math.PI, false);ctx.closePath();ctx.strokeStyle = k[i];ctx.lineWidth = 9;ctx.stroke();}} </script> ')
    for i in range(bbb):

        linie=(tekst.get(str(i)+".0",str(i+1)+".0")) + "<br>"
        zami= linie.replace(" ", "&nbsp;")
        plik.write(zami)

    plik.write("</body></html>")
    plik.close()
    #print("zamknięcie pliku")
    przycisk.configure(state="active")
    przycisk1.configure(state="active")
def informacja():
    info = Tk()
    info.title("eTablica  - informacje o działaniu programu ")
    info.geometry("900x700")

    info_lab = Label(info,
                    bd=10,
                    text="""Program generuje pliki html które można wysłać np. za pomoca poczty email lub na        serwer FTP

Działanie:
Przyciśnięcie lewego przycisku myszy malowanie, przyciśnięcie prawego przycisku myszy
malowanie innm kolorem przyciśnięcie kółka skroll gumka

Białe pole tekstowe sluży do twożenia zwykłego tekstu. Umożliwia ono także używanie
znaczników HTML np: <b> pogrubiony tekst na stronie </b> itp.

Przycisk "generate" tworzy plik o nazwie etable"losowy numer".html,
twożony jest plik o takiej nazwie jaka znajduje się u góry programu na pasku tytułu.

Plik etable"losowy numer".html powstaje w miejscu gdzie znajduje sie program etable.exe

WAŻNE przyciśnięcie przycisku "generate" za każdym razem kasuje poprzedni plik
o nazwie znajdującej się na pasku tytułu programu umieszczając nowy plik html obok programu etable.exe
umożliwia to bierzącą aktualizację pliku do czasu zamknięcia okna.
Zanim okno nie zostanie zamknięte można wiele razy aktualizować plik np.etable12345.html
Ponowne uruchomienie programu utwoży kolejny losowy plik etable12346.html zwrócić szczególną
uwagę na numer pliku w pasku tytułu aby nie był taki sam jak numer wcześniejszych plików znajdujących się
obok programu gdyż zostaną zamienione. ROZWIĄZANIE uruchomić ponownie program gdy mamy
plik o tej samej nazwie obok programu etable.exe, zanim nie naciśnie się przycisku "generate"
nic nie bedzie zamienione.

Przycisk "send" wysyła plik etable"losowy numer".html za pomocą wbudowanego FTP port 21 na serwer WWW
Administrator serwera powinien utwożyć odpowiednie lokalizacje na pliki
Aby wysłać plik trzeba: podac nazwę serwera np: ' szkola.server.pl '
                              login do serwera        ' nauczyciel '
                              hasło do serwera             ' hasło '            pole z (*******)
          katalog w którym pliki bedą umieszczane ' chemia_klasa_7c'

    przykładowy rezultat plik dostępny na:               www.szkola.pl/chemia_klasa_7c/etable12345.html

funkolpl@gmail.com Białystok 2020

Działanie programu nie jest w 100% przetestowane i może zdażyć się jakiś problem
w białym polu tekstowym NIE WYSYŁĄĆ ŻADNYCH HASEL, LOGINÓW I DANYCH ZASTRZEŻONYCH

                """ ,
                height= 900,
                width = 700,
                font=(10),
                anchor=W,
                justify=LEFT)


    info_lab.pack(side = TOP)


    info.mainloop()


przycisk = tk.Button(frame,bg="#6666CC", text="?", command = informacja)
przycisk.pack(side = LEFT)
serwer = Entry(frame,bg="#99CC33", bd =5)
serwer.insert(END,"server")
serwer.pack(side = LEFT)
login = Entry(frame,bg="#99CC33", bd =5)
login.insert(END,"login")
login.pack(side = LEFT)
halo = Entry(frame, bg="#99CC33", show='*', bd =5)
halo.insert(END,"password")
halo.pack(side = LEFT)
kat = Entry(frame, bg="#99CC33", bd =5)
kat.insert(END,"")
kat.pack(side = LEFT)

przycisk1 = tk.Button(frame,bg="#996633", text="send", command = ftpa)
przycisk1.configure(state="disabled")
przycisk1.pack(side = LEFT)
przycisk = tk.Button(frame,bg="#6666CC", text="generate", command = wysylanie)
przycisk.pack(side = LEFT)
ksztalt = Canvas(okno,
           width=width_e,
           height=height_e,
           bd=0,
           bg='silver'
           )


ksztalt.pack()

tekst = tk.Text(okno,width=int(width_e),height=int(height_e),bg="white")
myscrollbar=Scrollbar(okno,orient="vertical",command=tekst.yview)
tekst.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")

tekst.pack()

def motionl(event):
    x, y = event.x, event.y
    #print('{}, {}'.format(x, y))
    listax.append(x)
    listay.append(y)
    kolor.append("blue")

    ksztalt.create_oval(x-1, y-1, x+3, y+3, outline='blue',fill = 'blue')

def motionp(event):
    x, y = event.x, event.y
    #print('{}, {}'.format(x, y))
    listax.append(x)
    listay.append(y)
    kolor.append("magenta")

    ksztalt.create_oval(x-1, y-1, x+3, y+3, outline='magenta',fill = 'magenta')

def erase(event):
    x, y = event.x, event.y
    #print('{}, {}'.format(x, y))
    listax.append(x)
    listay.append(y)
    kolor.append("white")
    ksztalt.create_oval(x-1, y-1, x+9, y+9, outline='silver',fill = 'silver')


ksztalt.bind('<B1-Motion>', motionl)
ksztalt.bind('<B3-Motion>', motionp)
ksztalt.bind('<B2-Motion>', erase)

okno.mainloop()


