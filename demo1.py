#ctrl+b
#1、导入Image类
from PIL import Image
#2、使用Image 的对象读取图片
image_name = 'logo.jpg'
img = Image.open(image_name)
#3、将图片转为灰度图像
img = img.convert('L')
img.save('fff.jpg')
#4、获取原图大小，并根据实际需要缩小图片
w,h = img.size
#如果图片太大，将高和宽做等比例缩放
if w > 100:
	h = int((100/w)*h)
	w = 100
#防止图片缩放时质量下降，增加滤镜处理
img = img.resize((w,h),Image.ANTIALIAS)
img.save('fff2.jpg')
# ctrl+/
# 5、将缩小的图片像素点的颜色值转为字符并存放到列表
data = []
#替换字符的列表(从左到右颜色是逐渐加深)
chars = [' ',',','1','+','n','D','@','M']
# 6、根据图片宽度和高度遍历像素点并取出每个像素点的颜色
for i in range(0,h):
	line = ''
	for j in range(0,w):
		#取出像素点的值
		pi = img.getpixel((j,i))
		#用字符去替换像素点的颜色值
		for k in range(0,8):
			if pi < (k+1) * 32:
				line += chars [7-k]
				break
	data.append(line)

# 6、将保存的字符列表写入到文件中。
f = open(image_name+'.txt','w')
for d in data:
#f.write(d)
	print(d,file=f)
f.close()
print('转换成功！')