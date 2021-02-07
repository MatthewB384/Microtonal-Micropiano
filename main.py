from winsound import Beep
from tkinter import Tk,Button #BUTTON

window = Tk()
window.title('Piano')
window.geometry('316x155+52+52')

s = 1.0293
c = 261.63
cols = ['black','grey','white']
txts = ['  \n\n','\n\n\n','  \n\n\n\n\n']

notes = [
  [0,0,2],[2,4,2],[4,8,2],[6,10,2],[8,14,2],[10,18,2],[12,22,2],[14,24,2],
  [1,1,1],[2,3,1],[3,5,1],[4,7,1],[5.5,9,1],[7,11,1],[8,13,1],[9,15,1],[10,17,1],[11,19,1],[12,21,1],[13.5,23,1], #COMMENT OUT THIS LINE TO REMOVE MICROTONES
  [1,2,0],[3,6,0],[7,12,0],[9,16,0],[11,20,0]
]

for pos,note,col in notes:
  exec(f'''def c{note}():
  Beep(int({c*s**note}),200)''')
  Button(window,text=txts[col],font=('consolas',15),bg=cols[col],command=eval(f'c{note}')).place(x=pos*20,y=0)

  window.mainloop()
