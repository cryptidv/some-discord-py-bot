from utils.reddit import SubReddit
from discord.embeds import Embed
from utils.responses import ResponseType
from utils.discordutils import rand_color

async def reddit(ctx, sub):
    post = await (await SubReddit(sub).init()).get_random_by_hot()

    if not post:
        await ctx.respond(f'The subreddit **`r/{sub}`** does not exist. Check spelling and try again.', ResponseType.WARN)

    if post.nsfw and not ctx.channel.nsfw:
        await ctx.respond('No nsfw in a not nsfw channel, tsk tsk.', ResponseType.FORB)
        return False

    embed = Embed()
    embed.color = rand_color()
    embed.title = post.title
    embed.url = 'https://reddit.com' + post.link
    
    embed.set_footer(text=f'👍 {post.score}')
    embed.set_author(name=f'r/{post.sub}', url=f'https://reddit.com/r/{post.sub}')

    if post.self_txt:
        embed.description = post.self_txt
    
    if post.url:
        print(post.url)
        embed.set_image(url=post.url)

    await ctx.send(embed=embed)
