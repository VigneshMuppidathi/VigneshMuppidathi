class Document:
    def __init__(self,docId,docName,docDetails):
        self.docId=docId
        self.docName=docName
        self.docDetails=docDetails
class DocumentArchive:
    def __init__(self,archiveId,documentList):
        self.archiveId=archiveId
        self.documentList=documentList
    def findDatefromDocumentDetails(self):
        doclist=[]
        for doc in self.documentList:
            val=doc.docDetails.split(',')
            if doc.docDetails.count('/')==2:
                for x in val:
                    if '/' in x:
                        doclist.append((doc.docId,x))
        return doclist
    def countDocumentofGivenType(self,docname):
        c=0
        for doc in self.documentList:
            Type=doc.docName.split('.')[1]
            if Type==docname:
                c+=1
        return c
n=int(input())
documents=[]
for i in range(n):
    docId=int(input())
    docName=input()
    docDetails=input()
    d=Document(docId,docName,docDetails)
    documents.append(d)
archive=DocumentArchive(10,documents)
for i in archive.findDatefromDocumentDetails():
    print(i[0],i[1])
docname=input()
print("Document Count =",archive.countDocumentofGivenType(docname))
