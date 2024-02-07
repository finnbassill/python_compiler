



class Parse():
    
    def __init__(self):


    



    def __peek(self, offset = 0) -> str:
        if (self.i + offset >= len(self.file_str)):
            return None
        
        return self.file_str[self.i + offset]

    def __consume(self) -> str:
        temp_char = self.file_str[self.i]
        self.i += 1
        return temp_char
    