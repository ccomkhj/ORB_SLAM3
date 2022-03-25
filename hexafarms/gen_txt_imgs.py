frame_num = 1471
f = open('rgb.txt', 'w+')

for i in range(frame_num):
    f.write('%f rgb/frame%d.png\n' %(0.3*(i+1), i+1))

f.close()