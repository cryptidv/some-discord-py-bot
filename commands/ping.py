async def ping(ctx):
    await ctx.send(f'Pong! {ctx.bot.latency*1000} ms')