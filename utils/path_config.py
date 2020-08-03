import os

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print(BASE_PATH)
FILE_PATH = os.path.join(BASE_PATH, 'dataconfig','NLE1.xlsx')
TEST_PATH = os.path.join(BASE_PATH, 'test','suite')