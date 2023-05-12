package org.my.system.controller;

import jakarta.annotation.Resource;
import org.my.system.domain.Test;
import org.my.system.service.TestService;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * 如果返回的是Json格式的数据，用RestController
 * 如果返回的是页面，用Controller
 */
@RestController
//@RequestMapping("/system")
public class TestController {

    @Resource
    private TestService testService;

    @RequestMapping("/test")
    public List<Test> test() {
        return testService.list();
    }
}
