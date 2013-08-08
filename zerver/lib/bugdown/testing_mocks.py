
import ujson

def twitter(tweet_id):
    if tweet_id not in ["112652479837110273", "287977969287315456", "287977969287315457"]:
        return None
    return ujson.loads("""{
  "coordinates": null,
  "created_at": "Sat Sep 10 22:23:38 +0000 2011",
  "truncated": false,
  "favorited": false,
  "id_str": "112652479837110273",
  "in_reply_to_user_id_str": "783214",
  "text": "@twitter meets @seepicturely at #tcdisrupt cc.@boscomonkey @episod http://t.co/6J2EgYM",
  "contributors": null,
  "id": 112652479837110273,
  "retweet_count": 0,
  "in_reply_to_status_id_str": null,
  "geo": null,
  "retweeted": false,
  "possibly_sensitive": false,
  "in_reply_to_user_id": 783214,
  "user": {
    "profile_sidebar_border_color": "eeeeee",
    "profile_background_tile": true,
    "profile_sidebar_fill_color": "efefef",
    "name": "Eoin McMillan ",
    "profile_image_url": "http://a1.twimg.com/profile_images/1380912173/Screen_shot_2011-06-03_at_7.35.36_PM_normal.png",
    "created_at": "Mon May 16 20:07:59 +0000 2011",
    "location": "Twitter",
    "profile_link_color": "009999",
    "follow_request_sent": null,
    "is_translator": false,
    "id_str": "299862462",
    "favourites_count": 0,
    "default_profile": false,
    "url": "http://www.eoin.me",
    "contributors_enabled": false,
    "id": 299862462,
    "utc_offset": null,
    "profile_image_url_https": "https://si0.twimg.com/profile_images/1380912173/Screen_shot_2011-06-03_at_7.35.36_PM_normal.png",
    "profile_use_background_image": true,
    "listed_count": 0,
    "followers_count": 9,
    "lang": "en",
    "profile_text_color": "333333",
    "protected": false,
    "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme14/bg.gif",
    "description": "Eoin's photography account. See @mceoin for tweets.",
    "geo_enabled": false,
    "verified": false,
    "profile_background_color": "131516",
    "time_zone": null,
    "notifications": null,
    "statuses_count": 255,
    "friends_count": 0,
    "default_profile_image": false,
    "profile_background_image_url": "http://a1.twimg.com/images/themes/theme14/bg.gif",
    "screen_name": "imeoin",
    "following": null,
    "show_all_inline_media": false
  },
  "in_reply_to_screen_name": "twitter",
  "in_reply_to_status_id": null
}""")