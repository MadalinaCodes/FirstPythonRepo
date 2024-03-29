import sqlite3
from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///marketplace2.db', echo=True) # echo arata fiecare query(log cu ora si actiunea) la rularea in python - vedem pasii in terminal


# conection = sqlite3.connect('marketplace.db')

# cursor = conection.cursor()

# conection.execute()

# cursor = conection.cursor()
#
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL,
#     email TEXT NOT NULL,
#     password TEXT NOT NULL
#     # facultate integer not null
#     );
#     """
# )

# CONCEPTUALIZARE PRIN INTERMEDIUL OOP
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key = True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))

# creates database
Base.metadata.create_all(engine)
#cream o sesiune pe baze de date
Session = sessionmaker(bind=engine)
sesiune = Session()

lista_useri = [
    {
        'username': 'dan',
        'email': 'dan@gmail.com',
        'password': 'asdan'
    },
    {
        'username': 'asgda',
        'email': 'dahgasgn@gmail.com',
        'password': 'asdjashan'
    },
    {
        'username': 'whatever',
        'email': 'dan@gmail.com',
        'password': 'asdan'
    }
]

#INSERT
# for element in lista_useri:
#     user = Users(**element)
#     sesiune.add(user)

# sesiune.commit()

# SELECT
all_entries = sesiune.query(Users).all()

for user in all_entries:
    print(f'{user.username}, {user.email}\n')

# SEARCH
users = sesiune.query(Users).filter_by(email='dan@gmail.com').all()
for user in users:
    print(user.username, user.email, user.password)


    # print(user.username, user.email)

# user_nou = Users(username='adrian', email='adrian@email.com', password='adrianbarosanul')

# #inseram un user nou
# sesiune.add(user_nou)
# sesiune.commit()






    # FUNCTIONALITATI BY DEFAULT PRIN

    # def all(self):
    #     pass




#
# exemplu pentru dorian
# select * from users
# where {user.username} == username or user.email == email
#
# == user = Users()
# if user.parola == password
#     show user dashboarb




#
# c = Users()
# c.username




# session.query(Users).all()



















