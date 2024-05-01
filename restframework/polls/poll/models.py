from django.db import models

from django.contrib.auth.models import User

# Models HierArchy

# 1)    8 - 15       --->      Poll Model
# 2)    19 - 26      --->      Choice Model
# 3)    29 - 36      --->      Vote Model



class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.question
    
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name="choices",on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.choice_text
    

class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes',on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    class Meta:
        unique_together = ("poll", "voted_by")
