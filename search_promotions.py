import pandas as pd
import xml.etree.ElementTree as et 
import os

def main_readxml_change_type(input):
    promotion = readxml_file(input)
    promotion['MMBR_PROM_ID'] = promotion['MMBR_PROM_ID'].astype('str')
    promotion['COUPON_ID'] = promotion['COUPON_ID'].astype('str')
    promotion['EntityId'] = promotion['EntityId'].astype('str')
    return promotion

    
def readxml_file(input):
    promotion = pd.DataFrame()
    name_file = ""

    lenght = 8 - len(input)
    for i in range(lenght):
        input = '0'+input
    file = os.listdir('./temp')
    for files in file:
        if input in files:
            name_file = files
    promotion = LPE_PromotionBucketEntity_csv(name_file)
    return promotion

def transform_xml_BucketEntity(xml_doc):
    attr = xml_doc.attrib
    for xml in xml_doc .iter('LPE_PromotionBucketEntity'):
        dict = attr.copy()
        dict.update(xml.attrib)
        
        yield dict

def transform_xml_PromotionHeader(xml_doc):
    attr = xml_doc.attrib
    for xml in xml_doc .iter('LPE_PromotionHeader'):
        dict = attr.copy()
        dict.update(xml.attrib)
        
        yield dict        

def LPE_PromotionBucketEntity_csv(xml_doc):
    etree = et.parse(f"./temp/{xml_doc}")
    myroot = etree.getroot()
    trans1 = list(transform_xml_PromotionHeader(myroot))
    trans2 = list(transform_xml_BucketEntity(myroot))
    tr_df = pd.DataFrame(trans1)
    tr_df2 = pd.DataFrame(trans2)
    df1 = tr_df[['MMBR_PROM_ID','COUPON_ID','STRT_DATE','END_DATE','PROM_DESC']]
    df2 = tr_df2[['MMBR_PROM_ID','EntityId']]
    data_promitions = pd.merge(df1,df2)
    data_promitions = data_promitions[['MMBR_PROM_ID','COUPON_ID','STRT_DATE','END_DATE','EntityId','PROM_DESC']]
    return data_promitions


def search_promotion_all(keyword,number,input):
    if input != '':
        data = main_readxml_change_type(input)
        promotion = []
        if (keyword == "COUPON_ID") & ((len(number) >= 3) & (len(number) <= 5)) :
            promotion = data.loc[data['COUPON_ID']==number]
            promotion = promotion.values.tolist()
        elif (keyword == "PROMOTION_ID") & ((len(number) >= 4) & (len(number) <=6) ) :
            promotion = data.loc[data['MMBR_PROM_ID']==number]
            promotion = promotion.values.tolist()
        elif (keyword == "PRODUCT_ID")& (len(number) == 7) :
            promotion = data.loc[data['EntityId']==number]
            promotion = promotion.values.tolist()
        return promotion
    else:
        return None








