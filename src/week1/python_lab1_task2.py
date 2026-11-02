def greet_user(name: str) -> str:
    cleaned_name = name.strip().capitalize() or "Stranger"
    return f"Hello, {cleaned_name}! Welcome to Python!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
