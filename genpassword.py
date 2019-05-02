def genpassword():
    import random
    strength = input('How strong do you want your password, weak is 0, medium is 1 and strong is 2')
    if strength == 0:
        snum = 6
    elif strength == 1:
        snum = 9
    else:
        snum = 12
    sample = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?()"
    password = "".join(random.sample(sample,snum))
    print(password)