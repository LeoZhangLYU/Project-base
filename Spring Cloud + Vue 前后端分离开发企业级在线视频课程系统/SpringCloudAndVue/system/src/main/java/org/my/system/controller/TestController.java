package org.my.system.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * 如果返回的是Json格式的数据，用RestController
 * 如果返回的是页面，用Controller
 */
@RestController
//@RequestMapping("/system")
public class TestController {

    @RequestMapping("/test")
    public String test() {
        return "Success";
    }
}
