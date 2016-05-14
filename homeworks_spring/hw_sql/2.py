import sqlite3 as sq
def unpaid (user_id):
    query = "select Users.name, Orders.id, sum(price) from Users " \
            "inner join Orders on Users.id = user_id " \
            "inner join GoodsInOrders on Orders.id = order_id " \
            "inner join Goods on Goods.id = good_id " \
            "where Users.id = ? and paid = 0 " \
            "group by Orders.id "
    with sq.connect("data.sqlite") as con:
        cur = con.cursor()
        data = cur.execute(query, [user_id]).fetchall()
    return data
