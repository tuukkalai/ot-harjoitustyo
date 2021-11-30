from invoke import task

@task
def start(ctx):
    ctx.run('python src/main.py')

@task
def test(ctx):
    ctx.run('pytest src --envfile ./.env.test')

@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest src --envfile ./.env.test')

@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage html')

@task(coverage_report)
def coverage_ff(ctx):
    ctx.run('firefox ./htmlcov/index.html')