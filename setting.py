# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


TOKEN = os.environ.get("TELEGRAM_TOKEN") # 環境変数の値をTOKENに代入
api_key = os.environ.get("api_key") # 環境変数の値をapi_keyに代入
api_secret_key = os.environ.get("api_secret_key") # 環境変数の値をapi_secret_keyに代入
access_token = os.environ.get("access_token") # 環境変数の値をaccess_tokenに代入
access_token_secret = os.environ.get("access_token_secret") # 環境変数の値をaccess_token_secretに代入
