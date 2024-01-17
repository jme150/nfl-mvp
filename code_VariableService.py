"""
    NFL MVP Tracker -- Variable Service
    Judah Ellison
    December 2023/January 2024
"""
# Define VariableService class
class VariableService:
    '''
    CLASS: VariableService
    METHODS: __init__, get_instance
    '''
    # Initialize the single instance of VariableService class
    singleton = None

    def __init__(self):
        '''
        METHOD: __init__
            Constructor for VariableService class (stores variables for NFL 
                MVP Tracker)
        PARAMETERS: None
        RETURNS: None (sets default values)
        '''
        # Initialize the variables that need to be stored throughout program
        self.x = 0
        self.y = 0
    
    @classmethod
    def get_instance(cls):
        '''
        METHOD: get_instance()
            Get the instance created for the VariableService class when it was
                first initialized
        PARAMETERS:
            cls - a reference to the VariableService class methods
        RETURNS:
            VariableService.singleton - the singleton instance of the
                VariableService class
        '''
        # If the class hasn't been called yet
        if VariableService.singleton == None:
            # Initialize a new instance
            VariableService.singleton = VariableService()
        # Return the singleton instance of VariableService
        return VariableService.singleton
    
def set_position(x, y):
    '''
    FUNCTION: set_position()
        Stores the x and y coordinates that were clicked in VariablesService
            for future reference
    PARAMETERS:
        x - float - x-coordinate that was clicked
        y - float - y-coordinate that was clicked
    RETURNS: None (stores these values for future reference)
    '''
    instance = VariableService.get_instance()
    instance.x = x
    instance.y = y

def get_position_x():
    '''
    FUNCTION: get_position_x()
        Returns the x-coordinate value that was stored in VariableService
    PARAMETERS: None
    RETURNS:
        x - float - x-coordinate that was stored in VariableService
    '''
    instance = VariableService.get_instance()
    return instance.x

def get_position_y():
    '''
    FUNCTION: get_position_y()
        Returns the y-coordinate value that was stored in VariableService
    PARAMETERS: None
    RETURNS:
        y - float - y-coordinate that was stored in VariableService
    '''
    instance = VariableService.get_instance()
    return instance.y