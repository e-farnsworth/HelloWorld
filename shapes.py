# This will help you calculate the shapes areas.

def main():
    tri_area = calc_tri_area(4,7)
    print(f'the area of the triangle is {tri_area}')

def calc_tri_area(base, height):
    area = base * height / 2
    return area

main()
