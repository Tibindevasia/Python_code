
def conv_fah(cel):

    """Takes one integer argument for convert temperatures in degrees
    Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32."""

    while True:
        try:
            if type(cel) == int:
                fah = (cel * 9/5) + 32
                break
        except Exception as e:
            print("Enter a valid input", e)

    return fah

print(conv_fah(35))

