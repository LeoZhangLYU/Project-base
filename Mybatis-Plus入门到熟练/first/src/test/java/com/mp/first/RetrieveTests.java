package com.mp.first;

import com.baomidou.mybatisplus.core.conditions.Wrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;
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
    public void selectById() {
        User user = userMapper.selectById(1094590409767661570l);
        System.out.println(user);
    }

    @Test
    public void selectIds() {
        List<Long> list = Arrays.asList(1088250446457389058l, 1094590409767661570l, 1094592041087729666l);
        List<User> userList = userMapper.selectBatchIds(list);
        userList.forEach(System.out::println);
    }

    @Test
    public void selectByMap() {
//        map.put("name","王天风")
//        map.put("age",30")
//        where name = "王天风" and age = 30
        Map<String, Object> map = new HashMap<>();
//        map.put("name","王天风");
        map.put("age", 31);
        List<User> userList = userMapper.selectByMap(map);
        userList.forEach(System.out::println);
    }

    /**
     * 1.名字中包含雨，并且年龄小于40
     */
    @Test
    public void selectByWrapper() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
//        方法2
//        QueryWrapper<User> query = Wrappers.<User>query();
        userQueryWrapper.like("name", "雨").lt("age", 40);
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 2.名字中包含雨，并且年龄大于等于10且小于等于40，并且email不为空
     */
    @Test
    public void selectByWrapper2() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.like("name", "雨").between("age", 20, 40).isNotNull("email");
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }

    /**
     * 3.名字为王姓或者年龄大于等于25，按照年龄降序排列，年龄相同按照id升序排列
     */
    @Test
    public void selectByWrapper3() {
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.likeRight("name", "王").or().ge("age", 25).orderByDesc("age").orderByAsc("id");
        List<User> userList = userMapper.selectList(userQueryWrapper);
        userList.forEach(System.out::println);
    }
}
