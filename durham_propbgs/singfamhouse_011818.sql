\copy datahub_be_app_singfamhouse17(id,mean_sfno,tot_sfno,num_sfno,mean_sfoo,tot_sfoo,num_sfoo,prc_sfno) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtualenv/development/datahub-dw/durham_propbgs/singfamhouse_bgs_011818.csv' WITH DELIMITER ',' CSV HEADER;
