function setOptions () {
  var options
  if (this.selectgroup.value === 'democount') {
    options = [{label: 'Total Population in 1970', value: 'pop70'},
      {label: 'Total White Population in 1970', value: 'nhwht70'},
      {label: 'Total Black Population in 1970', value: 'nhblk70'},
      {label: 'Total Asian Population in 1970', value: 'asian70'},
      {label: 'Total Hawaiian Population in 1970', value: 'haw70'},
      {label: 'Age 25 and Older in 1970', value: 'ag25up70'},
      {label: 'Total Population in 1980', value: 'pop80'},
      {label: 'Total White Population in 1980', value: 'nhwht80'},
      {label: 'Total Black Population in 1980', value: 'nhblk80'},
      {label: 'Total Native Population in 1980', value: 'ntv80'},
      {label: 'Total Asian Population in 1980', value: 'asian80'},
      {label: 'Total Hispanic Population in 1980', value: 'hisp80'},
      {label: 'Total Hawaiian Population in 1980', value: 'haw80'},
      {label: 'Age 25 and Older in 1980', value: 'ag25up80'},
      {label: 'Total Population in 1990', value: 'pop90'},
      {label: 'Total White Population in 1990', value: 'nhwht90'},
      {label: 'Total Black Population in 1990', value: 'nhblk90'},
      {label: 'Total Native Population in 1990', value: 'ntv90'},
      {label: 'Total Asian Population in 1990', value: 'asian90'},
      {label: 'Total Hispanic Population in 1990', value: 'hisp90'},
      {label: 'Total Hawaiian Population in 1990', value: 'haw90'},
      {label: 'Age 25 and Older in 1990', value: 'ag25up90'},
      {label: 'Total Population in 2000', value: 'pop00'},
      {label: 'Total White Population in 2000', value: 'nhwht00'},
      {label: 'Total Black Population in 2000', value: 'nhblk00'},
      {label: 'Total Native Population in 2000', value: 'ntv00'},
      {label: 'Total Asian Population in 2000', value: 'asian00'},
      {label: 'Total Hispanic Population in 2000', value: 'hisp00'},
      {label: 'Total Hawaiian Population in 2000', value: 'haw00'},
      {label: 'Age 25 and Older in 2000', value: 'ag25up00'},
      {label: 'Total Population in 2010', value: 'pop10'},
      {label: 'Total White Population in 2010', value: 'nhwht10'},
      {label: 'Total Black Population in 2010', value: 'nhblk10'},
      {label: 'Total Native Population in 2010', value: 'ntv10'},
      {label: 'Total Asian Population in 2010', value: 'asian10'},
      {label: 'Total Hispanic Population in 2010', value: 'hisp10'},
      {label: 'Total Hawaiian Population in 2010', value: 'haw10'},
      {label: 'Age 25 and Older in 2012', value: 'ag25up12'},
      {label: 'Total Population in 2016', value: 'pop16'},
      {label: 'Total White Population in 2016', value: 'nhwht16'},
      {label: 'Total Black Population in 2016', value: 'nhblk16'},
      {label: 'Total Native Population in 2016', value: 'ntv16'},
      {label: 'Total Asian Population in 2016', value: 'asian16'},
      {label: 'Total Hawaiian Population in 2016', value: 'haw16'},
      {label: 'Total Other Population in 2016', value: 'oth16'},
      {label: 'Total Two or More Races Population in 2016', value: 'twomr16'},
      {label: 'Total Hispanic Population in 2016', value: 'hisp16'},
      {label: 'Change in Population between 2000 and 2016', value: 'cpop0016'},
      {label: 'Change in Population between 2010 and 2016', value: 'cpop1016'},
      {label: 'Age 25 and Older in 2016', value: 'ag25up16'}]
  }
  else if (this.selectgroup.value === 'demopercent') {
    options = [{label: 'Percent White Population in 1970', value: 'pnhwht70'},
      {label: 'Percent Black Population in 1970', value: 'pnhblk70'},
      {label: 'Percent Asian Population in 1970', value: 'pasian70'},
      {label: 'Percent Hawaiian Population in 1970', value: 'phaw70'},
      {label: 'Percent White Population in 1980', value: 'pnhwht80'},
      {label: 'Percent Black Population in 1980', value: 'pnhblk80'},
      {label: 'Percent Native Population in 1980', value: 'pntv80'},
      {label: 'Percent Asian Population in 1980', value: 'pasian80'},
      {label: 'Percent Hispanic Population in 1980', value: 'phisp80'},
      {label: 'Percent Hawaiian Population in 1980', value: 'phaw80'},
      {label: 'Percent White Population in 1990', value: 'pnhwht90'},
      {label: 'Percent Black Population in 1990', value: 'pnhblk90'},
      {label: 'Percent Native Population in 1990', value: 'pntv90'},
      {label: 'Percent Asian Population in 1990', value: 'pasian90'},
      {label: 'Percent Hispanic Population in 1990', value: 'phisp90'},
      {label: 'Percent Hawaiian Population in 1990', value: 'phaw90'},
      {label: 'Percent White Population in 2000', value: 'pnhwht00'},
      {label: 'Percent Black Population in 2000', value: 'pnhblk00'},
      {label: 'Percent Native Population in 2000', value: 'pntv00'},
      {label: 'Percent Asian Population in 2000', value: 'pasian00'},
      {label: 'Percent Hispanic Population in 2000', value: 'phisp00'},
      {label: 'Percent Hawaiian Population in 2000', value: 'phaw00'},
      {label: 'Percent White Population in 2010', value: 'pnhwht10'},
      {label: 'Percent Black Population in 2010', value: 'pnhblk10'},
      {label: 'Percent Native Population in 2010', value: 'pntv10'},
      {label: 'Percent Asian Population in 2010', value: 'pasian10'},
      {label: 'Percent Hispanic Population in 2010', value: 'phisp10'},
      {label: 'Percent Hawaiian Population in 2010', value: 'phaw10'},
      {label: 'Percent White Population in 2016', value: 'pnhwht16'},
      {label: 'Percent Black Population in 2016', value: 'pnhblk16'},
      {label: 'Percent Native Population in 2016', value: 'pntv16'},
      {label: 'Percent Asian Population in 2016', value: 'pasian16'},
      {label: 'Percent Hawaiian Population in 2016', value: 'phaw16'},
      {label: 'Percent Other Population in 2016', value: 'poth16'},
      {label: 'Percent Two or More Races Population in 2016', value: 'ptwomr16'},
      {label: 'Percent Hispanic Population in 2016', value: 'phisp16'}]
  }
  else if (this.selectgroup.value === 'pcdemo') {
    options = [{label: 'Percent Change in White Population between 2000 and 2010', value: 'pcnhwht0010'},
      {label: 'Percent Change in Black Population between 2000 and 2010', value: 'pcnhblk0010'},
      {label: 'Percent Change in Asian Population between 2000 and 2010', value: 'pcasian0010'},
      {label: 'Percent Change in Hispanic Population between 2000 and 2010', value: 'pchisp0010'},
      {label: 'Percent Change in Population between 2000 and 2016', value: 'pcpop0016'},
      {label: 'Percent Change in White Population between 2000 and 2016', value: 'pcnhwht0016'},
      {label: 'Percent Change in Black Population between 2000 and 2016', value: 'pcnhblk0016'},
      {label: 'Percent Change in Asian Population between 2000 and 2016', value: 'pcasian0016'},
      {label: 'Percent Change in Hispanic Population between 2000 and 2016', value: 'pchisp0016'},
      {label: 'Percent Change in Population between 2010 and 2016', value: 'pcpop1016'},
      {label: 'Percent Change in White Population between 2010 and 2016', value: 'pcnhwht1016'},
      {label: 'Percent Change in Black Population between 2010 and 2016', value: 'pcnhblk1016'},
      {label: 'Percent Change in Asian Population between 2010 and 2016', value: 'pcasian1016'},
      {label: 'Percent Change in Hispanic Population between 2010 and 2016', value: 'pchisp1016'}]
  }
  else if (this.selectgroup.value === 'realcount') {
    options = [{label: 'Total Housing Units in 1970', value: 'hu70'},
      {label: 'Total Vacant Housing in 1970', value: 'vac70'},
      {label: 'Total Occupied Housing in 1970', value: 'ohu70'},
      {label: 'Total Owner Occupied Housing in 1970', value: 'own70'},
      {label: 'Total Rental Housing in 1970', value: 'rent70'},
      {label: 'Total Housing Units in 1980', value: 'hu80'},
      {label: 'Total Vacant Housing in 1980', value: 'vac80'},
      {label: 'Total Occupied Housing in 1980', value: 'ohu80'},
      {label: 'Total Owner Occupied Housing in 1980', value: 'own80'},
      {label: 'Total Rental Housing in 1980', value: 'rent80'},
      {label: 'Total Housing Units in 1990', value: 'hu90'},
      {label: 'Total Vacant Housing in 1990', value: 'vac90'},
      {label: 'Total Occupied Housing in 1990', value: 'ohu90'},
      {label: 'Total Owner Occupied Housing in 1990', value: 'own90'},
      {label: 'Total Rental Housing in 1990', value: 'rent90'},
      {label: 'Total Housing Units in 2000', value: 'hu00'},
      {label: 'Total Vacant Housing in 2000', value: 'vac00'},
      {label: 'Total Occupied Housing in 2000', value: 'ohu00'},
      {label: 'Total Owner Occupied Housing in 2000', value: 'own00'},
      {label: 'Total Rental Housing in 2000', value: 'rent00'},
      {label: 'Total Housing Units in 2010', value: 'hu10'},
      {label: 'Total Vacant Housing in 2010', value: 'vac10'},
      {label: 'Total Occupied Housing in 2010', value: 'ohu10'},
      {label: 'Total Owner Occupied Housing in 2010', value: 'own10'},
      {label: 'Total Rental Housing in 2010', value: 'rent10'},
      {label: 'Total Housing Units in 2016', value: 'hu16'},
      {label: 'Total Occupied Housing in 2016', value: 'ohu16'},
      {label: 'Total Vacant Housing in 2016', value: 'vac16'},
      {label: 'Total Owner Occupied Housing in 2016', value: 'own16'},
      {label: 'Total Rental Housing in 2016', value: 'rent16'}]
  }
  else if (this.selectgroup.value === 'realpercent') {
    options = [{label: 'Percent Vacant Housing in 1970', value: 'pvac70'},
      {label: 'Percent Occupied Housing in 1970', value: 'pohu70'},
      {label: 'Percent Owner Occupied Housing in 1970', value: 'pown70'},
      {label: 'Percent Rental Housing in 1970', value: 'prent70'},
      {label: 'Percent Vacant Housing in 1980', value: 'pvac80'},
      {label: 'Percent Occupied Housing in 1980', value: 'pohu80'},
      {label: 'Percent Owner Occupied Housing in 1980', value: 'pown80'},
      {label: 'Percent Rental Housing in 1980', value: 'prent80'},
      {label: 'Percent Vacant Housing in 1990', value: 'pvac90'},
      {label: 'Percent Occupied Housing in 1990', value: 'pohu90'},
      {label: 'Percent Owner Occupied Housing in 1990', value: 'pown90'},
      {label: 'Percent Rental Housing in 1990', value: 'prent90'},
      {label: 'Percent Vacant Housing in 2000', value: 'pvac00'},
      {label: 'Percent Occupied Housing in 2000', value: 'pohu00'},
      {label: 'Percent Owner Occupied Housing in 2000', value: 'pown00'},
      {label: 'Percent Rental Housing in 2000', value: 'prent00'},
      {label: 'Percent Vacant Housing in 2010', value: 'pvac10'},
      {label: 'Percent Occupied Housing in 2010', value: 'pohu10'},
      {label: 'Percent Owner Occupied Housing in 2010', value: 'pown10'},
      {label: 'Percent Rental Housing in 2010', value: 'prent10'},
      {label: 'Percent Occupied Housing in 2016', value: 'pohu16'},
      {label: 'Percent Vacant Housing in 2016', value: 'pvac16'},
      {label: 'Percent Owner Occupied Housing in 2016', value: 'pown16'},
      {label: 'Percent Rental Housing in 2016', value: 'prent16'}]
  }
  else if (this.selectgroup.value === 'realvalue') {
    options = [{label: 'Median Home Value in 1970, Adjusted to 2017 Dollars', value: 'mhmval70a17'},
      {label: 'Median Home Value in 1970', value: 'mhmval70'},
      {label: 'Median Rent in 1970', value: 'mrent70'},
      {label: 'Median Rent in 1970, Adjusted to 2017 Dollars', value: 'mrent70a17'},
      {label: 'Median Home Value in 1980', value: 'mhmval80'},
      {label: 'Median Home Value in 1980, Adjusted to 2017 Dollars', value: 'mhmval80a17'},
      {label: 'Median Rent in 1980', value: 'mrent80'},
      {label: 'Median Rent in 1980, Adjusted to 2017 Dollars', value: 'mrent80a17'},
      {label: 'Median Home Value in 1990', value: 'mhmval90'},
      {label: 'Median Home Value in 1990, Adjusted to 2017 Dollars', value: 'mhmval90a17'},
      {label: 'Median Rent in 1990', value: 'mrent90'},
      {label: 'Median Rent in 1990, Adjusted to 2017 Dollars', value: 'mrent90a17'},
      {label: 'Median Home Value in 2000', value: 'mhmval00'},
      {label: 'Median Home Value in 2000, Adjusted to 2017 Dollars', value: 'mhmval00a17'},
      {label: 'Median Rent in 2000', value: 'mrent00'},
      {label: 'Median Rent in 2000, Adjusted to 2017 Dollars', value: 'mrent00a17'},
      {label: 'Median Home Value in 2012', value: 'mhmval12'},
      {label: 'Median Home Value in 2012, Adjusted to 2017 Dollars', value: 'mhmval12a17'},
      {label: 'Median Rent in 2012', value: 'mrent12'},
      {label: 'Median Rent in 2012, Adjusted to 2017 Dollars', value: 'mrent12a17'},
      {label: 'Median Home Value in 2016', value: 'mhmval16'},
      {label: 'Median Rent in 2016', value: 'mrent16'},
      {label: 'Median Home Value in 2016, Adjusted to 2017 Dollars', value: 'mhmval16a17'},
      {label: 'Median Rent in 2016, Adjusted to 2017 Dollars', value: 'mrent16a17'}]
  }
  else if (this.selectgroup.value === 'crealvalue') {
    options = [{label: 'Change in Median Home Value between 2000 and 2012, Adjusted to 2017 Dollars', value: 'cmhmval0012a17'},
      {label: 'Change in Median Rent between 2000 and 2012, Adjusted to 2017 Dollars', value: 'cmrent0012a17'},
      {label: 'Change in Median Home Value between 2000 and 2016, Adjusted to 2017 Dollars', value: 'cmhmval0016a17'},
      {label: 'Change in Median Rent between 2000 and 2016, Adjusted to 2017 Dollars', value: 'cmrent0016a17'},
      {label: 'Change in Median Home Value between 2012 and 2016, Adjusted to 2017 Dollars', value: 'cmhmval1216a17'},
      {label: 'Change in Median Rent between 2012 and 2016, Adjusted to 2017 Dollars', value: 'cmrent1216a17'}]
  }
  else if (this.selectgroup.value === 'pcrealvalue') {
    options = [{label: 'Percent Change in Median Home Value between 2000 and 2012, Adjusted to 2017 Dollars', value: 'pcmhmval0012a17'},
      {label: 'Percent Change in Median Rent between 2000 and 2012, Adjusted to 2017 Dollars', value: 'pcmrent0012a17'},
      {label: 'Percent Change in Median Home Value between 2000 and 2016, Adjusted to 2017 Dollars', value: 'pcmhmval0016a17'},
      {label: 'Percent Change in Median Rent between 2000 and 2016, Adjusted to 2017 Dollars', value: 'pcmrent0016a17'},
      {label: 'Percent Change in Median Home Value between 2012 and 2016, Adjusted to 2017 Dollars', value: 'pcmhmval1216a17'},
      {label: 'Percent Change in Median Rent between 2012 and 2016, Adjusted to 2017 Dollars', value: 'pcmrent1216a17'}]
  }
  else if (this.selectgroup.value === 'realsale') {
    options = [{label: 'Mean Sale Price of Single Family Homes between 1998 and 2000', value: 'meansp9800'},
      {label: 'Minimum Sale Price of Single Family Homes between 1998 and 2000', value: 'minsp9800'},
      {label: 'Maximum Sale Price of Single Family Homes between 1998 and 2000', value: 'maxsp9800'},
      {label: 'Median Sale Price of Single Family Homes between 1998 and 2000', value: 'mediansp9800'},
      {label: 'Standard Deviation of Sale Price for Single Family Homes between 1998 and 2000', value: 'stddevsp9800'},
      {label: 'Total Sale Price of Single Family Homes between 1998 and 2000', value: 'totsp9800'},
      {label: 'Number of Homes Sold between 1998 and 2000', value: 'nums9800'},
      {label: 'Mean Sale Price of Single Family Homes between 1998 and 2000, Adjusted to 2017 Dollars', value: 'meansp9800a17'},
      {label: 'Minimum Sale Price of Single Family Homes between 1998 and 2000, Adjusted to 2017 Dollars', value: 'minsp9800a17'},
      {label: 'Maximum Sale Price of Single Family Homes between 1998 and 2000, Adjusted to 2017 Dollars', value: 'maxsp9800a17'},
      {label: 'Median Sale Price of Single Family Homes between 1998 and 2000, Adjusted to 2017 Dollars', value: 'mediansp9800a17'},
      {label: 'Total Sale Price of Single Family Homes between 1998 and 2000, Adjusted to 2017 Dollars', value: 'totsp9800a17'},
      {label: 'Mean Sale Price of Single Family Homes between 2008 and 2009', value: 'meansp0809'},
      {label: 'Minimum Sale Price of Single Family Homes between 2008 and 2009', value: 'minsp0809'},
      {label: 'Maximum Sale Price of Single Family Homes between 2008 and 2009', value: 'maxsp0809'},
      {label: 'Median Sale Price of Single Family Homes between 2008 and 2009', value: 'mediansp0809'},
      {label: 'Standard Deviation of Sale Price for Single Family Homes between 2008 and 2009', value: 'stddevsp0809'},
      {label: 'Total Sale Price of Single Family Homes between 2008 and 2009', value: 'totsp0809'},
      {label: 'Number of Homes Sold between 2008 and 2009', value: 'nums0809'},
      {label: 'Mean Sale Price of Single Family Homes between 2008 and 2009, Adjusted to 2017 Dollars', value: 'meansp0809a17'},
      {label: 'Minimum Sale Price of Single Family Homes between 2008 and 2009, Adjusted to 2017 Dollars', value: 'minsp0809a17'},
      {label: 'Maximum Sale Price of Single Family Homes between 2008 and 2009, Adjusted to 2017 Dollars', value: 'maxsp0809a17'},
      {label: 'Median Sale Price of Single Family Homes between 2008 and 2009, Adjusted to 2017 Dollars', value: 'mediansp0809a17'},
      {label: 'Total Sale Price of Single Family Homes between 2008 and 2009, Adjusted to 2017 Dollars', value: 'totsp0809a17'},
      {label: 'Mean Sale Price of Single Family Homes between 2015 and 2017', value: 'meansp1517'},
      {label: 'Minimum Sale Price of Single Family Homes between 2015 and 2017', value: 'minsp1517'},
      {label: 'Maximum Sale Price of Single Family Homes between 2015 and 2017', value: 'maxsp1517'},
      {label: 'Median Sale Price of Single Family Homes between 2015 and 2017', value: 'mediansp1517'},
      {label: 'Standard Deviation of Sale Price for Single Family Homes between 2015 and 2017', value: 'stddevsp1517'},
      {label: 'Total Sale Price of Single Family Homes between 2015 and 2017', value: 'totsp1517'},
      {label: 'Number of Homes Sold between 2015 and 2017', value: 'nums1517'},
      {label: 'Mean Sale Price of Single Family Homes between 2015 and 2017, Adjusted to 2017 Dollars', value: 'meansp1517a17'},
      {label: 'Minimum Sale Price of Single Family Homes between 2015 and 2017, Adjusted to 2017 Dollars', value: 'minsp1517a17'},
      {label: 'Maximum Sale Price of Single Family Homes between 2015 and 2017, Adjusted to 2017 Dollars', value: 'maxsp1517a17'},
      {label: 'Median Sale Price of Single Family Homes between 2015 and 2017, Adjusted to 2017 Dollars', value: 'mediansp1517a17'},
      {label: 'Total Sale Price of Single Family Homes between 2015 and 2017, Adjusted to 2017 Dollars', value: 'totsp1517a17'}]
  }
  else if (this.selectgroup.value === 'realcost') {
    options = [{label: 'Gross Rent as Percent of Household Income in 2012', value: 'grprchi12'},
      {label: 'Gross Rent as Percent of Household Income in 2016', value: 'grprchi16'},
      {label: 'Percent Change Gross Rent as Percent of Household Income between 2012 and 2016', value: 'pcgrprchi1216'},
      {label: 'Morgage Monthly Owners Cost as a Percent of Household Income in 2012', value: 'mmocphi12'},
      {label: 'Morgage Monthly Owners Cost as a Percent of Household Income with Morgage in 2012', value: 'mmocphiym12'},
      {label: 'Morgage Monthly Owners Cost as a Percent of Household Income without Morgage in 2012', value: 'mmocphinm12'},
      {label: 'Morgage Monthly Owners Cost as a Percent of Household Income in 2016', value: 'mmocphi16'},
      {label: 'Morgage Monthly Owners Cost as a Percent of Household Income with Morgage in 2016', value: 'mmocphiym16'},
      {label: 'Morgage Monthly Owners Cost as a Percent of Household Income without Morgage in 2016', value: 'mmocphinm16'},
      {label: 'Percent Change in Morgage Monthly Owners Cost as a Percent of Household Income with Morgage between 2012 and 2016', value: 'pcmmocphiym1216'}]
  }
  else if (this.selectgroup.value === 'crealsale') {
    options = [{label: 'Change in Mean Sale Price for Single Family Homes between 2000 and 2009, Adjusted to 2017 Dollars', value: 'cmeansp0009a17'},
      {label: 'Change in Median Sale Price for Single Family Homes between 2000 and 2009, Adjusted to 2017 Dollars', value: 'cmediansp0009a17'},
      {label: 'Change in Mean Sale Price for Single Family Homes between 2009 and 2017, Adjusted to 2017 Dollars', value: 'cmeansp0917a17'},
      {label: 'Change in Median Sale Price for Single Family Homes between 2009 and 2017, Adjusted to 2017 Dollars', value: 'cmediansp0917a17'},
      {label: 'Change in Mean Sale Price for Single Family Homes between 2000 and 2017, Adjusted to 2017 Dollars', value: 'cmeansp0017a17'},
      {label: 'Change in Median Sale Price for Single Family Homes between 2000 and 2017, Adjusted to 2017 Dollars', value: 'cmediansp0017a17'}]
  }
  else if (this.selectgroup.value === 'pcrealsale') {
    options = [{label: 'Percent Change in Mean Sale Price for Single Family Homes between 2000 and 2009, Adjusted to 2017 Dollars', value: 'pcmeansp0009a17'},
      {label: 'Percent Change in Median Sale Price for Single Family Homes between 2000 and 2009, Adjusted to 2017 Dollars', value: 'pcmediansp0009a17'},
      {label: 'Percent Change in Mean Sale Price for Single Family Homes between 2009 and 2017, Adjusted to 2017 Dollars', value: 'pcmeansp0917a17'},
      {label: 'Percent Change in Median Sale Price for Single Family Homes between 2009 and 2017, Adjusted to 2017 Dollars', value: 'pcmediansp0917a17'},
      {label: 'Percent Change in Mean Sale Price for Single Family Homes between 2000 and 2017, Adjusted to 2017 Dollars', value: 'pcmeansp0017a17'},
      {label: 'Percent Change in Median Sale Price for Single Family Homes between 2000 and 2017, Adjusted to 2017 Dollars', value: 'pcmediansp0017a17'}]
  }
  else if (this.selectgroup.value === 'income') {
    options = [{label: 'Median Household Income in 1970', value: 'hinc70'},
      {label: 'Median Household Income in 1970, Adjusted to 2017 Dollars', value: 'hinc70a17'},
      {label: 'Median Household Income in 1980', value: 'hinc80'},
      {label: 'Median Household Income in 1980, Adjusted to 2017 Dollars', value: 'hinc80a17'},
      {label: 'Median Household Income for Whites in 1980', value: 'hincw80'},
      {label: 'Median Household Income for Whites in 1980, Adjusted to 2017 Dollars', value: 'hincw80a17'},
      {label: 'Median Household Income for Blacks in 1980', value: 'hincb80'},
      {label: 'Median Household Income for Blacks in 1980, Adjusted to 2017 Dollars', value: 'hincb80a17'},
      {label: 'Median Household Income for Hispanics in 1980', value: 'hinch80'},
      {label: 'Median Household Income for Hispanics in 1980, Adjusted to 2017 Dollars', value: 'hinch80a17'},
      {label: 'Median Household Income for Asians in 1980', value: 'hinca80'},
      {label: 'Median Household Income for Asians in 1980, Adjusted to 2017 Dollars', value: 'hinca80a17'},
      {label: 'Median Household Income in 1990', value: 'hinc90'},
      {label: 'Median Household Income in 1990, Adjusted to 2017 Dollars', value: 'hinc90a17'},
      {label: 'Median Household Income for Whites in 1990', value: 'hincw90'},
      {label: 'Median Household Income for Whites in 1990, Adjusted to 2017 Dollars', value: 'hincw90a17'},
      {label: 'Median Household Income for Blacks in 1990', value: 'hincb90'},
      {label: 'Median Household Income for Blacks in 1990, Adjusted to 2017 Dollars', value: 'hincb90a17'},
      {label: 'Median Household Income for Hispanics in 1990', value: 'hinch90'},
      {label: 'Median Household Income for Hispanics in 1990, Adjusted to 2017 Dollars', value: 'hinch90a17'},
      {label: 'Median Household Income for Asians in 1990', value: 'hinca90'},
      {label: 'Median Household Income for Asians in 1990, Adjusted to 2017 Dollars', value: 'hinca90a17'},
      {label: 'Median Household Income in 2000', value: 'hinc00'},
      {label: 'Median Household Income in 2000, Adjusted to 2017 Dollars', value: 'hinc00a17'},
      {label: 'Median Household Income for Whites in 2000', value: 'hincw00'},
      {label: 'Median Household Income for Whites in 2000, Adjusted to 2017 Dollars', value: 'hincw00a17'},
      {label: 'Median Household Income for Blacks in 2000', value: 'hincb00'},
      {label: 'Median Household Income for Blacks in 2000, Adjusted to 2017 Dollars', value: 'hincb00a17'},
      {label: 'Median Household Income for Hispanics in 2000', value: 'hinch00'},
      {label: 'Median Household Income for Hispanics in 2000, Adjusted to 2017 Dollars', value: 'hinch00a17'},
      {label: 'Median Household Income for Asians in 2000', value: 'hinca00'},
      {label: 'Median Household Income for Asians in 2000, Adjusted to 2017 Dollars', value: 'hinca00a17'},
      {label: 'Median Household Income in 2012', value: 'hinc12'},
      {label: 'Median Household Income in 2012, Adjusted to 2017 Dollars', value: 'hinc12a17'},
      {label: 'Median Household Income for Whites in 2012', value: 'hincw12'},
      {label: 'Median Household Income for Whites in 2012, Adjusted to 2017 Dollars', value: 'hincw12a17'},
      {label: 'Median Household Income for Blacks in 2012', value: 'hincb12'},
      {label: 'Median Household Income for Blacks in 2012, Adjusted to 2017 Dollars', value: 'hincb12a17'},
      {label: 'Median Household Income for Hispanics in 2012', value: 'hinch12'},
      {label: 'Median Household Income for Hispanics in 2012, Adjusted to 2017 Dollars', value: 'hinch12a17'},
      {label: 'Median Household Income for Asians in 2012', value: 'hinca12'},
      {label: 'Median Household Income for Asians in 2012, Adjusted to 2017 Dollars', value: 'hinca12a17'},
      {label: 'Median Household Income in 2016', value: 'hinc16'},
      {label: 'Median Household Income in 2016, Adjusted to 2017 Dollars', value: 'hinc16a17'},
      {label: 'Median Household Income for Whites in 2016', value: 'hincw16'},
      {label: 'Median Household Income for Whites in 2016, Adjusted to 2017 Dollars', value: 'hincw16a17'},
      {label: 'Median Household Income for Blacks in 2016', value: 'hincb16'},
      {label: 'Median Household Income for Blacks in 2016, Adjusted to 2017 Dollars', value: 'hincb16a17'},
      {label: 'Median Household Income for Natives in 2016', value: 'hincn16'},
      {label: 'Median Household Income for Natives in 2016, Adjusted to 2017 Dollars', value: 'hincn16a17'},
      {label: 'Median Household Income for Asians in 2016', value: 'hinca16'},
      {label: 'Median Household Income for Asians in 2016, Adjusted to 2017 Dollars', value: 'hinca16a17'},
      {label: 'Median Household Income for Hawaiians in 2016', value: 'hincp16'},
      {label: 'Median Household Income for Hawaiians in 2016, Adjusted to 2017 Dollars', value: 'hincp16a17'},
      {label: 'Median Household Income for Other in 2016', value: 'hinco16'},
      {label: 'Median Household Income for Other in 2016, Adjusted to 2017 Dollars', value: 'hinco16a17'},
      {label: 'Median Household Income for Two or More Races in 2016', value: 'hincm16'},
      {label: 'Median Household Income for Two or More Races in 2016, Adjusted to 2017 Dollars', value: 'hincm16a17'},
      {label: 'Median Household Income for Hispanics in 2016', value: 'hinch16'},
      {label: 'Median Household Income for Hispanics in 2016, Adjusted to 2017 Dollars', value: 'hinch16a17'}]
  }
  else if (this.selectgroup.value === 'cincome') {
    options = [{label: 'Change in Household Income between 2000 and 2012, Adjusted to 2017 Dollars', value: 'chinc0012a17'},
      {label: 'Change in Household Income for White Population between 2000 and 2012, Adjusted to 2017 Dollars', value: 'chincw0012a17'},
      {label: 'Change in Household Income for Black Population between 2000 and 2012, Adjusted to 2017 Dollars', value: 'chincb0012a17'},
      {label: 'Change in Household Income for Asian Population between 2000 and 2012, Adjusted to 2017 Dollars', value: 'chinca0012a17'},
      {label: 'Change in Household Income for Hispanic Population between 2000 and 2012, Adjusted to 2017 Dollars', value: 'chinch0012a17'},
      {label: 'Change in Household Income between 2012 and 2016, Adjusted to 2017 Dollars', value: 'chinc1216a17'},
      {label: 'Change in Household Income for White Population between 2012 and 2016, Adjusted to 2017 Dollars', value: 'chincw1216a17'},
      {label: 'Change in Household Income for Black Population between 2012 and 2016, Adjusted to 2017 Dollars', value: 'chincb1216a17'},
      {label: 'Change in Household Income for Asian Population between 2012 and 2016, Adjusted to 2017 Dollars', value: 'chinca1216a17'},
      {label: 'Change in Household Income for Hispanic Population between 2012 and 2016, Adjusted to 2017 Dollars', value: 'chinch1216a17'},
      {label: 'Change in Household Income between 2000 and 2016, Adjusted to 2017 Dollars', value: 'chinc0016a17'},
      {label: 'Change in Household Income for White Population between 2000 and 2016, Adjusted to 2017 Dollars', value: 'chincw0016a17'},
      {label: 'Change in Household Income for Black Population between 2000 and 2016, Adjusted to 2017 Dollars', value: 'chincb0016a17'},
      {label: 'Change in Household Income for Asian Population between 2000 and 2016, Adjusted to 2017 Dollars', value: 'chinca0016a17'},
      {label: 'Change in Household Income for Hispanic Population between 2000 and 2016, Adjusted to 2017 Dollars', value: 'chinch0016a17'}]
  }
  else if (this.selectgroup.value === 'pcincome') {
    options = [{label: 'Percent Change in Household Income between 2000 and 2012, Adjusted to 2017 Dollars', value: 'pchinc0012a17'},
      {label: 'Percent Change in Household Income for White Population between 2000 and 2012, Adjusted to 2017 Dollars', value: 'pchincw0012a17'},
      {label: 'Percent Change in Household Income for Black Population between 2000 and 2012, Adjusted to 2017 Dollars', value: 'pchincb0012a17'},
      {label: 'Percent Change in Household Income for Asian Population between 2000 and 2012, Adjusted to 2017 Dollars', value: 'pchinca0012a17'},
      {label: 'Percent Change in Household Income for Hispanic Population between 2000 and 2012, Adjusted to 2017 Dollars', value: 'pchinch0012a17'},
      {label: 'Percent Change in Household Income between 2012 and 2016, Adjusted to 2017 Dollars', value: 'pchinc1216a17'},
      {label: 'Percent Change in Household Income for White Population between 2012 and 2016, Adjusted to 2017 Dollars', value: 'pchincw1216a17'},
      {label: 'Percent Change in Household Income for Black Population between 2012 and 2016, Adjusted to 2017 Dollars', value: 'pchincb1216a17'},
      {label: 'Percent Change in Household Income for Asian Population between 2012 and 2016, Adjusted to 2017 Dollars', value: 'pchinca1216a17'},
      {label: 'Percent Change in Household Income for Hispanic Population between 2012 and 2016, Adjusted to 2017 Dollars', value: 'pchinch1216a17'},
      {label: 'Percent Change in Household Income between 2000 and 2016, Adjusted to 2017 Dollars', value: 'pchinc0016a17'},
      {label: 'Percent Change in Household Income for White Population between 2000 and 2016, Adjusted to 2017 Dollars', value: 'pchincw0016a17'},
      {label: 'Percent Change in Household Income for Black Population between 2000 and 2016, Adjusted to 2017 Dollars', value: 'pchincb0016a17'},
      {label: 'Percent Change in Household Income for Asian Population between 2000 and 2016, Adjusted to 2017 Dollars', value: 'pchinca0016a17'},
      {label: 'Percent Change in Household Income for Hispanic Population between 2000 and 2016, Adjusted to 2017 Dollars', value: 'pchinch0016a17'}]
  }
  else if (this.selectgroup.value === 'pir') {
    options = [{label: 'Price Income Ratio between 1998 and 2000', value: 'pir9800'},
      {label: 'Price Income Ratio between 2008 and 2012', value: 'pir0812'},
      {label: 'Price Income Ratio between 2015 and 2017', value: 'pir1517'}]
  }
  else if (this.selectgroup.value === 'education') {
    options = [{label: 'Number of High School Graduates in 1970', value: 'hs70'},
      {label: 'Percent High School Graduates in 1970', value: 'phs70'},
      {label: 'Number of College Graduates in 1970', value: 'col70'},
      {label: 'Percent College Graduates in 1970', value: 'pcol70'},
      {label: 'Number of High School Graduates in 1980', value: 'hs80'},
      {label: 'Percent High School Graduates in 1980', value: 'phs80'},
      {label: 'Number of College Graduates in 1980', value: 'col80'},
      {label: 'Percent College Graduates in 1980', value: 'pcol80'},
      {label: 'Number of High School Graduates in 1990', value: 'hs90'},
      {label: 'Percent High School Graduates in 1990', value: 'phs90'},
      {label: 'Number of College Graduates in 1990', value: 'col90'},
      {label: 'Percent College Graduates in 1990', value: 'pcol90'},
      {label: 'Number of High School Graduates in 2000', value: 'hs00'},
      {label: 'Percent High School Graduates in 2000', value: 'phs00'},
      {label: 'Number of College Graduates in 2000', value: 'col00'},
      {label: 'Percent College Graduates in 2000', value: 'pcol00'},
      {label: 'Number of High School Graduates in 2012', value: 'hs12'},
      {label: 'Percent High School Graduates in 2012', value: 'phs12'},
      {label: 'Number of College Graduates in 2012', value: 'col12'},
      {label: 'Percent College Graduates in 2012', value: 'pcol12'},
      {label: 'Percent Change in College Graduates between 2000 and 2012', value: 'pccol0012'},
      {label: 'Number of Males with Bachelor Degrees in 2016', value: 'batm16'},
      {label: 'Number of Males with Mater Degrees in 2016', value: 'masm16'},
      {label: 'Number of Males with Professional Degrees in 2016', value: 'prom16'},
      {label: 'Number of Males with a PhD in 2016', value: 'phdm16'},
      {label: 'Number of Females with Bachelor Degrees in 2016', value: 'batf16'},
      {label: 'Number of Females with Master Degrees in 2016', value: 'masf16'},
      {label: 'Number of Females with Professional Degrees in 2016', value: 'prof16'},
      {label: 'Number of Females with a PhD in 2016', value: 'phdf16'},
      {label: 'Number of College Graduates in 2016', value: 'col16'},
      {label: 'Percent College Graduates in 2016', value: 'pcol16'},
      {label: 'Percent Change in College Graduates between 2012 and 2016', value: 'pccol1216'},
      {label: 'Percent Change in College Graduates between 2000 and 2016', value: 'pccol0016'}]
  }
  else if (this.selectgroup.value === 'employment') {
    options = [{label: 'Civilian Labor Force in 1970', value: 'clf70'},
      {label: 'Number of Unemployed in 1970', value: 'unemp70'},
      {label: 'Percent Unempolyment in 1970', value: 'punemp70'},
      {label: 'Civilian Labor Force in 1980', value: 'clf80'},
      {label: 'Number of Unemployed in 1980', value: 'unemp80'},
      {label: 'Percent Unempolyment in 1980', value: 'punemp80'},
      {label: 'Civilian Labor Force in 1990', value: 'clf90'},
      {label: 'Number of Unemployed in 1990', value: 'unemp90'},
      {label: 'Percent Unempolyment in 1990', value: 'punemp90'},
      {label: 'Civilian Labor Force in 2000', value: 'clf00'},
      {label: 'Number of Unemployed in 2000', value: 'unemp00'},
      {label: 'Percent Unempolyment in 2000', value: 'punemp00'},
      {label: 'Civilian Labor Force in 2012', value: 'clf12'},
      {label: 'Number of Unemployed in 2012', value: 'unemp12'},
      {label: 'Percent Unempolyment in 2012', value: 'punemp12'}]
  }
  return options
}

export default setOptions
