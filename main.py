from pyscript import display, document

# clubs
def club_cooking(e):
    club1 = {'Club Name' : 'Cooking Club',
        'Description' : 'Where young, aspiring ghouls practice their cooking skills to help feed others in the Creepteria.',
        'Meeting Time' : '3:00-5:00',
        'Location' : 'Creepteria Kitchen',
        'President' : 'Deuce Gorgon',
        'Number of Members' : '20',
        'Category' : 'Non-Academic'
    }

    
keys = ['Club Name', 'Description', 'Meeting Time', 'Location', 'President', 'Number of Members', 'Category']
values = ['Cooking Club', 'Where young, aspiring ghouls practice their cooking skills to help feed others in the Creepteria.', '3:00-5:00', 'Creepteria Kitchen', 'Deuce Gorgon', '20', 'Non-Academic']

club1 = dict(zip(keys, values)) # convert and combine
display(values, target='output_clubs')




def club_science(e):
    club2 = {'Club Name' : 'Mad Science Club',
            'Description' : 'In search of the greater good with science!',
            'Meeting Time' : '2:00-4:30',
            'Location' : 'Gymnasium',
            'President' : 'Frankie Stein',
            'Number of Members' : '25',
            'Category' : 'Academic'
    }


keys2 = ['Club Name', 'Description', 'Meeting Time', 'Location', 'President', 'Number of Members', 'Category']
values2 = ['Mad Science Club', 'In search of the greater good with science!', '2:00-4:30', 'Gymnasium', 'Frankie Stein', '25', 'Academic']

club2 = dict(zip(keys, values)) # convert and combine
display(values2, target='output_clubs')




def club_growl(e):
    club3 = {'Club Name' : 'Growl Choir',
            'Description' : 'A place where people can growl and sing their hearts out.',
            'Meeting Time' : '3:00-4:30',
            'Location' : 'Clawditorium',
            'President' : 'Scarah Screams',
            'Number of Members' : '38',
            'Category' : 'Non-Academic'
    }


keys3 = ['Club Name', 'Description', 'Meeting Time', 'Location', 'President', 'Number of Members', 'Category']
values3 = ['Growl Choir', 'A place where people can growl and sing their hearts out.', '3:00-4:30', 'Clawditorium', 'Scarah Screams', '38', 'Non-Academic']

club3 = dict(zip(keys, values)) # convert and combine
display(values3, target='output_clubs')




def club_gym(e):
    club4 = {'Club Name' : 'Gymnastics Club',
            'Description' : 'A time for gymnasts to show their true potential in competitions.',
            'Meeting Time' : '3:00-5:00',
            'Location' : 'Gymnasium',
            'President' : 'Toralei Stripe',
            'Number of Members' : '15',
            'Category' : 'Non-Academic'
    }


keys4 = ['Club Name', 'Description', 'Meeting Time', 'Location', 'President', 'Number of Members', 'Category']
values4 = ['Gymnastics Club', 'A time for gymnasts to show their true potential in competitions.', '3:00-5:00', 'Gymnasium', 'Toralei Stripe', '15', 'Non-Academic']

club4 = dict(zip(keys, values)) # convert and combine
display(values4, target='output_clubs')



# grades calculator
def getting_genaverage(e):

    first_name = document.getElementById('fname').value
    last_name = document.getElementById('lname').value

    subject1 = float(document.getElementById('eng').value)
    subject2 = float(document.getElementById('mathymatiks').value)
    subject3 = float(document.getElementById('sci').value)
    subject4 = float(document.getElementById('socsci').value)
    subject5 = float(document.getElementById('lang').value)
    subject6 = float(document.getElementById('fil').value)

    number_of_days = [5, 5, 5, 3, 3, 3]
    Fanglish, Clawculus, Biteology, Hisstory, Gore_Languages, Fanglipino = number_of_days

    weighted_final = (subject1 * Fanglish) + (subject2 * Clawculus) + (subject3 * Biteology) + (subject4 * Hisstory) + (subject5 * Gore_Languages) + (subject6 * Fanglipino)
    
    final_message = f"""To {first_name} {last_name}, here are your grades\n
    Fanglish: {subject1}\n
    Clawculus: {subject2}\n
    Biteology: {subject3}\n
    Hisstory: {subject4}\n
    Gore Languages: {subject5}\n
    Fanglipino: {subject6}\n
    your total weighted average is: {round(weighted_final, 2)}"""

    display(final_message, target="output_grades")





