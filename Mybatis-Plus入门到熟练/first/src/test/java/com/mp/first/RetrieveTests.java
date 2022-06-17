package com.mp.first;

import com.mp.first.dao.UserMapper;
import com.mp.first.entity.User;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.lang.reflect.Array;
import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@SpringBootTest
@RunWith(SpringRunner.class)
class RetrieveTests {

    @Autowired
    private UserMapper userMapper;

    @Test
    public void selectById(){
        User user = userMapper.selectById(1094590409767661570l);
        System.out.println(user);
    }

    @Test
    public void selectIds(){
        List<Long> list = Arrays.asList(1088250446457389058l, 1094590409767661570l, 1094592041087729666l);
        List<User> userList = userMapper.selectBatchIds(list);
        userList.forEach(System.out::println);
    }

    @Test
    public void selectByMap(){
//        map.put("name","王天风")
//        map.put("age",30")
//        where name = "王天风" and age = 30
        Map<String, Object> map = new HashMap<>();
//        map.put("name","王天风");
        map.put("age",31);
        List<User> userList = userMapper.selectByMap(map);
        userList.forEach(System.out::println);
    }
}
