--------------------
Arrays				|
--------------------
	# 专门用于操作数组的方法
	# 大都是静态方法

--------------------
Arrays-静态方法		|
--------------------
	
	String		toString(T[] t);
					* 打印出数组,以,号分隔每个单位
	List<T>		asList(T...t);
					* 把可变长数组转换为LIST集合
	Stream<T>	stream(T...t);
					* 转换为流
