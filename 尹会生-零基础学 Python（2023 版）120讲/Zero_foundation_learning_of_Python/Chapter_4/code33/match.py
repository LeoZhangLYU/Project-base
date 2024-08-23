# NOTE: match语句的语法
http_response_status = 404
match http_response_status:
    case 400:
        print('Bad Request')
    case 404:
        print('Not Found')
    case 418:
        print("'I'm a teapot")
    case _:  # 通用匹配
        print('Unknown Error')
