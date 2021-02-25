import re


# Creating Class
class Searching:
    # Function for searching the line and initializing the counter
    def function(self, word):

        self.word = word
        file = open("LGPL.txt", "rt")
        # file created with the name and include the number of occurrence
        outputfile = open(self.word + ".txt", "a")
        filetostring = file.read()
        # To remove the special character in the code
        for ch in ['\\n', '`', '*', '_', '{', '}', '[', ']',
                   '(', ')', '>', '#', '+', '-', '.',
                   '!', '$', '\'', '@', str([0 - 9]),
                   '(', ')', ',', '"', '\\xc0', '<', ";"]:
            if ch in filetostring:
                filetostring = filetostring.replace(ch, " ")

        # print(filetostring)
        filetostring = filetostring.upper()
        # print(filetostring)
        file_split = filetostring.split("\n")
        # print(file_split)
        self.word = self.word
        self.word = self.word.upper()
        # print(self.word)

        # To Find the length and fill the data inside the file

        occurence = re.findall(self.word, filetostring)  # regx
        length_occurence = str(len(occurence)) + "\n"
        outputfile.write(length_occurence)
        file_split_double = []
        # Searching of the specific key in the txt file
        for i in range(len(file_split)):
            file_split_double = file_split[i].split(" ")
            # print(file_split_double)
            for j in range(len(file_split_double)):
                if re.findall(self.word, file_split_double[j]):
                    if j == 0:
                        outputfile.write(file_split_double[j] +
                                         " " + file_split_double[j + 1] + "\n")
                    elif j == len(file_split_double) - 1:
                        outputfile.write(file_split_double[j - 1] +
                                         " " + file_split_double[j] + "\n")
                    else:
                        outputfile.write(file_split_double[j - 1] + " " +
                                         file_split_double[j] + " " +
                                         file_split_double[j + 1] + "\n")


if __name__ == '__main__':
    # Take the input data
    input_data = []
    # Pushing the data to the class
    obj1 = Searching()
    for i in range(5):
        input_data.append(input("Enter the words" + '\n'))
    for i in range(5):
        obj1.function(input_data[i])
