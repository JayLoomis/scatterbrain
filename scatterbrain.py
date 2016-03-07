
# Projects are containers. Each has a due date, a priority, a contact list, a set of info links, and
# can contain other projects and lists of tasks.

# Tasks are chunks of work. They have an estimated number of time chunks to complete, and optionally a
# due date, priority, contact list, links, and lists of sub tasks.

# Chores are things that you get rewarded for doing on time. You can set them by time, and they'll get put
#  in the next administrative block until you check it off.

# Use case: Heavy email
# Things come up during the day. You should, for example, check your email in your five minute chunk cool
# down periods. Let's say you're looking at your mail and you see that you need to send a reply mail that's going
# to take time and effort to compose. This is a new task! You can easily start new tasks, and tasks needn't be
# associated with a particular project. When you create a new task, you can specify that you need to work on it
# in your next chunk, or add it to your current day with a simple command.

# Follow-ups are items that come up during a chunk. You can quickly add a follow-up, with a priority, and it will be
# added to the appropriate cool-down period automatically. It's easy to expand a follow-up to a stand-alone task or
# to a project. But you don't have to distract yourself with that level of scrutiny when you enter them.

# Some open issues:
# * How to differentiate between work-day and home tasks?

import datetime


class Contact:
    """
    Structure-style class for holding contact information.
    """

    def __init__(self, last, first, email, discipline=None, role=None, phone=None):
        self.__last_name = last
        self.__first_name = first
        self.__discipline = discipline
        self.__role = role
        self.__phone = phone
        self.__email = email

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, name):
        self.__last_name = name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, name):
        self.__first_name = name

    @property
    def discipline(self):
        return self.__discipline

    @discipline.setter
    def discipline(self, contact_discipline):
        self.__discipline = contact_discipline

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, contact_role):
        self.__role = contact_role

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone_number):
        self.__phone = phone_number

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, address):
        self.__email = address


class WorkItem:
    """
    The base class for tasks and projects.
    """
    def __init__(self):
        self.__description = None
        self.__due_date = None
        self.__priority = -1
        self.__contacts = []
        self.__info_links = None
        self.__tasks = None

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, desc):
        assert type(desc) == str, 'Value passed as a WorkItem description is not a string.'
        self.__description = desc

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, value):
        if value < -1 or value > 2:
            raise ValueError('Priority values must be between -1 and 2.')

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, date):
        if date < datetime.datetime.now():
            raise ValueError('Due dates must be in the future.')

    def add_contact(self, contact):
        # Validate the argument?

        self.__contacts.append(contact)

    def remove_contact(self, last, first):
        for index, contact in enumerate(self.__contacts):
            if contact.last_name == last and contact.first_name == first:
                del self.__contacts[index]
                return True

        # We'll only get to this point if the name isn't found
        return False









