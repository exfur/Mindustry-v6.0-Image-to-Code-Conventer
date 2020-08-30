from PIL import Image
out = open('output.txt','a')
img = Image.open('venv/Source/a7xyi-89d96.png','r')
pixel_values = list(img.getdata())
##print(pixel_values)
to_sort=[]
y = 80
x = 0
b = False
for i in range(0,len(pixel_values)):
    to_sort.append([])
    if (i % 80 == 0) and (b == True):
        y -= 1
        x = 0
    x += 1
    to_sort[i].append(str('draw color ' + str(pixel_values[i][0]) + ' ' + str(pixel_values[i][1]) + ' ' + str(pixel_values[i][2]) + ' 255 0 0'))
    to_sort[i].append(str('draw rect ' + str(x) + ' ' + str(y) + ' 1 1 0 0'))
    b = True
sort=sorted(to_sort)
out.write(sort[0][0]+'\n')
for i in range(1,len(pixel_values)):
    if sort[i-1][0] == sort[i][0]:
        out.write(sort[i][1]+'\n')
    else:
        out.write(sort[i][0]+'\n')
        out.write(sort[i][1]+'\n')
out.close()