# PyDiary

With PyDiary application user can add and edit diary notes. With PyDiary application multiple users can keep diary notes on single application by logging in with their own user credentials.

PyDiary is part of course work at University of Helsinki.

## Documentation

- [Requirement specification](./documentation/requirement_specification.md)
- [Work hour records](./documentation/work-hour-records.md)
- [Architecture](./documentation/architecture.md)

## Installation

### Install Poetry dependencies

```sh
poetry install
```

## Start the application

```sh
poetry run invoke start
```

## Other command line functionalities

### Run tests

```sh
poetry run invoke test
```

### Create HTML test coverage report

```sh
poetry run invoke coverage-html
```

#### Create HTML test coverage report and open it with Firefox

```sh
poetry run invoke coverage-ff
```

After creating the html report, next shell command is called

```sh
firefox ./htmlcov/index.html
```

### Create CLI test coverage report

```sh
poetry run invoke coverage-report
```

### Run lint score

```sh
poetry run invoke lint
```

### Run code formatting

```sh
poetry run invoke format
```
