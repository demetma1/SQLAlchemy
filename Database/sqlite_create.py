from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, \
    SmallInteger, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session
from datetime import datetime

engine = create_engine("sqlite:////web/sqlite-Data/example.db")
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')

class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer(), nullable=False)

    __table_args__ = (
        CheckConstraint('quantity > 0', name='quantity_check'),
    )

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now, nullable=False)
    date_shipped = Column(DateTime())

class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    order = relationship("Order", backref='order_lines')
    item = relationship("Item")

Base.metadata.create_all(engine)

#Step 1. Creating Session
session = Session(bind=engine)

#import sqlite3

#conn = sqlite3.connect('/web/Sqlite-Data/example.db')

#c = conn.cursor()

#c.execute('''
 #         CREATE TABLE person
 #         (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
 #       ''')
#c.execute('''
 #         CREATE TABLE address
 #        (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
 #         post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
 #         FOREIGN KEY(person_id) REFERENCES person(id))
 #        ''')

#c.execute('''
 #         INSERT INTO person VALUES(1, 'pythoncentral')
 #       ''')
#c.execute('''
 #         INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
 #        ''')

#conn.commit()
#conn.close()





