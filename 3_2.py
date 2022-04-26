#сериализация и десериализация на yaml
import yaml
from yaml.loader import SafeLoader

user = {'UserName': 'Alex',
        'Password': 'NaniOmaiwaShinderu',
        'phone': '+375333333333',
        'AccessKeys': ['EmployeeTable',
                       'SoftwaresList',
                       'HardwareList']}

with open('data.yaml', 'w') as dj:
    yaml.dump(user, dj, sort_keys=False)

with open('data.yaml', 'r') as dj:
    loaded = yaml.load(dj, Loader=SafeLoader)  
    print(loaded)
