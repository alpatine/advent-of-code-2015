def readDataFile(fileName: str) -> str:
    with open(fileName) as dataFile:
        return dataFile.read()

def d01data() -> str: return readDataFile('d01_data.txt')
def d02data() -> str: return readDataFile('d02_data.txt')
def d03data() -> str: return readDataFile('d03_data.txt')
def d04data() -> str: return readDataFile('d04_data.txt')
def d05data() -> str: return readDataFile('d05_data.txt')
def d06data() -> str: return readDataFile('d06_data.txt')
def d07data() -> str: return readDataFile('d07_data.txt')
def d08data() -> str: return readDataFile('d08_data.txt')
