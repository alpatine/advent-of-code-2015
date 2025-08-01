def readDataFile(fileName: str) -> str:
    with open(fileName) as dataFile:
        return dataFile.read()

def d01data() -> str: return readDataFile('d01_data.txt')
def d02data() -> str: return readDataFile('d02_data.txt')
