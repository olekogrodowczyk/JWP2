from math import sqrt


class Vector3D:
    def __init__(self, x,y,z):
        self.x = x
        self.y=y
        self.z=z

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}"
    
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_z(self):
        return self._y
    
    def calculateVectorNorm(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, o):
        x = self.x + o.x
        y = self.y + o.y
        z = self.z + o.z
        return Vector3D(x,y,z) 
    
    def __sub__(self, o):
        x = self.x - o.x
        y = self.y - o.y
        z = self.z - o.z
        return Vector3D(x,y,z)
    
    def __mul__(self, skalar):
        self.x = self.x * skalar
        self.y = self.y * skalar
        self.z = self.z * skalar
   
    def dot(self, o):
        x = self.x * o.x
        y = self.y * o.y
        z = self.z * o.z
        return x + y + z
    
    def cross(self, o):
        return [self.y * o.z - self.z * o.y,
             self.z * o.x - self.x * o.z,
             self.x * o.y - self.y * o.x]
    
    def are_orthogonal(self, o):
        return self.dot(o) == 0

vector1 = Vector3D(2, 5, 8)
vector2 = Vector3D(2, 4, 8)

print(f'Vector1 x: {vector1.x}')
print(f'Vector1 y: {vector1.y}')
print(f'Vector1 z: {vector1.z}')

print(f'Vector2 x: {vector2.x}')
print(f'Vector2 y: {vector2.y}')
print(f'Vector2 z: {vector2.z}')

print(f'Vector1 norm: {vector1.calculateVectorNorm()}' )
print(f'Vector2 norm: {vector2.calculateVectorNorm()}' )

print(f'Sum: {vector1 + vector2}')
print(f'Sub: {vector1 - vector2}')
print(f'Dot: {vector1.dot(vector2)}')
print(f'Cross: {vector1.cross(vector2)}')
print(f'Are orthogonal: {vector1.are_orthogonal(vector2)}')

vector1 * 3
print(f'Vector1 skalar * 3: {vector1}')

vector2 * 2
print(f'Vector1 skalar * 2: {vector2}')
        
