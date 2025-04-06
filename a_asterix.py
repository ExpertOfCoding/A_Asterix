from itertools import chain
import tkinter as tk
from math import sqrt
map=[
    [0,0,0,2],
    [0,0,0,0],
    [0,0,0,0],
    [1,0,0,0]
]
sp=[]
ep=[]
def print_the_map():
  global map
  for i in range(len(map)):
    for j in range(len(map[i])):
      print("no : ", map[i][j][1])
      if map[i][j][1]==[1]:
        print("yeas")
        for z in buttonlist:
          print(z[1], (i+3,j+1))
          if z[1]==(i+3,j+1):
            z[0].config(bg="yellow")
def visual(paths):
  for z in buttonlist:
    if z[1]==(paths[0]+3,paths[1]+1):
        z[0].config(bg="yellow")
def paint_layout(paths):
  for i in paths:
    for z in buttonlist:
      if z[1]==(i[0]+3,i[1]+1):
        z[0].config(bg="yellow")

def rst(start=None,end=None,size=4,obstacles = None):
  global continueloop,map,sp,ep
  s = int(size)
  
  if start==None:
    sp = start = (s-1,0)
  else:
    sp = start
  if end==None:
    ep = end  = (0,s-1)
  else:
    ep = end
  print("Start sp : ",sp ,ep)
  map=[
  ]
  for i in range(0,s):
    map.append([])
    for j in range(0,s):
      if obstacles!=None:
        if (i,j) in obstacles:
          map[i].append([-1,0])
          continue
      if (i,j)==sp:
        map[i].append([1,0])
      elif (i,j)==ep:
        map[i].append([2,0])
      else:
        map[i].append([0,0])
  map[sp[0]][sp[1]]=[1,0]
  map[ep[0]][ep[1]]=[2,0]
  continueloop = True
  print_map()
  print("SP: ",sp," EP: ",ep)
  return map
def print_map():
  global map
  for i in range(0,len(map)):
    for j in range(0,len(map[i])):
      print(map[i][j],end=" ")
    print()
def calculate_distance_to_starting_point(y,x):
  return int(sqrt(abs(sp[0]-y)**2 + abs(sp[1]-x)**2)*10)
def calculate_distance(y,x):
  return int(sqrt(abs(sp[0]-y)**2 + abs(sp[1]-x)**2)*10)+int(sqrt(abs(ep[0]-y)**2 + abs(ep[1]-x)**2)*10)
continueloop = True
def calculating(y,x):
  global continueloop
  try:
    if map[y][x][0]==0:
      if map[y][x][1]==0:
        print(y,x," is calculating")
        map[y][x][0]=calculate_distance(y,x)
        return
    elif map[y][x][0]==2:
      print("shortest way is found")
      continueloop = False
      return
  except:
    print("y,x is no in map")
def find():
  global continueloop,map,sp,ep
  if sp==ep:
    print("shortest way is no")
  else:
    sps = sp[0]
    spe = sp[1]
    eps = ep[0]
    epe = ep[1]
    print("sps,spe,eps,epe",sps,spe,eps,epe)
    while continueloop:
      if spe != 0:
        calculating(sps,spe-1)
      calculating(sps,spe+1)
      if sps != 0:
        calculating(sps-1,spe)
      calculating(sps+1,spe)
      if sps -1 >= 0 and spe -1 >= 0:
        calculating(sps-1,spe-1)
      if sps -1 >= 0 and spe +1 < len(map[0]):
        calculating(sps-1,spe+1)
      if sps +1 < len(map) and spe -1 >= 0:
        calculating(sps+1,spe-1)
      if sps +1 < len(map) and spe +1 < len(map[0]):
        calculating(sps+1,spe+1)
      if continueloop==False:
        break
      sl=[]
      for i in range(0,len(map)):
        for j in range(0,len(map[i])):
          c=[map[i][j][0],(i,j)]
          if c[0] not in (0,1,2,-1) and map[i][j][1] != [1]:
            sl.append(c)
      sl.sort()
      print("SL : ",sl)
      sps = sl[0][1][0]
      spe = sl[0][1][1]
      map[sps][spe][1]=[1]
      print_map()
      print("SP: ",sp," EP: ",ep)
    print_map()
    print("END POİNT : ",eps,epe)
    def points(p:tuple,path):
      ps=[]
      for i,j in [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]:
        try:
          print(p[0],p[1])
          if map[p[0]+i][p[1]+j][0] == 1 and not(p[0]==0 and i==-1) and not(p[1]==0 and j==-1):
            print("yeasssssirrr")
            return (p[0]+i,p[1]+j),path
          if map[p[0]+i][p[1]+j][1] == [1] and (p[0]+i,p[1]+j) not in path  and not(p[0]==0 and i==-1) and not(p[1]==0 and j==-1):
            ps.append( (p[0]+i,p[1]+j) )
        except:
          pass
      def have_neighbors(position,others):
        for a,b in [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]:
          try:
            if map[position[0]+a][position[1]+b][1] == [1] and (position[0]+a,position[1]+b) in others  and not(position[0]==0 and a==-1) and not(position[1]==0 and b==-1) and (position[0],position[1]) != others[-1] :
              print("NEW POİNT :" ,position , "NEİGHBOR  : ",position[0]+a,position[1]+b)
              return True
          except:
            pass
        return False
      if len(ps) == 0:
        pps=[]
        for i in range(len(map)):
          for j in range(len(map[i])):
            if map[i][j][1] == [1] and (i,j) and have_neighbors((i,j),path):
              pps.append((i,j))
        pps.sort(key=lambda x : calculate_distance_to_starting_point(x[0],x[1]))
        new_point = pps[0]
        print("NEW POİNT : ", new_point)
        for i,j in [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]:
          try:
            print(p[0],p[1])
            if map[new_point[0]+i][new_point[1]+j][1] == [1] and (new_point[0]+i,new_point[1]+j) in path  and not(new_point[0]==0 and i==-1) and not(new_point[1]==0 and j==-1):
              path=path[:path.index((new_point[0]+i,new_point[1]+j))+1]
              path.append((new_point[0],new_point[1]))
              print("FOUND İNDEX : ", path[-1])
              return path[-1], path
          except:
            pass
      ps.sort(key=lambda x : calculate_distance(x[0],x[1]))
      print(ps)
      return ps[0],path
    path=[]
    shortests,path=points(endP,path)
    path.append(shortests)
    while shortests != startP:
      print(path)
      shortests,path=points(shortests,path=path)
      path.append(shortests)
    paint_layout(path)
    

window = tk.Tk()
buttonlist=[]
obstaclelist=[]
startP=()
endP=()
def start_the_game():
  global obstaclelist,map,sp,ep,startP,endP
  print(obstaclelist,map,sp,ep)
  new_map = rst(size=int(Entry.get()),obstacles=obstaclelist,start=startP,end=endP)
  find()



def handleclick(row,column):
  global buttonlist,startP,endP
  for i in range(len(buttonlist)):
    if len(startP)==0 and buttonlist[i][1]==(row,column):
      startP=(row-3,column-1)
      buttonlist[i][0].config(bg="green")
    elif len(endP)==0 and buttonlist[i][1]==(row,column):
      endP=(row-3,column-1)
      buttonlist[i][0].config(bg="blue")
    elif (row-3,column-1)!=startP and (row-3,column-1)!=endP and buttonlist[i][1]==(row,column):
      obstaclelist.append((row-3,column-1))
      buttonlist[i][0].config(bg="red")

          

def button_clicked():
  global buttonlist,startP,endP
  print("BUTTON LİST : ",buttonlist)
  if len(buttonlist) != 0:
    print("not emt")
    for i in buttonlist:
      i[0].destroy()
      buttonlist=[]
  startP=()
  endP=()
  create_grid()
def create_grid():
  for i in range(3,int(Entry.get())+3):
    for j in range(1,int(Entry.get())+1):
      button = tk.Button(window, command=lambda row=i, column=j: handleclick(row, column), height = 3, width = 6,bg="gray")
      buttonlist.append([button,(i,j)])
      button.grid(row=i, column=j)
  start_button = tk.Button(text="Start",command=start_the_game)
  start_button.grid()
  buttonlist.append([start_button,()])
window.title("Path Finder")
window.geometry("800x600")
Label = tk.Label(window, text="Enter the map size")
Label.grid(row=0,column=0)
Entry = tk.Entry()
Entry.grid(row=1,column=0)
Button = tk.Button(text="Press To Create",command=button_clicked)
Button.grid(row=2,column=0)
# Create grid of 25
# buttons

window.mainloop()

