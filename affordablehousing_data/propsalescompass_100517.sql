\copy datahub_be_app_propsales(id,meansp,minsp,maxsp,mediansp,totsp,nums,mhi,pir) FROM 'propsalescompass_bgs_100517.csv' WITH DELIMITER ',' CSV HEADER;
