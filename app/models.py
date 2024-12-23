# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField


class Prompt(Model):
    statement = StringField()
    correct = BooleanField()
    likes = IntegerField()
    prompt = StringField()
    categories = StringField()
    keyword = StringField()

    def json_response(self):
        
        return {
            'categories': self.categories,
            'id': self.id,
            'prompt': self.prompt
        }

    def increase_likes(self):

        self.likes += 1
        self.save()

    def change_prompt(self, new_prompt):

        self.prompt = new_statement
        self.likes = 0
        self.save()
    
    def json_response_incorrect_guess(self):
        return(
            {'id': self.id,
            'prompt': self.prompt,
            'guesses': self.guesses,
            'incorrect': False}
        )

    def json_response_correct_guess(self):
        return(
            {'id': self.id,
            'prompt': self.prompt,
            'guesses': self.guesses,
            'correct': True}
        )

    # def keywords(self):

    