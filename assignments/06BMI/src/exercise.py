def main():
    #escribe tu código abajo de esta línea
import math
weight=float(input("Give me your weight in kg:"))
height=float(input("Give me your height in meters"))
BMI=((weight)/(height**2))
print("Your Body Max Index is", BMI)
if BMI<20:
    print("underweight")
if 20<=BMI<25:
    print("normal")
if 25<=BMI<30:
    print("overweight")
if 30<=BMI<40:
    print("obesity")
if BMI>=40:
    print("morbid obesity")   
pass
if __name__=='__main__':
    main()
