Week01
	数组，链表，跳表。
	前两个没感觉到新意，数组是连续的存储空间查找较方便，链表存储分散用指针指向下一个元素增删较方便
	对跳表还是挺惊讶的，索引高度log n 每层查找的元素是3个，在linkedlist基础上添加索引，查找增删时间空间复杂度达到O(n)
	跳表：升维+空间换时间
	
	栈，队列，优先队列，双端队列
	栈和队列，先入先出，先入后出，插入删除都是O(1)
	两个栈可以实现队列的功能，两个队列可以实现栈的功能
	栈和队列的结合-双端队列Deque（Double ended queue）插入删除也都是O(1)
	
	优先队列，插入O(1)，取出O(logN)(按照优先级取出)
	底层实现的数据结构较为复杂，一般是heap，bst，treap，用时间换取可以按优先级取数
	即每次插入之后队列都是有序的	
	