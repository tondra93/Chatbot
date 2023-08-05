import random

def unknown():
    response=['Could you please rephrase that?',
              "......",
              "Can not get that.",
              "What does that mean?"][random.randrange(4)]
    return response
    