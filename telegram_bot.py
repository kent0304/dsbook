import os
import setting
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# アクセストークン
TOKEN = setting.TOKEN
# TOKEN = os.environ["TELEGRAM_TOKEN"]


# Telegramのサーバと通信を行うクラス
class TelegramBot:
    # 応答内容の決定を行う
    def __init__(self, system):
        self.system = system

    # 対話開始時に呼ばれるメソッド
    def start(self, bot, update):
        # 辞書型 inputにユーザIDを設定
        # uttはユーザの発話、sessionIdはユーザを区別するためのId
        input = {'utt': None, 'sessionId': str(update.message.from_user.id)}

        # システムからの最初の発話をinitial_messageから取得し，送信
        update.message.reply_text(self.system.initial_message(input)["utt"])

    def message(self, bot, update):
        # 辞書型 inputにユーザからの発話とユーザIDを設定
        input = {'utt': update.message.text, 'sessionId': str(update.message.from_user.id)}

        # replyメソッドによりinputから発話を生成
        system_output = self.system.reply(input)

        # 発話を送信
        update.message.reply_text(system_output["utt"])

    # Telegramとの通信を開始
    def run(self):
        updater = Updater(TOKEN)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(MessageHandler(Filters.text, self.message))
        updater.start_polling()
        updater.idle()
