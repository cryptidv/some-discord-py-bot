from utils.reddit import SubReddit
from discord.embeds import Embed

async def reddit(ctx, sub):
    post = await (await SubReddit(sub).init()).get_random_by_hot()

    if post.nsfw and not ctx.channel.nsfw:
        await ctx.send(':x: No nsfw in a not nsfw channel tsk tsk')
        return False

    embed = Embed()
    embed.color = 0x0019FF
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