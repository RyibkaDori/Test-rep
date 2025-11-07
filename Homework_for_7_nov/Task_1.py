class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return ((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
    def __add__(self, other):
        assert isinstance(other, Vector), "Операция определена  только для векторов"
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
    def __sub__(self, other):
        assert isinstance(other, Vector), "Операция определена  только для векторов"
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        assert (isinstance(other, Vector) or isinstance(other, int) or isinstance(other, float))
        if isinstance(other, Vector):
            return (self.x*other.x + self.y*other.y + self.z*other.z)
        if (isinstance(other, int) or isinstance(other, float)):
            return Vector(self.x*other, self.y*other, self.z*other)
        else:
            raise ValueError(f'Эта операция не определена')
    def __rmul__(self, other):
        assert (isinstance(other, Vector) or isinstance(other, int) or isinstance(other, float))
        if (isinstance(other, int) or isinstance(other, float)):
            return Vector(self.x*other, self.y*other, self.z*other)
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


def input_vector():
    input_str = input("Введите координаты вектора (x,y,z): ")
    coords = [float(coord) for coord in input_str.split()]
    if len(coords) != 3:
        print("Ошибка: нужно ввести ровно 3 координаты")
        return None
    return Vector(coords[0], coords[1], coords[2])
def mass_center(spisok_tochek):
    C_M = Vector(0, 0 ,0)
    for vec in spisok_tochek:
        C_M += vec*((N)**(-1))
    return C_M

N = int(input('Введите количество точек:'))
Spisok_tochek = []
for i in range(N):
    vec = input_vector()
    Spisok_tochek.append(vec)
    if vec is None:
        vec = Vector(0,0,0)
        Spisok_tochek.append(vec)
center_mass = mass_center(Spisok_tochek)
#print(center_mass)
Max_S = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if ((Spisok_tochek[i].x/Spisok_tochek[j].x) == (Spisok_tochek[i].y/Spisok_tochek[j].y) == (Spisok_tochek[i].z/Spisok_tochek[j].z)) and ((Spisok_tochek[i].x/Spisok_tochek[k].x) == (Spisok_tochek[i].y/Spisok_tochek[k].y) == (Spisok_tochek[i].z/Spisok_tochek[k].z)):
                continue
            if i == N-2:
                break
            if j == N-1:
                continue
            st1 = abs(Spisok_tochek[j] - Spisok_tochek[i])
            st2 = abs(Spisok_tochek[k] - Spisok_tochek[i])
            st3 = abs(Spisok_tochek[k] - Spisok_tochek[j])
            p = (st1 + st2 + st3)/2
            S = (p*(p-st1)*(p-st2)*(p-st3))**(0.5)
            if S > Max_S:
                Max_S = S
print(Max_S)
