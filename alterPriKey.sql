ALTER TABLE jizhang_orderitems DROP PRIMARY KEY;
ALTER TABLE jizhang_orderitems ADD PRIMARY KEY (order_item,order_num);
