class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        print(h)
        found =False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))
    def __getitem__(self,key):
        h = self.get_hash(key)
        return h,self.arr[h]
   

t = HashTable()
t['saleek']=18
t['kalees']=20
t['sinan']=100
print(t['saleek'])
print(t.arr)
