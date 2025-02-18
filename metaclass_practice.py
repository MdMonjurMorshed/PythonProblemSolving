class MetaClass(type):
    _instance = {}
    def __new__(cls,name,bases,dict):
        if len(name)<=5:
            return {"error":"class name should contain above 5 character"}
        print(f"this is {cls}")
        print(f"this is {name}")
        print(f"this is {bases}")
        print(f"this is {dict}")
        
        return super().__new__(cls,name,bases,dict)
   
    def __call__(clss,*args,**kwargs):
        print(f" call method in metaclass is called")
        ## for making instanse unique or singleton
        
        # if clss  not in clss._instance:
        #     clss._instance[clss] = super().__call__(*args,**kwargs)


        # return clss._instance[clss]
        instance = super().__call__(*args, **kwargs)
        return instance
    
    def __init__(cls,name,bases,dict):
        print(dict['__init__'])
        print(f"initialize is called for {name}")
        return super().__init__(name,bases,dict)
    
class One(metaclass=MetaClass):
    def __init__(self,x):
        
        self.x=10 

one_obj = One(5)
obj_one = One(6)
print(one_obj==obj_one)