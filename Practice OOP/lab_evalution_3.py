print('This is Lab evaluation 3')
class Publication:
    def get_data(self):
        self.title=input('Enter the title:')
        self.price=int(input('Enter the price'))
    def put_data(self):
        print(f'Title:{self.title}\nPrice:{self.price}')
    
class Book(Publication):

    def get_data(self):
        super().get_data()
        self.page_count=int(input('Enter the page count:'))
    def put_data(self):
        super().put_data()
        print(f'Page Count:{self.page_count}')
    
class Tape(Publication):
    def get_data(self):
        super().get_data()
        self.playing_time=int(input('Enter the time in minute:'))
    def put_data(self):
        super().put_data()
        print(f'Time:{self.playing_time}')
b1=Book()
b1.get_data()
b1.put_data()
t1=Tape()
t1.get_data()
t1.put_data()

class Disk(Publication):
    def get_data(self):
        d={'c':'CD','d':'DVD'}
        super().get_data()
        self.disk_type=d[input('Enter c or d   ')]
    def put_data(self):
        super().put_data()
        print('your type is:',self.disk_type)
d=Disk()       
d.get_data()
d.put_data()

        

