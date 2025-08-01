def readDataFile(fileName: str) -> str:
    with open(fileName) as dataFile:
        return dataFile.read()

def d01data() -> str:
    return readDataFile('d1_data.txt')
