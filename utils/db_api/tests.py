from utils.db_api.sqlite import Database



db = Database()


def test():
    db.create_table_users()
    db.delete_all()
    users = db.select_all_users()
    print(f"Boshlang'ich holat: {users}")
    db.add_user(1, "Otabek", "otabek@gmail.com")
    db.add_user(2, "Bekzod", "bekzod@gmail.com")
    db.add_user(3, "Sherzod", "sherzod@gmail.com")
    db.add_user(4, "Anvar", "anvar@gmail.com")

    users = db.select_all_users()
    print(f"Keyingi holat: {users}")

    user = db.select_user(id=2)
    print(f"Tanlangan user: {user}")

test()
