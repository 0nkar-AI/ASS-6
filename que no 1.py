def suggest_completions(search_history, partial_query):
    # Convert the partial query to lowercase for case-insensitive matching
    partial_query = partial_query.lower()
    # Use a list comprehension to find matching completions
    suggestions = [item for item in search_history if item.lower().startswith(partial_query)]
    return suggestions

def main():
    search_history = [
        "apple",
        "banana",
        "carrot",
        "pear",
        "pineapple",
        "potato",
        "strawberry"
    ]
    
    # Get user input for partial search query
    partial_query = input("Enter your partial search query: ")
    
    # Get suggestions based on the user's input
    suggestions = suggest_completions(search_history, partial_query)
    
    # Display the suggestions
    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(suggestion)
    else:
        print("No suggestions found.")

if __name__ == "__main__":
    main()
