#In-class Exercises – Exceptions
class OutOfRange(Exception):
     pass
    #  def __init__(self, msg: object) -> None:
    #       super().__init__(msg)
def input_in_range(mn,mx):
    while True:
        try:
            value=int(input('Enter a value between range:'))
            if value>=mn and value<=mx:
                return value
            else:
                 raise  OutOfRange('Value out of range')
        except ValueError as ve:
             print('Please enter an int value')
        except Exception as e :
             print(type(e) ,e)
def create_list(n,mn,mx):
    l=[]
    try:
        for i in range(n):    
                l.append(input_in_range(mn,mx))
    except Exception as e:
         print(type(e),e,'c')
                 
    return l
try:
    f=open('my_list.txt','w')
    f.write(str(create_list(3,1,100)))
finally:
    f.close()
    print('file closed')


class InvalidWithdrawl(Exception):
    def __init__(self,msg,b=0,a=0) -> None:
         self.amount=a
         self.balance=b
         super().__init__(msg)

    def deficit(self):
         print(f'Your deficit is {abs(self.amount-self.balance)}')
total_balance=1000
amount=int(input('Enter amount to be drawn from the account: '))
try:
    if amount>total_balance:
        raise InvalidWithdrawl('You do not have enough',total_balance,amount)
except InvalidWithdrawl as obj:      #this line is important if i remove obj then my pattern changes
    print(obj)
    obj.deficit()


#2 
class NotList(Exception):
    pass      
try:
    print('hhhh')
    f=open('my_list.txt')
    content=eval(f.read())
    if not isinstance(content,list):
        raise NotList('Content is not list type')

except FileNotFoundError as fee:
     print('File does not exist',type(fee),fee)
except NotList as e:
    print('The file does not contain a list',type(e),e)
except Exception as e:
    print('File is empty',type(e),e)
else:
    print('Total integers in the list are',len(content))
finally:
    f.close()
    # pass