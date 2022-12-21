class MyClass (object):
	pass

dir(Myclass) 
my_instance = MyClass()
dir(my_instance)
type(my_instance)


my_instance = MyClass()
MyClass.class_attribute = 'hello'
my_instance.instance_attribute = 'world'
dir(my_instance)
print(my_instance.__class__)
type(my_instance)
print(my_instance.instance_attribute)
print(my_instance.class_attribute)
print(MyClass.instance_attribute)
