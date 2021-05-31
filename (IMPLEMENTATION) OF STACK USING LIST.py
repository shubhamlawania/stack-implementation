# STACK IMPLEMENTATION USING LIST (ALL OPERAIONS ----> PUSH,POP,DISPLAY,ISEMPTY,TOP)

#MAKING AN CLASS 
class stack_maker():
    def __init__(self):
        self.stack = []
        

    #IMPLEMENTING BASIC OPERATIONS LIKE ----> PUSH,POP
    def push(self,ele):
        (self.stack).append(ele)

    def pop(self) :
        self.stack.pop()
        #can also write as ---> (self.stack).pop()

    
    #OTHER OPERATIONS
    def display(self) :
        print(self.stack)
        
    #----NO USE OF THIS OPERATION AS ----> SIZE IS NOT PRE-DEFINED
    #def isfull(self):
    
    def isempty(self) :
        count = 0
        for ele in self.stack :
            count += 1
        if count == 0 :
            print("EMPTY STACK!")
        else:
            print("NOT EMPTY")
                       
    def top(self):
        print(self.stack[-1])
        


#####1.(TAKING INPUT AT COMPILE TIME)
        
print("TAKING INPUT AT ----->COMPILE TIME") 
new_stack = stack_maker()
#USING BASIC OPERATIONS ( with  display attribute )
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
new_stack.push(5)
new_stack.display()

new_stack.pop()
new_stack.pop()
new_stack.display()
# EXPLORTING OTHER OPERATIONS
new_stack.isempty()
new_stack.top()
new_stack.display()



####2. (TAKING ALL INPUT AT RUN TIME)
print("\n")
print("TAKING INPUT AT -----> RUN TIME")
new_stack_runtime = stack_maker()
repeat = True
while repeat == True :
    print("enter the operation you want to perform From (push,pop,display,isempty,top)")
    oper = input()

    if oper == 'push' :
        print("Enter a element to push in stakc: ")
        ele = input()
        new_stack_runtime.push(ele)
        print("WANT TO PERFORM MORE OPERATION?")
        value_rep = input()
        if value_rep == 'yes' or value_rep == 'y' :
            pass
        else :
            repeat = False
            
    elif oper == 'pop' :
        new_stack_runtime.pop()
        print("WANT TO PERFORM MORE OPERATION?")
        value_rep = input()
        if value_rep == 'yes' or value_rep == 'y' :
            pass
        else :
            repeat = False
            
    elif oper == 'display' :
        new_stack_runtime.display()
        print("WANT TO PERFORM MORE OPERATION?")
        value_rep = input()
        if value_rep == 'yes' or value_rep == 'y' :
            pass
        else :
            repeat = False
            
    elif oper == 'isempty' :
        new_stack_runtime.isempty()
        print("WANT TO PERFORM MORE OPERATION?")
        value_rep = input()
        if value_rep == 'yes' or value_rep == 'y' :
            pass
        else :
            repeat = False
            
    elif oper == 'top' :
        new_stack_runtime.top()
        print("WANT TO PERFORM MORE OPERATION?")
        value_rep = input()
        if value_rep == 'yes' or value_rep == 'y' :
            pass
        else :
            repeat = False
            
    else :
        print("INVALID OPERATION!")
        print("WANT TO PERFORM MORE OPERATION?")
        value_rep = input()
        if value_rep == 'yes' or value_rep == 'y' :
            pass
        else :
            repeat = False

