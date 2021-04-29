import inspect
import os


class Logger:

    def __int__(self):
        pass

    def get_info_for_frame(self):
        """
        This function retrives the information from the frame and helps to get all.
        """
        current_frame = inspect.currentframe()
        frame_info = inspect.getframeinfo(current_frame)
        line_no = frame_info.lineno
        file_name_with_location = frame_info.filename
        file_name = os.path.basename(frame_info.filename)
        function_name = frame_info.function
        return [line_no, file_name_with_location, file_name, function_name]
