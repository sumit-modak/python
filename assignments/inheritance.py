class vec2:
    def __init__(self, X, Y):
        x = X
        y = Y

class vec3(vec2):
    def __init__(self, X, Y, Z):
        super.__init__(self, X, Y)
        z = Z

v2 = vec2(3, 2)
v3 = vec3(2, 4, 1)

print(" {} {} {} ".format(v3.x, v3.y, v3.z))