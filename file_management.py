import os

class FileManagement():

    # Class Variables
    file_names = []     # list with all file/subdirectory paths
    current_index = 0   # current image that is displayed
    list_length = 0

    def __init__(self):
        super().__init__()
        self.file_names = self.get_files("anime_stuff")
        self.list_length = len(self.file_names)

    # get_files() --> Given a directory name, create a list of file names (.png, .jpg) within file_names
    def get_files(self, directory_path: str):
        file_names = []     # reset the list

        # loop through a given directory + append file/subdirectory names to file_names
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)

            # Base Case --> If file found, add to file_names
            if os.path.isfile(full_path):
                file_names.append(full_path)
            # Recursive Case --> If directory found, check files within, then add to file_names
            elif os.path.isdir(full_path):
                file_names.extend(self.get_files(full_path))

        return file_names

    # return the name of the current image to display
    def get_current_image(self):
        return self.file_names[self.current_index]

    # Check the previous image by traversing backwards the file_name list
    def set_previous_image(self):
        if self.current_index == 0:
            pass
        else:
            self.current_index -= 1

    # Check the next image by traversing forward the file_name list
    def set_next_image(self):
        if self.current_index == self.list_length - 1:
            pass
        else:
            self.current_index += 1
