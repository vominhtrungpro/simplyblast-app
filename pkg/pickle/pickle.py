import pickle

def save_token_to_local_storage(token):
    with open('access_token.pickle', 'wb') as f:
        pickle.dump(token, f)

def load_token_from_local_storage():
    try:
        with open('access_token.pickle', 'rb') as f:
            token = pickle.load(f)
            return token
    except FileNotFoundError:
        return None

# access_token = "your_access_token_here"
# save_token_to_local_storage(access_token)

# loaded_token = load_token_from_local_storage()
# print("Loaded Token:", loaded_token)
