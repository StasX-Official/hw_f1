#############################################################
# - - - - - - - - - - - HOMEWORK - - - - - - - - - - - - - -#
# - - - - - - - - project created as homework - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#By Kozosvyst_S for the STEP IT Academy Python Senior Course#
#############################################################
# Copyright (c) 2024 Kozosvyst Stas (StasX)
#############################################################

#DONATE -> https://ko-fi.com/stasx (18% of $199 goal!)

#ADVERTISING: Love what you do and make money too!!! -> https://ko-fi.com/

#####################################################################################################

class Player:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
    def __repr__(self):
        return f'{self.name} ({self.position})'

class Team:
    def __init__(self, name: str):
        self.name = name
        self.players = []
        
    def add_player(self, player: Player):
        self.players.append(player)
        
    def remove_player(self, player: Player):
        self.players.remove(player)

    def __repr__(self):
        return f'Team {self.name}: {", ".join(str(player) for player in self.players)}'


class Employee:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def __repr__(self):
        return f'{self.name} ({self.position})'

class Company:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, employee: Employee):
        self.employees.remove(employee)

    def __repr__(self):
        return f'Company {self.name}: {", ".join(str(emp) for emp in self.employees)}'


class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, employee: Employee):
        self.employees.remove(employee)

    def list_employees(self):
        return [str(emp) for emp in self.employees]

    def __repr__(self):
        return f'Department {self.name}: {", ".join(self.list_employees())}'
    
#####################################################################################################

#Owner: https://github.com/StasX-Official

#Copyright (c) 2024 Kozosvyst Stas (StasX)