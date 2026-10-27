class employee:
    def __init__ (self):
        print ("Employee object created")

    def __del__ (self):
        print ("Employee object deleted")

def create_obj():
    print ("Making obj")
    obj = employee ()
    print ("func end")
    return obj

print ("Obj created")
create_obj ()