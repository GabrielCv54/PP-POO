from sqlalchemy import create_engine, Column, Integer, String,ForeignKey, Text,DECIMAL,Date
from sqlalchemy.orm import relationship, sessionmaker,declarative_base

engine = create_engine('sqlite:///clube.db')
Session = sessionmaker(bind=engine)
session= Session()

Base=declarative_base()


class Time(Base):
    __tablename__='Time_Futebol'
    
    presidente=Column(String)
    name=Column(String,primary_key=True)
    ano_fundacao=Column(Integer)
    executive=Column(String)
    liga=Column(String)

    def __init__(self,presidente,name,ano,executive):
       self.presidente = presidente
       self.name = name
       self.ano = ano
       self.executive = executive
       self.liga = []

    def add_club(clube):
        new_club = session.query(Time).filter_by(name=clube).first()
        if not clube:
           new_club = Time(name=clube)
           session.add(new_club)
           session.commit()
    
    def add_president(name):
       new_president = session.query(Time).filter_by(presidente=name).first()
       if not name:
        new_president = Time(presidente=name)
        session.add(new_president)
        session.commit()

    def add_executive(nome):
        new_executive = session.query(Time).filter(executive=nome)
        if not nome:
           new_executive = Time(executive=nome)
           session.add(new_executive)
           session.commit()

    def add_league(self,liga):
        new_league = session.query(Time).filter_by(liga=self.liga).first()
        if not liga:
            #new_league = self.liga
            self.liga.append(new_league)
            session.add(new_league)
            session.commit()
    
    def atualizar_presidente(new):
        p = session
    

    def atualizar_executivo(new):
        e = session.query(Time)
    def main():
        while True:
            print('1- Adicionar um Time: ')
            print('2- Atuaizar o presidente do time: ')
            print('3- Atualizar o executivo do clube?: ')
            print('4- Adicionar liga a algum clube: ')
            print('5- Sair')
            option = int(input("Opção: "))
            if option == 1:
                club = input('Nome do clube: ')
                p = input('Presidente: ')
                year = int(input("Qual o ano de fundação do clube?: "))
                ex=input('Quem é o executivo do clube?: ')
                league = input("Qual a liga que ele joga?: ")
                add_club(club)
                add_president(p)
                session.add(year)
                add_executive(ex)
                add_league(league)
                
            elif option == 2:
               new_president = str(input("Novo Presidente: "))
               atualizar_presidente(new_president)
            elif option == 3:
              atualizar_executivo(new_executive)
            elif option == 5:
                break

    if __name__ == '__main__':
        main()
"""class Jogador(Base):
        __tablename__ = 'jogador'

        codigo = Column(Integer,primary_key=True,autoincrement=True)
        nome = Column(String)
        idade = Column(Integer)
        posição = Column(String)
        time = relationship('Time_Futebol',backref='jogador')
    

        def situação(self):
         situação = Column(String)
         return f'{situação}'
    
        def info(self):
            return f'<Jogador(nome={self.nome}, Posição={self.posição}, time= {self.time})>'"""


"""class Técnico(Base):
        __tablename__ = 'Treinador'
        
        licenca=Column(String)
        nome = Column(String)
        idade = Column(Integer)
        horario = Column(String)
        equipes=Column(String)

        def __init__(self,licenca,nome,idade,horario,equipes):
            self.licenca = licenca
            self.nome = nome 
            self.idade = idade
            self.horario = horario
            self.equipes = equipes

        def add_equipe(self,equipe):
              self.equipes = []
              self.equipes.append(equipe)

        def info_manager(self):
            return f'Treinador:(nome={self.nome}), licenca:(licenca={self.licenca})'"""
           
            

'''class Funcionario(Base):
     __tablename__ = 'funcionários'

     id_f=Column(Integer,primary_key=True,autoincrement=True)
     name=Column(String)
     area_trabalho = Column(String)
     horario = Column(Text)
      

     def info_funcionario(self):
        print('='*30)
        print(f'{self.id}')
        print(f'{self.name}')
        print(f'{self.area_trabalho}')'''



""" class Patrocinador(Base):
        __tablename__ = 'Patrocinadora'
        nome = Column(String,nullable=False)
        id_patrocinio = Column(Integer,primary_key=True)
        responsable = Column(String)
        financing = Column(DECIMAL)
        

        def __repr__(self):
         return f'Farmaceutica: {self.nome}\n Código: {self.id_patrocinio}\n Responsável: {self.responsable}\n' """


'''class Organizada(Base):
    __tablename__ = 'Torcidas Organizadas'
    
    cod_org = Column(Integer,primary_key=True)
    team = Column(String,ForeignKey('Time_Futebol.name'))
    twisted = Column(String)
    lider = Column(String)'''
   
'''

class Sala:
    def __init__(self):
        self.num = int(input('Número da Sala: '))
        self.setor = str(input('Qual é o setor da Sala de Hospital?: '))'''

#INSERT
'''data_insert = Time(presidente='Julio Casares',name='São Paulo FC',ano_fundacao=19030,executive='Carlos Belmonte',liga='Brasileirão')
session.add(data_insert)
session.commit()'''


'''insertion = Time(presidente='Marcelo Teixeira',name='Santos',ano_fundacao=1912,executive='Pedro Martins',liga='Brasileirão')
session.add(insertion)
session.commit()
'''

'''ind = Organizada(cod_org=11,team='São Paulo FC',twisted='Torcida Independente',lider='Henrique gomes(baby)')
session.add(ind)
session.commit()'''

'''artur = Técnico(licenca='PRO',nome='Artur Jorge',idade=52,horario='Das 7h até as 20h ')
#artur.add_equipe('Botafogo')
session.add(artur)
session.commit()'''


'''i = Time(presidente='Leila pereira',name='Palmeiras',ano_fundacao=1914,executive='Anderson barros',liga='Brasileirão')
session.add(i)
session.commit()'''

'''lucas = Jogador(codigo=14,nome="Lucas Moura",idade=32,posição="Ponta direita ou meia",time='São Paulo FC')
session.add(lucas)
session.commit()'''

#Mudando o presidente
'''i.atualizar_presidente("Pablo Marçal")
session.commit()'''

#UPDATE
'''year = session.query(Time).first()
year.ano_fundacao = 1930
session.commit()'''

'''session.execute('Alter TABLE Técnico DROP COLUMN licenca')
session.execute("ALTER TABLE Técnico ADD COLUMN código INT PRIMARY KEY AUTOINCREMENT  ")
session.commit()'''

#SELECT
'''clubs = session.query(Time).all()
for club in clubs:
    print(club.name)'''



#DELETE
'''session.query(Time).filter(Time.name=='Corinthians').delete()
session.commit()'''


Base.metadata.create_all(engine)
session.close()