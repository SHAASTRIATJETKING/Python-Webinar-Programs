import random

loweralfabets = "abcdefghijklmnopqrstuvwxyyz"

upperalfabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbersfrom0to9 = "0123456789"

Special_Symbols = "[]{}#()*;._$-@&!^?/\|<>"

all_requirements_to_generate_a_password = loweralfabets + \
    upperalfabets+numbersfrom0to9+Special_Symbols

Captcha_Requirements = loweralfabets+upperalfabets+numbersfrom0to9

length = 6

StrongPassword = " ".join(random.sample(
    all_requirements_to_generate_a_password, length))

Captcha = " ".join(random.sample(Captcha_Requirements, length))

print("****Congratulations, The Strong Password generated successfully to you****")
print()
print(StrongPassword)

print()

print("************************The Captcha Generated Successfully******************")
print()
print(Captcha)
