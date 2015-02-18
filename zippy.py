__author__ = 'Nicolas'
import zipfile

def getInfoList(file):
    with zipfile.ZipFile(file) as myzip:
        return myzip.infolist()

def getAttribute(iterable, attribute):
    return [getattr(i, attribute) for i in iterable]

def uncompressed_size(infolist):
    return sum(getAttribute(infolist, 'file_size'))

def main():
    zipfile = 'compress.zip'
    infoList = getInfoList(zipfile)
    print getAttribute(infoList, 'filename')
    print getAttribute(infoList, 'date_time')
    #print getAttribute(infoList, 'compress_type')
    #print getAttribute(infoList, 'comment')
    #print getAttribute(infoList, 'extra')
    #print getAttribute(infoList, 'create_system')
    #print getAttribute(infoList, 'create_version')
    #print getAttribute(infoList, 'extract_version')
    #print getAttribute(infoList, 'CRC')
    print getAttribute(infoList, 'compress_size')
    print getAttribute(infoList, 'file_size')
    print uncompressed_size(infoList)


if __name__ == '__main__':
    main()