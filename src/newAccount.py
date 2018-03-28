from __future__ import print_function
from .userinfo import UserInfo
import datetime
import json
import logging
import time
import requests
from requests_toolbelt import MultipartEncoder
import uuid
from .commentGen import commentGen
from .filesCount import filesCount
from random import *
import random
import os
from fake_useragent import UserAgent
from .bioGen import bioGen


class newAccount:
    # os.path.join(os.path.dirname(os.getcwd()), '')
    root = os.path.join(os.getcwd(), '')
    media_folder = os.path.join(root, 'media', '')
    print(media_folder)
    print('1. ' + root)
    # Signup Form Data #
    email = ''
    username = ''
    first_name = ''
    signup_password = ''
    seamless_login_enabled = 1

    follow_counter = 0
    like_counter = 0
    comment_counter = 0
    instauser_file = root+'instausers.txt'
    print(instauser_file)

    url = 'https://www.instagram.com/'
    url_tag = 'https://www.instagram.com/explore/tags/%s/?__a=1'
    url_likes = 'https://www.instagram.com/web/likes/%s/like/'
    url_unlike = 'https://www.instagram.com/web/likes/%s/unlike/'
    url_comment = 'https://www.instagram.com/web/comments/%s/add/'
    url_follow = 'https://www.instagram.com/web/friendships/%s/follow/'
    url_unfollow = 'https://www.instagram.com/web/friendships/%s/unfollow/'
    url_login = 'https://www.instagram.com/accounts/login/ajax/'
    url_signup = 'https://www.instagram.com/accounts/web_create_ajax/'
    url_logout = 'https://www.instagram.com/accounts/logout/'
    url_media_detail = 'https://www.instagram.com/p/%s/?__a=1'
    url_user_detail = 'https://www.instagram.com/%s/?__a=1'
    api_user_detail = 'https://i.instagram.com/api/v1/users/%s/info/'
    url_upload = 'https://www.instagram.com/create/upload/photo/'
    url_upload_configure = 'https://www.instagram.com/create/configure/'
    url_delete_media = 'https://www.instagram.com/create/%s/delete/'
    url_change_profile_pix = 'https://www.instagram.com/accounts/web_change_profile_picture/'
    url_edit_account = 'https://www.instagram.com/accounts/edit/'
    ####### Url Strings ########
    url_user = 'https://instagram.com/%s/'
    url_query = 'https://www.instagram.com/graphql/query/?query_hash=%s&variables=%s'
    url_ping_server = 'https://www.shopbraid.com/instapybot_log.php'
    url_bot_av_acct = 'https://www.shopbraid.com/bot_av_acct.php'
    url_bot_av_acct_update = 'https://www.shopbraid.com/bot_av_acct_update.php'
    edit_fields = {
        'biography': '',
        'chaining_enabled': 'on',
        'email': '',
        'external_url': '',
        'first_name': '',
        'gender': 3,
        'phone_number': '',
        'private_account': '',
        'username': ''
    }

    # General Data #
    instaAccount = 'shopbraid'
    log_mod = 0
    user_agent = "" ""
    accept_language = 'en-US,en;q=0.5'
    media_on_profile = []
    login_status = False
    csrftoken = ''
    default_content_type = 'application/x-www-form-urlencoded'
    min_post = 4

    fake_ua = UserAgent()
    saveBotsToFile = False
    saveBotsToServer = True
    botBatch = 7
    bot_id = 0
    def __init__(self):
        self.fake_ua = UserAgent()
        self.user_agent = str(self.fake_ua.random)
        self.s = requests.Session()
        self.bot_mode = 0

    def __delete__(self, instance):
        del self.fake_ua
        del self.user_agent
        del self.s
        del self.bot_mode
        print('Instance deleted')

    def clean_vars(self):
        self.email = self.email.lower()
        self.username = self.username.lower()

    def signup(self):
        log_string = 'Trying to signup ...\n'
        self.write_log(log_string)
        self.signup_post = {
            'email': self.email,
            'first_name': self.first_name,
            'password': self.signup_password,
            'seamless_login_enabled': self.seamless_login_enabled,
            'username': self.username
        }

        self.s.headers.update({
            'Accept': '*/*',
            'Accept-Language': self.accept_language,
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'User-Agent': self.user_agent,
            'X-Instagram-AJAX': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest'
        })

        r = self.s.get(self.url)
        self.s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        self.csrftoken = r.cookies['csrftoken']
        time.sleep(5 * random.random())
        signup = self.s.post(
            self.url_signup, data=self.signup_post, allow_redirects=True)
        self.s.headers.update({'X-CSRFToken': signup.cookies['csrftoken']})
        self.csrftoken = signup.cookies['csrftoken']
        # ig_vw=1536; ig_pr=1.25; ig_vh=772;  ig_or=landscape-primary;
        self.s.cookies['ig_vw'] = '1536'
        self.s.cookies['ig_pr'] = '1.25'
        self.s.cookies['ig_vh'] = '772'
        self.s.cookies['ig_or'] = 'landscape-primary'
        time.sleep(5 * random.random())

        if signup.status_code == 200:
            #r = self.s.get('https://www.instagram.com/')
            #finder = r.text.find(self.username)
            checker = json.loads(signup.text)
            try:
                user_id = checker['user_id']
                #status = checker['status']
                account_created = checker['account_created']
            except:
                user_id = ''
                #status = ''
                account_created = False
            if len(user_id) > 0 and account_created:
                self.bot_start = datetime.datetime.now()
                self.user_id = user_id
                print(self.username)
                self.login_status = True
                self.ping_server_and_log_file(self.saveBotsToFile, self.saveBotsToServer, self.botBatch)
                log_string = '%s signup successfull. You are loggedin!' % self.username
                self.write_log(log_string)
            else:
                print('USERNAME', self.username)
                print(self.s.headers)
                print(self.signup_post)
                print(json.loads(signup.text))
                print(r.text)
                self.login_status = False
                self.write_log('Signup error! Check your login data!')
        else:
            self.write_log('Signup! Connection error!')

    def ping_server_and_log_file(self, saveBotsToFile, saveBotsToServer, botBatch):
        if saveBotsToFile:
            f = open(self.instauser_file, 'a')
            f.write(self.username + ', ')
        if saveBotsToServer:
            url_ping_server = self.url_ping_server
            ping_body = {
                "username": self.username,
                "email": self.email,
                "first_name": self.first_name,
                "test": botBatch
            }
            r = self.s.post(url_ping_server, data=ping_body, allow_redirects=True)
            all_data = json.loads(r.text)
            if "Inserted" in all_data:
                if all_data["Inserted"]:
                    self.bot_id = all_data["BotID"]
                    print('{'+self.username+', '+self.email+', '+self.first_name+'} Logged at '+url_ping_server)
                else:
                    print(
                        '{' + self.username + ', ' + self.email +
                        ', ' + self.first_name + ' ' + botBatch + ' } Log at ' + url_ping_server+' failed!')
            with open('username.txt', 'wt') as f:
                f.write(self.username)

    def edit_account(self, data):
        if self.login_status:
            self.fill_account_details()
            edit_fields = self.edit_fields
            for field in data:
                edit_fields[field] = data[field]
            print(edit_fields)
            r = self.s.post(self.url_edit_account, data=edit_fields)
            print(r.text)

    def fill_account_details(self):
        self.edit_fields['email'] = self.username + '@gmail.com'
        self.edit_fields['first_name'] = self.username.replace('_', ' ').title()
        self.edit_fields['username'] = self.username

    def get_user_id_from_username(self, user):
        user_id_url = self.url_user_detail % user
        info = self.s.get(user_id_url)
        all_data = json.loads(info.text)
        print(all_data)
        user_id = all_data['graphql']['user']['id']
        return user_id

    def follow(self, user_id):
        """ Send http request to follow """
        if self.login_status:
            url_follow = self.url_follow % (user_id)
            try:
                follow = self.s.post(url_follow)
                if follow.status_code == 200:
                    self.follow_counter += 1
                    log_string = "Followed: %s #%i." % (user_id,
                                                        self.follow_counter)
                    self.write_log(log_string)
                    #username = self.get_username_by_user_id(user_id=user_id)
                    #insert_username(self, user_id=user_id, username=username)
                return follow
            except:
                logging.exception("Except on follow!")
        return False

    def logout(self):
        now_time = datetime.datetime.now()
        log_string = 'Logging out from new account'
        self.write_log(log_string)
        work_time = now_time - self.bot_start
        log_string = 'Bot work time: %s' % work_time
        self.write_log(log_string)

        try:
            logout_post = {'csrfmiddlewaretoken': self.csrftoken}
            logout = self.s.post(self.url_logout, data=logout_post)
            self.write_log("Logout success!")
            self.login_status = False
        except:
            logging.exception("Logout error!")

    def generate_uuid(self, uuid_type):
            generated_uuid = str(uuid.uuid4())
            if uuid_type:
                return generated_uuid
            else:
                return generated_uuid.replace('-', '')

    def design(self):
        media_uploads = []
        min_post = self.min_post
        input_name = "photo"
        media_folder = self.media_folder
        #print('2. ' + self.root)
        #print(media_folder)
        ext = '.jpg'
        mention = "@"+self.instaAccount
        media = ''
        if os.path.exists(self.root + 'media.txt'):
            with open(self.root + 'media.txt') as f:
                user_posts = f.readline()
                try:
                    user_posts = int(user_posts)
                except:
                    user_posts = 0
        else:
            user_posts = 0
        if user_posts < min_post:
            min_post = min_post - user_posts
            while len(media_uploads) < min_post:
                while media in media_uploads or media == '':
                    media = media_folder + random.choice(os.listdir(media_folder))
                    #print(media)
                media_comment = commentGen(randint(25, 30), 'hashtags', '')
                print(media + '\n')
                if self.upload_media(input_name, media, mention, media_comment):
                    media_uploads.append(media)
                    time.sleep(10)
            if self.change_profile_pix(input_name="profile_pic", filename="profilepic", file_address=media):
                with open(self.root + 'profile_pic.txt', 'w') as f:
                    f.write('updated')
            with open(self.root + 'media.txt', 'w') as f:
                f.write(str(len(media_uploads) + user_posts))
        line = ''
        try:
            with open(self.root + 'profile_pic.txt') as f:
                line = f.readline()
        except:
            if len(line) == 0 or line != "updated":
                media = media_folder + 'image' + str(randint(1, filesCount(media_folder, ext))) + ext
                if self.change_profile_pix(input_name="profile_pic", filename="profilepic", file_address=media):
                    with open(self.root + 'profile_pic.txt', 'w') as f:
                        f.write('updated')

    def change_profile_pix(self, input_name, filename, file_address):
        self.uuid = self.generate_uuid(False)
        url_change_profile_pix = self.url_change_profile_pix
        data = {input_name: (filename + '.jpg', open(file_address, 'rb'), 'image/jpeg')}
        m = MultipartEncoder(data, boundary=self.uuid)
        self.s.headers.update({'Content-Type': 'multipart/form-data; boundary=' + self.uuid})
        r = self.s.post(url_change_profile_pix, data=m.to_string())
        all_data = json.loads(r.text)
        changed = False
        if "changed_profile" in all_data:
            if all_data["changed_profile"]:
                changed = True
        if changed:
            log_text = "Profile Pix Successfully Changed"
            returnValue = True
        else:
            log_text = "Profile Pix Upload Failed!"
            returnValue = False
        print(log_text)
        self.s.headers.update({'Content-Type': self.default_content_type})
        return returnValue

    def upload_media(self, input_name, filename, mention, media_comment):
        self.uuid = self.generate_uuid(False)
        url_upload = self.url_upload
        upload_id = str(int(time.time() * 1000))
        data = {
            "upload_id": upload_id,
            input_name: (input_name+'.jpg', open(filename, 'rb'), 'image/jpeg')
        }
        m = MultipartEncoder(data, boundary=self.uuid)
        self.s.headers.update({'Content-Type': 'multipart/form-data; boundary='+self.uuid})
        self.s.headers.update({'Referer': 'https://www.instagram.com/create/style/'})
        r = self.s.post(url_upload, data=m.to_string())
        all_data = json.loads(r.text)
        trueAggregate = 0
        if "upload_id" in all_data:
            upload_id = all_data["upload_id"]
            print('UPLOAD ID: '+str(upload_id))
            trueAggregate += 1
            all_data = self.add_caption(upload_id, mention)
            print(all_data)
            if len(all_data) > 0:
                user_id = all_data["media"]["caption"]["user_id"]
                media_id_user_id = all_data["media"]["id"]
                media_id = str(media_id_user_id).replace("_"+str(user_id), "")
                if(len(media_id) > 0):
                    trueAggregate += 1
                self.like(media_id)
                do_comment = self.comment(media_id, media_comment)
                print(do_comment)
                self.default_headers()
                if trueAggregate == 2:
                    return True
                else:
                    return False
            else:
                #self.keep_following = False
                print('Media caption configuration failed. So comment was added')
                self.comment(upload_id, mention)
                return True

    def add_caption(self, upload_id, mention):
        caption = commentGen(1, 'caption', mention)
        configure_body = {
            "upload_id": upload_id,
            "caption": caption
        }
        print(caption)
        url_upload_configure = self.url_upload_configure
        self.s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        self.s.headers.update({'Referer': 'https://www.instagram.com/create/details/'})
        r = self.s.post(url_upload_configure, data=configure_body, allow_redirects=True)
        all_data = json.loads(r.text)
        if all_data["media"]["caption"] is None:
            ui = UserInfo()
            user_id = ui.get_user_id_by_login(self.username)
            media_id_user_id = all_data["media"]["id"]
            media_id = str(media_id_user_id).replace("_" + str(user_id), "")
            #self.delete_media(media_id)
            all_data = []
        return all_data

    def delete_media(self, media_id):
        """ Send http request to delete media """
        all_data = []
        if self.login_status:
            url_delete_media = self.url_delete_media % media_id
            try:
                delete_media = self.s.post(url_delete_media)
                all_data = json.loads(delete_media.text)
                if all_data["status"] == "ok":
                    log_string = "Media deleted: %s" % media_id
                    self.write_log(log_string)
            except:
                logging.exception("Except on delete_media!")
        print('DELETE!!!')
        return all_data

    def like(self, media_id):
        """ Send http request to like media by ID """
        if self.login_status:
            url_likes = self.url_likes % (media_id)
            try:
                like = self.s.post(url_likes)
                last_liked_media_id = media_id
                self.like_counter += 1
                log_string = "Liked: %s #%i." % (media_id, self.like_counter)
                print(log_string)
            except:
                logging.exception("Except on like!")
                like = 0
            return like


    def comment(self, media_id, comment_text):
        """ Send http request to comment """
        all_data = []
        if self.login_status:
            comment_post = {'comment_text': comment_text}
            url_comment = self.url_comment % media_id
            try:
                comment = self.s.post(url_comment, data=comment_post)
                all_data = json.loads(comment.text)
                if all_data["status"] == "ok":
                    #self.comments_counter += 1
                    #self.comments_today += 1
                    log_string = 'Write: "%s". #%i.' % (comment_text)
                    self.write_log(log_string)
            except:
                logging.exception("Except on comment!")
        print('Comment!!!')
        return all_data


    def default_headers(self):
        self.s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        self.s.headers.update({'Referer': 'https://www.instagram.com/'})

    def write_log(self, log_text):
        """ Write log by print() or logger """

        if self.log_mod == 0:
            try:
                now_time = datetime.datetime.now()
                print(now_time.strftime("%d.%m.%Y_%H:%M")  + " " + log_text)
            except UnicodeEncodeError:
                print("Your text has unicode problem!")
        elif self.log_mod == 1:
            # Create log_file if not exist.
            if self.log_file == 0:
                self.log_file = 1
                now_time = datetime.datetime.now()
                self.log_full_path = '%s%s_%s.log' % (
                    self.log_file_path, self.user_login,
                    now_time.strftime("%d.%m.%Y_%H:%M"))
                formatter = logging.Formatter('%(asctime)s - %(name)s '
                                              '- %(message)s')
                self.logger = logging.getLogger(self.user_login)
                self.hdrl = logging.FileHandler(self.log_full_path, mode='w')
                self.hdrl.setFormatter(formatter)
                self.logger.setLevel(level=logging.INFO)
                self.logger.addHandler(self.hdrl)
            # Log to log file.
            try:
                self.logger.info(log_text)
            except UnicodeEncodeError:
                print("Your text has unicode problem!")