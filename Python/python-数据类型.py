----------------------------
python-数据类型				|
----------------------------
	str			
	int			
	float
	list
	set
	dict
	tuple
	Iterator	# 迭代器
	Iterable	# 可迭代对象

---------------------------
python-数据类型				|
----------------------------
	Numbers
		# 数字
		# 类型
			整形('Python3中没有长整型和短整型')
			浮点形
			复数

	String
		# 字符串

	Boolean
		# 布尔值

	List
		# 列表
			arr = [1,2,'3']					//直接创建
			arr = list([1,2,3]);			//通过数组创建...
	Tuple
		# 元组
			tup = (1,2,3,'3',[236,'1'])		//直接创建
			tup = tuple([1,2,3]);			//通过现有数组创建
			
	Sets
		# 集合,通过全局函数创建			
			sets = set([1,3])				//通过函数创建,使用数组初始化,且数组元素中不可以嵌套数组
			sets = {1,2,3,4}				//直接创建

	Dictionaries
		# 字典
			dic = dict({1:2,3:4})		//通过函数创建
			dic = {1:'123','213':1}		//直接创建

	None
		# 空值
			


----------------------------
python-Numbers				|
----------------------------
	# Integral
		* boolean 与 int
	# 在boolean 中，0 与 False 表示 False,其他任意整数都表示 True
	# 在 int 中，True 表示1 ,False 表示 0
		x = 4
		x + = True // x += 1
	# 整数大小受限于机器的内存
	# 进制表示
		* 十进制	默认
		* 二进制	0b10101			//0b/B开头
		* 八进制	0o5567			//0o/O开头
		* 十六进制	0XA25DE			//0x/X开头

	# 判断字符串是不是数字
		x = "556"
		x.isdigit();
			* x,中不能有空格,返回 False
			* 只有'x是整数字符串',才会返回 Ttue

----------------------------
python-Boolean				|
----------------------------
	# 在python中仅仅只有两个值
		True False	

		* 只要是非零数值,非空字符串,非空list,非 None 等。都可以认为是 True,否则为False
	

		
	

----------------------------
python-集合框架				|
----------------------------
	List
	Tuple
	Set
	Dict
	