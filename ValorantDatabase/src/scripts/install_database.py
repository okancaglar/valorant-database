import csv
import logging
import argparse

import mysql.connector
from mysql.connector import MySQLConnection, Error

"""
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`player` (
  `name` VARCHAR(150) NOT NULL,
  `tag` VARCHAR(150) NOT NULL,
  `region` CHAR(3) NOT NULL,
  `rank` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`name`, `tag`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `valorantDatabase`.`round`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`round` (
  `player_name` VARCHAR(150) NOT NULL,
  `player_tag` VARCHAR(150) NOT NULL,
  `damage_round` DOUBLE NULL,
  `kills_round` DOUBLE NULL,
  `score_round` DOUBLE NULL,
  PRIMARY KEY (`player_name`, `player_tag`),
  CONSTRAINT `fk_round_player1`
    FOREIGN KEY (`player_name` , `player_tag`)
    REFERENCES `valorantDatabase`.`player` (`name` , `tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `valorantDatabase`.`total_game_stats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`total_game_stats` (
  `player_name` VARCHAR(150) NOT NULL,
  `player_tag` VARCHAR(150) NOT NULL,
  `headshots` INT NULL,
  `headshot_percent` DOUBLE NULL,
  `aces` INT NULL,
  `clutches` INT NULL,
  `flawless` INT NULL,
  `first_bloods` INT NULL,
  `kills` INT NULL,
  `deaths` INT NULL,
  `assists` INT NULL,
  `most_kills` INT NULL,
  `kd_ratio` DOUBLE NULL,
  `wins` INT NULL,
  `win_percent` DOUBLE NULL,
  PRIMARY KEY (`player_name`, `player_tag`),
  CONSTRAINT `fk_total_game_stats_player1`
    FOREIGN KEY (`player_name` , `player_tag`)
    REFERENCES `valorantDatabase`.`player` (`name` , `tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `valorantDatabase`.`player_agents`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`player_agents` (
  `player_name` VARCHAR(150) NOT NULL,
  `player_tag` VARCHAR(150) NOT NULL,
  `agents_usage_rank` INT NOT NULL,
  `agent_name` VARCHAR(50) NULL,
  PRIMARY KEY (`player_name`, `player_tag`, `agents_usage_rank`),
  CONSTRAINT `fk_player_agents_player1`
    FOREIGN KEY (`player_name` , `player_tag`)
    REFERENCES `valorantDatabase`.`player` (`name` , `tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `valorantDatabase`.`gun_stats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`gun_stats` (
  `player_name` VARCHAR(150) NOT NULL,
  `player_tag` VARCHAR(150) NOT NULL,
  `gun_usage_rank` INT NOT NULL,
  `gun_name` VARCHAR(50) NULL,
  `gun_head` INT NULL,
  `gun_body` INT NULL,
  `gun_leg` INT NULL,
  `gun_kills` INT NULL,
  PRIMARY KEY (`player_name`, `player_tag`, `gun_usage_rank`),
  CONSTRAINT `fk_gun_stats_player1`
    FOREIGN KEY (`player_name` , `player_tag`)
    REFERENCES `valorantDatabase`.`player` (`name` , `tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

"""


def insert_player_table(data:list, connector:MySQLConnection)-> None:

    query = ("insert into player values("
             "%s,"
             "%s,"
             "%s,"
             "%s)")

    cursor = connector.cursor()
    for row in data:
        print(row[0])
        player_row = [row[1], row[2], row[0], row[3]]
        cursor.execute(query, player_row)
    connector.commit()

    if cursor:
        cursor.close()

def insert_total_game_stats(data:list, connector:MySQLConnection) -> None:
    query = ("insert into total_game_stats values("
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s)")

    cursor = connector.cursor()

    for row in data:
        total_game_stats_row = [row[1],
                                row[2],
                                row[5],
                                row[6],
                                row[7],
                                row[8],
                                row[9],
                                row[10],
                                row[11],
                                row[12],
                                row[13],
                                row[16],
                                row[14],
                                row[18],
                                row[19]
        ]
        cursor.execute(query, total_game_stats_row)
    connector.commit()
    if cursor:
        cursor.close()


def insert_player_agents_table(data, connector: MySQLConnection) -> None:

    query = ("insert into player_agents values("
             "%s,"
             "%s,"
             "%s,"
             "%s)")

    cursor = connector.cursor()
    for row in data:
        player_agent1_row = [row[1],
        row[2],
        "1",
        row[20]]

        player_agent2_row = [row[1],
                             row[2],
                             "2",
                             row[21]]

        player_agent3_row = [row[1],
                             row[2],
                             "3",
                             row[22]]

        cursor.execute(query, player_agent1_row)
        cursor.execute(query, player_agent2_row)
        cursor.execute(query, player_agent3_row)

    connector.commit()
    if cursor:
        cursor.close()


def insert_gun_stats_table(data:list, connector:MySQLConnection) -> None:

    query = ("insert into gun_stats values("
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s)")
    cursor = connector.cursor()

    for row in data:
        gun1_stat_row = [row[1],
                         row[2],
                         "1",
                         row[23],
                         row[24],
                         row[25],
                         row[26],
                         row[27]]

        gun2_stat_row = [row[1],
                         row[2],
                         "2",
                         row[28],
                         row[29],
                         row[30],
                         row[31],
                         row[32]]
        gun3_stat_row = [row[1],
                         row[2],
                         "3",
                         row[33],
                         row[34],
                         row[35],
                         row[36],
                         row[37]]

        cursor.execute(query, gun1_stat_row)
        cursor.execute(query, gun2_stat_row)
        cursor.execute(query, gun3_stat_row)

    connector.commit()

    if cursor:
        cursor.close()


def insert_round_table(data:list, connector:MySQLConnection) -> None:

    query = ("insert into round values("
             "%s,"
             "%s,"
             "%s,"
             "%s,"
             "%s)")
    cursor = connector.cursor()

    for row in data:
        round_row = [row[1],
                     row[2],
                     row[4],
                     row[15],
                     row[17]]

        cursor.execute(query, round_row)
    connector.commit()

    if cursor:
        cursor.close()

def csv_to_list(fileName:str) -> list[list]:
    """@:return list that holds rows in csv file"""

    rows = []
    with open(fileName, "r") as file:
        fileReader = csv.reader(file)
        for row in fileReader:
            rows.append(row)
        file.close()
    rows.pop(0)
    return rows

def execute_sql_file(fileName, connection):


    with open(fileName) as file:
        sql_file = file.read()
        file.close()
    queries = sql_file.split(";")
    cursor = connection.cursor()

    try:
        for query in queries:
            if query.strip():
                cursor.execute(query)
        connection.commit()

        if cursor:
            cursor.close()
    except (Error, Exception) as error:
        logging.getLogger(__name__).error("database is not created Error: " + str(error))


def delete_repeated_row():

    cleandata = {}
    with open("data/val_stats.csv", "r") as file:
        dataReader = csv.reader(file)
        for row in dataReader:
            """ in some rows player name and player tag is combined inside the player name
            when clearing repeated rows at the same time split player name and tag """

            primarykey = row[1] + row[2]
            if (row[1] != '' or len(row[1].split(' ')) != 0) and (row[2] == "" or row[2] is None):
                row[2] ="#" + row[1].split("#", 1)[0]
            """------------------------------------------------------------------------------------"""
            if cleandata.get(primarykey) is None:
                cleandata[primarykey] = row
        file.close()

    with open("data/val_stats_clean.csv", "w") as file:
        dataWriter = csv.writer(file)
        for (key, value) in cleandata.items():
            dataWriter.writerow(value)
        file.close()

def check_primary_key_is_unique() -> bool:
    """ checker for clean data set that if it has unique primary key or not """

    with open("val_stats_clean.csv", "r") as file:
        dataBuffer = {}
        fileReader = csv.reader(file)
        for row in fileReader:
            primaryKey = row[1] + row[2]
            if dataBuffer.get(primaryKey):
                file.close()
                return False
            dataBuffer[primaryKey] = row
        file.close()
        return True


def create_database(port, user, password):
    create_db = mysql.connector.connect(port=port,
                                        user=user,
                                        password=password)

    execute_sql_file("/home/marcus-aurelius/dblab2023/databaseFinalProject/ValorantDatabase/src/scripts/createDatabase.sql", create_db)

    if create_db is not None and create_db.is_connected():
        create_db.close()


def insert_all_data(port, database_name, user, password) -> None:
    """ inserts all data in csv file to mysql database """

    rows = csv_to_list("/home/marcus-aurelius/dblab2023/databaseFinalProject/ValorantDatabase/src/scripts/val_stats_clean.csv")
    connector = MySQLConnection(host='localhost', port=port,
                                database=database_name, user=user,
                                password=password)

    insert_player_table(rows, connector)
    insert_total_game_stats(rows, connector)
    insert_round_table(rows, connector)
    insert_player_agents_table(rows, connector)
    insert_gun_stats_table(rows, connector)

    if connector is not None and connector.is_connected():
        connector.close()


def main() -> None:


    argparser = argparse.ArgumentParser()
    argparser.add_argument("port", help="port number of mysql server")
    argparser.add_argument("database_name", help="name of the database")
    argparser.add_argument("user_name", help="mysql server user name")
    argparser.add_argument("password", help="mysql server user password")

    args = argparser.parse_args()

    create_database(args.port, args.user_name, args.password)

    insert_all_data(port=args.port,
                    database_name=args.database_name,
                    user=args.user_name,
                    password=args.password)

if __name__ == "__main__":
    main()