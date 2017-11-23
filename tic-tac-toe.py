from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"

      #사용자가 버튼을 선택할 때마다 가로, 세로, 대각으로 동일한 문자가 있는지 체크
      if list[0]["text"] == list[1]["text"] and list[1]["text"] == list[2]["text"] and list[2]["text"] != "     " :
            win(list[0]["text"])
      elif list[3]["text"] == list[4]["text"] and list[4]["text"] == list[5]["text"] and list[5]["text"] != "     " :
            win(list[3]["text"])
      elif list[6]["text"] == list[7]["text"] and list[7]["text"] == list[8]["text"] and list[8]["text"] != "     " :
            win(list[6]["text"])
      elif list[0]["text"] == list[4]["text"] and list[4]["text"] == list[8]["text"] and list[8]["text"] != "     " :
            win(list[0]["text"])
      elif list[2]["text"] == list[4]["text"] and list[4]["text"] == list[6]["text"] and list[6]["text"] != "     " :
            win(list[2]["text"])
      elif list[0]["text"] == list[3]["text"] and list[3]["text"] == list[6]["text"] and list[6]["text"] != "     " :
            win(list[0]["text"])
      elif list[1]["text"] == list[4]["text"] and list[4]["text"] == list[7]["text"] and list[7]["text"] != "     " :
            win(list[1]["text"])
      elif list[2]["text"] == list[5]["text"] and list[5]["text"] == list[8]["text"] and list[8]["text"] != "     " :
            win(list[2]["text"])

#가로, 세로, 대각으로 동일한 문자가 있었을때 호출되는 함수: 승리 메세지 출력
def win(play) :
      print(str(play) + "님이 이겼습니다!")
      quit()

#승리 메세지를 출력하고 호출되는 함수 : 버튼 기능 비활성화
def quit():
      for b in list:
            b["command"] = ""

            
window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


