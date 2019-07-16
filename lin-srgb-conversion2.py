#color conversion linear to srgb

from math import *

def main():   

# for red
    red = int(input("enter red: "))  # get value as int; rgb has no decimal

    r = red/255  # divide by 255

    # conversion formula:
    # if your number is less than or equal to 0.040448,
        # you divide again by 12.92, then move to the next step.
    # if it's not less than or equal to, you just go to the next step.

    # take your number and add 0.055
    # take that sum and then divide by 1.055
    # take that quotient and raise to the power of 2.4 -- x ^ 2.4
    
    if(r <= 0.0404482362771082):
        x = r/12.92
    else:
        x = pow(((r+0.055)/1.055), 2.4)

    print("srgb value is", round(x,5))  # print result rounded to 5 dec places

# for green
    green = int(input("enter green: "))

    g = green/255

    if(g <= 0.0404482362771082):
        y = g/12.92
    else:
        y = pow(((g+0.055)/1.055), 2.4)

    print("srgb value is", round(y,5))

# for blue
    blue = int(input("enter green: "))

    b = blue/255

    if(b <= 0.0404482362771082):
        z = b/12.92
    else:
        z = pow(((b+0.055)/1.055), 2.4)

    print("srgb value is", round(z,5))

main()
