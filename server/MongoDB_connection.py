import pymongo

from enum import Enum

import sys
from Result import Result

class Players(Enum):
    Piti = "piti"
    Yosef = "yosef"
    Matanel = "matanel"
    Yonatan = "yonatan"
    Gelkop = "gelkop"
    Ohad = "ohad"
    Shalom = "shalom"
    Sapir = "sapir"
    Sasson = "sasson"
    Peretz = "peretz"


class MongoDBConnection:
    def __init__(self):
        """This constructor create connection to TBC(pt_table) db """
        self.client = pymongo.MongoClient(
            "mongodb+srv://yotanel:1234@leagueoflegendsdb.qlqofrr.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["pt_table"]

    def get_dictionary_champ(self, player_name: Players, *args, **kwargs) -> Result:
        """This function return Result.value is documents of champs_dict score for specific player"""
        table_name = str(player_name.value) + "_table"
        collection = self.db[table_name]
        documents = collection.find()
        champ_dict = {}
        for doc in documents:
            champ_dict = doc

        del champ_dict["_id"]

        return Result(error=Result.ErrorCode.ok, value=champ_dict)


if __name__ == '__main__':
    db = MongoDBConnection()
    result_obj: Result = db.get_dictionary_champ(player_name=Players.Gelkop)
    if result_obj.error != Result.ErrorCode.ok:
        quit()
    champ_dict = result_obj.value
    print(champ_dict)
