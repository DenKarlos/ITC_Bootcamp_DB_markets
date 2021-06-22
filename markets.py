import psycopg2
import random as rd
import pprint

bd_password = 'Sunpedro123!'
# bd_password = input("Введите пароль от Базы Данных: ")

pp = pprint.PrettyPrinter(indent=4)

conn = psycopg2.connect(
    dbname='markets',
    user='denkarlos',
    password=f'{bd_password}',
    host='localhost'
)

cur = conn.cursor()

def q_string(query, tbl=True):
    cur.execute(query)
    arr = []
    for i in cur.fetchall():
        for j in range(len(i)):
            if j != len(i)-1:
                arr.append(str(i[j]))
                arr.append(' ')
            else:
                arr.append(str(i[j]))
                if tbl:
                    arr.append('\n')
    if tbl:
        arr.insert(0, '\n')

    return ''.join(arr)


# 1. Найдите сколько разных типов продуктов в таблице globus.
res = q_string("SELECT Count(DISTINCT product_type_id) from globus;", False)
print(f'В "Глобусе" {res} разных типов продуктов.')

# 2. Используя HAVING найдите сколько и каких продуктов в narodnii испортятся меньше чем через 2 дня.
query = """SELECT product_name, Count(*)
            from narodnii where day_to_expire < 2
            group by product_name;"""
res = q_string(query)
print(f'В "Народном" меньше чем через 2 дня испортятся следующие продукты в следующем количестве: {res}')

# 3. Посчитайте в каком магазине больше сникерсов в globus или narodnii.
query = """ Select sum(product_amount)
            from narodnii
            where product_name = 'Snikers'"""
nar_snik = q_string(query, False)
query = """ Select sum(product_amount)
            from globus
            where product_name = 'Snikers'"""
glob_snik = q_string(query, False)
print(f'В "Глобусе" {glob_snik} - сникерсов, а в "Народном" {nar_snik} - сникерсов.')

# 4. Посмотрите продукты в globus и narodnii у которых product_type равен сроку годности продукта.

# 5. Посмотрите продукты из globus и narodnii у которых одинаковый срок годности.

# 6. Через Python подключитесь к БД main и узнайте сколько ВСЕГО piyaz в магазине globus.
query = """ Select sum(product_amount)
            from globus
            where product_name = 'Piyaz'"""
res = q_string(query, False)
print(f'В "Глобусе" {res} продуктов с названием "Piyaz"')

# 7. Через Python удалите из магазина narodnii все продукты у которых срок годности 0.
# query = """ DELETE *
#             from narodnii
#             where day_to_expire = 0"""
# cur.execute(query)

# 8. Если ПРОДУКТ и СРОК ГОДНОСТИ продукта одинаковы в globus и narodnii удалите эту запись из globus.
# query = """ DELETE *
#             from narodnii
#             where day_to_expire = 0"""
# cur.execute(query)

# 9. Напишите запрос, который выводит всю информацию продукта из народного,
# где количество продуктов 200 < продукт < 1001
# 10. Напишите запрос, который соединяет таблицы глобус народный
# и выводит day delivered
# 11. Напишите запрос, который соединяет таблицы глобус народный
# по столбцу глобуса и выводит название продукта
# 12. Напишите запрос, который соединяет таблицы глобус народный
# по столбцу народного и выводит название продукта
# 13. Напишите запрос, который соединяет таблицы глобус народный
# по столбцу глобуса и выводит название продукта
# 14. Напишите запрос, который соединяет таблицы глобус народный
# и выводит совпадения количества продуктов.
# 15. Напишите запрос, который выводит продукты глобуса,
# где название заканчивается на a, b, c, d, e, f, g, a
# 1. Cоздайте таблицу sizes которая хранит в себе размер ноги,
# уникальный id записи и время создание записи.
# 2. Создайте вторую таблицу которая хранит в себе id из таблицы sizes
# и имя человека с помощью INNER JOIN выведите на экран Имя человека и размер его обуви.


# print(f'Вывод бызы данных: {q_string("SELECT * from globus;")}- вот такая-вот')
