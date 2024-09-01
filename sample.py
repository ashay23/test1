import pickle

# Load the pickle file
with open('path_to_your_file.pkl', 'rb') as file:
    loaded_object = pickle.load(file)

# Check the type of the object
print(f"Type of the loaded object: {type(loaded_object)}")

# List all attributes and methods of the object
print("Attributes and methods of the loaded object:")
print(dir(loaded_object))

# If it's a known object type, you can access its attributes directly
# For example, if it's a scikit-learn model or a vectorizer:
if hasattr(loaded_object, 'get_params'):
    print("Parameters of the loaded object:")
    print(loaded_object.get_params())

# If it's a dictionary or list, you can print it directly or iterate over its contents
if isinstance(loaded_object, dict):
    print("Keys in the dictionary:")
    print(loaded_object.keys())

# You can also inspect specific attributes if you know what to look for
if hasattr(loaded_object, 'vocabulary_'):
    print("Vocabulary of the vectorizer:")
    print(loaded_object.vocabulary_)
