use jiz;
INSERT jizhang_customers VALUES 
(123,'felix','松岭路','青岛','山东',266100,'中国',18669851131,88615808,'felix@alu.com','taobao_felix','baidu_felix');
INSERT jizhang_customers VALUES 
(111,'felix','松岭路','青岛','山东',266100,'中国',18669851131,88615808,'felix@alu.com','taobao_felix','baidu_felix');
INSERT jizhang_customers VALUES 
(222,'maqi','松岭路','青岛','山东',266100,'中国',18669851131,88615808,'maqi@alu.com','taobao_maqi','baidu_maqi');

INSERT jizhang_vendors VALUES
(1,'Self','四季景园', '青岛','山东',266100, '中国');
INSERT jizhang_vendors VALUES
(2,'vend_1','广州街', '广州','广东',123456, '中国');

INSERT jizhang_products VALUES
(1, 1, '发带001', 5, 50, '绿色发带', 30, 1);
INSERT jizhang_products VALUES
(2, 1, '发带002', 20, 50, '发带002 浅黄色', 30, 1);
INSERT jizhang_products VALUES
(3, 1, '发带001', 5, 50, '绿色发带', 30, 2);
INSERT jizhang_products VALUES
(4, 2, '花布1号', 5, 20, '花布 - yellow', 300, 1);
INSERT jizhang_products VALUES
(5, 2, '花布', 5, 20, '紫色花布', 300, 1);


INSERT jizhang_orders VALUES
(1, '2014/01/01', 111, 1, 'http://taobao.com');
INSERT jizhang_orders VALUES
(2, '2013/11/01', 111, 1, 'http://taobao.com');
INSERT jizhang_orders VALUES
(3, '2013/12/31', 111, 1, 'http://taobao.com');
INSERT jizhang_orders VALUES
(4, '2013/12/31', 111, 1, 'http://taobao.com');
INSERT jizhang_orders VALUES
(5, '2014/02/08', 111, 1, 'http://taobao.com');
INSERT jizhang_orders VALUES
(6, '2014/02/12', 111, 1, 'http://taobao.com');



INSERT jizhang_orderitems VALUES
(1, 1, 1, 10, 50);
INSERT jizhang_orderitems VALUES
(2, 1, 1, 5, 50);
INSERT jizhang_orderitems VALUES
(3, 2, 2, 5, 50);
INSERT jizhang_orderitems VALUES
(4, 3, 3, 30, 20);
INSERT jizhang_orderitems VALUES
(5, 4, 4, 30, 20);
INSERT jizhang_orderitems VALUES
(6, 5, 4, 1, 20);
INSERT jizhang_orderitems VALUES
(7, 6, 3, 5, 20);

