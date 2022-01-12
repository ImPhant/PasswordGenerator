import random, json, sys

with open('config.json') as f:
    config = json.load(f)['config']

alphabet_low = config['alphabet_low']
alphabet_cap = config['alphabet_cap']
num = config['num']
simbols = config['simbols']

def script_help():
    print('\----------------------------------------------------------------/')
    print('|                              Help                              |')
    print('##################################################################')
    print('| Params:  Allow numbers (-n)                                    |')
    print('|          Allow simbols (-s))                                   |')
    print('| Caution: The first param must be the password lenght (number)! |')
    print('| Example: python3 ./main.py 15 -n -s                            |')
    print('##################################################################\n')

try:
    first_arg = sys.argv[1]
except Exception as error:
    print('Error: not enough params\n')
    script_help()
    quit()


allow_num = False
allow_simbols = False

for arg in sys.argv:
    if arg == '-n':
        allow_num = True
    elif arg == '-s':
        allow_simbols = True

if first_arg.isnumeric() is False:
    if first_arg == '-h':
        print('\nThis project was developed by Phant, you can discuss and suggest changes at: https://github.com/ImPhant/PasswordGenerator \n')
        script_help()
        quit()
        
    else:
        print('Error: invalid pass_len\n')
        script_help()
        quit()

print('##################################\n| Welcome to password generator! |\n##################################\n')

def create_pass(lenght, allow_num, allow_sim):
    password = ''

    if allow_num is True:
        if allow_sim is True:
            all = [alphabet_low, alphabet_cap, num, simbols]
        
        else:
            all = [alphabet_low, alphabet_cap, num]
    
    else:
        if allow_sim is True:
            all = [alphabet_low, alphabet_cap, simbols]

        else:
            all = [alphabet_low, alphabet_cap]
    
    for _ in range(0, lenght):
        character_type = random.choice(all)
        password += random.choice(character_type)
    
    print(f'Your password is: {password}\n\n')
    print('Thanks for using this project, here is the repository: https://github.com/ImPhant/PasswordGenerator')


create_pass(int(first_arg), allow_num, allow_simbols)
