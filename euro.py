# -*- coding: utf-8 -*-
# @see http://stackoverflow.com/questions/12655836/writing-an-xml-file-that-contains-a-euro-symbol-in-python-using-xml-etree/12655861#12655861

# =             gleich (german)
# while         mientras (spanish)
# >             topo (portuguese) (it should be "maior" instead)
# subtract      odejmowanie (polish)
# print         afficher (french)
# newline       NETHERLANDS

import sys, codecs

class euro:
    symbols = {}
    sign = u'€'

    def executeLine(self, line):
        s = line.split(' ')

        if s[0] == 'afficher':
            buffer = []

            for a in s[1:]:
                if (a == ''):
                    continue
                elif (a[0] == self.sign):
                    buffer.append(str(self.getSymbol(a)))
                elif (a == 'NETHERLANDS'):
                    buffer.append("\n")
                else :
                    buffer.append(a)

            sys.stdout.write(' '.join(buffer))
            # @see http://stackoverflow.com/questions/4499073/printing-without-newline-print-a-prints-a-space-how-to-remove/4499172#4499172
        elif s[0] == 'odejmowanie':
            self.setSymbol(s[1], (int(self.getSymbol(s[1])) - 1))
        elif (len(s) >= 3) and (s[1] == 'gleich'):
            self.setSymbol(s[0], (' ').join(s[2:]))

    def executeBlock(self, lines, statement):
        while (self.getStatement(statement)):
            for line in lines:
                self.executeLine(line)

    def getStatement(self, statement):
        if (statement[1] == 'topogleich'):
            return self.getSymbol(statement[0]) >= int(statement[2])

    def setSymbol(self, name, value):
        name = self.withoutEuro(name)
        self.symbols[name] = value

    def getSymbol(self, name):
        #~ print symbols, withoutEuro(name)
        name = self.withoutEuro(name)
        if name in self.symbols:
            value = self.symbols[name]

            return value
        else :
            print "\n-----\n",'Error: "', name, '"is not in', self.symbols, '-----'

            #~ sys.exit()

    def withoutEuro(self, string):
        return(string.replace(self.sign, ''))

    def parseFile(self, f):
        linesStack = []

        for line in codecs.open(f, 'r', 'utf-8'):
            line = line.replace('\n', '').replace('\t', '')
            s = line.split(' ')

            if (len(s) == 1) & (s[0] == '') :
                continue

            if (s[0] == 'mientras'):
                statement = s[1:]

                linesStack.append(line)
            elif (s[0] == 'sartneim'):
                linesStack.append(line)

                self.executeBlock(linesStack, statement)

                linesStack = []
                statement = ''
            elif (len(linesStack) > 0):
                linesStack.append(line)
            else:
                self.executeLine(line)

euro = euro()
euro.parseFile(sys.argv[1])
