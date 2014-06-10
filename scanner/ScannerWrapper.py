
import scanner_module

class ScannerWrapper:
    """This class wraps the c scanner"""
    text = None
    def __init__(self, instr):
        self.text = instr
        result = scanner_module.init_scanner("This is the input text")
        print result

    def get_token(self):
        result = scanner_module.get_token()
        return result
