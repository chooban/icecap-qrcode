from mailmerge import MailMerge
from datetime import date


template = "Avery_L7651_WordTemplate.doc"

def create_sheet(barcodes):
    document = MailMerge(template)
    print(document.get_merge_fields())
