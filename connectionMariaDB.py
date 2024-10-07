import sys
import mariadb

try:
    conn = mariadb.connect(
        user="agathaessence",
        password="agathaessence111",
        host="10.9.120.5",
        port=8080,
        database="agathaessence"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)