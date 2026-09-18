class error():
    def __init__(self, context:None, msg:None, proposition:None):
        self.context = context
        self.msg = msg
        self.proposition = proposition
        self.error_msg = self.get_error_message()
        self.push_error_to_user()

    def get_error_message(self) -> str:
        error_msg: str
        if self.context:
            error_msg = error_msg + "Context: " + self.context + ". "
        if self.msg:
            error_msg = error_msg + "Error: " + self.msg + ". "
        if self.proposition:
            error_msg = error_msg + "Try: " + self.proposition + ". "
        return error_msg

    def push_error_to_user(self) -> None:
        print(self.error_msg)