def main():
    url = 'https://webmail.eprotea-finexus.com/upp/faces/ccpayment.xhtml?h001_MTI=0200&h002_VNO=03&h003_TDT=20170929&h004_TTM=15402900&f001_MID=BIG001&f003_ProcCode=003000&f004_PAN=4444333322221111&f005_ExpDate=2304&f006_TxnDtTm=20170929154029&f007_TxnAmt=000000057280&f008_POSCond=59&f010_CurrCode=458&f012_CVV2=&f014_3DXID=&f015_3DARC=&f016_3DCAVVLen=&f017_3DCAVV=&f019_ExpTxnAmt=2&f022_ECI=00&f247_OrgTxnAmt=&f248_OrgCurrCode=&f249_TxnCh=WEB&f260_ServID=BIG&f261_HostID=&f262_SessID=&f263_MRN=11223344556677&f264_Locale=en&f265_RURL_CCPS=https://webmail.eprotea-finexus.com/upp/faces/sim_ccresponse.jsp&f266_RURL_CCPU=https://webmail.eprotea-finexus.com/upp/faces/sim_ccresponse.jsp&f267_RURL_CCPC=https://webmail.eprotea-finexus.com/upp/faces/sim_ccresponse.jsp&f268_CHName=Ishak Ismail&f269_IssName=CITIBANK&f270_ORN=&f271_ODesc=&f278_EMailAddr=&f279_HP=&f285_IPAddr=&f287_ExpOrgTxnAmt=&f288_IssCntrCde=&t001_SHT=MD5&t002_SHV=FC8BAB4B09C393E874161FD530333360'
    list = url.split('&')

    for l in list:
        (key, value) = l.split('=')
        print(key + " => " + value)


if __name__ == '__main__':
    main()
