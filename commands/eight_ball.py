import random
choices = [
    "As I see it, yes.",            
    "Ask again later.",                          
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "Don’t count on it.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it."
]

async def eight_ball(ctx, arg):
    a = ctx.author
    random.shuffle(choices)
    await ctx.send(f'{a.name} said: *`{arg}`*\nMy response is: **{random.choice(choices)}**')