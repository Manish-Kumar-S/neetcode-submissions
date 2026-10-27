class LinkedList:
    
    def __init__(self):
        self.ll = []
        self.size = 0

    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.ll[index]
        

    def insertHead(self, val: int) -> None:
        self.size += 1
        self.ll.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        self.size += 1
        self.ll.append(val)
        

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        self.ll.pop(index)
        self.size -= 1
        return True
        

    def getValues(self) -> List[int]:
        return self.ll
        
