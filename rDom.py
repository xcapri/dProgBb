import tldextract

def exDom(dom):
    ext = tldextract.extract(dom)
    open("out-root.txt", "a").write(ext.registered_domain+"\n")
    return ext.registered_domain


listdom = [i.strip() for i in open('list-subdo.txt').readlines()]

for dom in listdom:
    print(exDom(dom))
