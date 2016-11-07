from protorpc import messages

class AboutMessage(messages.Message):
    """String that stores an about message."""
    about = messages.StringField(1)
