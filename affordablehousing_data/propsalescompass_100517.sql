\copy datahub_be_app_propsales(id,meansp,minsp,maxsp,mediansp,totsp,nums,mhi,pir) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtualenv/development/datahub-dw/affordablehousing_data/propsalescompass_bgs_100517.csv' WITH DELIMITER ',' CSV HEADER;
