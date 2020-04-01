class TextMeta:
    infos = {}
    
    def readChunk(self, f, datalen):
        print("TEXT")
        metaType = ""

        character = f.read(1)
        extrabytes = 1

        while int.from_bytes(character, byteorder='big') != 0x00:
            metaType += chr(int.from_bytes(character, byteorder='big'))
            character = f.read(1)
            extrabytes += 1

        what = ""

        for _ in range (datalen - extrabytes + 4):
            what += chr(int.from_bytes(f.read(1), byteorder='big'))

        self.infos.update({metaType : what})



    def __str__(self):
        niceDisplayableInfo = ""
        for(key, value) in self.infos.items():
            niceDisplayableInfo += key + " :: " + value + "\n"

        return niceDisplayableInfo

    def clear(self):
        self.infos.clear()
        