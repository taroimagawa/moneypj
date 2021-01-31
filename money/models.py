from django.db import models

CHOICE = (('Taro', 'Taro'), ('Koki', 'Koki'), ('Kaze', 'Kaze'))

class Money(models.Model):
    purpose = models.CharField('用途', max_length=100)
    name = models.CharField(
        '名前',
        max_length=100,
        choices=CHOICE
        )
    amount = models.IntegerField('金額(円)')
    posted_date = models.DateTimeField('時刻', auto_now_add=True)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return self.purpose