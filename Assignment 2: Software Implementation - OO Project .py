class Person:
    def __init__(self, name, phone_number, email):
        self._name = name
        self._phone_number = phone_number
        self._email = email

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_email(self, email):
        self._email = email

    # Getter methods
    def get_name(self):
        return self._name

    def get_phone_number(self):
        return self._phone_number

    def get_email(self):
        return self._email

class Guider(Person):
    def __init__(self, name, phone_number, email, job_id, position):
        super().__init__(name, phone_number, email)
        self._job_id = job_id
        self._position = position


    # Setter methods
    def set_job_id(self, job_id):
        self._job_id = job_id

    def set_position(self, position):
        self._position = position

    # Getter methods
    def get_job_id(self):
        return self._job_id

    def get_position(self):
        return self._position

    def create_and_print_guider(name, phone_number, email, job_id, position):
        guider = Guider(name, phone_number, email, job_id, position)
        print("Name:", guider.get_name())
        print("Phone Number:", guider.get_phone_number())
        print("Email:", guider.get_email())
        print("Job ID:", guider.get_job_id())
        print("Position:", guider.get_position())


class Guest(Person):
    def __init__(self, name, phone_number, email):
        super().__init__(name, phone_number, email)

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_email(self, email):
        self._email = email

    # Getter methods
    def get_name(self):
        return self._name

    def get_phone_number(self):
        return self._phone_number

    def get_email(self):
        return self._email

def create_guest(name, phone_number, email):
    # Create a Guest object
    guest = Guest(name, phone_number, email)
    return guest


class Artist(Person):
    def __init__(self, name, phone_number, email, date_of_birth, awards):
        super().__init__(name, phone_number, email)
        self._date_of_birth = date_of_birth
        self._awards = awards
        self._artifacts_contributed = []  # Initialize an empty list to store contributed artifacts

    # Setter methods
    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def set_awards(self, awards):
        self._awards = awards

    def set_artifacts_contributed(self, artifacts_contributed):
        self._artifacts_contributed = artifacts_contributed

    # Getter methods
    def get_date_of_birth(self):
        return self._date_of_birth

    def get_awards(self):
        return self._awards

    def get_artifacts_contributed(self):
        return self._artifacts_contributed

    def add_award_to_artist(self, new_award):
        self._awards.append(new_award)
        print(f"Award '{new_award}' has been added to {self.get_name()}'s awards list.")


class Ticket:
    def __init__(self, guest, ticket_number, price):
        # Check if a guest is provided
        if not isinstance(guest, Guest):
            raise ValueError("A ticket can only be created if there is a guest.")
        # this line is created to insure that there is combustion relationship between the ticket and the guest since the ticket wont exist if there is no guest
        self._guest = guest
        self._ticket_number = ticket_number
        self._price = price

    # Setter methods
    def set_guest(self, guest):
        self._guest = guest

    def set_ticket_number(self, ticket_number):
        self._ticket_number= ticket_number

    def set_price(self, price):
        self._price = price

    # Getter methods
    def get_guest(self):
        return self._guest

    def get_ticket_number(self):
        return self._ticket_number

    def get_price(self):
        return self._price


    def show_ticket_prices(self):
        # This function shows all ticket prices
        print("Ticket Prices:")
        print("- Adult Ticket: AED 50")
        print("- Child Ticket: Free (with valid ID)")
        print("- Senior Ticket: Free (with valid ID)")
        print("- Student Ticket: Free (with valid ID)")
        print("- Group Ticket: 50% discount")

class Activity:
    def __init__(self, title, description, date):
        self._title = title
        self._description = description
        self._datetime = date

    # Setter methods
    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_datetime(self, date):
        self._datetime = date

    # Getter methods
    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_datetime(self):
        return self._datetime


class Exhibition(Activity):
    exhibitions = []  # Class variable to store all exhibitions

    def __init__(self, title, description, date, theme, location):
        super().__init__(title, description, date)
        self._theme = theme
        self._location = location
        Exhibition.exhibitions.append(self)  # Add the current exhibition to the list of all exhibitions

    # Setter methods
    def set_theme(self, theme):
        self._theme = theme

    def set_location(self, location):
        self._location = location

    # Getter methods
    def get_theme(self):
        return self._theme

    def get_location(self):
        return self._location

    def show_all_exhibitions():
        # This function shows all different exhibitions in the museum
        print("All Exhibitions in the Museum:")
        for exhibition in Exhibition.exhibitions:
            print("- Title:", exhibition.get_title())
            print("  Description:", exhibition.get_description())
            print("  Theme:", exhibition.get_theme())
            print("  Location:", exhibition.get_location())
            print("  Date/Time:", exhibition.get_datetime())


class Tour(Activity):
    def __init__(self, title, description, date, location, theme):
        super().__init__(title, description, date)
        self._location = location
        self._theme = theme

    # Setter methods
    def set_location(self, location):
        self._location = location

    def set_theme(self, theme):
        self._theme = theme

    # Getter methods
    def get_location(self):
        return self._location

    def get_theme(self):
        return self._theme

    def explain_tour_briefly(self):
        # function that explains the tour briefly
        print(f"Tour: {self.get_title()}")
        print(f"Location: {self._location}")
        print(f"Theme: {self._theme}")
        print(f"Date: {self.get_datetime()}")
        print(f"Description: {self.get_description()}")

class Event(Activity):
    def __init__(self, title, description, date, duration, attendees):
        super().__init__(title, description, date)
        self._title = title
        self._description = description
        self._date = date
        self._duration = duration
        self._attendees = attendees


    # Setter methods
    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_date(self, date):
        self._date = date

    def set_duration(self, duration):
        self._duration = duration

    def set_attendees(self, attendees):
        self._attendees = attendees

    # Getter methods
    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_date(self):
        return self._date

    def get_duration(self):
        return self._duration

    def get_attendees(self):
        return self._attendees

    def show_event_location(self):
        # a function that shows the event location
        print(f"Event: {self.get_title()}")
        print(f"Date: {self.get_datetime()}")
        print(f"Description: {self.get_description()}")
        print(f"Duration: {self._duration}")
        print(f"Attendees: {self._attendees}")

class Artifact:
    previous_artifacts = []  # Class variable to store previous artifacts

    def __init__(self, name, date_of_creation, description):
        self._name = name
        self._date_of_creation = date_of_creation
        self._description = description
        Artifact.previous_artifacts.append(self)  # Add the current artifact to the list of previous artifacts

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_date_of_creation(self, date_of_creation):
        self._date_of_creation = date_of_creation

    def set_description(self, description):
        self._description = description

    # Getter methods
    def get_name(self):
        return self._name

    def get_date_of_creation(self):
        return self._date_of_creation

    def get_description(self):
        return self._description


    def add_to_previous(cls, artifact):
        # the function adds an artifact to the list of previous artifacts
        cls.previous_artifacts.append(artifact)
        print(f"Artifact '{artifact._name}' has been added to the previous artifacts.")

class Catalog:
    def __init__(self):
        self._exhibitions = []
        self._tours = []
        self._events = []
        self._artifacts = []

    # Setter methods
    def add_exhibition(self, exhibition):
        # Add an exhibition to the catalog
        self._exhibitions.append(exhibition)

    def add_tour(self, tour):
        # Add a tour to the catalog
        self._tours.append(tour)

    def add_event(self, event):
        # Add an event to the catalog
        self._events.append(event)

    def add_artifact(self, artifact):
        # Add an artifact to the catalog
        self._artifacts.append(artifact)

    # Getter methods
    def get_exhibitions(self):
        # Get the list of exhibitions in the catalog
        return self._exhibitions

    def get_tours(self):
        # Get the list of tours in the catalog
        return self._tours

    def get_events(self):
        # Get the list of events in the catalog
        return self._events

    def get_artifacts(self):
        # Get the list of artifacts in the catalog
        return self._artifacts



# person class example
person1 = Person("Khaled", "0561111", "khaled@gmail.com")

# guider class example
Guider.create_and_print_guider("Ahmed", "0525222", "ahmed@gmail.com", "01", "Senior Guider")

#guest class example
guest = create_guest("Saeed", "488448", "saeed@gmail.com")

# artist class example
artist = Artist("Leonardo da Vinci", "2323", "leonardo.com", "99999", ["The best"])
artist.add_award_to_artist("Lifetime Achievement Award")

# ticket class example
guest = Guest("ahmed", "737373", "ahmed@.com")
ticket = Ticket(guest, "12111", 50)
ticket.show_ticket_prices()

# activity class example
activity = Activity("Light show", "Enjoy van gogh star nights", "2024-04-10")
print("Title:", activity.get_title())
print("Description:", activity.get_description())
print("Date:", activity.get_datetime())

exhibition1 = Exhibition("Ancient Artifacts", "Exhibition showcasing artifacts from ancient civilizations", "2024-04-10", "Ancient History", "Gallery 1")
exhibition2 = Exhibition("Modern Art", "Contemporary art exhibition featuring works from modern artists", "2024-04-15", "Contemporary Art", "Gallery 2")

Exhibition.show_all_exhibitions()

#tour class example
tour = Tour("Historical Tour", "Explore the historical sites of the city", "2024-04-20", "City Center", "Historical Sites")
tour.explain_tour_briefly()

# event class example
event = Event("Art Exhibition", "Exhibition showcasing masterpieces from the Louvre collection", "2024-04-25", "3 hours", ["Art Enthusiasts", "Art Collectors"])
event.show_event_location()

#artifact class exmaple
artifact1 = Artifact("Venus", "100 BCE", "Ancient Greek goddesse")
Artifact.add_to_previous(Artifact, artifact1)

#catalog class example
catalog = Catalog()

# Add some exhibitions to the catalog
catalog.add_exhibition("Ancient Artifacts Exhibition")
catalog.add_exhibition("Modern Art Exhibition")

# Add some tours to the catalog
catalog.add_tour("Historical Tour")
catalog.add_tour("Art Tour")

# Add some events to the catalog
catalog.add_event("Tech Conference")
catalog.add_event("Music Concert")

# Add some artifacts to the catalog
catalog.add_artifact("Venus de Milo")
catalog.add_artifact("Mona Lisa")

# Retrieve and print the contents of the catalog
print("Exhibitions:", catalog.get_exhibitions())
print("Tours:", catalog.get_tours())
print("Events:", catalog.get_events())
print("Artifacts:", catalog.get_artifacts())

# Define classes and functions from your provided code...

def guest_actions():
    print("Welcome, Guest!")
    ticket_choice = input("Would you like to purchase a ticket? (yes/no): ").lower()
    if ticket_choice in ["yes", "y"]:
        print("Here are the available ticket options:")
        ticket = Ticket(None, "12345", 50)  # Creating a temporary ticket without a guest
        ticket.show_ticket_prices()
    elif ticket_choice in ["no", "n"]:
        print("You chose not to purchase a ticket.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

def guider_actions():
    print("Welcome, Guider!")
    event_choice = input("Which event would you like to monitor? (Enter event name): ")
    # Assuming there is a list of events somewhere that the guider can choose from
    print(f"You chose to monitor the event: {event_choice}")

def artist_actions():
    print("Welcome, Artist!")
    artifact_name = input("Enter the name of your artifact: ")
    date_of_creation = input("Enter the date of creation: ")
    description = input("Enter a description of your artifact: ")
    artifact = Artifact(artifact_name, date_of_creation, description)
    Artifact.add_to_previous(Artifact, artifact)

# Main menu function
def display_menu(role):
    print(f"Welcome! Are you a {role}?")
    print("1. Yes")
    print("2. No")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"You selected {role}.")
        if role == "Guest":
            guest_actions()
        elif role == "Guider":
            guider_actions()
        elif role == "Artist":
            artist_actions()
    elif choice == "2":
        print(f"You're not a {role}.")
        # Proceed with other options
        # For example:
        # other_actions()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        display_menu(role)

# Main menu
print("Welcome to the Museum!")

while True:
    print("1. Guest")
    print("2. Guider")
    print("3. Artist")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_menu("Guest")
    elif choice == "2":
        display_menu("Guider")
    elif choice == "3":
        display_menu("Artist")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


