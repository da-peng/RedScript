#encoding=utf-8
import json

from db_util.mongodb_connect import *

collection = 'recommend_follow_user_info'

# IP 业务存储逻辑
class FollowRecommendUser(object):
    def __init__(self):
        self.client = MongoUtil().client
        self.collection = MongoUtil().db[collection]
        # print('Base __init__')

    def insert(self,data):
        self.collection.insert(data)




