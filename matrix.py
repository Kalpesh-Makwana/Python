class Matrix:
    def __init__(self, matrix_string):
        self.word=matrix_string.split("\n")

        for i in range(len(self.word)):
            self.word[i]=self.word[i].split()

        for i in range(len(self.word)):
            for j in range(len(self.word[i])):
                self.word[i][j]=int(self.word[i][j])

    def row(self, index):
        return self.word[index-1]

    def column(self, index):
        col=[]
        for i in range(len(self.word)):
            col.append(self.word[i][index-1])
        return col