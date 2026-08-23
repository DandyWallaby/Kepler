import Kepler.parser as parser

def handle_request_pipeline() -> None: # Handles PipeLine
    prompt = prompt_user()
    parsed_prompt = parse(prompt)
    tokens = tokenize(parsed_prompt)
    redirect_request(tokens)

def prompt_user() -> str: # Receive Prompt
    print("Prompt : ")
    user_prompt: str = input()
    return user_prompt

def parse(prompt: str) -> list[str]: # Split at Spaces
    
    return prompt.lower().split()
 
def tokenize(text: list[str]) -> list[str]: # Make Clearer Instructions
    tokenized_text: str = []
    deleted_words_count: int = 0

    for word in range(len(text)):
        stripped_word = text[word].strip("!?.,;:\"'")

        if stripped_word == '':
            deleted_words_count += 1
            continue

        tokenized_text.append(stripped_word)

        tokenized_text[word - deleted_words_count] = normalize_tokens(tokenized_text[word - deleted_words_count])
    return tokenized_text

def normalize_tokens(word) -> str: # Change Synonyms For Normalized Words
    synonyms : list[dict] = [
        {
        "token": "bonjour",
        "syn": ["salut", "allo", "salutations", "salutation", "yo", "sup", "wassup", "hey"]
        },
        {
        "token": "placer",
        "syn": ["mets", "met", "mettre", "place", "place", "dispose", "disposer", "range", "ranger", "pose", "poser", "sacre", "sacrer"]
        },
        {
            "token": "kepler",
            "syn": ["toi", "tu", "ia", "bro", "big", "ai", "buddy", "blud"]
        },
        {
        "token": "sa",
         "syn" : ["ca", "ça"]
         },
        {
        "token": "aller",
        "syn" : ["vas","va"]}
                            ]

    for token in synonyms:
        if word in token["syn"]:
            return token["token"]
    return word

def redirect_request(tokens):
    for token in tokens:
        match token:
            case "bonjour":
                parser.bonjour(tokens)
                break
handle_request_pipeline()