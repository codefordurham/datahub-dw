class bgs1317(models.Model):
   id = models.TextField(12,primary_key=True)
   meansp1314 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   meansp1314a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   minsp1314 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   minsp1314a17 = models.DecimalField(max_digits=13,decimal_places=2,null=True)
   maxsp1314 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   maxsp1314a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   mediansp1314 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   mediansp1314a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   totsp1314 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
   totsp1314a17 = models.DecimalField(max_digits=13,decimal_places=2,null=True)
   nums1314 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   mhi1314 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   mhi1314a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   pir1314 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   mean_sfno100517 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   tot_sfno100517 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   num_sfno100517 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   mean_sfoo100517 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   tot_sfoo100517 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
   num_sfoo100517 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   prc_sfno100517 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pop13 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pop14 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   ptwhnl13 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptwhnl14 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptblknl13 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptblknl14 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptasnl13 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptasnl14 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptothnl13 = models.DecimalField(max_digits=4,decimal_places=2,null=False)
   ptothnl14 = models.DecimalField(max_digits=4,decimal_places=2,null=False)
   ptlat13 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptlat14 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   meansp1517 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   meansp1517a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   minsp1517 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   minsp1517a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   maxsp1517 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   maxsp1517a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   mediansp1517 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   mediansp1517a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   totsp1517 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
   totsp1517a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   nums1517 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   mhi16 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   mhi16a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   pir1517 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   mgr_phi16 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   mmoc_phi16 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   mean_sfno011818 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   tot_sfno011818 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   num_sfno011818 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   mean_sfoo011818 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   tot_sfoo011818 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
   num_sfoo011818 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   prc_sfno011818 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pop16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   ptwhnl16 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptblknl16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ptnanl16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ptasnl16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ptpanl16 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptothnl16 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   pt2mnl16 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptlat16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)