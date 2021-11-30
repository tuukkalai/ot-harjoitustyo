# PyDiary

With PyDiary application user can add and edit diary notes. With PyDiary application multiple users can keep diary notes on single application by logging in with their own user credentials.

PyDiary is part of course work at University of Helsinki.

## Documentation

- [Requirement specification](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/documentation/requirement_specification.md)
- [Work hour records](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/documentation/work-hour-records.md)

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

### Create test coverage report

```sh
poetry run invoke coverage-report
```

### Open test coverage report on Firefox

```sh
poetry run invoke coverage-ff
```

### Run lint score

```sh
poetry run invoke lint
```

### Run code formatting

```sh
poetry run invoke format
```
