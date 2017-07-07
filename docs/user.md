
### 接口文档

#### 员工分公司列表
+ Request
`GET /yp/adm/staff_attributions/`


+ Response 200/400 (application/json)
```
{
    "code": 0,                            // 0为成功,其它失败
    "result": [
        {
            "text": "北京市",
            "value": "北京市"
        },
        {
            "text": "武汉市",
            "value": "武汉市"
        }
    ],
}
```

