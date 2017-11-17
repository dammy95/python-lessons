

class User:

	def __init__(self, username, email, age):
		self.username = username
		self.email = email
		self.age = age


class InvalidAgeException(Exception):
	pass


class TooYoungException(Exception):
	pass


class InvalidEmailException(Exception):
	pass


class InvalidUserNameException(Exception):
	pass


if __name__ == '__main__':
	directory = {}

	example_list = [
		("jane", "jane@example.com", 21),
		("bob", "bob@example", 19),
		("jane", "jane2@example.com", 25),
		("steve", "steve@somewhere", 15),
		("joe", "joe", 23),
		("anna", "anna@example.com", -3),
	]

	for username, email, age in example_list:

		try:
			if username in directory:
				raise InvalidUserNameException()
			if age < 0:
				raise InvalidAgeException()
			if age < 16:
				raise TooYoungException()
			if '@' not in username:
				raise InvalidUserNameException()

		except DuplicateUsernameError:
        	print("Username '%s' is in use." % username)
	    except InvalidAgeError:
	        print("Invalid age: %d" % age)
	    except UnderageError:
	        print("User %s is underage." % username)
	    except InvalidEmailError:
	        print("'%s' is not a valid email address." % email)

	    else:
	        directory[username] = User(username, email)
