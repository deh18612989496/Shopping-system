### 注册用户接口

请求地址:

    http://127.0.0.1:8000/api/cart/cart/
   
   
请求方式：

    get
请求参数：
      
      #从代码获取的view
    user string 用户  
    cart string 获取购物车数据
    user_id 用户id
    token 
    #从模型获取的
    c_goods 货物
    c_user  用户
    c_goods_num 货物数量
    
响应效果:

    {
    "code": 200,
    "msg": "请求成功",
    "data": {
        "carts": [],
        "total_price": ''
    }
    {
    code: 1008
    data: {}
    msg: "无法添加商品,请登录"
    }
    
响应参数:

    code int 状态码
    msg  string 响应描述
    data 结果
    
    