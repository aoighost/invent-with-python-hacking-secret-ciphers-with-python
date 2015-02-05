# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared
    translated = ''

    # the rest of the program is the same as the original Caesar program
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    print('Key #%s: %s' % (key, translated))
