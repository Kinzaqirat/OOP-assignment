class Logger:
    def __init__(self):
        print("Logger object created.")  # Constructor message

    def __del__(self):
        print("Logger object destroyed.")  # Destructor message


logger = Logger()  # This will call the constructor

del logger
