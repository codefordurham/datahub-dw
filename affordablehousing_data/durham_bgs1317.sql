\copy datahub_be_app_bgs1317(id,meansp1314,meansp1314a17,minsp1314,minsp1314a17,maxsp1314,maxsp1314a17,mediansp1314,mediansp1314a17,totsp1314,totsp1314a17,nums1314,mhi1314,mhi1314a17,pir1314,mean_sfno100517,tot_sfno100517,num_sfno100517,mean_sfoo100517,tot_sfoo100517,num_sfoo100517,prc_sfno100517,pop13,pop14,ptwhnl13,ptwhnl14,ptblknl13,ptblknl14,ptasnl13,ptasnl14,ptothnl13,ptothnl14,ptlat13,ptlat14,meansp1517,meansp1517a17,minsp1517,minsp1517a17,maxsp1517,maxsp1517a17,mediansp1517,mediansp1517a17,totsp1517,totsp1517a17,nums1517,mhi16,mhi16a17,pir1517,mgr_phi16,mmoc_phi16,mean_sfno011818,tot_sfno011818,num_sfno011818,mean_sfoo011818,tot_sfoo011818,num_sfoo011818,prc_sfno011818,pop16,ptwhnl16,ptblknl16,ptnanl16,ptasnl16,ptpanl16,ptothnl16,pt2mnl16,ptlat16) FROM 'durham_bgs1317.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;