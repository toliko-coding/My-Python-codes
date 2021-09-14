# ------------------------------------------------

def fread_print(fname):
    try:
        out=open(fname,"r")
        text=tuple((out.read()).split(' '))
        out.close()      
        i=1
        for s in text:
            print(i,"-",s)
            i=i+1
    except:
        print('There is no file named', fname)
        
fread_print('1.txt')
