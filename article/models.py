from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.article_id})
        return "http://127.0.0.1:8000%s" % path

    def __unicode__(self):
	return self.title


    class Meta:
	ordering = ['-date_time']

