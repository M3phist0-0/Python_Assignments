
import os

class ContextManager:
    """
    initializes attributes for Context Manager
     Attributes:
        file_name: file to load data
        mode(str): mode file is open
        destination(str): directory the working directory will be changed to
     Methods:
     __init__ : initializes the context manager with file name, mode, and destination
     __enter__ : changes working directory to specified destination, opens file, and returns file object
     __exit__ : closes the file and reverts working directory to og state
     """

    def __init__(self, file_name, mode, destination):
        """
        initializes attributes for Context Manager
         Args:
            file_name: file to load data
            mode: mode file is open
            destination: directory the working directory will be changed to
         Return:
         None
         """
        self.file_name = file_name
        self.mode = mode
        self.destination = destination
        self.cwd = os.getcwd()


    def __enter__(self):
        """
        Set up method
        Returns:
         the opened file and prints statement indicating change in directory
        """
        print('Before changing directory:', self.cwd)
        os.chdir(self.destination)
        print('After changing directory:', os.getcwd())

        self.file = open(self.file_name, self.mode)
        return self.file


    def __exit__(self, exc_type, exc_val, traceback):
        """
         tear down method
         Args:
            exc_type: the exception type
            exc_val: the exception instance
            traceback: the traceback objects

         """
        print("\nBefore changing directory:", os.getcwd())
        os.chdir(self.cwd)
        print('After changing directory (exit):', os.getcwd())

        if hasattr(self, 'file') and not self.file.closed:
              self.file.close()
              print(f'{self.file_name} closed.')





