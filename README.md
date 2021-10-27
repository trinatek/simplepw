# SimplePW  
Simple password generator class. Generates a user-customized, random password. Supports special characters, digits, uppercase, lowercase. Passwords will have at least one of every specified character type. The minimum password length is 4 characters.  

# Instructions  

    from src.simplepw.simplepw import SimplePW  
    
    """  
    Default settings for password options are:
    - Password length:           10
    - Special characters:     False
    - Digits:                  True
    - Uppercase:               True
    - Lowercase:               True
    """  
    
    # EXAMPLE 1: Create and configure a SimplePW object, then generate.

    SPW = SimplePW()  
    SPW.length = 12  
    SPW.special_chars = True  
    SPW.uppercase = True  
    SPW.lowercase = True  
    password = SPW.get()  

    # EXAMPLE 2: Create a password with default settings.
    default_password = SimplePW().get()  

    # EXAMPLE 3: Create a password with custom options in one line.  
    custom_password = SimplePW(length=50, digits=True, uppercase=False, lowercase=False).get()  
    
# Dependencies  
Python standard library: random, string  

# License  
MIT License  

# Install
Install editable package to ./src/simplepw  

    pip install -e git+https://github.com/trinatek/simplepw#egg=simplepw 
