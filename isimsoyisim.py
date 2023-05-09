from mimesis import Person


def generate_names(country, num_names):
    person = Person(locale=country)
    name_list = []
    for i in range(num_names):
        name_list.append(person.full_name())
    return name_list
