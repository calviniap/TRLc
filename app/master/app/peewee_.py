# /usr/bin/python
# encoding:utf-8
import time
start = time.time()
from peewee import *
from datetime import date

# 新建数据库 db
db = SqliteDatabase('people.db')
#db = MySQLDatabase("mydb", user="root", passwd="root")
#表格模型 Person：这是一个Model的概念
#连接数据库db
#db.connect()

class Person(Model):
    #CharField 为抽象数据类型 相当于 varchar
    name = CharField()
    #DateField 相当于 date
    birthday = DateField()
    #BooleanField 相当于 bool
    is_relative = BooleanField()

    # 所用数据库为db
    class Meta:
        database = db


class Pet(Model):
    #外连接的声明(和Person关联)
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db




#db.create_tables([Person, Pet])
# Storing Data
'''
uncle_bob = Person(name='Bob', birthday=date(1967, 1, 28), is_relative=True)
uncle_bob.save()

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
herb = Person.create(name='Herb', birthday=date(1950, 5, 1), is_relative=False)

grandma.name = 'Marry'
grandma.save()

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

# return the value of delete_instance() is the number of rows removed form the database

# delete Data
herb_mittens.delete_instance()  # he had a great life

# Modify Data
herb_fido.owner = uncle_bob
herb_fido.save()
bob_fido = herb_fido  # rename our variable for clarity






# 查询名字为Marry的person
grandma = Person.select().where(Person.name == 'Marry').get()

#列出Person表中所有的person
for person in Person.select():
    print(person.name, person.is_relative)



#查询Pet表中animal_type为cat的所有pet
query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

for pet in query:
    print(pet.name, pet.owner.name)

#查询Pet表中主人名为Bob的所有pet
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)

#查询Pet表中person为uncle_bob的所有pet
for pet in Pet.select().where(Pet.owner == 'uncle_bob'):
    print(pet.name)

#查询Pet表中person为uncle_bob结果按pet名排列
for pet in Pet.select().where(Pet.owner == 'uncle_bob').order_by(Pet.name):
    print(pet.name)

#将Person表中的person按生日降序查询
for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)

#查询Person表中person所拥有的pet数量及名字和类型
for person in Person.select():
    print(person.name, person.pets.count(), 'pets')
    for pet in person.pets:
        print('      ', pet.name, pet.animal_type)

#查询Person表中生日小于1940或大于1960的person
d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person
         .select()
         .where((Person.birthday < d1940) | (Person.birthday > d1960)))

#查询Person表中生日在1940和1960之间的person
for person in query:
    print(person.name, person.birthday)
query = (Person
         .select()
         .where((Person.birthday > d1940) & (Person.birthday < d1960)))

for person in query:
    print(person.name, person.birthday)

#按照expression查询person名开头为小写或大写 G 的person
expression = (fn.Lower(fn.Substr(Person.name, 1, 1)) == 'g')
for person in Person.select().where(expression):
    print(person.name)


增加數據
q = Person.insert(name='admin',birthday=2,is_relative=True)
q.execute()

刪除數據
q = Person.delete().where(Person.birthday == 3)
q.execute()

修改數據
q = Person.update(name='sdf').where(Person.birthday == 3)
q.execute()

查詢數據
for person in Person.select():
    print(person.name, person.is_relative)

for person in Person.select().where(Person.birthday==2):
    print(person.name, person.is_relative)
'''

#db.create_tables([Person, Pet])
# Storing Data
'''
uncle_bob = Person(name='Bob', birthday=date(1967, 1, 28), is_relative=True)
uncle_bob.save()

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
herb = Person.create(name='Herb', birthday=date(1950, 5, 1), is_relative=False)

grandma.name = 'Marry'
grandma.save()

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

# return the value of delete_instance() is the number of rows removed form the database

# delete Data
herb_mittens.delete_instance()  # he had a great life

# Modify Data
herb_fido.owner = uncle_bob
herb_fido.save()
bob_fido = herb_fido  # rename our variable for clarity






# 查询名字为Marry的person
grandma = Person.select().where(Person.name == 'Marry').get()

#列出Person表中所有的person
for person in Person.select():
    print(person.name, person.is_relative)



#查询Pet表中animal_type为cat的所有pet
query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

for pet in query:
    print(pet.name, pet.owner.name)

#查询Pet表中主人名为Bob的所有pet
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)

#查询Pet表中person为uncle_bob的所有pet
for pet in Pet.select().where(Pet.owner == 'uncle_bob'):
    print(pet.name)

#查询Pet表中person为uncle_bob结果按pet名排列
for pet in Pet.select().where(Pet.owner == 'uncle_bob').order_by(Pet.name):
    print(pet.name)

#将Person表中的person按生日降序查询
for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)

#查询Person表中person所拥有的pet数量及名字和类型
for person in Person.select():
    print(person.name, person.pets.count(), 'pets')
    for pet in person.pets:
        print('      ', pet.name, pet.animal_type)

#查询Person表中生日小于1940或大于1960的person
d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person
         .select()
         .where((Person.birthday < d1940) | (Person.birthday > d1960)))

#查询Person表中生日在1940和1960之间的person
for person in query:
    print(person.name, person.birthday)
query = (Person
         .select()
         .where((Person.birthday > d1940) & (Person.birthday < d1960)))

for person in query:
    print(person.name, person.birthday)

#按照expression查询person名开头为小写或大写 G 的person
expression = (fn.Lower(fn.Substr(Person.name, 1, 1)) == 'g')
for person in Person.select().where(expression):
    print(person.name)


增加數據
q = Person.insert(name='admin',birthday=2,is_relative=True)
q.execute()

刪除數據
q = Person.delete().where(Person.birthday == 3)
q.execute()

修改數據
q = Person.update(name='sdf').where(Person.birthday == 3)
q.execute()

#更新多个(将a打头的用户的value全部更新为1)
User.update(value = 1).where(User.name ** 'A%').execute()

查詢數據
for person in Person.select():
    print(person.name, person.is_relative)

for person in Person.select().where(Person.birthday==2):
    print(person.name, person.is_relative)
'''

'''
for data in Person.select().where(Person.id==17):
    print(data.name,data.birthday)
'''
'''
        fid = PrimaryKeyField()
        file_name = CharField()
        file_path = TextField()
        date_changed = DateTimeField()
        size = IntegerField()
'''

'''
class data(Model):
    id=IntegerField()
    pagename = CharField()
    pageurl = CharField()

    class Meta:
        database = db

for data in data.select().where(data.id==261):
    print(data.pagename,data.pageurl)


from peewee import *

#创建数据库实例
db = SqliteDatabase('base.db')

#建议自己的项目使用一个新的基类，Model是peewee的基类
class MyBaseModel(Model):
    class Meta:
        database = db

    @classmethod
    def getOne(cls, *query, **kwargs):
       #为了方便使用，新增此接口，查询不到返回None，而不抛出异常
       try:
          return cls.get(*query,**kwargs)
       except DoesNotExist:
           return None

#示范一个表
class User(MyBaseModel):
    name = CharField(unique=True)
    password = CharField()
    group = CharField(default='admin')
    value = FloatField(default=0.0)

#建表，仅需创建一次
User.create_table()

#新增行
User.create(name=name,password=password)

#查询一行
user = User.getOne(User.name='MyGod')
print(user.password)

#更新
user.value += 1
user.save()

#删除
user.delete_instances()

#查询多行
usersInGroup = User.select().where(User.group == 'admin')
usersStartsWithA = User.select().where(User.name ** 'A%')   #不区分大小写的like查询
usersWithOrder = User.select().where(User.group == 'admin').order_by(User.name.desc()) #按姓名倒序排序


#统计admin用户组所有用户的value总和
total = User.select(fn.Sum(User.value).alias('totalvalue')).where(User.group=='admin')

#更新多个(将a打头的用户的value全部更新为1)
User.update(value = 1).where(User.name ** 'A%').execute()



CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `fullname` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
INSERT INTO `users` VALUES (1,'otto',1),(2,'zjj',2);

CREATE TABLE `groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8
INSERT INTO `groups` VALUES (1,'oss'),(2,'dev');



CREATE TABLE `tasks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT '',
  `content` varchar(100) DEFAULT '',
  `type_id` int(11) default 0,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

insert into tasks (`id`, `name`, `content`, `type_id`)
values
(1, 'task_1', 'content_1', 0),
(2, 'task_2', 'content_2', 1);


'''

for data in Person.select().where(Person.id==17):
    print(data.name,data.birthday)

db.close()
end = time.time()
print(end-start)
input()