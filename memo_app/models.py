from django.db import models
from django.contrib.auth import get_user_model


class Memo(models.Model):
    content = models.CharField(max_length=2000,unique=True)
    update_datetime = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)

    def __str__(self):
        return 'id=' + str(self.id) + ', user=' + str(self.user)+ ', content=' + str(self.content)


class Comment(models.Model):
    comment = models.CharField(max_length=2000)
    update_datetime = models.DateTimeField(auto_now_add=True)
    memo = models.ForeignKey(Memo, db_column='memo_content',to_field='content',related_name="comment" ,on_delete=models.CASCADE)


    def __str__(self):
        return 'comment_id=' + str(self.id) + ',comment=' + str(self.comment) + ',memo_content=' + str(self.memo.content)
