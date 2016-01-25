
def  doesCircleExist( commands):
    slow_x,slow_y = 0,0
    fast_x,fast_y = 0,0
    slow_dir = "n"
    fast_dir = "n"
    slow,fast = 0,0
    l = len(commands)
    i=0
    while slow<=2500 and slow<l:
        slow_x,slow_y,slow_dir = move(slow_x,slow_y,commands[slow],slow_dir)
        if fast == l:
            fast = 0
        fast_x,fast_y,fast_dir = move(fast_x,fast_y,commands[fast],fast_dir)
        fast +=1
        if fast == l:
            fast = 0
        fast_x,fast_y,fast_dir = move(fast_x,fast_y,commands[fast],fast_dir)
        fast +=1
        slow+=1
        if slow_x == fast_x and slow_y == fast_y:
            return False
        return True
# return the position after move
def move(x,y,command,dir):
    if command == "G":
        if dir == "n":
            x +=1
        elif dir == "s":
            x-=1
        elif dir == "e":
            y+=1
        elif dir == "w":
            y-=1
    if command == "L":
        if dir == "n":
            dir = "w"
        elif dir == "w":
            dir = "s"
        elif dir == "s":
            dir = "e"
        elif dir == "e":
            dir = "n"
    if command == "R":
        if dir == "n":
            dir = "e"
        elif dir == "w":
            dir = "n"
        elif dir == "s":
            dir = "w"
        elif dir == "e":
            dir = "s"
    return x,y,dir
print doesCircleExist("L")