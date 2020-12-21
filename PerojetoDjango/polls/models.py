from django.db import models

class Question(models.Model):
    questionText = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.questionText


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text