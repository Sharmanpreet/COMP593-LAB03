
def main():

    # Define the complex data structure
    my_data = {
        'full_name': 'Sharmanpreet Kaur',
        'student_id': '10274523',
        'pizza_toppings': [
            'Sausage',
            'Extra cheese',
            'Tomato'
        ],
        'movies': [
            {
                'title': 'Dilwale',
                'genre': 'Romance'
            },
            {
                'title': 'Mohabbatein',
                'genre': 'Drama'
            }
        ]
    }

    # Add a new movie to the data structure
    new_movie = {'title': 'Uncharted', 'genre': 'Action'}
    my_data['movies'].append(new_movie)

    # Add some more pizza toppings to the data structure
    favourite_pizza_toppings = (['pineapple', 'bacon', 'hot pepper', 'sausage', 'pepperoni'])
    add_pizza_toppings_to_data(my_data, favourite_pizza_toppings)

    # Print information from the complex data structure
    print_my_student_id(my_data)
    print_pizza_toppings(my_data)
    print_movies_list(my_data)

    pass  

def print_my_name(data):
    name = f"My name is', {data['full_name']}, but you can call me Mam Sharman"
    
def print_my_student_id(data):
    sentence = f"My student ID is', {data['student_id']}"
    print(sentence)

def add_pizza_toppings_to_data(data, favourite_pizza_toppings):
    data['pizza_toppings'].extend(favourite_pizza_toppings)

    for i,p in enumerate(data['pizza_toppings']):
        data['pizza_toppings'][i] = p.capatalize()

        data['pizza_toppings'].sort()

def print_pizza_toppings(data):
    # Print the heading
    heading = f"{data['full_name']}'s favourite pizza toppings are:"
    print(heading)
    print('-' * len(heading))

    # Print dash list of all pizza toppings
    for p in data['pizza_toppings']:
        print(f"- {p}")
    print() 

def print_movies_list(data):

    # My favourite movies-
    print(f"{data['full_name'].split(' ')[1]} like to watch ", end='')
    for i,t in enumerate(data['movies']):
        print(g['genre'], end='')
        if i < len(data['movies'])-1:
            print(', ', end='')
    print('.', end='\n\n')        


main()