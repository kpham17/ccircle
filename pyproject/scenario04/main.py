import ccircle
import connection
import math

con = connection.create()
con.send('set_name', {'name': 'Spoofed1'})

while True:
    a = con.send('get_reward_ids')
    mr = []
    for x in a:
        z = con.send('get_reward_pos',{'id':x})
        if z != None:
            mr.append(z)
    x1,y1= con.send('get_pos')
    print(con.send('get_pos'))
    md = 0
    target = []
    for x2,y2 in mr:
        distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
        if distance > md:
            md = distance
            target = [x2,y2]

    print(target)
    xd = x1 - target[0]
    yd = y1 - target[1]

    c = max(abs(xd),abs(yd))
    xd *= 50/c
    yd *= 50/c
    print(xd)
    print(yd)
    con.send('set_velocity',{'vx':xd,'vy':yd})

# Write code to make money and kill the evil cat!
# See readme.txt !