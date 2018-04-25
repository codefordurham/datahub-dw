CREATE VIEW propsalesacs_2016_bgs AS
    SELECT PS.geoid10, PS.mean_sale_price, PS.min_sale_price, PS.max_sale_price, 
           PS.median_sale_price, PS.stddev_sale_price, PS.total_sale_price, PS.num_sales, ACS.mhi AS mhi,
           CAST(PS.median_sale_price AS DECIMAL)/CAST(ACS.mhi AS DECIMAL) AS pir, 
           mgr_phi AS mgr_phi, mmoc_phi AS mmoc_phi, PS.begin_date, PS.end_date
    FROM propsales_bgs_011818 AS PS
    INNER JOIN acsincome_bgs_2016 AS ACS ON (PS.geoid10=ACS.geoid10);
