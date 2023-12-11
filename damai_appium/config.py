# -*- coding: UTF-8 -*-
"""
__Author__ = "wahh159"
__Version__ = "1.0.1"
__Description__ = "大麦app抢票自动化"
__Created__ = 2023/12/8 9:10
"""
import json


class Config:
    def __init__(self, server_url, users,if_commit_order,priceList,dateList,dateLen):
        self.server_url = server_url
        self.users = users
        self.if_commit_order = if_commit_order
        self.priceList = priceList
        self.dateList = dateList
        self.dateLen = dateLen

    @staticmethod
    def load_config():
        with open('config.json', 'r', encoding='utf-8') as config_file:
            config = json.load(config_file)
        return Config(config['server_url'],
                      config['users'],
                      config['if_commit_order'],
                      config['priceList'],
                      config['dateList'],
                      config['dateLen']
                      )
