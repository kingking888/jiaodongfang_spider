import execjs

with open('./my.js') as f:  # 执行 JS 文件
    ctx = execjs.compile(f.read())

print(ctx.call('test'))