import tkinter as tk
import sqlite3 as sql

win=tk.Tk()
win.geometry("600x600")
win.resizable(False,False)

def add():
    ism=entryism.get()
    yosh=int(entryyosh.get())
    con=sql.connect("data.db")
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS uquvchi
    (ism VARCHAR,yosh INTEGER)''')
    cur.execute('''INSERT INTO uquvchi(ism,yosh)
    VALUES(?,?)''',(ism,yosh))
    con.commit()
    cur.close()
    con.close()
    entryism.delete(0,tk.END)
    entryyosh.delete(0,tk.END)

def chiqar():
    con = sql.connect("data.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS uquvchi
        (ism VARCHAR,yosh INTEGER)''')
    cur.execute("SELECT * FROM uquvchi")
    text=""
    for i in cur:
        text+=f"{i[0]} {i[1]}\n"
        label.config(text=text)






entryism=tk.Entry(win,width=15,font=(False,20))
entryism.pack()

entryyosh=tk.Entry(win,width=15,font=(False,20))
entryyosh.pack()

label=tk.Label(win,width=20,height=10,bg="black",fg="red",font=(False,20))
label.pack()

tugma=tk.Button(win,text="Q'oshish",command=add)
tugma.pack()

tugma2=tk.Button(win,text="chiqar",command=chiqar)
tugma2.pack()

win.mainloop()