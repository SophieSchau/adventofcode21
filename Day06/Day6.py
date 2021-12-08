import multiprocessing as mp

def readfile(file):
    with open(file) as f:
        lines = [x for x in f.readlines()]
    return lines

def uniques(list_a):
    set_a = {}
    for el in set(list_a):
        set_a[el]=list_a.count(el)
    return(set_a)

def n_decendants(birthdays, day, n=0):
    if all(x == 0 for x in birthdays.values()):
        return(n)
    
    child_birthdays = {}
    for cb in range(-8,day+1):
        child_birthdays[cb]=0

    for bd in birthdays:
        f = birthdays[bd]
        duration = day-bd
        if duration < 0:
            continue
        n_bd = int((duration-2)/7)
        n = n + n_bd*f
        c_bd = ([ bd+2+(x+1)*7 for x in range(n_bd)])
        
        for cb in c_bd:
            child_birthdays[cb]=child_birthdays[cb]+f
    
    return n_decendants(child_birthdays, day, n)

def main():
    start_cond = readfile('input-6.txt')
    birthdays = [int(x)-8 for x in start_cond[0].split(',') ]
    bd = uniques(birthdays)
    n = n_decendants(bd, 80, len(birthdays))
    print(f"{n} fish after 80 days!")
    
    m = n_decendants(bd, 256, len(birthdays))
    print(f"{m} fish after 256 days!")   
    
#    m = 0
#    pool = mp.Pool(processes=len(set(birthdays)))
#    outputs = [pool.apply_async(n_decendants, args=([bd], 256, 1)) for bd in set(birthdays)]
#    results = [p.get() for p in outputs]
#    for ii in range(len(results)):
#        n_parents = birthdays.count(set(birthdays)[ii])
#        m = m + results[ii]*n_parents
#    
#    print(f"{m} fish after 256 days!")
    

    


if __name__ == '__main__':
    main()