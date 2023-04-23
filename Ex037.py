# Numbering System Converter

n = int(input("Type any decimal number: "))
convertion = int(input("Choose the numbering system to convert:\n"
                       "Type \033[33m1\033[m to \033[33mbinary\033[m\n"
                       "Type \033[35m2\033[m to \033[35moctal\033[m\n"
                       "Type \033[34m3\033[m to \033[34mhexadecimal\033[m\n"))
if convertion == 1:
    print("\033[33m{}".format(bin(n)[2:]))
elif convertion == 2:
    print("\033[35m{}".format(oct(n)[2:]))
elif convertion == 3:
    print("\033[34m{}".format(hex(n)[2:]))
else:
    print("\033[31mInvalid input, choose between 1-3")
