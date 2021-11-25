
class DateClient :
    def main(self, args) :
        try :
            #  this could be changed to an IP name or address other than the localhost
            sock =  java.net.Socket("127.0.0.1", 6013)
            in = sock.getInputStream()
            bin =  java.io.BufferedReader( java.io.InputStreamReader(in))
            while ((line = bin.readLine()) != None) :
                print(line)
                sock.close()
        except java.lang.Exception as ioe :
            print(ioe)


if __name__=="__main__":
    DateClient().main([])