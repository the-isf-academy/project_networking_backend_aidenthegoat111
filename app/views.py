# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Prompt

@route_post(BASE_URL + 'new_prompt', args={'prompt':str, 'categories': str})
def new_prompt(args):
    new_prompt = Prompt(
        categories = args['categories'],
        prompt = args['prompt'],
        correct = False
    )

    new_prompt.save()

    return {'prompt': new_prompt.json_response()}

@route_get(BASE_URL + 'all_categories')
def all_categories(args):
    categories_list = ['all_categories']


    for categories in Prompt.objects.all():
        categories_list.append(categories.json_response())

    return {'category':categories_list}

@route_get(BASE_URL + 'all_prompt', args={'categories': str})
def all_prompts(args):
    prompt_list = ['all_prompts']

    for prompt in Prompt.objects.all():
        prompt_list.append(prompt.json_response())

    return {'prompt':prompt_list}

@route_post(BASE_URL + 'new_category', args={'categories': str})
def new_category(args):

    new_category = all_categories(
        category = args['categories']
    )

    new_category.save()

@route_get(BASE_URL + 'search', args={'keyword': str})
def search(args):
    if Prompt.objects.exists():

        search = []

        for prompt in Prompt.objects.all():
            search.append(prompt.json_response())
            return {'prompt': prompt_list}
        else:
            return {'error': 'no prompt exisit'}


@route_get(BASE_URL + 'random')
def random_prompt(args):

    random_prompt = Prompt.objects.order_by('?').first()
 
    return {'prompt': random_prompt.json_response()}