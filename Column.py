class Column():
    def check(memo):
        if memo.find('登入程序:') < 0:
            return False

        if memo.find('驗證封裝:') < 0:
            return False

        return True

    def createMemo(memo):
        memoArray = memo.replace("\r\n", "\r").replace("\t", "").split('\r')
        data = memoArray[12].split(':')[1] + ","
        data += memoArray[22].split(':')[1] + ","
        data += memoArray[23].split(':')[1] + ","
        data += memoArray[27].split(':')[1] + ","
        data += memoArray[28].split(':')[1] + ","
        return data