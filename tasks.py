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
    ctx.run('coverage report')

@task(coverage)
def coverage_html(ctx):
    ctx.run('coverage html')

@task(coverage_report)
def coverage_ff(ctx):
    ctx.run('firefox ./htmlcov/index.html')

@task
def lint(ctx):
    ctx.run('pylint src')

@task
def format(ctx):
    ctx.run('autopep8 --in-place --recursive src')