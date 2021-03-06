from django.conf import settings
from django.db import models
from django.utils import timezone

# ブログの投稿を管理するクラス
class Post(models.Model): #(models.Model) -> Djangoがデータベースに保存すべきもの
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)            #文字数が制限されたテキストを定義
    text = models.TextField()                           #文字数が制限されないテキストを定義
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログの投稿機能
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
