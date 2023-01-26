def getUserFloat(prompt):
    userFloat = float(0.0)
    while float(userFloat) <= 0.0:
        userFloat = input(prompt)
        try:
            float(userFloat) <= 0.0
        except ValueError:
            print('Input a float, not a string.')
    return userFloat
