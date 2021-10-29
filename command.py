from praw.reddit import Subreddit
from config import reddit
import random
limit = 300
# subreddit = reddit.subreddit("SkyPorn")


# for img in subreddit.hot(limit=10):
#     print(img.url)

def fantasy():

    subreddits = ['ImaginaryLandscapes', "ImaginaryTechnology"]

    subreddit = reddit.subreddit(random.choice(subreddits))
    times = ["day", "week", "year", "month", "all"]
    imgs = []
    functions = [subreddit.new, subreddit.hot, subreddit.top, ]

    statement = ""

    for submmision in functions[random.randint(0, len(functions)-1)](limit=limit):

        imgs.append(submmision.url)

    img = random.choice(imgs)

    print(img)
    return img


def future():

    subreddit = reddit.subreddit("futureporn")
    imgs = []
    functions = [subreddit.new, subreddit.hot, subreddit.top, ]

    statement = ""

    for submmision in functions[random.randint(0, len(functions)-1)](limit=limit):

        imgs.append(submmision.url)

    img = random.choice(imgs)

    return img


def wallpapersGeneral():

    subreddits = ["wallpapers",  "wallpaper",
                  "Wallpaper", "EarthPorn", "SkyPorn", "ExposurePorn"]
    subreddit = reddit.subreddit(random.choice(subreddits))
    imgs = []
    functions = [subreddit.new, subreddit.hot, subreddit.top, ]

    statement = ""

    for submmision in functions[random.randint(0, len(functions)-1)](limit=limit):

        imgs.append(submmision.url)

    img = random.choice(imgs)

    return img


def mobileWallpapers():
    subreddits = ["Verticalwallpapers",  "phonewallpapers", "MobileWallpaper"]

    subreddit = reddit.subreddit(random.choice(subreddits))
    imgs = []
    functions = [subreddit.new, subreddit.hot, subreddit.top, ]

    statement = ""

    for submmision in functions[random.randint(0, len(functions)-1)](limit=limit):

        imgs.append(submmision.url)

    img = random.choice(imgs)

    return img


def anime():
    subreddit = reddit.subreddit("Animewallpaper")
    imgs = []
    functions = [subreddit.new, subreddit.hot, subreddit.top, ]

    statement = ""

    for submmision in functions[random.randint(0, len(functions))-1](limit=limit):

        imgs.append(submmision.url)

    img = random.choice(imgs)
    print(img)
    return img


commands = {"fantasy": fantasy, "anime": anime, "wallpaper": wallpapersGeneral,
            "mobile": mobileWallpapers, "future": future}
