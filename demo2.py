#ctrl+b
#1、导入Image类
from PIL import Image

#取出像素点的函数
def get_chars(pi):
	#用字符去替换像素点的颜色值
	for k in range(0,8):
		if pi < (k+1) * 32:
			return chars [7-k]
#保存文件的函数
def save(image_name,data):
	# 6、将保存的字符列表写入到文件中。
	f = open(image_name+'.txt','w')
	for d in data:
		#f.write(d)
		print(d,file=f)
	f.close()

if __name__ == '__main__':
	#2、使用Image 的对象读取图片
	image_name = 'logo1.jpg'
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
			line += get_chars(pi)
		data.append(line)

	#保存到文件，调用函数
	save(image_name,data)
	print('转换成功！')