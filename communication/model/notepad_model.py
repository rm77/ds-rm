import shelve
import uuid
import os

class Notepad:
    def __init__(self):
        self.dbfile = 'notepad.db'
        self.db = shelve.open(self.dbfile,writeback=True)
    def list(self):
        data = []
        try:
            for i in self.db.keys():
                data.append(dict(id=i,data=self.db[i]))
            return dict(status='OK',data=data)
        except:
            return dict(status='ERR',msg='Error')
    def create(self,info):
        try:
            id = str(uuid.uuid1())
            self.db[id] = info
            return dict(status='OK',id=id)
        except:
            return dict(status='ERR',msg='Can not create entry')
    def delete(self,id):
        try:
            del self.db[id]
            return dict(status='OK',msg=f'entry {id} deleted', id=id)
        except:
            return dict(status='ERR',msg='Can not delete entry')
    def update(self,id,info):
        try:
            self.db[id]=info
            return dict(status='OK',msg=f'entry {id} updated', id=id)
        except:
            return dict(status='ERR',msg='')
    def read(self,id):
        try:
            return dict(status='OK',id=id,data=self.db[id])
        except:
            return dict(status='ERR',msg=f'entry {id} not found')



if __name__=='__main__':
    from datetime import datetime
    np = Notepad()
#    ----------- create
    date_info_str = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    data = dict(date=date_info_str,content=f'this is entry date {date_info_str}')
    r = np.create(info=data)
    print(r)

    date_info_str = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    data = dict(date=date_info_str,content=f'this is entry date {date_info_str}')
    r = np.create(info=data)
    print(r)

#    ------------ list
    print(np.list())
