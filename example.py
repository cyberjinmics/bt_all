#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol
from src.newAccount import newAccount
from src.usernameGen import usernameGen
import random

username = ''
password = ''
bot_id = 0
if len(username) == 0 or len(password) == 0:
    newAccount = newAccount()
    newAccount.username = usernameGen(3, True)
    newAccount.email = newAccount.username + '@gmail.com'
    newAccount.first_name = newAccount.username.replace("_", " ").title()
    newAccount.signup_password = 'b@tinlo18'
    newAccount.clean_vars()
    newAccount.signup()
    if newAccount.login_status:
        username = newAccount.username
        password = newAccount.signup_password
        bot_id = newAccount.bot_id
        print('Setting up account - bio, posts, and profile photo')
        newAccount.design()
        adjectives = [
            '✔ acclaimed', '🚀 advanced', '🍡 affordable', '🌐 agile', '☀ all-wheel-drive', '😤 astonishing', '🚅 automatic',
            '🚀 beyond-compare', '🚌 classic', '🚁 crash-tested', '🌌 custom-built', '🌌 custom-designed', '🚗 customized', '🎌 distinctive',
            '🚜 functional', '🚀 futuristic', '🌠 high-agility', '🎊 hybrid', '✈ innovative', '🎈 legendary', '☀ limitless',
            '⛅ low-emission', '🚌 luxurious', '❗ noteworthy', '🚜 performance-inspired',
            '🚂 powerful', '🚄 progressive', '🎆 dynamic', '🍔 easy-to-drive', '🌄 economical', '☄ effective', '🌉 elegant',
            '🚂 engineered',
            '✔ enhanced', '🌇 environmentally-friendly', '😊 ergonomic', '😣 extreme', '💑 family-friendly', '✈ fast',
            '🌅 fuel-efficient', '☄ ready-for-action', '🎇 reinforced', '💌 safe',
            '🚋 scientific',
            '🚅 sleek', '🚅 speedy', '🚙 sporty', '🗻 standard', '💐 stylish', '🗽 top-dollar', '🌋 top-level', '🌝 tuned',
            '🌝 ultimate',
            '🌌 ultra', '🌗 unparalled', '🎀 versatile'
        ]
        c = ['cars', 'metallic horses', 'vehicles', 'machines', 'road machines']
        #👑 The 💖 beautiful 🎀 fierce ✨ inspiring metallic horses collection🎁 covercar: @shopbraid 💎
        fills = random.sample(adjectives, 3)
        bio = {'biography': u'👑 The '+fills[0]+' '+fills[1]+' '+fills[2]+' '+random.choice(c)+' collection🎁 covercar: @shopbraid 💎'}
        newAccount.edit_account(bio)
        print('Logging out')
        newAccount.logout()

bot = InstaBot(
    login=username,
    password=password,
    like_per_day=1000,
    comments_per_day=0,
    tag_list=['bbnaija', 'follow4follow', 'f4f', 'cute'],
    tag_blacklist=['rain', 'thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=300,
    follow_time=1 * 60,
    unfollow_per_day=300,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2'])

#tag_list = input("Enter your hashtags: ")
bot.tag_list = open('D:/master/top_tags.txt').read().split()
print(bot.tag_list)

bot.bot_id = bot_id
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
