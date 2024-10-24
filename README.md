# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
My API is made for pictionary games for friends. Users will choose categories from the API and it will generate a word related to the category. 

### Models:


### Endpoints

*Replace this with a guide to your endpoints and model. You can write a Markdown chart [here](https://www.tablesgenerator.com/markdown_tables)*

| # Route name    | # Description                                                                                                             | # HTTP Method | # Payload             | # Example                                                                                                                                                                                      |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|---------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| add_prompt      | Adds new word and/or add a new category                                                                                   | post          | category prompt       | category_id = 1 category = sports prompt_id = 1 prompt = Football                                                                                                                              |
| all_prompts     | View all words available in a selected category                                                                           | get           | category              | category_id = 1 category = sports prompt_id = 1 prompt = Football  category_id = 1 category = sports prompt_id = 2 prompt = Basketball                                                         |
| generate_prompt | Generates a random word from a selected category                                                                          | get           | category              | category_id = 1 category = sports prompt_id = 1 prompt = Football                                                                                                                              |
| Guess_answer    | Player guesses the answer                                                                                                 | post          | category prompt guess | Correct guess: category_id = 1 category = sports prompt_id = 1 prompt = Football Correct = 1  Incorrect guess: category_id = 1 category = sports prompt_id = 1 prompt = Football Incorrect = 1 |
| search_prompt   | searches for words containing keywords in a selected category  Can also search for specific categories containing keyword | get           | keyword               | keyword = ball  category = sports id = 1 prompt = Football   category = sports id = 2 prompt = Basketball                                                                                      |
| random_prompt   | generates a random prompt                                                                                                 | get           | N/A                   | category = sports id = 2 prompt = basketball                                                                                                                                                   |
| all             | View all prompts in any categories                                                                                        | get           | N/A                   | category = sports id = 1 prompt = football  category = sports id = 2 prompt = basketball  category = movies id = 3 prompt = interstellar                                                       |

### all_categories

$ http GET 127.0.0.1:5000/thebestpictionary/all_categories

{
    "categories": [
        {
            "category_id": 1,
            "category": "movies"

            "category_id": 2,
            "category": "animals"
        }
    ]
}

### Get category from id

$ http GET 127.0.0.1:5000/thebestpictionary/one_category 

"category_id=1"

{
    "category_id": 1,
    "category": "movies"
}

### all_prompt

$ http GET 127.0.0.1:5000/thebestpictionary/all_prompt 

"category=movies"

{
    "correct": 0,
    "guesses": 0,
    "category_id": 1,
    "category": "movies",
    "prompt_id": 1,
    "prompt": "Twisters"

    "correct": 0,
    "guesses": 0,
    "category_id": 1,
    "category": "movies",
    "prompt_id": 2,
    "prompt": "Joker"

    "correct": 0,
    "guesses": 0,
    "category_id": 1,
    "category": "movies"
    "prompt_id": "3"
    "prompt": "Transformers"
}

### Add a category

```
$ http POST 127.0.0.1:5000/thebestpictionary/new_category 

{
    "category_id": 3,
    "category": "Sports"
}

### Add_prompt

$ http POST 127.0.0.1:5000/thebestpictionary/new_category "category": "Sports"
"new_prompt": "Football"

{
    "Correct": 0,
    "Guesses": 0
    "category_id": 3,
    "category": "Sports"
    "prompt_id": 4,
    "prompt": "Football"
}

### Guess the answer to a riddle

```
$ http POST 127.0.0.1:5000/riddles/guess id=1 guess="Carrot"

{
    "correct": {
        "answer": "A carrot",
        "correct": 1,
        "guesses": 1,
        "id": 1,
        "question": "What is orange and sounds like a parrot?"
    }
}

## Setup

Start the banjo server with: `banjo`

```
$ banjo
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

You can now access the riddle server at 127.0.0.1 from your own machine, or from
your public IP address if you know what it is. 


### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)

## Usage

If you already know the IP address and port of a running Riddle server, you can
interact with it using HTTP requests. In these examples, we will use the
`HTTPie` library to send HTTP requests from Terminal.

We are connecting to `127.0.0.1:5000`, which is the address of the Riddle server
when it is running locally.




