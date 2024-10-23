# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
My API is made for pictionary games for friends. Users will choose categories from the API and it will generate a word related to the category. 

### Models:


### Endpoints

*Replace this with a guide to your endpoints and model. You can write a Markdown chart [here](https://www.tablesgenerator.com/markdown_tables)*


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

$ http GET 127.0.0.1:5000/thebestpictionary/one_category id=1

{
    "category_id": 1,
    "category": "movies"
}

### all_prompt

$ http GET 127.0.0.1:5000/thebestpictionary/all_prompt category=movies

{
    "correct": 0,
    "guesses": 0,
    "id": 1,
    "category": "movies"
    "prompt": "Twisters"

    "correct": 0,
    "guesses": 0,
    "id": 1,
    "category": "movies"
    "prompt": "Joker"

    "correct": 0,
    "guesses": 0,
    "id": 1,
    "category": "movies"
    "prompt": "Transformers"
}

### Add a category

```
$ http POST 127.0.0.1:5000/thebestpictionary/new_category "new_category": "Sports"

{
    "category_id": 3,
    "category": "Sports"
}

### Add_prompt



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




