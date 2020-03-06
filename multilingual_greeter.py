def greet(greeting,nam):
    """Print Greetings with name"""

    print(greeting + " " +nam)

def language_input():
    language = input("please select your language: hindi/english/mexican:\n")
    if language == "hindi":
        name = input("aapka naam kya hai:\n")
        greet("namaste", name)
    elif language == "english":
        name = input("what is your name:\n")
        greet("hello")
    elif language == "mexican":
        name = input("cual es su nombre:\n")
        greet("hola")



language_input()






