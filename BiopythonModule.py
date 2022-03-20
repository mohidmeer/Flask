from Bio import SeqIO
import pandas
import csv
import os

def ProcessFasta(path):
    filename=os.path.basename(path)
    split=os.path.splitext(filename)
    CsvFileName=split[0]+".csv"
    CsvFilePath=os.path.join('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\csv',CsvFileName)
    seqObj=SeqIO.parse(path,'fasta')
    sequences=[]
    for seq in seqObj:
        sequences.append(seq)
    with open(CsvFilePath,  'w', newline="") as file:
        title=['Header','Sequences']
        Editor=csv.writer(file)
        # Editor.writerow(title)
        i=1
        for r in sequences:
            seqDesc=r.description
            sseq=r.seq
            SequenceData=[i,seqDesc,sseq]
            Editor.writerow(SequenceData)
            i=i+1
            
        file.close
        i=0;
    return CsvFilePath