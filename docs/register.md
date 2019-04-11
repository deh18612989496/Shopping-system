###文章查询接口api

请求URL:/api/user/user/

请求方式：POST

请求参数:
    u_username 用户名 string   必填值
    u_password  用户密码 string    必填值
    u_password2  确认密码 string   必填值
    u_email  邮箱 string    必填值
    
响应：

    正常响应:
    {
        'code': 200,
        data{
            'msg': '注册成功',
            'user_id': user.id
        
        }
    }
    
    失败响应：
    {
        'code':1001,
         'msg':'注册账号已经存在'
         data{
         }
         'code':1002, 
         'msg':'密码不一致
         data{
         }
         'code':1003, 
         'msg':'邮箱已经存在'
         data{
         }
         'code':1004, 
         'msg': '参数有误'
         data{
         }
         
         
    }
    
响应参数：
    
    code 响应状态码 int
    msg 响应提示    string
    data 结果  