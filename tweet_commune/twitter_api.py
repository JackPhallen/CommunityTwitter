import tweepy


class TwitterAPI:

    def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(self.auth)

    def post(self, status, img_paths=None):
        if img_paths:
            self._post_media(status, img_paths)
        else:
            self.api.update_status(status)

    def _post_media(self, status, img_paths):
        media_ids = [self._upload_media(path) for path in img_paths]
        self.api.update_status(status, media_ids=media_ids)

    def _upload_media(self, img_path):
        response = self.api.media_upload(img_path)
        return response.media_id
