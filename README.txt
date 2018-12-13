##########################
### KEY CODE GENERATOR ###
##########################
by Sigurd J. Setså
––––––––––––––––––––––––––



There are 4 functions that are included into this generator.

- key_generator #Generates a unique key that can be used to identify a purchase.
- key_printer #Transforms key into printable layout. (If no key is given, will also
generate a unique key.
- key_stripper #Strips keys of their printed state in order to store them properly.
- key_checker # Checks if key is in list.

By default, the program will use key_printer to generate and print a key in the
proper format. If you'd like to choose a different size, simply change size=15 to
whatever number you'd like in key_generator. Note that for every fifth character,
key_printer will also print a "-" for easier visibility. Therefore I either suggest
choosing a size that can be multiplied by 5, or to change the key_printer code.

Keys are stored in keys.txt.

Thank you for trying out my code!