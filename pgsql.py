import os
from sqlalchemy import Column, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


pg_user = os.environ.setdefault('POSTGRES_USER', 'postgres')
pg_passwd = os.environ.setdefault('POSTGRES_PASSWORD', 'postgres')
pg_server = os.environ.setdefault('POSTGRES_HOST', 'postgres')
pg_server_port = os.environ.setdefault('POSTGRES_PORT', 5432)
pg_db_name = os.environ.setdefault('POSTGRES_DB', 'postgres')


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    __tableargs__ = {
        'comment': 'Мастера портала'
    }

    user_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    user_name = Column(String(256), comment='Имя мастера')
    user_shop_link = Column(String(256), comment='Ссылка на магазин')
    user_profile_url = Column(String(256), comment='Ссылка на магазин')
    user_addr = Column(Text, comment='Адрес нахождения')
    followers = Column(Integer, comment='Количество подписчиков')
    products_count = Column(Integer, comment='Количество подписчиков')
    user_html = Column(Text, comment='Код страницы профиля')
    products = relationship('Products')

    def __repr__(self):
        return f'{self.users_id} {self.user_name} {self.user_profile_url}'


class User(Base):
    __tablename__ = 'user'
    __tableargs__ = {
        'comment': 'user of system'
    }

    pass

    def __repr__(self):
        return f'{self.product_id} {self.product_title} {self.product_url} {self.product_price}'


engine = create_engine(f'postgresql://{pg_user}:{pg_passwd}@{pg_server}:{pg_server_port}/{pg_db_name}')

Session = sessionmaker(bind=engine)
session = Session()
