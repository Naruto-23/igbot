"""
    instabot example

    Workflow:
        Like last images with hashtag.
"""

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("hashtags", type=str, nargs="+", help="hashtags")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p, proxy=args.proxy)

for hashtag in args.hashtags:
    bot.like_hashtag(hashtag)
    tags = ["ここに","いいねしたい","タグを","入力しておく"]
wait = 25 * 60 # in seconds => 25 minutes
retry = 5 * 60 * 60 # in hours => 5 hours

while True:
try:
for hashtag in tags:
bot.like_hashtag(hashtag)
sleep(wait)
except:
sleep(retry)
