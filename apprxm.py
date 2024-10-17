class Quad_Function:
    def __init__(self, c, xn):
        self._C = c
        self.xn = xn
    
    
    def get_y(self, x):
        return (x**2) - self._C
    
    
    def get_dy(self, x):
        return 2 * x
    
    
    def apprxm(self):
        x = self.xn
        for i in range(1, 10):
            x = x - self.get_y(x) / self.get_dy(x)
        
        return abs(x)
    
    
    def __str__(self):
        return f'\nf(x) = x^2 - {self._C}\n(x1) = {self.xn}\n'
    

if __name__ == '__main__':
    val = float(input('what value you want to find the sqrt of? '))
    x0 = float(input('give one first guess: '))
    func = Quad_Function(val, x0)
    
    print(func)
    
    print(f'Sqrt of {val} = {func.apprxm()}')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
