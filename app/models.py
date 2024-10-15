# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField


class Prompt(Model):
    statement = StringField()
    categories = StringField()
    correct = BooleanField()
    likes = IntegerField()
    prompt = StringField()

     def json_response(self):
        
        return {
            'id': self.id,
            'statement': self.statement,
            'likes': self.likes,
            'correct': self.correct,
            'categories': self.categories,
            'prompt': self.prompt
        }

   