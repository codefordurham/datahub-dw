CREATE VIEW propsalecompass AS
    SELECT PS.geoid10, PS.mean_sale_price, PS.min_sale_price, PS.max_sale_price, 
           PS.median_sale_price, PS.total_sale_price, PS.num_sales,
           CAST(DC.mhi_13 AS DECIMAL)+CAST(DC.mhi_14 AS DECIMAL)/2.0 AS mhi,
           CAST(PS.median_sale_price AS DECIMAL)/(CAST(DC.mhi_13 AS DECIMAL)+CAST(DC.mhi_14 AS DECIMAL)/2.0) AS pir, 
           PS.begin_date, PS.end_date
    FROM propsales_100517 AS PS
    INNER JOIN durhamcompass AS DC ON (PS.geoid10=DC.geoid10);
