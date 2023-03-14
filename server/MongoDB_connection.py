import pymongo

from enum import Enum, auto

import sys
from Result import Result


class Players(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    Piti = auto()
    Yosef = auto()
    Matanel = auto()
    Yonatan = auto()
    Gelkop = auto()
    Ohad = auto()
    Shalom = auto()
    Sapir = auto()
    Sasson = auto()
    Peretz = auto()


class MongoDBConnection:
    def __init__(self):
        """This constructor create connection to TBC(pt_table) db """
        self.client = pymongo.MongoClient(
            "mongodb+srv://yotanel:1234@leagueoflegendsdb.qlqofrr.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["pt_table"]

    def get_dictionary_champ(self, player_name: Players, *args, **kwargs) -> Result:
        """This function return Result.value is documents of champs_dict score for specific player"""
        doc_name = str(player_name.value) + "_table"
        collection = self.db[doc_name]
        documents = collection.find()
        champ_dict = {}
        for doc in documents:
            champ_dict = doc

        del champ_dict["_id"]

        return Result(error=Result.ErrorCode.ok, value=champ_dict)

    def get_users_dict(self, *args, **kwargs) -> Result:
        doc_name = "users"
        collection = self.db[doc_name]
        documents = collection.find()
        users_dict = {}
        for doc in documents:
            users_dict = doc

        return Result(error=Result.ErrorCode.ok, value=users_dict)


if __name__ == '__main__':
    db = MongoDBConnection()
    result_obj: Result = db.get_dictionary_champ(player_name=Players.Gelkop)
    if result_obj.error != Result.ErrorCode.ok:
        quit()
    champ_dict = result_obj.value
    print(champ_dict)
