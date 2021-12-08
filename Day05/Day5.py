def readfile(file):
    with open(file) as f:
        lines = [x for x in f.readlines()]
    return lines

def line(startpoint, endpoint):
    if (int(endpoint.split(',')[0])-int(startpoint.split(',')[0])) != 0:
        grad = (int(endpoint.split(',')[1])-int(startpoint.split(',')[1]))/(int(endpoint.split(',')[0])-int(startpoint.split(',')[0]))
    else:
        grad = None
    startx = int(startpoint.split(',')[0])
    endx = int(endpoint.split(',')[0])
    starty = int(startpoint.split(',')[1])
    endy = int(endpoint.split(',')[1])
    return({'grad': grad, 'startx': startx, 'endx':endx, 'starty': starty, 'endy':endy})

def main():
    input = readfile('input-5.txt')
    startpoints = [x.split('->')[0] for x in input ]
    endpoints = [x.split('->')[1] for x in input ]
    endpoints = [x.strip() for x in endpoints ]
    lines = [line(x[0], x[1]) for x in list(zip(startpoints, endpoints))]
    dangerpoints = []
    for  lin in lines:
        if lin['grad'] == None: # Vertical line
            for y in range(lin['starty'], lin['endy']+1):
                dangerpoints.append((lin['startx'], y))
            for y in range( lin['endy'], lin['starty'] +1):
                dangerpoints.append((lin['startx'], y))
        if lin['grad'] == 0: # Horizontal line
            for x in range(lin['startx'], lin['endx']+1):
                dangerpoints.append((x,lin['starty']))
            for x in range(lin['endx'], lin['startx'] +1):
                dangerpoints.append((x,lin['starty']))
    
    unique_danger = []
    double_danger = []
    for point in dangerpoints:  
        if (point not in unique_danger) and (point not in double_danger):
            unique_danger.append(point)
        elif point in unique_danger:
            unique_danger.remove(point)
            double_danger.append(point)
    print(f"horizontal and vertical lines are dangerous in {len(double_danger)} points!") 


    ################
    for  lin in lines:
        if lin['grad'] == 1: 
            for x in range(lin['startx'], lin['endx']+1):
                dangerpoints.append((x,lin['starty']+x-lin['startx']))
            for x in range(lin['endx'], lin['startx']+1):
                dangerpoints.append((x,lin['endy']+x-lin['endx']))

        if lin['grad'] == -1: 
            for x in range(lin['startx'], lin['endx']+1):
                dangerpoints.append((x,lin['starty']-x+lin['startx']))
            for x in range(lin['endx'], lin['startx']+1):
                dangerpoints.append((x,lin['endy']-x+lin['endx']))  

    unique_danger = []
    double_danger = []
    for point in dangerpoints:  
        if (point not in unique_danger) and (point not in double_danger):
            unique_danger.append(point)
        elif point in unique_danger:
            unique_danger.remove(point)
            double_danger.append(point)
    print(f"total danger in {len(double_danger)} points!") 


if __name__ == '__main__':
    main()