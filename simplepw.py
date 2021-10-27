import random
import string


class SimplePW:
    def __init__(
        self,
        length: int = 10,
        special_chars: bool = False,
        digits: bool = True,
        uppercase: bool = True,
        lowercase: bool = True,
    ):
        self.length = length
        self.special_chars = special_chars
        self.digits = digits
        self.uppercase = uppercase
        self.lowercase = lowercase

    def get(self) -> str:
        """Generates and returns a password with the user-specified options. The
        minimum password length is 4 characters.

        Returns:
            str: Final password meeting all user option requirements.
        """

        def get_random(possible_chars: str) -> str:
            # Returns a random sample of the possible characters specified, the sample
            # may not meet all specified password requirements requirements
            random_sample = random.sample(possible_chars, self.length)
            random_sample = "".join(random_sample)
            return random_sample

        # Minimum password length is 4 due to 4 total possible character requirements
        if self.length < 4:
            self.length = 4
        # Determine possible characters for the password based on user options
        possible_chars = self.get_possible_chars()
        # Generate a random sample, which may not meet all password requirements
        generated_password = get_random(possible_chars)
        # If the random sample doesn't meet requirements, keep generating until true
        while not self.meets_requirements(generated_password):
            generated_password = get_random(possible_chars)
        # Return
        return generated_password

    def get_possible_chars(self) -> str:
        """Returns a string of possible characters to use for generating the password
        based on user options.

        Returns:
            str: A string of all possible characters according to user options.
        """

        # Check user options to determine what characters to include
        possible_chars = []
        if self.special_chars:
            possible_chars.append(string.punctuation)
        if self.digits:
            possible_chars.append(string.digits)
        if self.uppercase:
            possible_chars.append(string.ascii_uppercase)
        if self.lowercase:
            possible_chars.append(string.ascii_lowercase)
        possible_chars = "".join(possible_chars)
        # Ensure that number of possible chars cannot be exceeded by length of specified password
        while len(possible_chars) < self.length:
            possible_chars += possible_chars
        # Return
        return possible_chars

    def meets_requirements(self, generated_password: str) -> bool:
        """Checks if the passed in string meets all user options.

        Args:
            generated_password (str): String which should be checked for requirements.

        Returns:
            bool: True if requirements are met, False if not
        """

        # If all requirements are met, return True, else return False
        if (
            all(
                [
                    self.check_special_chars(generated_password),
                    self.check_digits(generated_password),
                    self.check_uppercase(generated_password),
                    self.check_lowercase(generated_password),
                ]
            )
            == True
        ):
            return True
        else:
            return False

    def check_special_chars(self, generated_password: str) -> bool:
        """Checks passed in string and ensures at least one special char exists.

        Args:
            generated_password (str): String that should be evaluated.

        Returns:
            bool: True if special char is found, False if not
        """

        if self.special_chars:
            special_chars = string.punctuation
            for char in list(generated_password):
                if char in special_chars:
                    return True
        if not self.special_chars:
            return True
        else:
            return False

    def check_digits(self, generated_password: str) -> bool:
        """Checks passed in string and ensures at least one digit exists.

        Args:
            generated_password (str): String that should be evaluated.

        Returns:
            bool: True if digit char is found, False if not
        """

        if self.digits:
            for char in list(generated_password):
                if char.isdigit():
                    return True
        if not self.digits:
            return True
        else:
            return False

    def check_uppercase(self, generated_password: str) -> bool:
        """Checks passed in string and ensures at least one uppercase char exists.

        Args:
            generated_password (str): String that should be evaluated.

        Returns:
            bool: True if uppercase char is found, False if not
        """

        if self.uppercase:
            for char in list(generated_password):
                if char.isupper():
                    return True
        if not self.uppercase:
            return True
        else:
            return False

    def check_lowercase(self, generated_password: str) -> bool:
        """Checks passed in string and ensures at least lowercase char exists.

        Args:
            generated_password (str): String that should be evaluated.

        Returns:
            bool: True if lowercase char is found, False if not
        """

        if self.lowercase:
            for char in list(generated_password):
                if char.islower():
                    return True
        if not self.lowercase:
            return True
        else:
            return False
