class SymbolProperty:
    def __init__(self, type, value, level=0,signed=True):
        self.type = type
        self.value = value
        self.signed = signed
        self.level = level
    def get_type(self):
        return self.type
    def set_type(self, type):
        self.type = type
    def get_value(self):
        return self.value
    def set_value(self,value):
        self.value = value
    def get_signed(self):
        return self.signed
    def set_signed(self, signed):
        self.signed = signed
    def get_level(self):
        return self.level
    def set_level(self, level):
        self.level = level

class SymbolTable:
    def __init__(self):
        self.table = [{}]
        self.current_scope_level = 0

    def enterScope(self):
        self.current_scope_level += 1
        self.table.append({})
    
    def exitScope(self):
        if self.current_scope_level == 0:
            raise BaseException("exitScope error")
        self.table.pop()
        self.current_scope_level -= 1
    
    def addGlobal(self, name : str, property: SymbolProperty):
        if(self.table[0].get(name) != None):
            raise BaseException("global name already exist")
        property.set_level(0)
        self.table[0].update({name : property})
    
    def addLocal(self, name : str, property: SymbolProperty):
        if(self.table[self.current_scope_level].get(name) != None):
            raise BaseException("local name already exist")
        property.set_level(self.current_scope_level)
        self.table[self.current_scope_level].update({name : property})
    
    def getProperty(self, name : str) -> SymbolProperty:
        for i in range(self.current_scope_level, -1, -1):
            if(self.table[i].get(name) != None):
                return self.table[i].get(name)
        raise BaseException("name doesn't exist")
    
    def setProperty(self, name : str, value):
        for i in range(self.current_scope_level, -1, -1):
            if(self.table[i].get(name) != None):
                property = self.table[i].get(name)
                property.set_value(value)
                self.table[i].update({name : property})
                return
        raise BaseException("name doesn't exist")