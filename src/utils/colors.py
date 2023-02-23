class Colors():
    def color(self, string, number, brigth, bg=False):
        if bg:
            num = "4" 
        else:
            num = "3"
        return f"\033[{str(brigth)};{num}{str(number)}m" + string + "\033[m"


    def red(self, string, brigth=0, bg=False):
        return self.color(string, 1, brigth, bg)


    def green(self, string, brigth=0, bg=False):
        return self.color(string, 2, brigth, bg)
    

    def yellow(self, string, brigth=0, bg=False):
        return self.color(string, 3, brigth, bg)
    

    def blue(self, string, brigth=0, bg=False):
        return self.color(string, 4, brigth, bg)
    
    
    def magenta(self, string, brigth=0, bg=False):
        return self.color(string, 5, brigth, bg)
    

    def cyan(self, string, brigth=0, bg=False):
        return self.color(string, 6, brigth, bg)
    

    def white(self, string, brigth=0, bg=False):
        return self.color(string, 7, brigth, bg)
    

colors = Colors()
