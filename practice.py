# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# def main():
#     None
    
# __name__ == '__main__'

# map = [([1] * MAP_WIDTH)] + ([([1] + ([0] * (MAP_WIDTH - 2)) + [1]) for _ in range(MAP_HEIGHT) - 2)]) + [([1] * MAP_WIDTH)]
                             
# map = [([1] * MAP_WIDTH)] + ([1] + ([0] * ((MAP_WIDTH — 2) + [1])) for _ in range(MAP_HEIGHT — 2) + [([1] * MAP_WIDTH)])


# class Player:
#     def __init__(self, x, y):
#         self.id = 2
#         self.coords = [x, y]
#         self.attributes = {
#             "level": 1,
#             "xp": 0,
#             "Health": 80,
#             'Mana' == 'Energy': 20,
#             "Strength": 7,
#             "Defense": 4
#         }
#         self.weapon = ["None", 0]
#         self. armor = ["Basic Chainmail"]
#         self.role = ["Paladin", "Bard", "Rogue", "Ranger"]
#         self.inventory = []
#         self.spells = []
#         self.skills = []

#     def __repr__(self):
#         return f"Player {self.role} Beginner Stats: {self.attributes}"

#     def __len__(self):
#         return len(self.attributes)

#     def __getitem__(self, i):
#         return self.attributes[i]

#     def __setitem__(self, i, v):
#         self.attributes[i] = v

#     def __delitem__(self, i):
#         del self.attributes[i]
        