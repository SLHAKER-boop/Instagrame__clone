from kivymd.uix.screen import MDScreen


import json
from libs.components.post_card import PostCard

from libs.components.circular_avatar_image import CircularAvatarImage


class HomePage(MDScreen):
    profile_picture = 'https://scontent.fcmb4-2.fna.fbcdn.net/v/t1.6435-9/120818183_330624244865762_2297467628981635920_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=XT1uWHnZzIsAX9WmMei&_nc_ht=scontent.fcmb4-2.fna&oh=00_AT8BrttDwb6jM4cGx62uKaOdC3t8OMHuFF63o1R1M8ibNQ&oe=61E16F91'

    def on_enter(self):
        self.list_stories()
        self.list_posts()

    def list_stories(self):
        with open('assets/data/stories.json') as f_obj:
            data = json.load(f_obj)
            for name in data:
                self.ids.stories.add_widget(CircularAvatarImage(
                    avatar = data[name]['avatar'],
                    name = name
                ))
    
    def list_posts(self):
        with open('assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username = username,
                    avatar = data[username]['avatar'],
                    profile_pic = self.profile_picture,
                    post = data[username]['post'],
                    caption = data[username]['caption'],
                    likes = data[username]['likes'],
                    comments = data[username]['comments'],
                    posted_ago = data[username]['posted_ago'],
                ))
