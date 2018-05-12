        {label: 'Mean Sale Price, for Single Family Homes, between 1998 and 2000', value: 'meansp9800', type: 'bgs'},
        {label: 'Mean Sale Price, for Single Family Homes, between 1998 and 2000, Adjusted to 2017 Dollars', value: 'meansp9800a17', type: 'bgs'},
        {label: 'Minimum Sale Price, for Single Family Homes, between 1998 and 2000', value: 'minsp9800', type: 'bgs'},
        {label: 'Minimum Sale Price, for Single Family Homes, between 1998 and 2000, Adjusted to 2017 Dollars', value: 'minsp9800a17', type: 'bgs'},
        {label: 'Maximum Sale Price, for Single Family Homes, between 1998 and 2000', value: 'maxsp9800', type: 'bgs'},
        {label: 'Maximum Sale Price, for Single Family Homes, between 1998 and 2000, Adjusted to 2017 Dollars', value: 'maxsp9800a17', type: 'bgs'},
        {label: 'Median Sale Price, for Single Family Homes, between 1998 and 2000', value: 'mediansp9800', type: 'bgs'},
        {label: 'Median Sale Price, for Single Family Homes, between 1998 and 2000, Adjusted to 2017 Dollars', value: 'mediansp9800a17', type: 'bgs'},
        {label: 'Standard Deviation of Sale Price, for Single Family Homes, between 1998 and 2000', value: 'stddevsp9800', type: 'bgs'},
        {label: 'Standard Deviation of Sale Price, for Single Family Homes, between 1998 and 2000, Adjusted to 2017 Dollars', value: 'stddevsp9800a17', type: 'bgs'},
        {label: 'Total Sale Price, for Single Family Homes, between 1998 and 2000', value: 'totsp9800', type: 'bgs'},
        {label: 'Total Sale Price, for Single Family Homes, between 1998 and 2000, Adjusted to 2017 Dollars', value: 'totsp9800a17', type: 'bgs'},
        {label: 'Number of Homes Sold, for Single Family Homes, between 1998 and 2000', value: 'nums9800', type: 'bgs'},
        {label: 'Median Houshold Income, in 1900', value: 'mhi99', type: 'bgs'},
        {label: 'Median Houshold Income, in 1999, Adjusted to 2017 Dollars', value: 'mhi99a17', type: 'bgs'},
        {label: 'Price Income Ratio, between 1998 and 2000', value: 'pir9800', type: 'bgs'},
        {label: 'Median Gross Rent as a Percentage Of Household Income In The Past 12 Months, in 1999', value: 'mgr_phi99', type: 'bgs'},
        {label: 'Median Selected Monthly Owner Costs as a Percentage Of Household Income In The Past 12 Months, in 1999', value: 'mmoc_phi99', type: 'bgs'},
        {label: 'Total Population, in 2000', value: 'pop00', type: 'bgs'},
        {label: 'Percent White Non-Hispanic, in 2000', value: 'ptwhnl00', type: 'bgs'},
        {label: 'Percent Black Non-Hispanic, in 2000', value: 'ptblknl00', type: 'bgs'},
        {label: 'Percent Native Non-Hispanic, in 2000', value: 'ptnanl00', type: 'bgs'},
        {label: 'Percent Asian Non-Hispanic, in 2000', value: 'ptasnl00', type: 'bgs'},
        {label: 'Percent Pacific Islanders and Hawaiian Non-Hispanic, in 2000', value: 'ptpanl00', type: 'bgs'},
        {label: 'Percent Other Non-Hispanic, in 2000', value: 'ptothnl00', type: 'bgs'},
        {label: 'Percent 2 or More Races Non-Hispanic, in 2000', value: 'pt2mnl00', type: 'bgs'},
        {label: 'Percent Hispanic, in 2000', value: 'ptlat00', type: 'bgs'},
        {label: 'Mean Value of Single Family Non-Owner Occupied Homes, in 2001', value: 'mean_sfno2001', type: 'bgs'},
        {label: 'Total Value of Single Family Non-Owner Occupied Homes, in 2001', value: 'tot_sfno2001', type: 'bgs'},
        {label: 'Number of Single Family Non-Owner Occupied Homes, in 2001', value: 'num_sfno2001', type: 'bgs'},
        {label: 'Mean Value of Single Family Owner Occupied Homes, in 2001', value: 'mean_sfoo2001', type: 'bgs'},
        {label: 'Total Value of Single Family Owner Occupied Homes, in 2001', value: 'tot_sfoo2001', type: 'bgs'},
        {label: 'Number of Single Family Owner Occupied Homes, in 2001', value: 'num_sfoo2001', type: 'bgs'},
        {label: 'Percent of Single Family Non-Owner Occupied Homes, in 2001', value: 'prc_sfno2001', type: 'bgs'}

      if (this.select.value === 'meansp9800' && this.select.type === 'bgs') {
        desc = 'Mean Sale Price, for Single Family Homes: ' + numberWithCommas(this.currentDurhambg.meansp9800)
      }
      else if (this.select.value === 'meansp9800a17' && this.select.type === 'bgs') {
        desc = 'Mean Sale Price, for Single Family Homes, Adjusted to 2017 Dollars: ' + numberWithCommas(this.currentDurhambg.meansp9800a17)
      }
      else if (this.select.value === 'minsp9800' && this.select.type === 'bgs') {
        desc = 'Minimum Sale Price, for Single Family Homes: ' + numberWithCommas(this.currentDurhambg.minsp9800)
      }
      else if (this.select.value === 'minsp9800a17' && this.select.type === 'bgs') {
        desc = 'Minimum Sale Price, for Single Family Homes, Adjusted to 2017 Dollars: ' + numberWithCommas(this.currentDurhambg.minsp9800a17)
      }
      else if (this.select.value === 'maxsp9800' && this.select.type === 'bgs') {
        desc = 'Maximum Sale Price, for Single Family Homes: ' + numberWithCommas(this.currentDurhambg.maxsp9800)
      }
      else if (this.select.value === 'maxsp9800a17' && this.select.type === 'bgs') {
        desc = 'Maximum Sale Price, for Single Family Homes, Adjusted to 2017 Dollars: ' + numberWithCommas(this.currentDurhambg.maxsp9800a17)
      }
      else if (this.select.value === 'mediansp9800' && this.select.type === 'bgs') {
        desc = 'Median Sale Price, for Single Family Homes: ' + numberWithCommas(this.currentDurhambg.mediansp9800)
      }
      else if (this.select.value === 'mediansp9800a17' && this.select.type === 'bgs') {
        desc = 'Median Sale Price, for Single Family Homes, Adjusted to 2017 Dollars: ' + numberWithCommas(this.currentDurhambg.mediansp9800a17)
      }
      else if (this.select.value === 'stddevsp9800' && this.select.type === 'bgs') {
        desc = 'Standard Deviation of Sale Price, for Single Family Homes: ' + numberWithCommas(this.currentDurhambg.stddevsp9800)
      }
      else if (this.select.value === 'stddevsp9800a17' && this.select.type === 'bgs') {
        desc = 'Standard Deviation of Sale Price, for Single Family Homes, Adjusted to 2017 Dollars: ' + numberWithCommas(this.currentDurhambg.stddevsp9800a17)
      }
      else if (this.select.value === 'totsp9800' && this.select.type === 'bgs') {
        desc = 'Total Sale Price, for Single Family Homes: ' + numberWithCommas(this.currentDurhambg.totsp9800)
      }
      else if (this.select.value === 'totsp9800a17' && this.select.type === 'bgs') {
        desc = 'Total Sale Price, for Single Family Homes, Adjusted to 2017 Dollars: ' + numberWithCommas(this.currentDurhambg.totsp9800a17)
      }
      else if (this.select.value === 'nums9800' && this.select.type === 'bgs') {
        desc = 'Number of Homes Sold, for Single Family Homes: ' + numberWithCommas(this.currentDurhambg.nums9800)
      }
      else if (this.select.value === 'mhi99' && this.select.type === 'bgs') {
        desc = 'Median Houshold Income: ' + numberWithCommas(this.currentDurhambg.mhi99)
      }
      else if (this.select.value === 'mhi99a17' && this.select.type === 'bgs') {
        desc = 'Median Houshold Income, Adjusted to 2017 Dollars: ' + numberWithCommas(this.currentDurhambg.mhi99a17)
      }
      else if (this.select.value === 'pir9800' && this.select.type === 'bgs') {
        desc = 'Price Income Ratio: ' + numberWithCommas(this.currentDurhambg.pir9800)
      }
      else if (this.select.value === 'mgr_phi99' && this.select.type === 'bgs') {
        desc = 'Median Gross Rent as a Percentage Of Household Income In The Past 12 Months: ' + numberWithCommas(this.currentDurhambg.mgr_phi99)
      }
      else if (this.select.value === 'mmoc_phi99' && this.select.type === 'bgs') {
        desc = 'Median Selected Monthly Owner Costs as a Percentage Of Household Income In The Past 12 Months: ' + numberWithCommas(this.currentDurhambg.mmoc_phi99)
      }
      else if (this.select.value === 'pop00' && this.select.type === 'bgs') {
        desc = 'Total Population: ' + numberWithCommas(this.currentDurhambg.pop00)
      }
      else if (this.select.value === 'ptwhnl00' && this.select.type === 'bgs') {
        desc = 'Percent White Non-Hispanic: ' + numberWithCommas(this.currentDurhambg.ptwhnl00)
      }
      else if (this.select.value === 'ptblknl00' && this.select.type === 'bgs') {
        desc = 'Percent Black Non-Hispanic: ' + numberWithCommas(this.currentDurhambg.ptblknl00)
      }
      else if (this.select.value === 'ptnanl00' && this.select.type === 'bgs') {
        desc = 'Percent Native Non-Hispanic: ' + numberWithCommas(this.currentDurhambg.ptnanl00)
      }
      else if (this.select.value === 'ptasnl00' && this.select.type === 'bgs') {
        desc = 'Percent Asian Non-Hispanic: ' + numberWithCommas(this.currentDurhambg.ptasnl00)
      }
      else if (this.select.value === 'ptpanl00' && this.select.type === 'bgs') {
        desc = 'Percent Pacific Islanders and Hawaiian Non-Hispanic: ' + numberWithCommas(this.currentDurhambg.ptpanl00)
      }
      else if (this.select.value === 'ptothnl00' && this.select.type === 'bgs') {
        desc = 'Percent Other Non-Hispanic: ' + numberWithCommas(this.currentDurhambg.ptothnl00)
      }
      else if (this.select.value === 'pt2mnl00' && this.select.type === 'bgs') {
        desc = 'Percent 2 or More Races Non-Hispanic: ' + numberWithCommas(this.currentDurhambg.pt2mnl00)
      }
      else if (this.select.value === 'ptlat00' && this.select.type === 'bgs') {
        desc = 'Percent Hispanic: ' + numberWithCommas(this.currentDurhambg.ptlat00)
      }
      else if (this.select.value === 'mean_sfno2001' && this.select.type === 'bgs') {
        desc = 'Mean Value of Single Family Non-Owner Occupied Homes: ' + numberWithCommas(this.currentDurhambg.mean_sfno2001)
      }
      else if (this.select.value === 'tot_sfno2001' && this.select.type === 'bgs') {
        desc = 'Total Value of Single Family Non-Owner Occupied Homes: ' + numberWithCommas(this.currentDurhambg.tot_sfno2001)
      }
      else if (this.select.value === 'num_sfno2001' && this.select.type === 'bgs') {
        desc = 'Number of Single Family Non-Owner Occupied Homes: ' + numberWithCommas(this.currentDurhambg.num_sfno2001)
      }
      else if (this.select.value === 'mean_sfoo2001' && this.select.type === 'bgs') {
        desc = 'Mean Value of Single Family Owner Occupied Homes: ' + numberWithCommas(this.currentDurhambg.mean_sfoo2001)
      }
      else if (this.select.value === 'tot_sfoo2001' && this.select.type === 'bgs') {
        desc = 'Total Value of Single Family Owner Occupied Homes: ' + numberWithCommas(this.currentDurhambg.tot_sfoo2001)
      }
      else if (this.select.value === 'num_sfoo2001' && this.select.type === 'bgs') {
        desc = 'Number of Single Family Owner Occupied Homes: ' + numberWithCommas(this.currentDurhambg.num_sfoo2001)
      }
      else if (this.select.value === 'prc_sfno2001' && this.select.type === 'bgs') {
        desc = 'Percent of Single Family Non-Owner Occupied Homes: ' + numberWithCommas(this.currentDurhambg.prc_sfno2001)
      }
