### 注册用户接口

请求地址：

    /api/user/auth/register/
请求方式: 

    POST

请求参数:

    u_username string  账号  必填 长度4-10
    u_password string  密码  必填 长度4-32
    u_password2 string 确认密码  必填  长度4-32
    u_email string 邮箱   必填

响应结果:

    {
        'code': 1001,
        'msg': ‘账号已存在’,
        'data': {
        
        }
    }
    
    {
        'code': 200,
        'msg': '请求成功',
        'data':{
            'user_id': 1
        }
    }

响应参数:

    code int 状态码
    msg  string 响应描述
    data 结果
