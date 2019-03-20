import json
import termcolor

f= open("person.json", 'r')

person = json.load(f)

print()


for elem in person:
    termcolor.cprint('Name: ', 'green', end='')
    print(elem['FirstName'], elem['Lastname'])

    termcolor.cprint('Age: ', 'green', end='')
    print(elem['Age'])

    for i, num in enumerate(elem['Phonenumber']):
        termcolor.cprint('Phone {}:'.format(i),'yellow')
        termcolor.cprint("  Type: ",'blue', end='')
        print(num['type'])


        termcolor.cprint("  Number: ", 'blue', end='')
        print(num['number'])

