import mariadb as db
import dbcreds


class DbInteraction:

    def add_win_loss_to_db(self, result):
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO fight_result(win) VALUES({result})")
        conn.commit()

        cursor.close()
        conn.close()

    def dislay_record(self):
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(
            f"select count(*) as wins from fight_result fr where win = 1")
        win_count = cursor.fetchone()

        cursor.execute(
            f"select count(*) as wins from fight_result fr where win = 0")
        loss_count = cursor.fetchone()

        cursor.close()
        conn.close()

        print(f"Your Record: {win_count[0]} wins ----- {loss_count[0]} losses")
