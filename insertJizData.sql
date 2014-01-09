use jiz;
INSERT jizhang_customers VALUES 
(123,'felix','song lin road','qingdao','shandong',266100,'China',18669851131,88615808,'felix@alu.com','taobao_felix','baidu_felix');
INSERT jizhang_customers VALUES 
(111,'felix','song lin road','qingdao','shandong',266100,'China',18669851131,88615808,'felix@alu.com','taobao_felix','baidu_felix');
INSERT jizhang_customers VALUES 
(222,'maqi','song lin road','qingdao','shandong',266100,'China',18669851131,88615808,'maqi@alu.com','taobao_maqi','baidu_maqi');

INSERT jizhang_vendors VALUES
(1,'Self','Si Ji Jing Yuan', 'QD','SD',266100, 'China');
INSERT jizhang_vendors VALUES
(2,'vend_1','guangzhou street', 'GZ','GD',123456, 'China');

INSERT jizhang_products VALUES
(1, 1, 'fa dai 001', 5, 50, 'green fa dai', 30, 1);
INSERT jizhang_products VALUES
(2, 1, 'fa dai 002', 20, 50, 'fa dai 002 yellow', 30, 1);
INSERT jizhang_products VALUES
(3, 1, 'fa dai 001', 5, 50, 'green fa dai', 30, 2);
INSERT jizhang_products VALUES
(4, 2, 'hua bu', 5, 20, 'hua bu - yellow', 300, 1);

INSERT jizhang_orders VALUES
(1, '2014/01/01', 111, 1, 'http://taobao.com');
INSERT jizhang_orders VALUES
(2, '2013/11/01', 111, 1, 'http://taobao.com');
INSERT jizhang_orders VALUES
(3, '2013/12/31', 111, 1, 'http://taobao.com');
INSERT jizhang_orders VALUES
(4, '2013/12/31', 111, 1, 'http://taobao.com');

INSERT jizhang_orderitems VALUES
(1, 1, 1, 10, 50);
INSERT jizhang_orderitems VALUES
(2, 1, 1, 5, 50);
INSERT jizhang_orderitems VALUES
(3, 1, 1, 5, 50);
INSERT jizhang_orderitems VALUES
(4, 1, 4, 30, 20);


