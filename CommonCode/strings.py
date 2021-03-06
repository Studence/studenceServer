class Strings:

    @staticmethod
    def isEmpty(string):
        if string == '':
            return True
        elif string == None:
            return True
        else:
            return False

    @staticmethod
    def notEmpty(string):
        return not Strings.isEmpty(string)

    @staticmethod
    def length(string):
        return len(string)

    @staticmethod
    def qoutedString(string):
        return "'" + string + "'"

    @staticmethod
    def getFormattedEmail(builder):
        return builder.localPart + '@' + builder.domain

    @staticmethod
    def getConcatinateStringWithAtTheRate(str1, str2):
        return str1 + '@' + str2

    @staticmethod
    def getFormattedName(builder):
        return builder.firstName.title() + ' ' + builder.lastName.title()

    @staticmethod
    def areEquals(str1, str2):
        return str1 == str2

    @staticmethod
    def toLower(str1):
        return str(str1).lower()

    @staticmethod
    def concatinateWithUnderScore(str1, str2):
        return str1 + "_" + str2

    @staticmethod
    def concatinate(str1, str2):
        return str1 + str2

    @staticmethod
    def copy(message1, message2):
        return message1.CopyFrom(message2)

    @staticmethod
    def getTittleCaseStringMaker(data):
        Char1 = '^'
        Char2 = '^^'
        resultString = ''
        counter = 1
        for x in data.split(' '):
            if (counter == 1):
                resultString = resultString + Char2 + x.lower()
            else:
                resultString = resultString + Char1 + x.lower()
            counter = counter + 1
        return resultString

    @staticmethod
    def splitString(char, string):
        return string.split(char)
