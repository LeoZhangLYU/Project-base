package com.mp.first;

import com.mp.first.dao.UserMapper;
import com.mp.first.entity.User;
import org.junit.Assert;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.time.LocalDateTime;
import java.util.List;

@SpringBootTest
@RunWith(SpringRunner.class)
class InsertTests {

    @Autowired
    private UserMapper userMapper;

    @Test
    public void insert(){
        User user = new User();
        user.setName("向东");
        user.setAge(26);
        user.setEmail("xiangd@baomidou.com");
        user.setManagerId(1088248166370832385l);
        user.setCreateTime(LocalDateTime.now());
        int i = userMapper.insert(user);
        System.out.println("影像记录数："+i);
    }
}
