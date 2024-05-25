def desided(password):
    alfavit_EU =  'abcdefghigklmnopqrstuvyxwz12345678№;#%*90ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smeshenie = 7
    message = password
    itog = ''
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
    return (itog)

def ensided(password):
    alfavit_EU =  'abcdefghigklmnopqrstuvyxwz12345678№;#%*90ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smeshenie = 7
    message = password
    itog = ''
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto - smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
    return (itog)