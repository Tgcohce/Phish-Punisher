import requests
import random
import string
from concurrent.futures import ThreadPoolExecutor

thread_count = 99


def generate_random_user():
    names = [
        "James", "John", "Robert", "Michael", "William", "David", "Richard",
        "Charles", "Joseph", "Thomas", "Christopher", "Daniel", "Paul", "Mark",
        "Donald", "George", "Kenneth", "Steven", "Edward", "Brian", "Ronald",
        "Anthony", "Kevin", "Jason", "Matthew", "Gary", "Timothy", "Jose",
        "Larry", "Jeffrey", "Frank", "Scott", "Eric", "Stephen", "Andrew",
        "Raymond", "Gregory", "Joshua", "Jerry", "Dennis", "Walter", "Patrick",
        "Peter", "Harold", "Douglas", "Henry", "Carl", "Arthur", "Ryan",
        "Roger", "Joe", "Juan", "Jack", "Albert", "Jonathan", "Justin",
        "Terry", "Gerald", "Keith", "Samuel", "Willie", "Ralph", "Lawrence",
        "Nicholas", "Roy", "Benjamin", "Bruce", "Brandon", "Adam", "Harry",
        "Fred", "Wayne", "Billy", "Steve", "Louis", "Jeremy", "Aaron", "Randy",
        "Howard", "Eugene", "Carlos", "Russell", "Bobby", "Victor", "Martin",
        "Ernest", "Phillip", "Todd", "Jesse", "Craig", "Alan", "Shawn",
        "Clarence", "Sean", "Philip", "Chris", "Johnny", "Earl", "Jimmy",
        "Antonio", "Danny", "Bryan", "Tony", "Luis", "Mike", "Stanley",
        "Leonard", "Nathan", "Dale", "Manuel", "Rodney", "Curtis", "Norman",
        "Allen", "Marvin", "Vincent", "Glenn", "Jeffery", "Travis", "Jeff",
        "Chad", "Jacob", "Lee", "Melvin", "Alfred", "Kyle", "Francis",
        "Bradley", "Jesus", "Herbert", "Frederick", "Ray", "Joel", "Edwin",
        "Don", "Eddie", "Ricky", "Troy", "Randall", "Barry", "Alexander",
        "Bernard", "Mario", "Leroy", "Francisco", "Marcus", "Micheal",
        "Theodore", "Clifford", "Miguel", "Oscar", "Jay", "Jim", "Tom",
        "Calvin", "Alex", "Jon", "Ronnie", "Bill", "Lloyd", "Tommy", "Leon",
        "Derek", "Warren", "Darrell", "Jerome", "Floyd", "Leo", "Alvin", "Tim",
        "Wesley", "Gordon", "Dean", "Greg", "Jorge", "Dustin", "Pedro",
        "Derrick", "Dan", "Lewis", "Zachary", "Corey", "Herman", "Maurice",
        "Vernon", "Roberto", "Clyde", "Glen", "Hector", "Shane", "Ricardo",
        "Sam", "Rick", "Lester", "Brent", "Ramon", "Charlie", "Tyler",
        "Gilbert", "Gene", "Marc", "Reginald", "Ruben", "Brett", "Angel",
        "Nathaniel", "Rafael", "Leslie", "Edgar", "Milton", "Raul", "Ben",
        "Chester", "Cecil", "Duane", "Franklin", "Andre", "Elmer", "Brad",
        "Gabriel", "Ron", "Mitchell", "Roland", "Arnold", "Harvey", "Jared",
        "Adrian", "Karl", "Cory", "Claude", "Erik", "Darryl", "Jamie", "Neil",
        "Jessie", "Christian", "Javier", "Fernando", "Clinton", "Ted",
        "Mathew", "Tyrone", "Darren", "Lonnie", "Lance", "Cody", "Julio",
        "Kelly", "Kurt", "Allan", "Nelson", "Guy", "Clayton", "Hugh", "Max",
        "Dwayne", "Dwight", "Armando", "Felix", "Jimmie", "Everett", "Jordan",
        "Ian", "Wallace", "Ken", "Bob", "Jaime", "Casey", "Alfredo", "Alberto",
        "Dave", "Ivan", "Johnnie", "Sidney", "Byron", "Julian", "Isaac",
        "Morris", "Clifton", "Willard", "Daryl", "Ross", "Virgil", "Andy",
        "Marshall", "Salvador", "Perry", "Kirk", "Sergio", "Marion", "Tracy",
        "Seth", "Kent", "Terrance", "Rene", "Eduardo", "Terrence", "Enrique",
        "Freddie", "Wade", "Mary", "Patricia", "Linda", "Barbara", "Elizabeth",
        "Jennifer", "Maria", "Susan", "Margaret", "Dorothy", "Lisa", "Nancy",
        "Karen", "Betty", "Helen", "Sandra", "Donna", "Carol", "Ruth",
        "Sharon", "Michelle", "Laura", "Sarah", "Kimberly", "Deborah",
        "Jessica", "Shirley", "Cynthia", "Angela", "Melissa", "Brenda", "Amy",
        "Anna", "Rebecca", "Virginia", "Kathleen", "Pamela", "Martha", "Debra",
        "Amanda", "Stephanie", "Carolyn", "Christine", "Marie", "Janet",
        "Catherine", "Frances", "Ann", "Joyce", "Diane", "Alice", "Julie",
        "Heather", "Teresa", "Doris", "Gloria", "Evelyn", "Jean", "Cheryl",
        "Mildred", "Katherine", "Joan", "Ashley", "Judith", "Rose", "Janice",
        "Kelly", "Nicole", "Judy", "Christina", "Kathy", "Theresa", "Beverly",
        "Denise", "Tammy", "Irene", "Jane", "Lori", "Rachel", "Marilyn",
        "Andrea", "Kathryn", "Louise", "Sara", "Anne", "Jacqueline", "Wanda",
        "Bonnie", "Julia", "Ruby", "Lois", "Tina", "Phyllis", "Norma", "Paula",
        "Diana", "Annie", "Lillian", "Emily", "Robin", "Peggy", "Crystal",
        "Gladys", "Rita", "Dawn", "Connie", "Florence", "Tracy", "Edna",
        "Tiffany", "Carmen", "Rosa", "Cindy", "Grace", "Wendy", "Victoria",
        "Edith", "Kim", "Sherry", "Sylvia", "Josephine", "Thelma", "Shannon",
        "Sheila", "Ethel", "Ellen", "Elaine", "Marjorie", "Carrie",
        "Charlotte", "Monica", "Esther", "Pauline", "Emma", "Juanita", "Anita",
        "Rhonda", "Hazel", "Amber", "Eva", "Debbie", "April", "Leslie",
        "Clara", "Lucille", "Jamie", "Joanne", "Eleanor", "Valerie",
        "Danielle", "Megan", "Alicia", "Suzanne", "Michele", "Gail", "Bertha",
        "Darlene", "Veronica", "Jill", "Erin", "Geraldine", "Lauren", "Cathy",
        "Joann", "Lorraine", "Lynn", "Sally", "Regina", "Erica", "Beatrice",
        "Dolores", "Bernice", "Audrey", "Yvonne", "Annette", "June",
        "Samantha", "Marion", "Dana", "Stacy", "Ana", "Renee", "Ida", "Vivian",
        "Roberta", "Holly", "Brittany", "Melanie", "Loretta", "Yolanda",
        "Jeanette", "Laurie", "Katie", "Kristen", "Vanessa", "Alma", "Sue",
        "Elsie", "Beth", "Jeanne", "Vicki", "Carla", "Tara", "Rosemary",
        "Eileen", "Terri", "Gertrude", "Lucy", "Tonya", "Ella", "Stacey",
        "Wilma", "Gina", "Kristin", "Jessie", "Natalie"
    ]

    def generate_password():
        # choose random line of password form the password.txt file
        with open('pass.txt') as f:
            lines = f.readlines()
            return random.choice(lines).strip()

    domains = [
        "hotmail.com", "gmail.com", "aol.com", "mail.com", "yahoo.com",
        "outlook.com", "icloud.com", "protonmail.com"
    ]
    name = random.choice(names)
    domain = random.choice(domains)
    digits = "".join([random.choice(string.digits) for i in range(4)])
    username = name + digits + "@" + domain
    passwrd = generate_password()
    return username, passwrd


def main():
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = [
            executor.submit(generate_random_user) for _ in range(thread_count)
        ]
        url = ''

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    c = 0
    for future in futures:
        print(c + 1, "th request")
        username, passwd = future.result()
        data = {'email': username, 'password': passwd}

        try:
            print(data)
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()  # Raise an error for bad status codes
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")

            #print(f"Response Text: {response.text}") # website html because regardless of the input it will say invalid credentials
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        c += 1


main()
