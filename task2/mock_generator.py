import random
import string

domains = ["hotmail.com", "gmail.com", "aol.com", "mail.ua", "mail.by", "yahoo.com"]

names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Charles", "Joseph", "Thomas",
                  "Christopher", "Daniel", "Paul", "Mark", "Donald", "George", "Kenneth", "Steven", "Edward", "Brian",
                  "Ronald", "Anthony", "Kevin", "Jason", "Matthew", "Gary", "Timothy", "Jose", "Larry", "Jeffrey",
                  "Frank", "Scott", "Eric", "Stephen", "Andrew", "Raymond", "Gregory", "Joshua", "Jerry", "Dennis",
                  "Walter", "Patrick", "Peter", "Harold", "Douglas", "Henry", "Carl", "Arthur", "Ryan", "Roger"]

lastnames = ["Huang", "Reid", "Bass", "Pitts", "Lee", "Forbes", "Flynn", "Olson", "Finley", "Shepherd", "West",
             "Houston", "Pugh", "Snow", "Herman", "Simon", "Atkins", "Davidson", "Bernard", "Marsh", "Shields", "Noble",
             "Vazquez", "Johns", "Wade", "Lynn", "Curtis", "Mccormick", "Mccall", "Valentine", "Bean", "Allison",
             "Cardenas", "Rojas", "Sexton", "Scott", "Russo", "Bartlett", "Patel", "Clay", "Dillon", "Orr", "Lin",
             "Hammond", "Romero", "Fernandez", "Campos", "Buckley", "Freeman", "Daniel"]

cities = ["Honaunau ", "Montreal ", "Stonehouse ", "Muskogee ", "Preesall ", "Fort Pierce ", "Victoria ", "Glassboro ",
          "Overland Park ", "Wauchope ", "Framlingham ", "Bloomfield ", "Gainesville ", "McCook ", "Towcester ",
          "Whitman ", "Seymour ", "Oswestry ", "Whaley Bridge ", "East Retford ", "Durant ", "Frome ", "Kilgore ",
          "Livingston ", "Saint Charles ", "Hemsworth ", "Barton-upon-Humber ", "Leighton-Linslade ", "Hannibal ",
          "Hazard ", "Chester ", "Jim Thorpe ", "Melksham ", "Florissant ", "Goshen ", "Valparaiso ", "Darlington ",
          "Oshawa ", "Coleshill ", "Nampa ", "Weirton ", "Oak Park ", "Albuquerque ", "Telluride ", "Perc ", "Corinth ",
          "Attleboro ", "Hamilton ", "Wadhurst ", "Manningtree"]

countries = ["Venezuela", "Cuba", "Rwanda", "Sudan", "Montserrat", "Northern Mariana Islands", "American Samoa",
             "Guinea-Bissau", "Zimbabwe", "British Indian Ocean Territory", "Japan", "Sint Maarten", "South Georgia",
             "Switzerland", "Dominican Republic"]


def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


def get_random_from(array):
    return array[random.randint(0, len(array) - 1)]


def generate_random_email(username_length):
    return random_char(username_length) + '@' + domains[random.randint(0, len(domains) - 1)]


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


print("Type number on lines to generate: ")
data_number = int(input())
for i in range(data_number):
    print(generate_random_email(random.randint(3, 20)),
          get_random_from(names),
          get_random_from(lastnames),
          get_random_from(cities),
          get_random_from(countries),
          random_with_N_digits(9),
          sep=", ")
