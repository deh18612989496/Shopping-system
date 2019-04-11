### 注册用户接口

请求地址:

    http://127.0.0.1:8000/api/goods/home/
   
   
请求方式：

    get
请求参数：

    u_username string 账号  必填    长度4-32
    u_password string 密码    必填  长度3-10
    u_password2 string 确认密码 必填  长度3-10
    u_email string 邮箱   必填
    
响应效果:

    {
        'code':200,
        'msg':成功，
        'data':{
        ‘main_wheels':[],
        'main_navs':[],
        'main_mustbuys':[],
        'main_shops':[],
        'main_shows':[],
        }
    
    
    }
    
响应参数:

    code int 状态码
    msg  string 响应描述
    data 结果