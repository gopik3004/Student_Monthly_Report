
class FILE_handling:

    def readFromFile(self,file_name):
        MFile=open(file_name,'r')
        return MFile.read().replace('\n','')
    def writeToFile(self,file_name,values):
        MFile= open(file_name,'w')
        MFile.write(values)

class Query_Extractor(FILE_handling):
    def list_Of_SQL_cmds(self,QueryFile):
        cmds=FILE_handling().readFromFile(QueryFile).split(';')
        cmds.pop()
        return cmds