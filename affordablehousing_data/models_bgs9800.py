class bgs9800(models.Model):
   id = models.TextField(12,primary_key=True)
   meansp9800 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   meansp9800a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   minsp9800 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   minsp9800a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   maxsp9800 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   maxsp9800a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   mediansp9800 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   mediansp9800a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   stddevsp9800 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   stddevsp9800a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   totsp9800 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
   totsp9800a17 = models.DecimalField(max_digits=13,decimal_places=2,null=True)
   nums9800 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   mhi99 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   mhi99a17 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   pir9800 = models.DecimalField(max_digits=14,decimal_places=2,null=True)
   mgr_phi99 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   mmoc_phi99 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   pop00 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   ptwhnl00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ptblknl00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ptnanl00 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptasnl00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ptpanl00 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   ptothnl00 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   pt2mnl00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ptlat00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   mean_sfno2001 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   tot_sfno2001 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   num_sfno2001 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   mean_sfoo2001 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   tot_sfoo2001 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
   num_sfoo2001 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   prc_sfno2001 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
