class bgs00Serializer (serializers.ModelSerializer):
    class Meta:
        model = bgs00
        fields = ('id','meansp9800','meansp9800a17','minsp9800','minsp9800a17','maxsp9800','maxsp9800a17','mediansp9800','mediansp9800a17','totsp9800','totsp9800a17','nums9800','mhi99','mhi99a17','pir9800','mgr_phi99','mmoc_phi99','pop00','ptwhnl00','ptblknl00','ptnanl00','ptasnl00','ptpanl00','ptothnl00','pt2mnl00','ptlat00','mean_sfno2001','tot_sfno2001','num_sfno2001','mean_sfoo2001','tot_sfoo2001','num_sfoo2001','prc_sfno2001')
