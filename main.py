import praw
import tts
from win10toast import ToastNotifier
from web_ss import screenshot
from video_editor import create_video
import os
from dotenv import load_dotenv
from resize_img import resize_img

load_dotenv()
toaster = ToastNotifier()

user_agent = "Scraper 1.0"

reddit = praw.Reddit(
    client_id=os.getenv("ID"),
    client_secret=os.getenv("SECRET"),
    user_agent=user_agent,
)

sr_name = "talesfromtechsupport"
title = ""
url = ""
reddit_id = ""
paragraphs = []
ctr = 0
try:
    exports = os.listdir("exports")
except FileNotFoundError:
    exports = []
reddit_id = None

for submission in reddit.subreddit(sr_name).hot(limit=None):

    # if ctr < 56:
    #     ctr += 1
    #     continue
    post = submission.link_flair_text
    if post != "MOD":
        title = submission.title.replace('"', " ")
        url = submission.url
        print(url)
        reddit_id = submission.id

        if reddit_id not in exports:
            paragraphs = screenshot(url, reddit_id)

            if paragraphs is not None:
                lengths = tts.create(title, paragraphs, reddit_id)
                resize_img(reddit_id)
                create_video(lengths, reddit_id, title)
                toaster.show_toast("Tiktok Creator", "Exported!")
            else:
                print("Too long")
        else:
            print("already made")


# todo: return text to convert from screenshots to have equal amount of wav and png
# todo: fix positioning
# ! problem with title with quotations
# ! mali ang speech sa text?
# ! still error sa exports (sirang ss)

# if reddit_id not in exports:
#     paragraphs = screenshot(url, reddit_id)

#     if paragraphs is not None:
#         lengths = tts.create(title, paragraphs, reddit_id)
#         resize_img(reddit_id)
#         create_video(lengths, reddit_id, title)
#         toaster.show_toast("Tiktok Creator", "Exported!")
#     else:
#         print("Too long")
# else:
#     print("already made")
