        
def unpack(user_input):
    
    
    inputs_list = user_input.split(" ")
    if len(inputs_list) != 2:
        raise ValueError("Input must be two parts. i.e number + unit")
    
    
    number, unit1 = inputs_list
    try:
        number = float(number)
        return number, unit1
    except ValueError:
        print(f'Cant convert {number} to float')
            
            
def calculate(number, unit1):
    units = {
        'kg': number / 2.205, #Default
        'km': number * 1.609, #Default
        'c': (number - 32) * 5/9, #Default
        'lb': number * 2.205, # *
        'miles':number / 1.609, # /
        'f': (number * 9/5) + 32
    }
    if unit1 == 'kg' or unit1 == 'km' or unit1 == 'c':
        if unit1 == 'kg':
            return f"{round(number)} kg is {round(units['lb'])} lbs"
        if unit1 == 'km':
            return f"{round(number)} km is {round(units['miles'])} miles"
        if unit1 == 'c':
            return f"{round(number)}C° is {round(units['f'])}F°"

    
    if unit1 == "lb" or unit1 == 'miles' or unit1 == 'f':
        if unit1 == 'lb':
            return f"{round(number)} lb is {round(units['kg'])} kg"
        if unit1 == 'miles':
            return f"{round(number)} miles is {round(units['km'])} km"
        if unit1 == 'f':
            return f"{round(number)} F° is {round(units['c'])}C°"

def main():
    while True:
        try:
            user_input = input('Type in your conversion: ')
            unpacked = unpack(user_input)
            print(calculate(*unpacked))
            break
        except (ValueError, TypeError):
            print('Input must be two parts. i.e number + unit')
            

if __name__ == '__main__':
    main()