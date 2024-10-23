# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Prompt

@route_post(BASE_URL + 'new_prompt', args={'prompt':str, 'categories': str})
def new_prompt(args):
    new_prompt = Prompt(
        categories = args['categories'],
        prompt = args['prompt'],
        correct = 0,
        guesses = 0
    )

    new_statement.save()

    return {'statement': new_statement.json_response()}

@route_get(BASE_URL + 'all_categories')
def all_categories(args):
    categories_list = [],


    for categories in Prompt.objects.all():
        categories_list.append(categories.json_response())

    return {'category':categories_list}

@route_get(BASE_URL + 'all_prompt', args={'categories': str})
def all_prompts(args):
    prompts_list = []

    for prompt in Prompt.objects.all():
        prompt_list.append(prompt.json_response())

    return {'prompt':prompt_list}

@route_post(BASE_URL + 'new_prompt', args={'prompt': str})
def new_prompt(args):    

    new_category = all_categories(
        category = args['category']
    )

    new_category.save()

@route_post(BASE_URL + 'new_category', args={'categories': str})
def new_category(args):

    new_category = all_categories(
        category = args['categories']
    )

    new_category.save()