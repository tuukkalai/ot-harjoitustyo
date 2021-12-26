# Requirement specification

## Purpose of the application

With the application, user has the ability to log events in a diary by adding entries.

Multiple registered users can use the application, with their own logs in the journal.

## Users

Application is used with _regular user_ role.

## User Interface

The application consists of following views.

- Login
- Create new user
- List diary entries
- Editing an entry

## Functionalities

### Before logging in / registering

- [x] User can register new user to the system
  - [x] Username must be unique, min. 3 characters
  - [x] Password must be min. 3 characters long

- [x] User can log in
  - [x] Logging in is done by inputting username and correct password to form, and clicking "Login"
  - [x] In the event of invalid username, or invalid username and password combination, login screen notifies the user

### After logging in

- [x] User can view list of diary entries
- [x] User can create a new entry
  - [x] Entry is only visible to logged in user
- [x] User can open an entry to edit mode
- [x] User can log out

### View entries mode

- [x] Filtering entries based on categories

### Edit mode

- [x] User can update the entry heading
- [x] User can update the entry text
  - [x] After update the user is kept on current entry edit screen
- [x] User can delete the entry
  - [x] After deletion user is returned to list of entries
- [x] User can return to list of entries without deleting or updating entry
- [x] Adding/removing categories to entries
