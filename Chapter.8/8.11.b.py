# encoding: utf-8
def describePerson(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
    try:
        print('Occupation:' + person['occupation'])
    except KeyError:
        pass


person_1 = {'name': 'Throatowbbler Mangrove', 'age': 42}
introPersion = describePerson(person_1)
person_2 = {'name': 'Throatowbbler Mangrove', 'age': 42, 'occupation': 'camper'}
introPersion = describePerson(person_2)
